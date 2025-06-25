# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_file = QLineEdit(self.centralwidget)
        self.line_file.setObjectName(u"line_file")
        self.line_file.setEnabled(False)
        self.line_file.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.line_file)

        self.btn_file = QPushButton(self.centralwidget)
        self.btn_file.setObjectName(u"btn_file")

        self.horizontalLayout_2.addWidget(self.btn_file)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_validate = QPushButton(self.centralwidget)
        self.btn_validate.setObjectName(u"btn_validate")

        self.horizontalLayout.addWidget(self.btn_validate)

        self.btn_fix = QPushButton(self.centralwidget)
        self.btn_fix.setObjectName(u"btn_fix")

        self.horizontalLayout.addWidget(self.btn_fix)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, -1, 20, -1)
        self.checkKommune = QCheckBox(self.centralwidget)
        self.checkKommune.setObjectName(u"checkKommune")
        self.checkKommune.setChecked(True)

        self.horizontalLayout_9.addWidget(self.checkKommune)

        self.checkDato = QCheckBox(self.centralwidget)
        self.checkDato.setObjectName(u"checkDato")
        self.checkDato.setChecked(True)
        self.checkDato.setTristate(False)

        self.horizontalLayout_9.addWidget(self.checkDato)

        self.checkPersonnr = QCheckBox(self.centralwidget)
        self.checkPersonnr.setObjectName(u"checkPersonnr")
        self.checkPersonnr.setChecked(True)

        self.horizontalLayout_9.addWidget(self.checkPersonnr)

        self.checkNavn = QCheckBox(self.centralwidget)
        self.checkNavn.setObjectName(u"checkNavn")
        self.checkNavn.setChecked(True)

        self.horizontalLayout_9.addWidget(self.checkNavn)

        self.horizontalLayout_9.setStretch(0, 10)
        self.horizontalLayout_9.setStretch(1, 10)
        self.horizontalLayout_9.setStretch(2, 10)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.text_result = QTextEdit(self.centralwidget)
        self.text_result.setObjectName(u"text_result")
        self.text_result.setEnabled(True)
        self.text_result.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.text_result.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.text_result)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuPRValidator = QMenu(self.menubar)
        self.menuPRValidator.setObjectName(u"menuPRValidator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPRValidator.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_file.setText(QCoreApplication.translate("MainWindow", u"Last opp fil", None))
        self.btn_validate.setText(QCoreApplication.translate("MainWindow", u"Valider felter", None))
        self.btn_fix.setText(QCoreApplication.translate("MainWindow", u"Korriger felter", None))
        self.checkKommune.setText(QCoreApplication.translate("MainWindow", u"Valider kommune", None))
        self.checkDato.setText(QCoreApplication.translate("MainWindow", u"Valider f\u00f8dselsdato", None))
        self.checkPersonnr.setText(QCoreApplication.translate("MainWindow", u"Valider personnummer", None))
        self.checkNavn.setText(QCoreApplication.translate("MainWindow", u"Valider navn", None))
        self.menuPRValidator.setTitle(QCoreApplication.translate("MainWindow", u"PRValidator ", None))
    # retranslateUi

