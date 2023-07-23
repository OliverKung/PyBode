# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI\pybode.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pyBode(object):
    def setupUi(self, pyBode):
        pyBode.setObjectName("pyBode")
        pyBode.resize(1280, 720)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        pyBode.setFont(font)
        self.centralwidget = QtWidgets.QWidget(pyBode)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.AFG_IP = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AFG_IP.sizePolicy().hasHeightForWidth())
        self.AFG_IP.setSizePolicy(sizePolicy)
        self.AFG_IP.setObjectName("AFG_IP")
        self.verticalLayout_4.addWidget(self.AFG_IP)
        self.verticalLayout_12.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.OSC_IP = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OSC_IP.sizePolicy().hasHeightForWidth())
        self.OSC_IP.setSizePolicy(sizePolicy)
        self.OSC_IP.setObjectName("OSC_IP")
        self.verticalLayout_2.addWidget(self.OSC_IP)
        self.verticalLayout_12.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_12)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.OSC_Input = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OSC_Input.sizePolicy().hasHeightForWidth())
        self.OSC_Input.setSizePolicy(sizePolicy)
        self.OSC_Input.setObjectName("OSC_Input")
        self.OSC_Input.addItem("")
        self.OSC_Input.addItem("")
        self.OSC_Input.addItem("")
        self.OSC_Input.addItem("")
        self.verticalLayout_9.addWidget(self.OSC_Input)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_11.addWidget(self.label_9)
        self.OSC_Output = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OSC_Output.sizePolicy().hasHeightForWidth())
        self.OSC_Output.setSizePolicy(sizePolicy)
        self.OSC_Output.setObjectName("OSC_Output")
        self.OSC_Output.addItem("")
        self.OSC_Output.addItem("")
        self.OSC_Output.addItem("")
        self.OSC_Output.addItem("")
        self.verticalLayout_11.addWidget(self.OSC_Output)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.OSC_Sync = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OSC_Sync.sizePolicy().hasHeightForWidth())
        self.OSC_Sync.setSizePolicy(sizePolicy)
        self.OSC_Sync.setObjectName("OSC_Sync")
        self.OSC_Sync.addItem("")
        self.OSC_Sync.addItem("")
        self.OSC_Sync.addItem("")
        self.OSC_Sync.addItem("")
        self.verticalLayout_10.addWidget(self.OSC_Sync)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_8, 2, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.AFG_Excition = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AFG_Excition.sizePolicy().hasHeightForWidth())
        self.AFG_Excition.setSizePolicy(sizePolicy)
        self.AFG_Excition.setObjectName("AFG_Excition")
        self.AFG_Excition.addItem("")
        self.AFG_Excition.addItem("")
        self.verticalLayout_5.addWidget(self.AFG_Excition)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.AFG_Sync = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AFG_Sync.sizePolicy().hasHeightForWidth())
        self.AFG_Sync.setSizePolicy(sizePolicy)
        self.AFG_Sync.setObjectName("AFG_Sync")
        self.AFG_Sync.addItem("")
        self.AFG_Sync.addItem("")
        self.verticalLayout_6.addWidget(self.AFG_Sync)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_22.addWidget(self.label_18)
        self.Amplitude = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Amplitude.sizePolicy().hasHeightForWidth())
        self.Amplitude.setSizePolicy(sizePolicy)
        self.Amplitude.setObjectName("Amplitude")
        self.verticalLayout_22.addWidget(self.Amplitude)
        self.horizontalLayout_2.addLayout(self.verticalLayout_22)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_7, 1, 0, 1, 1)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_13.addWidget(self.label_10)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_15.addWidget(self.label_12)
        self.SampleMode = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SampleMode.sizePolicy().hasHeightForWidth())
        self.SampleMode.setSizePolicy(sizePolicy)
        self.SampleMode.setObjectName("SampleMode")
        self.SampleMode.addItem("")
        self.SampleMode.addItem("")
        self.SampleMode.addItem("")
        self.SampleMode.addItem("")
        self.verticalLayout_15.addWidget(self.SampleMode)
        self.horizontalLayout_5.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_16.addWidget(self.label_13)
        self.AverageTimes = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AverageTimes.sizePolicy().hasHeightForWidth())
        self.AverageTimes.setSizePolicy(sizePolicy)
        self.AverageTimes.setObjectName("AverageTimes")
        self.verticalLayout_16.addWidget(self.AverageTimes)
        self.horizontalLayout_5.addLayout(self.verticalLayout_16)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_13.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_13, 3, 0, 1, 1)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.SyncTriggerEnable = QtWidgets.QCheckBox(self.centralwidget)
        self.SyncTriggerEnable.setObjectName("SyncTriggerEnable")
        self.verticalLayout_17.addWidget(self.SyncTriggerEnable)
        self.LoadVNC = QtWidgets.QPushButton(self.centralwidget)
        self.LoadVNC.setObjectName("LoadVNC")
        self.verticalLayout_17.addWidget(self.LoadVNC)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setObjectName("StartButton")
        self.horizontalLayout.addWidget(self.StartButton)
        self.STOPButton = QtWidgets.QPushButton(self.centralwidget)
        self.STOPButton.setObjectName("STOPButton")
        self.horizontalLayout.addWidget(self.STOPButton)
        self.verticalLayout_17.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_17, 5, 0, 1, 1)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_18.addWidget(self.label_14)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_19.addWidget(self.label_15)
        self.StartFrequency = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartFrequency.sizePolicy().hasHeightForWidth())
        self.StartFrequency.setSizePolicy(sizePolicy)
        self.StartFrequency.setObjectName("StartFrequency")
        self.verticalLayout_19.addWidget(self.StartFrequency)
        self.horizontalLayout_6.addLayout(self.verticalLayout_19)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_20.addWidget(self.label_16)
        self.StopFrequency = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StopFrequency.sizePolicy().hasHeightForWidth())
        self.StopFrequency.setSizePolicy(sizePolicy)
        self.StopFrequency.setObjectName("StopFrequency")
        self.verticalLayout_20.addWidget(self.StopFrequency)
        self.horizontalLayout_6.addLayout(self.verticalLayout_20)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_21.addWidget(self.label_17)
        self.Points = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Points.sizePolicy().hasHeightForWidth())
        self.Points.setSizePolicy(sizePolicy)
        self.Points.setObjectName("Points")
        self.verticalLayout_21.addWidget(self.Points)
        self.horizontalLayout_6.addLayout(self.verticalLayout_21)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.verticalLayout_18.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_18, 4, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 2)
        self.gridLayout.setRowStretch(3, 2)
        self.gridLayout.setRowStretch(4, 2)
        self.gridLayout.setRowStretch(5, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.plotyWidget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.plotyWidget.setObjectName("plotyWidget")
        self.gridLayout_2.addWidget(self.plotyWidget, 0, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 8)
        pyBode.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pyBode)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menubar.setObjectName("menubar")
        pyBode.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(pyBode)
        self.statusbar.setObjectName("statusbar")
        pyBode.setStatusBar(self.statusbar)

        self.retranslateUi(pyBode)
        QtCore.QMetaObject.connectSlotsByName(pyBode)

    def retranslateUi(self, pyBode):
        _translate = QtCore.QCoreApplication.translate
        pyBode.setWindowTitle(_translate("pyBode", "pyBode GUI"))
        self.label_4.setText(_translate("pyBode", "AFG IP"))
        self.AFG_IP.setText(_translate("pyBode", "192.168.31.24"))
        self.label_3.setText(_translate("pyBode", "OSC IP"))
        self.OSC_IP.setText(_translate("pyBode", "192.168.31.32"))
        self.label_6.setText(_translate("pyBode", "OSC Channel Select"))
        self.label_7.setText(_translate("pyBode", "Input"))
        self.OSC_Input.setItemText(0, _translate("pyBode", "CH1"))
        self.OSC_Input.setItemText(1, _translate("pyBode", "CH2"))
        self.OSC_Input.setItemText(2, _translate("pyBode", "CH3"))
        self.OSC_Input.setItemText(3, _translate("pyBode", "CH4"))
        self.label_9.setText(_translate("pyBode", "Output"))
        self.OSC_Output.setItemText(0, _translate("pyBode", "CH1"))
        self.OSC_Output.setItemText(1, _translate("pyBode", "CH2"))
        self.OSC_Output.setItemText(2, _translate("pyBode", "CH3"))
        self.OSC_Output.setItemText(3, _translate("pyBode", "CH4"))
        self.label_8.setText(_translate("pyBode", "Sync"))
        self.OSC_Sync.setItemText(0, _translate("pyBode", "CH1"))
        self.OSC_Sync.setItemText(1, _translate("pyBode", "CH2"))
        self.OSC_Sync.setItemText(2, _translate("pyBode", "CH3"))
        self.OSC_Sync.setItemText(3, _translate("pyBode", "CH4"))
        self.label_5.setText(_translate("pyBode", "AFG Channel Select"))
        self.label.setText(_translate("pyBode", "Excition"))
        self.AFG_Excition.setItemText(0, _translate("pyBode", "CH1"))
        self.AFG_Excition.setItemText(1, _translate("pyBode", "CH2"))
        self.label_2.setText(_translate("pyBode", "Sync"))
        self.AFG_Sync.setItemText(0, _translate("pyBode", "CH1"))
        self.AFG_Sync.setItemText(1, _translate("pyBode", "CH2"))
        self.label_18.setText(_translate("pyBode", "Amp"))
        self.Amplitude.setText(_translate("pyBode", "1"))
        self.label_10.setText(_translate("pyBode", "Sample Channel Setting"))
        self.label_12.setText(_translate("pyBode", "Sample"))
        self.SampleMode.setItemText(0, _translate("pyBode", "normal"))
        self.SampleMode.setItemText(1, _translate("pyBode", "average"))
        self.SampleMode.setItemText(2, _translate("pyBode", "peak_detect"))
        self.SampleMode.setItemText(3, _translate("pyBode", "high_resolution"))
        self.label_13.setText(_translate("pyBode", "Average"))
        self.SyncTriggerEnable.setText(_translate("pyBode", "Sync Trigger Enable"))
        self.LoadVNC.setText(_translate("pyBode", "LOAD VNC"))
        self.StartButton.setText(_translate("pyBode", "START"))
        self.STOPButton.setText(_translate("pyBode", "STOP"))
        self.label_14.setText(_translate("pyBode", "Frequency Setting"))
        self.label_15.setText(_translate("pyBode", "Start"))
        self.StartFrequency.setText(_translate("pyBode", "1e3"))
        self.label_16.setText(_translate("pyBode", "Stop"))
        self.StopFrequency.setText(_translate("pyBode", "1e6"))
        self.label_17.setText(_translate("pyBode", "Point"))
        self.Points.setText(_translate("pyBode", "100"))
from PyQt5 import QtWebEngineWidgets
