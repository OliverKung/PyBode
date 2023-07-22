# pyBode GUI with Kivy
import numpy as np
import pyqtgraph as pg
import sys
import os,time,multiprocessing,threading
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtCore import QUrl,pyqtSlot,QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
import GUI

class mainCode(QMainWindow,GUI.Ui_pyBode):
    def __init__(self):
        QMainWindow.__init__(self)
        GUI.Ui_pyBode.__init__(self)
        self.setupUi(self)
        self.checkLifeTimer = QTimer()
        self.checkLifeTimer.timeout.connect(self.lifecheck)

    @pyqtSlot()
    def on_StartButton_clicked(self):
        AFG_IP = self.AFG_IP.text()
        OSC_IP = self.OSC_IP.text()
        ExcitionChannel = self.AFG_Excition.currentText()
        SyncTrigger = self.AFG_Sync.currentText()
        InputChannel = self.OSC_Input.currentText()
        OutputChannel = self.OSC_Output.currentText()
        SyncChannel = self.OSC_Sync.currentText()
        SampleMethod = self.SampleMode.currentText()
        AveragePoint = str(self.AverageTimes.value())
        StartFrequency = self.StartFrequency.text()
        StopFrequency = self.StopFrequency.text()
        Points = self.Points.text()
        Amp = self.Amplitude.text()
        if(self.SyncTriggerEnable.isChecked() == True):
            shell_cmd = "python pyBode.py --osc-ip "+OSC_IP+\
                        " --afg-ip "+AFG_IP+\
                        " -eC "+ExcitionChannel+\
                        " -sT "+SyncTrigger+\
                        " -iC "+InputChannel+\
                        " -oC "+OutputChannel+\
                        " -sC "+SyncChannel+\
                        " -s "+SampleMethod+\
                        " -aT "+AveragePoint+\
                        " -sF "+StartFrequency+\
                        " -eF "+StopFrequency+\
                        " -p "+Points+\
                        " -a "+Amp+\
                        " -sTE true --no-gui"
        else:
            shell_cmd = "python pyBode.py --osc-ip "+OSC_IP+\
                        " --afg-ip "+AFG_IP+\
                        " -eC "+ExcitionChannel+\
                        " -iC "+InputChannel+\
                        " -oC "+OutputChannel+\
                        " -s "+SampleMethod+\
                        " -aT "+AveragePoint+\
                        " -sF "+StartFrequency+\
                        " -eF "+StopFrequency+\
                        " -p "+Points+\
                        " -a "+Amp+\
                        " -sTE false --no-gui"
        time.sleep(0.5)
        self.pyBode_cmd_process = multiprocessing.Process(target=os_system_thread,args=(shell_cmd,))
        self.pyBode_cmd_process.start()
        self.checkLifeTimer.start(200)

    @pyqtSlot()
    def on_LoadVNC_clicked(self):
        vnc_cmd=""
        vnc_install_dir=""
        with open("./pyBode.conf") as f:
            line = f.readline()
            if(line.split(" = ")[0]=="VNC_VIEWER_INSTALL_DIR"):
                vnc_install_dir=line.split("=")[1]
        vnc_cmd=vnc_install_dir+" "+self.OSC_IP.text()
        vnc_process = multiprocessing.Process(target=os_system_thread,args=(vnc_cmd,))
        vnc_process.start()

    def loadHtml(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "name.html"))
        self.plotyWidget.load(QUrl.fromLocalFile(file_path))

    def lifecheck(self):
        if not self.pyBode_cmd_process.is_alive():
            self.checkLifeTimer.stop()
            self.loadHtml()

def os_system_thread(shell_cmd):
    os.system(shell_cmd)

if __name__=="__main__":
    app = QApplication(sys.argv)
    mainc=mainCode()
    mainc.show()
    mainc.loadHtml()
    sys.exit(app.exec_())