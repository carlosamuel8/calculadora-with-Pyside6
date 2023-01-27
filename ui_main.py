# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import resource_rc

class Ui_Mainwindow(object):
    def setupUi(self, Mainwindow):
        if not Mainwindow.objectName():
            Mainwindow.setObjectName(u"Mainwindow")
        Mainwindow.resize(373, 403)
        icon = QIcon()
        icon.addFile(u"iconjanela1.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Mainwindow.setWindowIcon(icon)
        self.centralwidget = QWidget(Mainwindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid black;\n"
"	font-size: 30px;\n"
"	color: black;\n"
"	background-color:white;\n"
"	border-radius: 12px;\n"
"	font: 22pt \"Bahnschrift\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(61,61,61);\n"
"	background-color: rgb(238,238,238);\n"
"}\n"
"\n"
"QWidget#centralwidget{\n"
"	background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0.0681818 rgba(203, 203, 203, 255), stop:0.514124 rgba(232, 232, 232, 255), stop:0.931818 rgba(203, 203, 203, 255));\n"
"}\n"
"\n"
"QLabel#visor{\n"
"	border: 1px solid black;\n"
"	font-size: 30px;\n"
"	color: black;\n"
"	background-color:white;\n"
"	border-radius: 11px;\n"
"}\n"
"\n"
"QPushButton#btdelete{\n"
"	font-size: 20px;\n"
"	color: black;\n"
"	background-color:red;\n"
"	border-radius: 12px;\n"
"	box-shadow:  ;\n"
"}\n"
"QPushButton#btdelete:hover{\n"
"	color: rgb(61,61,61);\n"
"	background-color: rgb(238,238,238);\n"
"}\n"
"\n"
"QPushButton#btsoma{\n"
"	font-size: 20px;\n"
"	color: black;\n"
"	background-color: rg"
                        "b(53, 255, 60);\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton#btsoma:hover{\n"
"	color: rgb(61,61,61);\n"
"	background-color: rgb(238,238,238);\n"
"}\n"
"\n"
"QPushButton#btigual{\n"
"	font-size: 20px;\n"
"	background-color: rgb(255, 226, 62);\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton#btigual:hover{\n"
"	color: rgb(61,61,61);\n"
"	background-color: rgb(238,238,238);\n"
"}\n"
"\n"
"QPushButton#btce{\n"
"	font-size: 20px;\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton#btce:hover{\n"
"	color: rgb(61,61,61);\n"
"	background-color: rgb(238,238,238);\n"
"}\n"
"\n"
"")
        self.visor = QLabel(self.centralwidget)
        self.visor.setObjectName(u"visor")
        self.visor.setGeometry(QRect(10, 20, 351, 71))
        self.visor.setStyleSheet(u"QLabel#visor{\n"
"	border: 1px solid black;\n"
"	color: black;\n"
"	background-color:white;\n"
"	border-radius: 11px;\n"
"	font: 30pt \"Bahnschrift\";\n"
"}")
        self.visor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 110, 351, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bt2 = QPushButton(self.gridLayoutWidget)
        self.bt2.setObjectName(u"bt2")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(13)
        sizePolicy.setHeightForWidth(self.bt2.sizePolicy().hasHeightForWidth())
        self.bt2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt2, 2, 1, 1, 1)

        self.btdiv = QPushButton(self.gridLayoutWidget)
        self.btdiv.setObjectName(u"btdiv")
        sizePolicy.setHeightForWidth(self.btdiv.sizePolicy().hasHeightForWidth())
        self.btdiv.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btdiv, 1, 3, 1, 1)

        self.btponto = QPushButton(self.gridLayoutWidget)
        self.btponto.setObjectName(u"btponto")
        sizePolicy.setHeightForWidth(self.btponto.sizePolicy().hasHeightForWidth())
        self.btponto.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btponto, 3, 2, 1, 1)

        self.bt9 = QPushButton(self.gridLayoutWidget)
        self.bt9.setObjectName(u"bt9")
        sizePolicy.setHeightForWidth(self.bt9.sizePolicy().hasHeightForWidth())
        self.bt9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt9, 0, 2, 1, 1)

        self.bt7 = QPushButton(self.gridLayoutWidget)
        self.bt7.setObjectName(u"bt7")
        sizePolicy.setHeightForWidth(self.bt7.sizePolicy().hasHeightForWidth())
        self.bt7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt7, 0, 0, 1, 1)

        self.btigual = QPushButton(self.gridLayoutWidget)
        self.btigual.setObjectName(u"btigual")
        sizePolicy.setHeightForWidth(self.btigual.sizePolicy().hasHeightForWidth())
        self.btigual.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btigual, 3, 3, 1, 1)

        self.bt6 = QPushButton(self.gridLayoutWidget)
        self.bt6.setObjectName(u"bt6")
        sizePolicy.setHeightForWidth(self.bt6.sizePolicy().hasHeightForWidth())
        self.bt6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt6, 1, 2, 1, 1)

        self.bt5 = QPushButton(self.gridLayoutWidget)
        self.bt5.setObjectName(u"bt5")
        sizePolicy.setHeightForWidth(self.bt5.sizePolicy().hasHeightForWidth())
        self.bt5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt5, 1, 1, 1, 1)

        self.btsub = QPushButton(self.gridLayoutWidget)
        self.btsub.setObjectName(u"btsub")
        sizePolicy.setHeightForWidth(self.btsub.sizePolicy().hasHeightForWidth())
        self.btsub.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btsub, 2, 3, 1, 1)

        self.btmult = QPushButton(self.gridLayoutWidget)
        self.btmult.setObjectName(u"btmult")
        sizePolicy.setHeightForWidth(self.btmult.sizePolicy().hasHeightForWidth())
        self.btmult.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u"asterisco.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btmult.setIcon(icon1)
        self.btmult.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.btmult, 1, 4, 1, 1)

        self.bt1 = QPushButton(self.gridLayoutWidget)
        self.bt1.setObjectName(u"bt1")
        sizePolicy.setHeightForWidth(self.bt1.sizePolicy().hasHeightForWidth())
        self.bt1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt1, 2, 0, 1, 1)

        self.btce = QPushButton(self.gridLayoutWidget)
        self.btce.setObjectName(u"btce")
        sizePolicy.setHeightForWidth(self.btce.sizePolicy().hasHeightForWidth())
        self.btce.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btce, 0, 3, 1, 1)

        self.btdelete = QPushButton(self.gridLayoutWidget)
        self.btdelete.setObjectName(u"btdelete")
        sizePolicy.setHeightForWidth(self.btdelete.sizePolicy().hasHeightForWidth())
        self.btdelete.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u"deleteicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btdelete.setIcon(icon2)
        self.btdelete.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.btdelete, 0, 4, 1, 1)

        self.bt8 = QPushButton(self.gridLayoutWidget)
        self.bt8.setObjectName(u"bt8")
        sizePolicy.setHeightForWidth(self.bt8.sizePolicy().hasHeightForWidth())
        self.bt8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt8, 0, 1, 1, 1)

        self.bt3 = QPushButton(self.gridLayoutWidget)
        self.bt3.setObjectName(u"bt3")
        sizePolicy.setHeightForWidth(self.bt3.sizePolicy().hasHeightForWidth())
        self.bt3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt3, 2, 2, 1, 1)

        self.bt4 = QPushButton(self.gridLayoutWidget)
        self.bt4.setObjectName(u"bt4")
        sizePolicy.setHeightForWidth(self.bt4.sizePolicy().hasHeightForWidth())
        self.bt4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt4, 1, 0, 1, 1)

        self.bt0 = QPushButton(self.gridLayoutWidget)
        self.bt0.setObjectName(u"bt0")
        sizePolicy.setHeightForWidth(self.bt0.sizePolicy().hasHeightForWidth())
        self.bt0.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.bt0, 3, 0, 1, 2)

        self.btsoma = QPushButton(self.gridLayoutWidget)
        self.btsoma.setObjectName(u"btsoma")
        self.btsoma.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btsoma.sizePolicy().hasHeightForWidth())
        self.btsoma.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btsoma, 2, 4, 2, 1)

        Mainwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Mainwindow)

        QMetaObject.connectSlotsByName(Mainwindow)
    # setupUi

    def retranslateUi(self, Mainwindow):
        Mainwindow.setWindowTitle(QCoreApplication.translate("Mainwindow", u"Calculadora", None))
        self.visor.setText("")
        self.bt2.setText(QCoreApplication.translate("Mainwindow", u"2", None))
        self.btdiv.setText(QCoreApplication.translate("Mainwindow", u"/", None))
        self.btponto.setText(QCoreApplication.translate("Mainwindow", u".", None))
        self.bt9.setText(QCoreApplication.translate("Mainwindow", u"9", None))
        self.bt7.setText(QCoreApplication.translate("Mainwindow", u"7", None))
        self.btigual.setText(QCoreApplication.translate("Mainwindow", u"=", None))
        self.bt6.setText(QCoreApplication.translate("Mainwindow", u"6", None))
        self.bt5.setText(QCoreApplication.translate("Mainwindow", u"5", None))
        self.btsub.setText(QCoreApplication.translate("Mainwindow", u"-", None))
        self.btmult.setText("")
        self.bt1.setText(QCoreApplication.translate("Mainwindow", u"1", None))
        self.btce.setText(QCoreApplication.translate("Mainwindow", u"CE", None))
        self.btdelete.setText("")
        self.bt8.setText(QCoreApplication.translate("Mainwindow", u"8", None))
        self.bt3.setText(QCoreApplication.translate("Mainwindow", u"3", None))
        self.bt4.setText(QCoreApplication.translate("Mainwindow", u"4", None))
        self.bt0.setText(QCoreApplication.translate("Mainwindow", u"0", None))
        self.btsoma.setText(QCoreApplication.translate("Mainwindow", u"+", None))
    # retranslateUi

