# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(603, 704)
        self.btn_search_devices = QPushButton(Form)
        self.btn_search_devices.setObjectName(u"btn_search_devices")
        self.btn_search_devices.setGeometry(QRect(280, 590, 100, 32))
        self.btn_exit = QPushButton(Form)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(420, 590, 100, 32))
        self.lbl_config_select = QLabel(Form)
        self.lbl_config_select.setObjectName(u"lbl_config_select")
        self.lbl_config_select.setGeometry(QRect(50, 20, 61, 30))
        self.btn_save_device = QPushButton(Form)
        self.btn_save_device.setObjectName(u"btn_save_device")
        self.btn_save_device.setGeometry(QRect(460, 20, 80, 32))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 110, 491, 31))
        self.lay_shop1_goods = QHBoxLayout(self.widget)
        self.lay_shop1_goods.setObjectName(u"lay_shop1_goods")
        self.lay_shop1_goods.setContentsMargins(0, 0, 0, 0)
        self.lbl_shop1_goods_config = QLabel(self.widget)
        self.lbl_shop1_goods_config.setObjectName(u"lbl_shop1_goods_config")

        self.lay_shop1_goods.addWidget(self.lbl_shop1_goods_config)

        self.txt_shop1_goods_config = QTextEdit(self.widget)
        self.txt_shop1_goods_config.setObjectName(u"txt_shop1_goods_config")

        self.lay_shop1_goods.addWidget(self.txt_shop1_goods_config)

        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 150, 491, 31))
        self.lay_price1 = QHBoxLayout(self.layoutWidget)
        self.lay_price1.setObjectName(u"lay_price1")
        self.lay_price1.setContentsMargins(0, 0, 0, 0)
        self.lbl_shop1_price_config = QLabel(self.layoutWidget)
        self.lbl_shop1_price_config.setObjectName(u"lbl_shop1_price_config")

        self.lay_price1.addWidget(self.lbl_shop1_price_config)

        self.txt_shop1_price1_config = QTextEdit(self.layoutWidget)
        self.txt_shop1_price1_config.setObjectName(u"txt_shop1_price1_config")

        self.lay_price1.addWidget(self.txt_shop1_price1_config)

        self.combo_config = QComboBox(Form)
        self.combo_config.setObjectName(u"combo_config")
        self.combo_config.setGeometry(QRect(120, 20, 321, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_search_devices.setText(QCoreApplication.translate("Form", u"\u626b\u63cf\u8bbe\u5907", None))
        self.btn_exit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.lbl_config_select.setText(QCoreApplication.translate("Form", u"\u914d\u7f6e\u9009\u62e9", None))
        self.btn_save_device.setText(QCoreApplication.translate("Form", u"\u53e6\u5b58\u914d\u7f6e", None))
        self.lbl_shop1_goods_config.setText(QCoreApplication.translate("Form", u"\u5546\u5e97\u914d\u7f6e1", None))
        self.lbl_shop1_price_config.setText(QCoreApplication.translate("Form", u"\u4ef7\u683c\u914d\u7f6e1", None))
    # retranslateUi

