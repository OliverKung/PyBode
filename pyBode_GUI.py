# pyBode GUI with Kivy
import numpy as np
import pyqtgraph as pg
import sys
import os,time,multiprocessing,subprocess,re
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtCore import QUrl,pyqtSlot,QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
import GUI,progressbar

def check_ip(ipAddr):
    compile_ip=re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if compile_ip.match(ipAddr):
        return True
    else:
        return False

class WarningWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WARNING")

class mainCode(QMainWindow,GUI.Ui_pyBode):
    def __init__(self):
        QMainWindow.__init__(self)
        GUI.Ui_pyBode.__init__(self)
        self.setupUi(self)
        self.checkLifeTimer = QTimer()
        self.checkLifeTimer.timeout.connect(self.lifecheck)
        self.OSC_Sync.setEnabled(False)
        self.AFG_Sync.setEnabled(False)
        self.STOPButton.setEnabled(False)
        self.AverageTimes.setEnabled(False)
        self.SampleMode.currentTextChanged.connect(self.on_SampleMode_currentTextChanged)

    @pyqtSlot()
    def on_StartButton_clicked(self):
        if(check_ip(self.AFG_IP.text())!=True or check_ip(self.OSC_IP.text())!=True):
            warningwindow = WarningWindow()
            warningwindow.show()
            return
        self.STOPButton.setEnabled(True)
        self.StartButton.setEnabled(False)
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
        self.pyBode_cmd_process = subprocess.Popen(shell_cmd)
        self.checkLifeTimer.start(200)
        self.bar = progressbar.pyqtbar()

    @pyqtSlot()
    def on_LoadVNC_clicked(self):
        vnc_cmd=""
        vnc_install_dir=""
        with open("./pyBode.conf") as f:
            line = f.readline()
            if(line.split(" = ")[0]=="VNC_VIEWER_INSTALL_DIR"):
                vnc_install_dir=line.split("=")[1]
        vnc_cmd=vnc_install_dir+" "+self.OSC_IP.text()
        vnc_process = multiprocessing.Process(target=os.system,args=(vnc_cmd,))
        vnc_process.start()

    @pyqtSlot()
    def on_SyncTriggerEnable_clicked(self):
        if not self.SyncTriggerEnable.isChecked():
            self.OSC_Sync.setEnabled(False)
            self.AFG_Sync.setEnabled(False)
        else:
            self.OSC_Sync.setEnabled(True)
            self.AFG_Sync.setEnabled(True)

    @pyqtSlot()
    def on_STOPButton_clicked(self):
        self.pyBode_cmd_process.kill()
        self.STOPButton.setEnabled(False)
        self.StartButton.setEnabled(True)

    @pyqtSlot()
    def on_SampleMode_currentTextChanged(self):
        if(self.SampleMode.currentText()!="average"):
            self.AverageTimes.setEnabled(False)
        else:
            self.AverageTimes.setEnabled(True)

    def loadHtml(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "name.html"))
        self.plotyWidget.load(QUrl.fromLocalFile(file_path))

    def lifecheck(self):
        if not self.pyBode_cmd_process.poll()==None:
            self.checkLifeTimer.stop()
            self.loadHtml()
            self.StartButton.setEnabled(True)
            self.STOPButton.setEnabled(False)
            self.bar.close
        else:
             with open(".\\temp\\progress.csv","r") as tmp:
                line = tmp.readline()
                freq = float(line.split(",")[0])
                currentjob = float(line.split(",")[1])
                totaljob = float(line.split(",")[2])
                self.bar.set_value(freq,int(100*currentjob/totaljob))


if __name__=="__main__":
    app = QApplication(sys.argv)
    mainc=mainCode()
    mainc.show()
    mainc.loadHtml()
    sys.exit(app.exec_())