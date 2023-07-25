import numpy as np
import pyqtgraph as pg
import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QMessageBox,QSystemTrayIcon,QMenu
from PyQt5.QtCore import QUrl,pyqtSlot,QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
import PyQt5.QtCore as QtCore
from PyQt5.QtGui import QIcon
import channelSetWindow
import ctypes,argparse,subprocess

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
        # self.SetButton.clicked.connect(self.on_SetButton_clicked)
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