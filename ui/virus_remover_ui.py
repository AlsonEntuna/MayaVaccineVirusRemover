# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'virus_remover_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(396, 230)
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_scan = QPushButton(MainWindow)
        self.btn_scan.setObjectName(u"btn_scan")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_scan.sizePolicy().hasHeightForWidth())
        self.btn_scan.setSizePolicy(sizePolicy)
        self.btn_scan.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.btn_scan)

        self.groupBox = QGroupBox(MainWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txtb_results = QTextBrowser(self.groupBox)
        self.txtb_results.setObjectName(u"txtb_results")

        self.verticalLayout_2.addWidget(self.txtb_results)


        self.verticalLayout.addWidget(self.groupBox)

        self.btn_remove_virus = QPushButton(MainWindow)
        self.btn_remove_virus.setObjectName(u"btn_remove_virus")
        self.btn_remove_virus.setEnabled(False)
        self.btn_remove_virus.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.btn_remove_virus)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Virus Remover", None))
        self.btn_scan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Results", None))
        self.btn_remove_virus.setText(QCoreApplication.translate("MainWindow", u"Resolve Virus Issue", None))
    # retranslateUi

