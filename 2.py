# -*- coding: utf-8 -*-
import glob
import os
import sys
from threading import Thread

import albumentations as A
import apprcc_rc
import cv2
import numpy as np
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = None
        self.verticalLayout_4 = None
        self.gridLayout = None
        self.verticalLayout_2 = None
        self.verticalLayout = None
        self.pushButton = None
        self.gridLayout_2 = None
        self.lineEdit_43 = None
        self.label_27 = None
        self.label_52 = None
        self.lineEdit_40 = None
        self.label_9 = None
        self.lineEdit_4 = None
        self.lineEdit_2 = None
        self.label_32 = None
        self.label_53 = None
        self.label_30 = None
        self.label_38 = None
        self.label_13 = None
        self.label = None
        self.lineEdit_54 = None
        self.lineEdit_6 = None
        self.label_21 = None
        self.label_59 = None
        self.label_44 = None
        self.lineEdit_24 = None
        self.lineEdit_51 = None
        self.label_62 = None
        self.label_24 = None
        self.lineEdit_50 = None
        self.label_26 = None
        self.label_72 = None
        self.lineEdit_28 = None
        self.lineEdit_32 = None
        self.label_34 = None
        self.lineEdit_33 = None
        self.label_42 = None
        self.label_12 = None
        self.label_18 = None
        self.lineEdit_5 = None
        self.lineEdit_17 = None
        self.label_69 = None
        self.label_61 = None
        self.label_48 = None
        self.lineEdit_3 = None
        self.label_40 = None
        self.lineEdit_21 = None
        self.lineEdit_37 = None
        self.label_37 = None
        self.lineEdit_12 = None
        self.label_14 = None
        self.label_29 = None
        self.lineEdit_48 = None
        self.lineEdit_23 = None
        self.lineEdit_44 = None
        self.lineEdit_45 = None
        self.label_70 = None
        self.lineEdit_13 = None
        self.lineEdit_39 = None
        self.lineEdit_52 = None
        self.lineEdit_26 = None
        self.label_6 = None
        self.lineEdit_22 = None
        self.label_16 = None
        self.label_71 = None
        self.lineEdit_16 = None
        self.label_67 = None
        self.label_20 = None
        self.label_23 = None
        self.label_35 = None
        self.lineEdit_10 = None
        self.lineEdit_30 = None
        self.lineEdit_15 = None
        self.lineEdit_14 = None
        self.lineEdit_47 = None
        self.lineEdit_41 = None
        self.lineEdit_42 = None
        self.label_41 = None
        self.lineEdit_35 = None
        self.lineEdit_53 = None
        self.lineEdit_9 = None
        self.lineEdit_55 = None
        self.lineEdit_36 = None
        self.lineEdit_18 = None
        self.label_19 = None
        self.label_68 = None
        self.lineEdit_8 = None
        self.label_15 = None
        self.lineEdit_27 = None
        self.lineEdit_25 = None
        self.label_46 = None
        self.label_50 = None
        self.label_8 = None
        self.label_36 = None
        self.lineEdit_29 = None
        self.label_25 = None
        self.label_22 = None
        self.label_7 = None
        self.lineEdit_38 = None
        self.lineEdit_11 = None
        self.label_28 = None
        self.lineEdit_49 = None
        self.label_60 = None
        self.lineEdit_31 = None
        self.lineEdit_46 = None
        self.lineEdit = None
        self.label_58 = None
        self.label_2 = None
        self.label_11 = None
        self.label_45 = None
        self.label_5 = None
        self.lineEdit_7 = None
        self.label_3 = None
        self.label_4 = None
        self.label_10 = None
        self.label_43 = None
        self.label_39 = None
        self.label_17 = None
        self.lineEdit_20 = None
        self.lineEdit_34 = None
        self.label_31 = None
        self.label_49 = None
        self.label_33 = None
        self.label_47 = None
        self.lineEdit_19 = None
        self.label_51 = None
        self.horizontalLayout = None
        self.progressBar = None
        self.pushButton_2 = None
        self.pushButton_3 = None
        self.pushButton_4 = None
        self.menubar = None
        self.statusbar = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 475)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
                                         "background:url(:/img/1.jpg)\n"
                                         "}")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"#pushButton:hover{\n"
                                      "background-color:rgba(0, 136, 204, 90);\n"
                                      "color:rgb(255, 170, 255);\n"
                                      "}\n"
                                      "#pushButton:pressed{\n"
                                      "background-color:rgba(0, 136, 204, 40);\n"
                                      "color:rgb(255, 170, 255);\n"
                                      "}\n"
                                      "#pushButton{\n"
                                      "background-color:rgba(0, 170, 255, 140);\n"
                                      "color:rgb(85, 255, 255);\n"
                                      "font: 11pt \"\u9ed1\u4f53\";\n"
                                      "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                      "border-style:solid;\n"
                                      "border-width:1px;\n"
                                      "border-color:rgba(255, 170, 0,255);\n"
                                      "border-radius:6px;\n"
                                      "outline-style:solid;\n"
                                      "outline-width:1px;\n"
                                      "outline-color:rgb(255, 170, 127);\n"
                                      "outline-offset:1px;\n"
                                      "}")

        self.verticalLayout.addWidget(self.pushButton)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.lineEdit_43 = QLineEdit(self.centralwidget)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setStyleSheet(u"#lineEdit_43{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_43, 3, 7, 1, 1)

        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"#label_27{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_27, 4, 4, 1, 1)

        self.label_52 = QLabel(self.centralwidget)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"#label_52{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_52, 3, 4, 1, 1)

        self.lineEdit_40 = QLineEdit(self.centralwidget)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setStyleSheet(u"#lineEdit_40{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_40, 8, 9, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setStyleSheet(u"#label_9{\n"
                                   "color:rgb(85, 255, 255);\n"
                                   "font: 11pt \"\u9ed1\u4f53\";\n"
                                   "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                   "}")

        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 2)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"#lineEdit_4{\n"
                                      "background-color:rgba(0, 170, 255, 140);\n"
                                      "color:rgb(85, 255, 255);\n"
                                      "font: 11pt \"\u9ed1\u4f53\";\n"
                                      "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                      "border-style:solid;\n"
                                      "border-width:1px;\n"
                                      "border-color:rgba(255, 170, 0,255);\n"
                                      "border-radius:6px;\n"
                                      "outline-style:solid;\n"
                                      "outline-width:1px;\n"
                                      "outline-color:rgb(255, 170, 127);\n"
                                      "outline-offset:1px;\n"
                                      "}")

        self.gridLayout_2.addWidget(self.lineEdit_4, 4, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"#lineEdit_2{\n"
                                      "background-color:rgba(0, 170, 255, 140);\n"
                                      "color:rgb(85, 255, 255);\n"
                                      "font: 11pt \"\u9ed1\u4f53\";\n"
                                      "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                      "border-style:solid;\n"
                                      "border-width:1px;\n"
                                      "border-color:rgba(255, 170, 0,255);\n"
                                      "border-radius:6px;\n"
                                      "outline-style:solid;\n"
                                      "outline-width:1px;\n"
                                      "outline-color:rgb(255, 170, 127);\n"
                                      "outline-offset:1px;\n"
                                      "}")

        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"#label_32{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_32, 8, 2, 1, 2)

        self.label_53 = QLabel(self.centralwidget)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"#label_53{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_53, 6, 6, 1, 1)

        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"#label_30{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_30, 7, 4, 1, 1)

        self.label_38 = QLabel(self.centralwidget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"#label_38{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_38, 5, 8, 1, 1)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"#label_13{color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_13, 3, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"#label{\n"
                                 "color:rgb(85, 255, 255);\n"
                                 "font: 11pt \"\u9ed1\u4f53\";\n"
                                 "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                 "}")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit_54 = QLineEdit(self.centralwidget)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setStyleSheet(u"#lineEdit_54{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_54, 11, 9, 1, 1)

        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"#lineEdit_6{\n"
                                      "background-color:rgba(0, 170, 255, 140);\n"
                                      "color:rgb(85, 255, 255);\n"
                                      "font: 11pt \"\u9ed1\u4f53\";\n"
                                      "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                      "border-style:solid;\n"
                                      "border-width:1px;\n"
                                      "border-color:rgba(255, 170, 0,255);\n"
                                      "border-radius:6px;\n"
                                      "outline-style:solid;\n"
                                      "outline-width:1px;\n"
                                      "outline-color:rgb(255, 170, 127);\n"
                                      "outline-offset:1px;\n"
                                      "}")

        self.gridLayout_2.addWidget(self.lineEdit_6, 6, 1, 1, 1)

        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"#label_21{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_21, 1, 4, 1, 1)

        self.label_59 = QLabel(self.centralwidget)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"#label_59{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_59, 11, 2, 1, 1)

        self.label_44 = QLabel(self.centralwidget)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"#label_44{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_44, 4, 6, 1, 1)

        self.lineEdit_24 = QLineEdit(self.centralwidget)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setStyleSheet(u"#lineEdit_24{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_24, 5, 5, 1, 1)

        self.lineEdit_51 = QLineEdit(self.centralwidget)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setStyleSheet(u"#lineEdit_51{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_51, 12, 7, 1, 1)

        self.label_62 = QLabel(self.centralwidget)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"#label_62{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_62, 9, 8, 1, 2)

        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"#label_24{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_24, 9, 4, 1, 1)

        self.lineEdit_50 = QLineEdit(self.centralwidget)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        self.lineEdit_50.setStyleSheet(u"#lineEdit_50{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_50, 11, 7, 1, 1)

        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"#label_26{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_26, 2, 4, 1, 1)

        self.label_72 = QLabel(self.centralwidget)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setStyleSheet(u"#label_72{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_72, 13, 6, 1, 1)

        self.lineEdit_28 = QLineEdit(self.centralwidget)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setStyleSheet(u"#lineEdit_28{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_28, 9, 5, 1, 1)

        self.lineEdit_32 = QLineEdit(self.centralwidget)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setStyleSheet(u"#lineEdit_32{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_32, 13, 5, 1, 1)

        self.label_34 = QLabel(self.centralwidget)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"#label_34{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_34, 3, 8, 1, 1)

        self.lineEdit_33 = QLineEdit(self.centralwidget)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setStyleSheet(u"#lineEdit_33{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_33, 1, 9, 1, 1)

        self.label_42 = QLabel(self.centralwidget)
        self.label_42.setObjectName(u"label_42")
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        self.label_42.setStyleSheet(u"#label_42{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_42, 0, 8, 1, 2)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"#label_12{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_12, 2, 2, 1, 1)

        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"#label_18{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_18, 10, 4, 1, 1)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"#lineEdit_5{\n"
                                      "background-color:rgba(0, 170, 255, 140);\n"
                                      "color:rgb(85, 255, 255);\n"
                                      "font: 11pt \"\u9ed1\u4f53\";\n"
                                      "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                      "border-style:solid;\n"
                                      "border-width:1px;\n"
                                      "border-color:rgba(255, 170, 0,255);\n"
                                      "border-radius:6px;\n"
                                      "outline-style:solid;\n"
                                      "outline-width:1px;\n"
                                      "outline-color:rgb(255, 170, 127);\n"
                                      "outline-offset:1px;\n"
                                      "}")

        self.gridLayout_2.addWidget(self.lineEdit_5, 5, 1, 1, 1)

        self.lineEdit_17 = QLineEdit(self.centralwidget)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setStyleSheet(u"#lineEdit_17{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_17, 10, 3, 1, 1)

        self.label_69 = QLabel(self.centralwidget)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setStyleSheet(u"#label_69{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_69, 11, 6, 1, 1)

        self.label_61 = QLabel(self.centralwidget)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"#label_61{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_61, 10, 6, 1, 1)

        self.label_48 = QLabel(self.centralwidget)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"#label_48{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_48, 9, 6, 1, 1)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"#lineEdit_3{\n"
                                      "background-color:rgba(0, 170, 255, 140);\n"
                                      "color:rgb(85, 255, 255);\n"
                                      "font: 11pt \"\u9ed1\u4f53\";\n"
                                      "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                      "border-style:solid;\n"
                                      "border-width:1px;\n"
                                      "border-color:rgba(255, 170, 0,255);\n"
                                      "border-radius:6px;\n"
                                      "outline-style:solid;\n"
                                      "outline-width:1px;\n"
                                      "outline-color:rgb(255, 170, 127);\n"
                                      "outline-offset:1px;\n"
                                      "}")

        self.gridLayout_2.addWidget(self.lineEdit_3, 3, 1, 1, 1)

        self.label_40 = QLabel(self.centralwidget)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"#label_40{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_40, 7, 8, 1, 1)

        self.lineEdit_21 = QLineEdit(self.centralwidget)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setStyleSheet(u"#lineEdit_21{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_21, 2, 5, 1, 1)

        self.lineEdit_37 = QLineEdit(self.centralwidget)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setStyleSheet(u"#lineEdit_37{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_37, 5, 9, 1, 1)

        self.label_37 = QLabel(self.centralwidget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"#label_37{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_37, 4, 8, 1, 1)

        self.lineEdit_12 = QLineEdit(self.centralwidget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setStyleSheet(u"#lineEdit_12{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_12, 3, 3, 1, 1)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setStyleSheet(u"#label_14{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_14, 0, 4, 1, 2)

        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"#label_29{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_29, 6, 4, 1, 1)

        self.lineEdit_48 = QLineEdit(self.centralwidget)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        self.lineEdit_48.setStyleSheet(u"#lineEdit_48{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_48, 9, 7, 1, 1)

        self.lineEdit_23 = QLineEdit(self.centralwidget)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setStyleSheet(u"#lineEdit_23{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_23, 4, 5, 1, 1)

        self.lineEdit_44 = QLineEdit(self.centralwidget)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setStyleSheet(u"#lineEdit_44{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_44, 4, 7, 1, 1)

        self.lineEdit_45 = QLineEdit(self.centralwidget)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        self.lineEdit_45.setStyleSheet(u"#lineEdit_45{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_45, 5, 7, 1, 1)

        self.label_70 = QLabel(self.centralwidget)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"#label_70{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_70, 12, 8, 1, 1)

        self.lineEdit_13 = QLineEdit(self.centralwidget)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setStyleSheet(u"#lineEdit_13{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_13, 5, 3, 1, 1)

        self.lineEdit_39 = QLineEdit(self.centralwidget)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setStyleSheet(u"#lineEdit_39{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_39, 7, 9, 1, 1)

        self.lineEdit_52 = QLineEdit(self.centralwidget)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setStyleSheet(u"#lineEdit_52{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_52, 13, 7, 1, 1)

        self.lineEdit_26 = QLineEdit(self.centralwidget)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setStyleSheet(u"#lineEdit_26{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_26, 7, 5, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"#label_6{\n"
                                   "color:rgb(85, 255, 255);\n"
                                   "font: 11pt \"\u9ed1\u4f53\";\n"
                                   "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                   "}")

        self.gridLayout_2.addWidget(self.label_6, 7, 0, 1, 1)

        self.lineEdit_22 = QLineEdit(self.centralwidget)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setStyleSheet(u"#lineEdit_22{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_22, 3, 5, 1, 1)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"#label_16{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_16, 6, 2, 1, 1)

        self.label_71 = QLabel(self.centralwidget)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"#label_71{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_71, 12, 6, 1, 1)

        self.lineEdit_16 = QLineEdit(self.centralwidget)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setStyleSheet(u"#lineEdit_16{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_16, 9, 3, 1, 1)

        self.label_67 = QLabel(self.centralwidget)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"#label_67{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_67, 10, 8, 1, 1)

        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"#label_20{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_20, 12, 4, 1, 1)

        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"#label_23{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_23, 1, 6, 1, 1)

        self.label_35 = QLabel(self.centralwidget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"#label_35{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_35, 13, 4, 1, 1)

        self.lineEdit_10 = QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"#lineEdit_10{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_10, 1, 3, 1, 1)

        self.lineEdit_30 = QLineEdit(self.centralwidget)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setStyleSheet(u"#lineEdit_30{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_30, 11, 5, 1, 1)

        self.lineEdit_15 = QLineEdit(self.centralwidget)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setStyleSheet(u"#lineEdit_15{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_15, 7, 3, 1, 1)

        self.lineEdit_14 = QLineEdit(self.centralwidget)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setStyleSheet(u"#lineEdit_14{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_14, 6, 3, 1, 1)

        self.lineEdit_47 = QLineEdit(self.centralwidget)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        self.lineEdit_47.setStyleSheet(u"#lineEdit_47{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_47, 8, 7, 1, 1)

        self.lineEdit_41 = QLineEdit(self.centralwidget)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setStyleSheet(u"#lineEdit_41{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_41, 1, 7, 1, 1)

        self.lineEdit_42 = QLineEdit(self.centralwidget)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setStyleSheet(u"#lineEdit_42{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_42, 2, 7, 1, 1)

        self.label_41 = QLabel(self.centralwidget)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"#label_41{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_41, 10, 2, 1, 1)

        self.lineEdit_35 = QLineEdit(self.centralwidget)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setStyleSheet(u"#lineEdit_35{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_35, 3, 9, 1, 1)

        self.lineEdit_53 = QLineEdit(self.centralwidget)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setStyleSheet(u"#lineEdit_53{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_53, 10, 9, 1, 1)

        self.lineEdit_9 = QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"#lineEdit_9{\n"
                                      "background-color:rgba(0, 170, 255, 140);\n"
                                      "color:rgb(85, 255, 255);\n"
                                      "font: 11pt \"\u9ed1\u4f53\";\n"
                                      "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                      "border-style:solid;\n"
                                      "border-width:1px;\n"
                                      "border-color:rgba(255, 170, 0,255);\n"
                                      "border-radius:6px;\n"
                                      "outline-style:solid;\n"
                                      "outline-width:1px;\n"
                                      "outline-color:rgb(255, 170, 127);\n"
                                      "outline-offset:1px;\n"
                                      "}")

        self.gridLayout_2.addWidget(self.lineEdit_9, 9, 1, 1, 1)

        self.lineEdit_55 = QLineEdit(self.centralwidget)
        self.lineEdit_55.setObjectName(u"lineEdit_55")
        self.lineEdit_55.setStyleSheet(u"#lineEdit_55{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_55, 12, 9, 1, 1)

        self.lineEdit_36 = QLineEdit(self.centralwidget)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setStyleSheet(u"#lineEdit_36{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_36, 4, 9, 1, 1)

        self.lineEdit_18 = QLineEdit(self.centralwidget)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setStyleSheet(u"#lineEdit_18{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_18, 11, 3, 1, 1)

        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"#label_19{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_19, 11, 4, 1, 1)

        self.label_68 = QLabel(self.centralwidget)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"#label_68{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_68, 11, 8, 1, 1)

        self.lineEdit_8 = QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"#lineEdit_8{\n"
                                      "background-color:rgba(0, 170, 255, 140);\n"
                                      "color:rgb(85, 255, 255);\n"
                                      "font: 11pt \"\u9ed1\u4f53\";\n"
                                      "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                      "border-style:solid;\n"
                                      "border-width:1px;\n"
                                      "border-color:rgba(255, 170, 0,255);\n"
                                      "border-radius:6px;\n"
                                      "outline-style:solid;\n"
                                      "outline-width:1px;\n"
                                      "outline-color:rgb(255, 170, 127);\n"
                                      "outline-offset:1px;\n"
                                      "}")

        self.gridLayout_2.addWidget(self.lineEdit_8, 8, 1, 1, 1)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"#label_15{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_15, 5, 2, 1, 1)

        self.lineEdit_27 = QLineEdit(self.centralwidget)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setStyleSheet(u"#lineEdit_27{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_27, 8, 5, 1, 1)

        self.lineEdit_25 = QLineEdit(self.centralwidget)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setStyleSheet(u"#lineEdit_25{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_25, 6, 5, 1, 1)

        self.label_46 = QLabel(self.centralwidget)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"#label_46{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_46, 7, 6, 1, 2)

        self.label_50 = QLabel(self.centralwidget)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"#label_50{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_50, 5, 0, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"#label_8{\n"
                                   "color:rgb(85, 255, 255);\n"
                                   "font: 11pt \"\u9ed1\u4f53\";\n"
                                   "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                   "}")

        self.gridLayout_2.addWidget(self.label_8, 9, 0, 1, 1)

        self.label_36 = QLabel(self.centralwidget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"#label_36{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_36, 2, 6, 1, 1)

        self.lineEdit_29 = QLineEdit(self.centralwidget)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setStyleSheet(u"#lineEdit_29{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_29, 10, 5, 1, 1)

        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"#label_25{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_25, 2, 8, 1, 1)

        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"#label_22{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_22, 1, 8, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"#label_7{\n"
                                   "color:rgb(85, 255, 255);\n"
                                   "font: 11pt \"\u9ed1\u4f53\";\n"
                                   "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                   "}")

        self.gridLayout_2.addWidget(self.label_7, 8, 0, 1, 1)

        self.lineEdit_38 = QLineEdit(self.centralwidget)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setStyleSheet(u"#lineEdit_38{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_38, 6, 9, 1, 1)

        self.lineEdit_11 = QLineEdit(self.centralwidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setStyleSheet(u"#lineEdit_11{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_11, 2, 3, 1, 1)

        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"#label_28{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_28, 5, 4, 1, 1)

        self.lineEdit_49 = QLineEdit(self.centralwidget)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        self.lineEdit_49.setStyleSheet(u"#lineEdit_49{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_49, 10, 7, 1, 1)

        self.label_60 = QLabel(self.centralwidget)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"#label_60{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_60, 12, 2, 1, 1)

        self.lineEdit_31 = QLineEdit(self.centralwidget)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setStyleSheet(u"#lineEdit_31{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_31, 12, 5, 1, 1)

        self.lineEdit_46 = QLineEdit(self.centralwidget)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        self.lineEdit_46.setStyleSheet(u"#lineEdit_46{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_46, 6, 7, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"#lineEdit{\n"
                                    "background-color:rgba(0, 170, 255, 140);\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "border-style:solid;\n"
                                    "border-width:1px;\n"
                                    "border-color:rgba(255, 170, 0,255);\n"
                                    "border-radius:6px;\n"
                                    "outline-style:solid;\n"
                                    "outline-width:1px;\n"
                                    "outline-color:rgb(255, 170, 127);\n"
                                    "outline-offset:1px;\n"
                                    "}")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_58 = QLabel(self.centralwidget)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"#label_58{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_58, 8, 8, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"#label_2{\n"
                                   "color:rgb(85, 255, 255);\n"
                                   "font: 11pt \"\u9ed1\u4f53\";\n"
                                   "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                   "}")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"#label_11{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_11, 1, 2, 1, 1)

        self.label_45 = QLabel(self.centralwidget)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"#label_45{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_45, 5, 6, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"#label_5{\n"
                                   "color:rgb(85, 255, 255);\n"
                                   "font: 11pt \"\u9ed1\u4f53\";\n"
                                   "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                   "}")

        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"#lineEdit_7{\n"
                                      "background-color:rgba(0, 170, 255, 140);\n"
                                      "color:rgb(85, 255, 255);\n"
                                      "font: 11pt \"\u9ed1\u4f53\";\n"
                                      "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                      "border-style:solid;\n"
                                      "border-width:1px;\n"
                                      "border-color:rgba(255, 170, 0,255);\n"
                                      "border-radius:6px;\n"
                                      "outline-style:solid;\n"
                                      "outline-width:1px;\n"
                                      "outline-color:rgb(255, 170, 127);\n"
                                      "outline-offset:1px;\n"
                                      "}")

        self.gridLayout_2.addWidget(self.lineEdit_7, 7, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"#label_3{\n"
                                   "color:rgb(85, 255, 255);\n"
                                   "font: 11pt \"\u9ed1\u4f53\";\n"
                                   "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                   "}")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"#label_4{\n"
                                   "color:rgb(85, 255, 255);\n"
                                   "font: 11pt \"\u9ed1\u4f53\";\n"
                                   "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                   "}")

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"#label_10{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_10, 4, 2, 1, 2)

        self.label_43 = QLabel(self.centralwidget)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"#label_43{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_43, 3, 6, 1, 1)

        self.label_39 = QLabel(self.centralwidget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"#label_39{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_39, 6, 8, 1, 1)

        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"#label_17{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_17, 7, 2, 1, 1)

        self.lineEdit_20 = QLineEdit(self.centralwidget)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setStyleSheet(u"#lineEdit_20{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_20, 1, 5, 1, 1)

        self.lineEdit_34 = QLineEdit(self.centralwidget)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setStyleSheet(u"#lineEdit_34{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_34, 2, 9, 1, 1)

        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"#label_31{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_31, 8, 4, 1, 1)

        self.label_49 = QLabel(self.centralwidget)
        self.label_49.setObjectName(u"label_49")
        sizePolicy.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy)
        self.label_49.setStyleSheet(u"#label_49{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_49, 0, 6, 1, 2)

        self.label_33 = QLabel(self.centralwidget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"#label_33{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_33, 9, 2, 1, 1)

        self.label_47 = QLabel(self.centralwidget)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"#label_47{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_47, 8, 6, 1, 1)

        self.lineEdit_19 = QLineEdit(self.centralwidget)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setStyleSheet(u"#lineEdit_19{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")

        self.gridLayout_2.addWidget(self.lineEdit_19, 12, 3, 1, 1)

        self.label_51 = QLabel(self.centralwidget)
        self.label_51.setObjectName(u"label_51")
        sizePolicy.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy)
        self.label_51.setStyleSheet(u"#label_51{\n"
                                    "color:rgb(85, 255, 255);\n"
                                    "font: 11pt \"\u9ed1\u4f53\";\n"
                                    "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                    "}")

        self.gridLayout_2.addWidget(self.label_51, 0, 0, 1, 2)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setStyleSheet(u"#progressBar{\n"
                                       "background-color:rgba(0, 170, 255, 140);\n"
                                       "color:rgb(85, 255, 255);\n"
                                       "font: 11pt \"\u9ed1\u4f53\";\n"
                                       "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                       "border-style:solid;\n"
                                       "border-width:1px;\n"
                                       "border-color:rgba(255, 170, 0,255);\n"
                                       "border-radius:6px;\n"
                                       "outline-style:solid;\n"
                                       "outline-width:1px;\n"
                                       "outline-color:rgb(255, 170, 127);\n"
                                       "outline-offset:1px;\n"
                                       "}")
        self.progressBar.setValue(0)

        self.horizontalLayout.addWidget(self.progressBar)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"#pushButton_2:hover{\n"
                                        "background-color:rgba(0, 136, 204, 90);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_2:pressed{\n"
                                        "background-color:rgba(0, 136, 204, 40);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_2{\n"
                                        "background-color:rgba(0, 170, 255, 140);\n"
                                        "color:rgb(85, 255, 255);\n"
                                        "font: 11pt \"\u9ed1\u4f53\";\n"
                                        "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-color:rgba(255, 170, 0,255);\n"
                                        "border-radius:6px;\n"
                                        "outline-style:solid;\n"
                                        "outline-width:1px;\n"
                                        "outline-color:rgb(255, 170, 127);\n"
                                        "outline-offset:1px;\n"
                                        "}")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"#pushButton_3:hover{\n"
                                        "background-color:rgba(0, 136, 204, 90);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_3:pressed{\n"
                                        "background-color:rgba(0, 136, 204, 40);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_3{\n"
                                        "background-color:rgba(0, 170, 255, 140);\n"
                                        "color:rgb(85, 255, 255);\n"
                                        "font: 11pt \"\u9ed1\u4f53\";\n"
                                        "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-color:rgba(255, 170, 0,255);\n"
                                        "border-radius:6px;\n"
                                        "outline-style:solid;\n"
                                        "outline-width:1px;\n"
                                        "outline-color:rgb(255, 170, 127);\n"
                                        "outline-offset:1px;\n"
                                        "}")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"#pushButton_4:hover{\n"
                                        "background-color:rgba(0, 136, 204, 90);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_4:pressed{\n"
                                        "background-color:rgba(0, 136, 204, 40);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_4{\n"
                                        "background-color:rgba(0, 170, 255, 140);\n"
                                        "color:rgb(85, 255, 255);\n"
                                        "font: 11pt \"\u9ed1\u4f53\";\n"
                                        "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-color:rgba(255, 170, 0,255);\n"
                                        "border-radius:6px;\n"
                                        "outline-style:solid;\n"
                                        "outline-width:1px;\n"
                                        "outline-color:rgb(255, 170, 127);\n"
                                        "outline-offset:1px;\n"
                                        "}")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.verticalLayout_4.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"数据增强工具", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u7247\u76ee\u5f55", None))
        self.lineEdit_43.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u7070\u5ea6\u5316\u6982\u7387</p></body></html>",
                                                         None))
        self.label_52.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u968f\u673a\u8272\u8c03\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_40.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p align=\"center\">\u566a\u58f0\u7c7b</p></body></html>",
                                                        None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p align=\"center\">\u589e\u5f3a\u7c7b</p></body></html>",
                                                         None))
        self.label_53.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u5f39\u6027\u53d8\u6362\u6982\u7387</p></body></html>",
                                                         None))
        self.label_30.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>RGB\u53d8\u6362\u6982\u7387</p></body></html>",
                                                         None))
        self.label_38.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u65cb\u8f6c\u6982\u7387</p></body></html>",
                                                         None))
        self.label_13.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u4e58\u6027\u566a\u58f0\u6982\u7387</p></body></html>",
                                                         None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"<html><head/><body><p>\u5747\u503c\u6a21\u7cca\u6982\u7387</p></body></html>",
                                                      None))
        self.lineEdit_54.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u8fc7\u66dd\u6982\u7387</p></body></html>",
                                                         None))
        self.label_59.setText(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p>HE\u6982\u7387</p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u70b9\u53d8\u6362\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_24.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_51.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p align=\"center\">\u5176\u4ed6</p></body></html>",
                                                         None))
        self.label_24.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u901a\u9053\u53d8\u6362\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_50.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u4eae\u5ea6\u5bf9\u6bd4\u5ea6\u6982\u7387</p></body></html>",
                                                         None))
        self.label_72.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u586b\u5145\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_28.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_32.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u7ffb\u8f6c\u955c\u50cf\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_33.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p align=\"center\">\u5f62\u53d8\u7c7b</p></body></html>",
                                                         None))
        self.label_12.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u9ad8\u65af\u566a\u58f0\u6982\u7387</p></body></html>",
                                                         None))
        self.label_18.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>BCS\u53d8\u6362\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_17.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u7f51\u683c\u4e22\u5f03\u6982\u7387</p></body></html>",
                                                         None))
        self.label_61.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u5757\u72b6\u4e22\u5f03\u6982\u7387</p></body></html>",
                                                         None))
        self.label_48.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u50cf\u7d20\u4e22\u5f03\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u7ffb\u8f6c\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_21.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_37.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u7f29\u653e\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_12.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p align=\"center\">\u8272\u5f69\u7c7b</p></body></html>",
                                                         None))
        self.label_29.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u4f3d\u739b\u53d8\u6362\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_48.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_23.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_44.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_45.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u56fe\u50cf\u5927\u5c0f</p></body></html>",
                                                         None))
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_39.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_52.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_26.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>\u8fd0\u52a8\u6a21\u7cca\u6982\u7387</p></body></html>",
                                                        None))
        self.lineEdit_22.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u9510\u5316\u6982\u7387</p></body></html>",
                                                         None))
        self.label_71.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u88c1\u526a\u586b\u5145\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_16.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_67.setText(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u968f\u673a\u96fe</p></body></html>",
                                       None))
        self.label_20.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>HSV\u53d8\u6362\u6982\u7387</p></body></html>",
                                                         None))
        self.label_23.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u7f51\u683c\u6d17\u724c\u6982\u7387</p></body></html>",
                                                         None))
        self.label_35.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u53cd\u8272\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_30.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_15.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_14.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_47.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_41.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_42.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_41.setText(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p>CLAHE\u6982\u7387</p></body></html>",
                                       None))
        self.lineEdit_35.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_53.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_9.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_55.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_36.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_18.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>PCA\u53d8\u6362\u6982\u7387</p></body></html>",
                                                         None))
        self.label_68.setText(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u968f\u673a\u96ea</p></body></html>",
                                       None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u6d6e\u96d5\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_27.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_25.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p align=\"center\">\u6b63\u5219\u7c7b</p></body></html>",
                                                         None))
        self.label_50.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u68f1\u955c\u6a21\u7cca\u6982\u7387</p></body></html>",
                                                         None))
        self.label_8.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>\u4e0b\u91c7\u6837\u6982\u7387</p></body></html>",
                                                        None))
        self.label_36.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u900f\u89c6\u53d8\u6362\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_29.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>90\u5ea6\u65cb\u8f6c\u6982\u7387</p></body></html>",
                                                         None))
        self.label_22.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u8f6c\u7f6e\u6982\u7387</p></body></html>",
                                                         None))
        self.label_7.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>\u8d85\u50cf\u7d20\u6982\u7387</p></body></html>",
                                                        None))
        self.lineEdit_38.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u8910\u8272\u5316\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_49.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u538b\u7f29\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_31.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_46.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u955c\u50cf\u6982\u7387</p></body></html>",
                                                         None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>\u4e2d\u503c\u6a21\u7cca\u6982\u7387</p></body></html>",
                                                        None))
        self.label_11.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>ISO\u566a\u58f0\u6982\u7387</p></body></html>",
                                                         None))
        self.label_45.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u5149\u5b66\u7578\u53d8\u6982\u7387</p></body></html>",
                                                         None))
        self.label_5.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>\u9ad8\u65af\u6a21\u7cca\u6982\u7387</p></body></html>",
                                                        None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>\u9ad8\u7ea7\u6a21\u7cca\u6982\u7387</p></body></html>",
                                                        None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p>\u9ad8\u65af\u6a21\u7cca\u6982\u7387</p></body></html>",
                                                        None))
        self.label_10.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p align=\"center\">\u9510\u5316\u7c7b</p></body></html>",
                                                         None))
        self.label_43.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u7f51\u683c\u53d8\u6362\u6982\u7387</p></body></html>",
                                                         None))
        self.label_39.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u5b89\u5168\u65cb\u8f6c\u6982\u7387</p></body></html>",
                                                         None))
        self.label_17.setText(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p>USM\u6982\u7387</p></body></html>", None))
        self.lineEdit_20.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.lineEdit_34.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u8272\u8c03\u5206\u79bb\u6982\u7387</p></body></html>",
                                                         None))
        self.label_49.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p align=\"center\">\u7578\u53d8\u7c7b</p></body></html>",
                                                         None))
        self.label_33.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u5f52\u4e00\u5316\u6982\u7387</p></body></html>",
                                                         None))
        self.label_47.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p>\u901a\u9053\u4e22\u5f03\u6982\u7387</p></body></html>",
                                                         None))
        self.lineEdit_19.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow",
                                                         u"<html><head/><body><p align=\"center\">\u6a21\u7cca\u7c7b</p></body></html>",
                                                         None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5904\u7406", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u5904\u7406", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u5904\u7406", None))
        # retranslateUi

        self.lineEdit.textChanged.connect(lambda: self.testchange0())
        self.lineEdit_2.textChanged.connect(lambda: self.testchange1())
        self.lineEdit_3.textChanged.connect(lambda: self.testchange2())
        self.lineEdit_4.textChanged.connect(lambda: self.testchange3())
        self.lineEdit_5.textChanged.connect(lambda: self.testchange4())
        self.lineEdit_6.textChanged.connect(lambda: self.testchange5())
        self.lineEdit_7.textChanged.connect(lambda: self.testchange6())
        self.lineEdit_8.textChanged.connect(lambda: self.testchange7())
        self.lineEdit_9.textChanged.connect(lambda: self.testchange8())
        self.lineEdit_10.textChanged.connect(lambda: self.testchange9())
        self.lineEdit_11.textChanged.connect(lambda: self.testchange10())
        self.lineEdit_12.textChanged.connect(lambda: self.testchange11())
        self.lineEdit_13.textChanged.connect(lambda: self.testchange12())
        self.lineEdit_14.textChanged.connect(lambda: self.testchange13())
        self.lineEdit_15.textChanged.connect(lambda: self.testchange14())
        self.lineEdit_16.textChanged.connect(lambda: self.testchange15())
        self.lineEdit_17.textChanged.connect(lambda: self.testchange16())
        self.lineEdit_18.textChanged.connect(lambda: self.testchange17())
        self.lineEdit_19.textChanged.connect(lambda: self.testchange18())
        self.lineEdit_20.textChanged.connect(lambda: self.testchange19())
        self.lineEdit_21.textChanged.connect(lambda: self.testchange20())
        self.lineEdit_22.textChanged.connect(lambda: self.testchange21())
        self.lineEdit_23.textChanged.connect(lambda: self.testchange22())
        self.lineEdit_24.textChanged.connect(lambda: self.testchange23())
        self.lineEdit_25.textChanged.connect(lambda: self.testchange24())
        self.lineEdit_26.textChanged.connect(lambda: self.testchange25())
        self.lineEdit_27.textChanged.connect(lambda: self.testchange26())
        self.lineEdit_28.textChanged.connect(lambda: self.testchange27())
        self.lineEdit_29.textChanged.connect(lambda: self.testchange28())
        self.lineEdit_30.textChanged.connect(lambda: self.testchange29())
        self.lineEdit_31.textChanged.connect(lambda: self.testchange30())
        self.lineEdit_32.textChanged.connect(lambda: self.testchange31())
        self.lineEdit_33.textChanged.connect(lambda: self.testchange32())
        self.lineEdit_34.textChanged.connect(lambda: self.testchange33())
        self.lineEdit_35.textChanged.connect(lambda: self.testchange34())
        self.lineEdit_36.textChanged.connect(lambda: self.testchange35())
        self.lineEdit_37.textChanged.connect(lambda: self.testchange36())
        self.lineEdit_38.textChanged.connect(lambda: self.testchange37())
        self.lineEdit_39.textChanged.connect(lambda: self.testchange38())
        self.lineEdit_40.textChanged.connect(lambda: self.testchange39())
        self.lineEdit_41.textChanged.connect(lambda: self.testchange40())
        self.lineEdit_42.textChanged.connect(lambda: self.testchange41())
        self.lineEdit_43.textChanged.connect(lambda: self.testchange42())
        self.lineEdit_44.textChanged.connect(lambda: self.testchange43())
        self.lineEdit_45.textChanged.connect(lambda: self.testchange44())
        self.lineEdit_46.textChanged.connect(lambda: self.testchange45())
        self.lineEdit_47.textChanged.connect(lambda: self.testchange46())
        self.lineEdit_48.textChanged.connect(lambda: self.testchange47())
        self.lineEdit_49.textChanged.connect(lambda: self.testchange48())
        self.lineEdit_50.textChanged.connect(lambda: self.testchange49())
        self.lineEdit_51.textChanged.connect(lambda: self.testchange50())
        self.lineEdit_52.textChanged.connect(lambda: self.testchange51())
        self.lineEdit_53.textChanged.connect(lambda: self.testchange52())
        self.lineEdit_54.textChanged.connect( self.testchange53())
        self.pushButton_4.clicked.connect(lambda: MainWindow.close())
    @Slot()
    def testchange0(self):
        global g
        g[0] = float(self.lineEdit.text())

    @Slot()
    def testchange1(self):
        global g
        g[1] = float(self.lineEdit_2.text())

    @Slot()
    def testchange2(self):
        global g
        g[2] = float(self.lineEdit_3.text())

    @Slot()
    def testchange3(self):
        global g
        g[3] = float(self.lineEdit_4.text())

    @Slot()
    def testchange4(self):
        global g
        g[4] = float(self.lineEdit_5.text())

    @Slot()
    def testchange5(self):
        global g
        g[5] = float(self.lineEdit_6.text())

    @Slot()
    def testchange6(self):
        global g
        g[6] = float(self.lineEdit_7.text())

    @Slot()
    def testchange7(self):
        global g
        g[7] = float(self.lineEdit_8.text())

    @Slot()
    def testchange8(self):
        global g
        g[8] = float(self.lineEdit_9.text())

    @Slot()
    def testchange9(self):
        global g
        g[9] = float(self.lineEdit_10.text())

    @Slot()
    def testchange10(self):
        global g
        g[10] = float(self.lineEdit_11.text())

    @Slot()
    def testchange11(self):
        global g
        g[11] = float(self.lineEdit_12.text())

    @Slot()
    def testchange12(self):
        global g
        g[12] = float(self.lineEdit_13.text())

    @Slot()
    def testchange13(self):
        global g
        g[13] = float(self.lineEdit_14.text())

    @Slot()
    def testchange14(self):
        global g
        g[14] = float(self.lineEdit_15.text())

    @Slot()
    def testchange15(self):
        global g
        g[15] = float(self.lineEdit_16.text())

    @Slot()
    def testchange16(self):
        global g
        g[16] = float(self.lineEdit_17.text())

    @Slot()
    def testchange17(self):
        global g
        g[17] = float(self.lineEdit_18.text())

    @Slot()
    def testchange18(self):
        global g
        g[18] = float(self.lineEdit_19.text())

    @Slot()
    def testchange19(self):
        global g
        g[19] = float(self.lineEdit_20.text())

    @Slot()
    def testchange20(self):
        global g
        g[20] = float(self.lineEdit_21.text())

    @Slot()
    def testchange21(self):
        global g
        g[21] = float(self.lineEdit_22.text())

    @Slot()
    def testchange22(self):
        global g
        g[22] = float(self.lineEdit_23.text())

    @Slot()
    def testchange23(self):
        global g
        g[23] = float(self.lineEdit_24.text())

    @Slot()
    def testchange24(self):
        global g
        g[24] = float(self.lineEdit_25.text())

    @Slot()
    def testchange25(self):
        global g
        g[25] = float(self.lineEdit_26.text())

    @Slot()
    def testchange26(self):
        global g
        g[26] = float(self.lineEdit_27.text())

    @Slot()
    def testchange27(self):
        global g
        g[27] = float(self.lineEdit_28.text())

    @Slot()
    def testchange28(self):
        global g
        g[28] = float(self.lineEdit_29.text())

    @Slot()
    def testchange29(self):
        global g
        g[29] = float(self.lineEdit_30.text())

    @Slot()
    def testchange30(self):
        global g
        g[30] = float(self.lineEdit_31.text())

    @Slot()
    def testchange31(self):
        global g
        g[31] = float(self.lineEdit_32.text())

    @Slot()
    def testchange32(self):
        global g
        g[32] = float(self.lineEdit_33.text())

    @Slot()
    def testchange33(self):
        global g
        g[33] = float(self.lineEdit_34.text())

    @Slot()
    def testchange34(self):
        global g
        g[34] = float(self.lineEdit_35.text())

    @Slot()
    def testchange35(self):
        global g
        g[35] = float(self.lineEdit_36.text())

    @Slot()
    def testchange36(self):
        global g
        g[36] = float(self.lineEdit_37.text())

    @Slot()
    def testchange37(self):
        global g
        g[37] = float(self.lineEdit_38.text())

    @Slot()
    def testchange38(self):
        global g
        g[38] = float(self.lineEdit_39.text())

    @Slot()
    def testchange39(self):
        global g
        g[39] = float(self.lineEdit_40.text())

    @Slot()
    def testchange40(self):
        global g
        g[40] = float(self.lineEdit_41.text())

    @Slot()
    def testchange41(self):
        global g
        g[41] = float(self.lineEdit_42.text())

    @Slot()
    def testchange42(self):
        global g
        g[42] = float(self.lineEdit_43.text())

    @Slot()
    def testchange43(self):
        global g
        g[43] = float(self.lineEdit_44.text())

    @Slot()
    def testchange44(self):
        global g
        g[44] = float(self.lineEdit_45.text())

    @Slot()
    def testchange45(self):
        global g
        g[45] = float(self.lineEdit_46.text())

    @Slot()
    def testchange46(self):
        global g
        g[46] = float(self.lineEdit_47.text())

    @Slot()
    def testchange47(self):
        global g
        g[47] = float(self.lineEdit_48.text())

    @Slot()
    def testchange48(self):
        global g
        g[48] = float(self.lineEdit_49.text())

    @Slot()
    def testchange49(self):
        global g
        g[49] = float(self.lineEdit_50.text())

    @Slot()
    def testchange50(self):
        global g
        g[50] = float(self.lineEdit_51.text())

    @Slot()
    def testchange51(self):
        global g
        g[51] = float(self.lineEdit_52.text())

    @Slot()
    def testchange52(self):
        global g
        g[52] = float(self.lineEdit_53.text())

    @Slot()
    def testchange53(self):
        global g
        g[53] = float(self.lineEdit_54.text())


