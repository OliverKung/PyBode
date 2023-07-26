import numpy as np
import pyqtgraph as pg
import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMessageBox
from PyQt5.QtCore import QUrl,pyqtSlot,QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
import PyQt5.QtCore as QtCore
from PyQt5.QtGui import QIcon
import channelSetWindow
import ctypes,argparse,subprocess

def WarningBox(message):
    warningwindow = QMessageBox(QMessageBox.Warning,"Warning",message)
    warningwindow.exec_()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--afg-ip",type=str,default="",required=True,help="IP addr of function generator")
    parser.add_argument("--osc-ip",type=str,default="",required=True,help="IP addr of oscilliscope")
    return parser.parse_args()

class mainCode(QDialog,channelSetWindow.Ui_Dialog):
    def __init__(self,osc_ip,afg_ip):
        QDialog.__init__(self)
        channelSetWindow.Ui_Dialog.__init__(self)
        self.setupUi(self)
        self.osc_ip=osc_ip
        self.afg_ip=afg_ip
        self.AFG_CH1_LoadZ.setEnabled(False)
        self.AFG_CH2_LoadZ.setEnabled(False)
        self.AFG_CH1_LoadZ.setText("50")
        self.AFG_CH2_LoadZ.setText("50")
        self.AFG_CH1_LoadState.currentTextChanged.connect(self.on_ch1_loadstate_changed)
        self.AFG_CH2_LoadState.currentTextChanged.connect(self.on_ch2_loadstate_changed)
    @pyqtSlot()
    def on_ch1_loadstate_changed(self):
        if(self.AFG_CH1_LoadState.currentText()=="HiZ"):
            self.AFG_CH1_LoadZ.setEnabled(False)
        else:
            self.AFG_CH1_LoadZ.setEnabled(True)

    @pyqtSlot()
    def on_ch2_loadstate_changed(self):
        if(self.AFG_CH2_LoadState.currentText()=="HiZ"):
            self.AFG_CH2_LoadZ.setEnabled(False)
        else:
            self.AFG_CH2_LoadZ.setEnabled(True)
    
    @pyqtSlot()
    def on_SetButton_clicked(self):
        ch1load = self.AFG_CH1_LoadZ.text() if self.AFG_CH1_LoadState.currentText()!="HiZ" else "HZ"
        ch2load = self.AFG_CH2_LoadZ.text() if self.AFG_CH2_LoadState.currentText()!="HiZ" else "HZ"
        cmd_str =   "python channelSet.py"+\
                    " --osc-ip "+self.osc_ip+\
                    " --afg-ip "+self.afg_ip+\
                    " -o1a "+self.OSC_CH1_Atte.currentText()+\
                    " -o2a "+self.OSC_CH2_Atte.currentText()+\
                    " -o3a "+self.OSC_CH3_Atte.currentText()+\
                    " -o4a "+self.OSC_CH4_Atte.currentText()+\
                    " -o1u "+self.OSC_CH1_Unit.currentText()+\
                    " -o2u "+self.OSC_CH2_Unit.currentText()+\
                    " -o3u "+self.OSC_CH3_Unit.currentText()+\
                    " -o4u "+self.OSC_CH4_Unit.currentText()+\
                    " -a1l "+ch1load+\
                    " -a2l "+ch2load
        # print(cmd_str)
        self.channelSetProcess = subprocess.Popen(cmd_str)
        WarningBox("Set Success")
        self.accept()

    @pyqtSlot()
    def on_LoadButton_clicked(self):
        with open(".\\temp\\channelstate.csv","r") as f:
            lines=f.readlines()
            for line in lines:
                name = line.split("=")[0]
                value = line.split("=")[1].replace("\n","")
                if(name == "o1a"):self.OSC_CH1_Atte.setCurrentIndex(int(value))
                if(name == "o2a"):self.OSC_CH2_Atte.setCurrentIndex(int(value))
                if(name == "o3a"):self.OSC_CH3_Atte.setCurrentIndex(int(value))
                if(name == "o4a"):self.OSC_CH4_Atte.setCurrentIndex(int(value))
                if(name == "o1u"):self.OSC_CH1_Unit.setCurrentIndex(int(value))
                if(name == "o2u"):self.OSC_CH2_Unit.setCurrentIndex(int(value))
                if(name == "o3u"):self.OSC_CH3_Unit.setCurrentIndex(int(value))
                if(name == "o4u"):self.OSC_CH4_Unit.setCurrentIndex(int(value))
                if(name == "a1l"):
                    if(value == "HZ"):
                        self.AFG_CH1_LoadState.setCurrentIndex(0)
                        self.AFG_CH1_LoadZ.setEnabled(False)
                    else:
                        self.AFG_CH1_LoadState.setCurrentIndex(1)
                        self.AFG_CH1_LoadZ.setText(value)
                if(name == "a2l"):
                    if(value == "HZ"):
                        self.AFG_CH2_LoadState.setCurrentIndex(0)
                        self.AFG_CH2_LoadZ.setEnabled(False)
                    else:
                        self.AFG_CH2_LoadState.setCurrentIndex(1)
                        self.AFG_CH2_LoadZ.setText(value)
        WarningBox("Load Success")
    @pyqtSlot()
    def on_SaveButton_clicked(self):
        ch1load = self.AFG_CH1_LoadZ.text() if self.AFG_CH1_LoadState.currentText()!="HiZ" else "HZ"
        ch2load = self.AFG_CH2_LoadZ.text() if self.AFG_CH2_LoadState.currentText()!="HiZ" else "HZ"
        with open(".\\temp\\channelstate.csv","w") as f:
            f.write("o1a="+str(self.OSC_CH1_Atte.currentIndex())+"\r")
            f.write("o2a="+str(self.OSC_CH2_Atte.currentIndex())+"\r")
            f.write("o3a="+str(self.OSC_CH3_Atte.currentIndex())+"\r")
            f.write("o4a="+str(self.OSC_CH4_Atte.currentIndex())+"\r")
            f.write("o1u="+str(self.OSC_CH1_Unit.currentIndex())+"\r")
            f.write("o2u="+str(self.OSC_CH2_Unit.currentIndex())+"\r")
            f.write("o3u="+str(self.OSC_CH3_Unit.currentIndex())+"\r")
            f.write("o4u="+str(self.OSC_CH4_Unit.currentIndex())+"\r")
            f.write("a1l="+ch1load+"\r")
            f.write("a2l="+ch2load+"\r")
        WarningBox("Save State")
if __name__=="__main__":
    args = parse_args()
    app = QApplication(sys.argv)
    icon = QIcon(".\\Resource\\PyBode.ico")
    mainc=mainCode(args.osc_ip,args.afg_ip)
    mainc.setWindowIcon(icon)
    if(sys.platform == "win32"):
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'myappid')
    mainc.show()
    sys.exit(app.exec_())