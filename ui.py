from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


# User Interface класс
class Ui_ui(object):

    def setupUi(self, ui):
        if not ui.objectName():
            ui.setObjectName(u"ui")
        ui.resize(663, 327)
        ui.setMinimumSize(QSize(663, 327))
        ui.setMaximumSize(QSize(663, 327))

        self.centralwidget = QWidget(ui)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
                                         "color:rgb(0,0,0);\n"
                                         "background-color:#000000;\n"
                                         "}\n"
                                         "")
        self.Input = QLineEdit(self.centralwidget)
        self.Input.setObjectName(u"Input")
        self.Input.setGeometry(QRect(250, 10, 161, 21))
        self.Input.setStyleSheet(u"border-width: 1px;\n"
                                    "border-style: solid;\n"
                                    "border-color: #4fa08b;\n"
                                    "background-color: #222b2e;\n"
                                    "color: #00FF00;")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 40, 641, 271))
        self.textBrowser.setCurrentFont(QFont("Courier New"))
        self.textBrowser.setFontPointSize(9)
        self.textBrowser.setStyleSheet(u"border-width: 1px;\n"
                                       "border-style: solid;\n"
                                       "border-color: #4fa08b;\n"
                                       "background-color: #222b2e;\n"
                                       "color: #00FF00;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 11, 241, 16))
        self.label.setStyleSheet(u"color: #00FF00;")
        self.Search = QPushButton(self.centralwidget)
        self.Search.setObjectName(u"Search")
        self.Search.setGeometry(QRect(420, 10, 231, 23))
        self.Search.setStyleSheet(u"QPushButton{\n"
                                  "border-style: solid;\n"
                                  "border-color: #050a0e;\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 5px;\n"
                                  "color: #00FF00;\n"
                                  "padding: 2px;\n"
                                  "background-color: #151a1e;\n"
                                  "}\n"
                                  "QPushButton::default{\n"
                                  "border-style: solid;\n"
                                  "border-color: #050a0e;\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 5px;\n"
                                  "color: #FF0000;\n"
                                  "padding: 2px;\n"
                                  "background-color: #151a1e;;\n"
                                  "}\n"
                                  "QPushButton:hover{\n"
                                  "border-style: solid;\n"
                                  "border-color: #050a0e;\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 5px;\n"
                                  "color: #FF0000;\n"
                                  "padding: 2px;\n"
                                  "background-color: #1c1f1f;\n"
                                  "}\n"
                                  "QPushButton:pressed{\n"
                                  "border-style: solid;\n"
                                  "border-color: #050a0e;\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 5px;\n"
                                  "color: #FF0000;\n"
                                  "padding: 2px;\n"
                                  "background-color: #2c2f2f;\n"
                                  "}\n"
                                  "QPushButton:disabled{\n"
                                  "border-style: solid;\n"
                                  "border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, "
                                  "stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
                                  "border-right-color: ql"
                                  "ineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                  "stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
                                  "border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
                                  "stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
                                  "border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, "
                                  "stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
                                  "border-width: 1px;\n"
                                  "border-radius: 5px;\n"
                                  "color: #808086;\n"
                                  "padding: 2px;\n"
                                  "background-color: rgb(142,142,142);\n"
                                  "}")

        ui.setCentralWidget(self.centralwidget)

        self.retranslateUi(ui)

        QMetaObject.connectSlotsByName(ui)

    # setupUi

    def retranslateUi(self, ui):
        ui.setWindowTitle(QCoreApplication.translate("ui", u"Curse", None))
        self.textBrowser.setText(QCoreApplication.translate("ui", u"", None))
        self.label.setText(QCoreApplication.translate("ui", u"Введите стаж работы сотрудника(в месяцах):", None))
        self.Input.setText("0")
        self.Search.setText(QCoreApplication.translate("ui", u"Поиск", None))
    # retranslateUi