def process(extract_path):
    global g, count, imagelen
    img_list = os.listdir(extract_path)
    imagelen = int(len(glob.glob('%s/*' % extract_path)))

    transform = A.Compose([
        # 模糊
        A.Blur(p=g[0]),  # 模糊
        A.MedianBlur(p=g[1]),  # 中值模糊
        A.AdvancedBlur(p=g[2]),  # 高级模糊
        A.GaussianBlur(p=g[3]),  # 高斯模糊
        A.GlassBlur(p=g[4]),  # 棱镜模糊
        A.MedianBlur(p=g[5]),  # 中值模糊
        A.MotionBlur(p=g[6]),  # 运动模糊
        A.Superpixels(p=g[7]),  # 超像素
        A.Downscale(p=g[8]),  # 下采样
        # 噪声
        A.ISONoise(p=g[9]),  # ISO噪声
        A.GaussNoise(p=g[10]),  # 高斯噪声
        A.MultiplicativeNoise(p=g[11]),  # 乘性噪声
        # 锐化
        A.Emboss(p=g[12]),  # 浮雕
        A.Sharpen(p=g[13]),  # 锐化
        A.UnsharpMask(p=g[14]),  # 非锐化
        # 增强
        A.Normalize(p=g[15]),  # 归一化
        A.CLAHE(p=g[16], clip_limit=1),  # 自适应直方图均衡化
        A.Equalize(p=g[17]),  # 直方图均衡化
        A.ImageCompression(p=g[18]),  # 压缩
        # 颜色
        A.Solarize(p=g[19]),  # 过曝
        A.RandomBrightnessContrast(p=g[20]),  # 随机亮度对比度
        A.RandomToneCurve(p=g[21]),  # 随机色调
        A.ToGray(p=g[22]),  # 灰度化
        A.ToSepia(p=g[23]),  # 褐色化
        A.RandomGamma(p=g[24]),  # 随机伽玛
        A.RGBShift(p=g[25]),  # RGB变换
        A.Posterize(p=g[26]),  # 色调分离
        A.ChannelShuffle(p=g[27]),  # 通道随机化
        A.ColorJitter(p=g[28]),  # BCS变换
        A.FancyPCA(p=g[29]),  # PCA变换
        A.HueSaturationValue(p=g[30]),  # HSV变换
        A.InvertImg(p=g[31]),  # 反色

        # 变换
        A.Transpose(p=g[32]),  # 转置
        A.RandomRotate90(p=g[33]),  # 随机90度旋转
        A.Flip(p=g[34]),  # 翻转和镜像
        A.RandomScale(p=g[35]),  # 随机缩放
        A.Rotate(p=g[36]),  # 旋转
        A.SafeRotate(p=g[37]),  # 安全旋转
        A.VerticalFlip(p=g[38]),  # 上下翻转
        A.HorizontalFlip(p=g[39]),  # 水平翻转
        # 畸变
        A.RandomGridShuffle(p=g[40]),  # 随机网格变换
        A.Perspective(p=g[41]),  # 透视变换
        A.GridDistortion(p=g[42]),  # 网格变换
        A.PiecewiseAffine(p=g[43]),  # 点仿射变换
        A.OpticalDistortion(p=g[44]),  # 光学畸变
        A.ElasticTransform(p=g[45]),  # 弹性变换
        # 正则
        A.ChannelDropout(p=g[46]),  # 通道丢弃
        A.PixelDropout(p=g[47]),  # 像素丢弃
        A.CoarseDropout(p=g[48]),  # 块状丢弃
        A.GridDropout(p=g[49], unit_size_max=6, unit_size_min=2),  # 网格丢弃
        A.CropAndPad(p=g[50], px=(0, 6)),  # 裁剪加填充
        A.PadIfNeeded(p=g[51]),  # 填充
        # 其他
        A.RandomFog(p=g[52]),
        A.RandomSnow(p=g[53]),
        A.Resize(p=g[56], height=640, width=640),  # 调整大小
    ])
    for i in img_list:
        img = cv2.imread(os.path.join(extract_path, i))
        img1 = transform(image=np.array(img))['image']
        cv2.imwrite(extract_path + str(count) + '.jpg', img1)
        count += 1
        c = int((count / imagelen)*100)
        ui.progressBar.setValue(c)

if __name__ == '__main__':
    g = [0.0 for i in range(58)]
    extract_path = 'c:'
    count = 1
    imagelen = 1


    def var():
        global extract_path
        extract_path = QFileDialog.getExistingDirectory()


    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('111.ico'))
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    ui.pushButton.clicked.connect(lambda: var())
    ui.pushButton_2.clicked.connect(lambda: process(extract_path))
    mainWindow.show()
    sys.exit(app.exec())
