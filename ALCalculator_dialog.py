# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ALCalculatorDialog
                                 A QGIS plugin
 This plugin calculates a total area or length of features in a vector layer.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-02-20
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Bartosz Łęczycki
        email                : bartosz.leczycki98@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import *
from qgis.utils import *
from qgis.core import *
from PyQt5.QtCore import *
from qgis.PyQt.QtGui import *
from PyQt5.QtWidgets import *
from qgis.gui import *

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ALCalculator_dialog_base.ui'))


class ALCalculatorDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ALCalculatorDialog, self).__init__(parent)

        self.setupUi(self)
        
        self.stackedWidget.setCurrentWidget(self.home)

        self.pbAreaPage.clicked.connect(self.gotoArea)
        self.pbLengthPage.clicked.connect(self.gotoLength)
        self.pbJumpArea.clicked.connect(self.gotoArea)
        self.pbJumpLength.clicked.connect(self.gotoLength)

        self.cbLengthLayerList.setFilters(QgsMapLayerProxyModel.LineLayer)
        self.cbAreaLayerList.setFilters(QgsMapLayerProxyModel.PolygonLayer)

        self.pbLengthCalc.clicked.connect(self.onPbLengthCalcClicked)
        self.pbAreaCalc.clicked.connect(self.onPbAreaCalcClicked)

        

    def onPbLengthCalcClicked(self):
        precision_value = self.sbLengthPrecision.value()
        layer = self.cbLengthLayerList.currentLayer()
        miles_conv = 0.621371192
        yard_conv = 1093.6132983377
        meters_conv = 1000
        if self.rbLengthMeters.isChecked():
            total_length = 0
            for feat in layer.getFeatures():
                geometry = feat.geometry()
                total_length += geometry.length()
            total_length = total_length * meters_conv
            self.lblLengthResult.setText('%.*f' % (precision_value, total_length))
        elif self.rbLengthKilometers.isChecked():
            total_length = 0
            for feat in layer.getFeatures():
                geometry = feat.geometry()
                total_length += geometry.length()
            self.lblLengthResult.setText('%.*f' % (precision_value, total_length))
        elif self.rbLengthMiles.isChecked():
            total_length = 0
            for feat in layer.getFeatures():
                geometry = feat.geometry()
                total_length += geometry.length()
            total_length = total_length * miles_conv
            self.lblLengthResult.setText('%.*f' % (precision_value, total_length))
        elif self.rbLengthYards.isChecked():
            total_length = 0
            for feat in layer.getFeatures():
                geometry = feat.geometry()
                total_length += geometry.length()
            total_length = total_length * yard_conv
            self.lblLengthResult.setText('%.*f' % (precision_value, total_length))


    def onPbAreaCalcClicked(self):
        precision_value = self.sbAreaPrecision.value()
        layer = self.cbAreaLayerList.currentLayer()
        sqmiles_conv = 0.386102159
        sqyards_conv = 1195990.05
        sqmeters_conv = 1000000
        hectares_conv = 100
        acres_conv = 10000
        if self.rbAreaMeters.isChecked():
            total_area = 0
            for feat in layer.getFeatures():
                geometry = feat.geometry()
                total_area += geometry.area()
            total_area = total_area * sqmeters_conv
            self.lblAreaResult.setText('%.*f' % (precision_value, total_area))
        elif self.rbAreaKilometers.isChecked():
            total_area = 0
            for feat in layer.getFeatures():
                geometry = feat.geometry()
                total_area += geometry.area()
            self.lblAreaResult.setText('%.*f' % (precision_value, total_area))
        elif self.rbAreaAres.isChecked():
            total_area = 0
            for feat in layer.getFeatures():
                geometry = feat.geometry()
                total_area += geometry.area()
                total_area = total_area * acres_conv
            self.lblAreaResult.setText('%.*f' % (precision_value, total_area))
        elif self.rbAreaHectares.isChecked():
            total_area = 0
            for feat in layer.getFeatures():
                geometry = feat.geometry()
                total_area += geometry.area()
                total_area = total_area * hectares_conv
            self.lblAreaResult.setText('%.*f' % (precision_value, total_area))
        elif self.rbAreaMiles.isChecked():
            total_area = 0
            for feat in layer.getFeatures():
                geometry = feat.geometry()
                total_area += geometry.area()
                total_area = total_area * sqmiles_conv
            self.lblAreaResult.setText('%.*f' % (precision_value, total_area))
        elif self.rbAreaYards.isChecked():
            total_area = 0
            for feat in layer.getFeatures():
                geometry = feat.geometry()
                total_area += geometry.area()
                total_area = total_area * sqyards_conv
            self.lblAreaResult.setText('%.*f' % (precision_value, total_area))

        #debug
        print(precision_value)


    def gotoArea(self):
        self.stackedWidget.setCurrentWidget(self.area)
        
    def gotoLength(self):
        self.stackedWidget.setCurrentWidget(self.length)


