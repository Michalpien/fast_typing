# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FastTypingGui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FastTyping(object):
    def setupUi(self, FastTyping):
        if not FastTyping.objectName():
            FastTyping.setObjectName(u"FastTyping")
        FastTyping.resize(1020, 794)
        FastTyping.setMinimumSize(QSize(1000, 0))
        self.action_Open = QAction(FastTyping)
        self.action_Open.setObjectName(u"action_Open")
        self.centralwidget = QWidget(FastTyping)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Sunken)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ExitButton = QPushButton(self.page)
        self.ExitButton.setObjectName(u"ExitButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExitButton.sizePolicy().hasHeightForWidth())
        self.ExitButton.setSizePolicy(sizePolicy)
        self.ExitButton.setMinimumSize(QSize(0, 0))
        self.ExitButton.setMaximumSize(QSize(250, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.ExitButton.setFont(font)

        self.gridLayout_3.addWidget(self.ExitButton, 4, 0, 1, 1)

        self.StartButton = QPushButton(self.page)
        self.StartButton.setObjectName(u"StartButton")
        sizePolicy.setHeightForWidth(self.StartButton.sizePolicy().hasHeightForWidth())
        self.StartButton.setSizePolicy(sizePolicy)
        self.StartButton.setMinimumSize(QSize(0, 0))
        self.StartButton.setMaximumSize(QSize(250, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.StartButton.setFont(font1)

        self.gridLayout_3.addWidget(self.StartButton, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 225, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 5, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(200, 16777215))
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.page_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(200, 16777215))
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(200, 16777215))
        self.pushButton_4.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton_1 = QPushButton(self.page_2)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMaximumSize(QSize(200, 16777215))
        self.pushButton_1.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.BackButton = QPushButton(self.page_2)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self.BackButton, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.displayText = QTextEdit(self.page_3)
        self.displayText.setObjectName(u"displayText")
        self.displayText.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setPointSize(15)
        self.displayText.setFont(font3)
        self.displayText.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.displayText.setInputMethodHints(Qt.ImhNone)
        self.displayText.setReadOnly(True)

        self.gridLayout_4.addWidget(self.displayText, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.enterText = QTextEdit(self.page_3)
        self.enterText.setObjectName(u"enterText")
        self.enterText.setMaximumSize(QSize(16777215, 40))
        self.enterText.setFont(font3)
        self.enterText.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.enterText.setInputMethodHints(Qt.ImhNone)

        self.gridLayout_4.addWidget(self.enterText, 5, 0, 1, 1)

        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_3.setFont(font4)

        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_6 = QGridLayout(self.page_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_7 = QSpacerItem(20, 191, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_7, 1, 0, 1, 1)

        self.mistakes_label = QLabel(self.page_4)
        self.mistakes_label.setObjectName(u"mistakes_label")
        font5 = QFont()
        font5.setPointSize(20)
        self.mistakes_label.setFont(font5)

        self.gridLayout_6.addWidget(self.mistakes_label, 6, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 190, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 8, 0, 1, 1)

        self.Results = QLabel(self.page_4)
        self.Results.setObjectName(u"Results")
        font6 = QFont()
        font6.setPointSize(30)
        self.Results.setFont(font6)

        self.gridLayout_6.addWidget(self.Results, 2, 0, 1, 1, Qt.AlignHCenter)

        self.char_per_minute_label = QLabel(self.page_4)
        self.char_per_minute_label.setObjectName(u"char_per_minute_label")
        self.char_per_minute_label.setFont(font5)

        self.gridLayout_6.addWidget(self.char_per_minute_label, 4, 0, 1, 1, Qt.AlignHCenter)

        self.words_per_minute_label = QLabel(self.page_4)
        self.words_per_minute_label.setObjectName(u"words_per_minute_label")
        self.words_per_minute_label.setFont(font5)

        self.gridLayout_6.addWidget(self.words_per_minute_label, 5, 0, 1, 1, Qt.AlignHCenter)

        self.ExitButton_2 = QPushButton(self.page_4)
        self.ExitButton_2.setObjectName(u"ExitButton_2")
        self.ExitButton_2.setMinimumSize(QSize(200, 0))
        self.ExitButton_2.setMaximumSize(QSize(200, 16777215))
        font7 = QFont()
        font7.setPointSize(13)
        self.ExitButton_2.setFont(font7)

        self.gridLayout_6.addWidget(self.ExitButton_2, 7, 0, 1, 1, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        FastTyping.setCentralWidget(self.centralwidget)

        self.retranslateUi(FastTyping)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FastTyping)
    # setupUi

    def retranslateUi(self, FastTyping):
        FastTyping.setWindowTitle(QCoreApplication.translate("FastTyping", u"MainWindow", None))
        self.action_Open.setText(QCoreApplication.translate("FastTyping", u"&Open", None))
        self.ExitButton.setText(QCoreApplication.translate("FastTyping", u"Exit", None))
        self.StartButton.setText(QCoreApplication.translate("FastTyping", u"Start", None))
        self.label.setText(QCoreApplication.translate("FastTyping", u"Press \"Start\"", None))
        self.pushButton_2.setText(QCoreApplication.translate("FastTyping", u"20 sec", None))
        self.pushButton_3.setText(QCoreApplication.translate("FastTyping", u"30 sec", None))
        self.pushButton_4.setText(QCoreApplication.translate("FastTyping", u"40 sec", None))
        self.pushButton_1.setText(QCoreApplication.translate("FastTyping", u"10 sec", None))
        self.BackButton.setText(QCoreApplication.translate("FastTyping", u"Back", None))
#if QT_CONFIG(tooltip)
        self.displayText.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.enterText.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("FastTyping", u"Start typing to get started", None))
        self.mistakes_label.setText(QCoreApplication.translate("FastTyping", u"mistakes", None))
        self.Results.setText(QCoreApplication.translate("FastTyping", u"Results:", None))
        self.char_per_minute_label.setText(QCoreApplication.translate("FastTyping", u"char_per_minute", None))
        self.words_per_minute_label.setText(QCoreApplication.translate("FastTyping", u"words_per_minute", None))
        self.ExitButton_2.setText(QCoreApplication.translate("FastTyping", u"Exit", None))
    # retranslateUi

