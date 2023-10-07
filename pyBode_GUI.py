# pyBode GUI with Kivy
import numpy as np
import pyqtgraph as pg
import sys
import os,time,multiprocessing,subprocess,re
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QMessageBox,QSystemTrayIcon,QMenu
from PyQt5.QtCore import QUrl,pyqtSlot,QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
import PyQt5.QtCore as QtCore
from PyQt5.QtGui import QIcon
import GUI,progressbar,channelSet
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.offline
import ctypes
import pandas as pd 
import math
def check_ip(ipAddr):
    compile_ip=re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if compile_ip.match(ipAddr):
        return True
    else:
        return False

def WarningBox(message):
    warningwindow = QMessageBox(QMessageBox.Warning,"Warning",message)
    warningwindow.exec_()

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
        self.actionSave.triggered.connect(self.on_SaveDefaultBut_clicked)
        self.actionLoad.triggered.connect(self.on_LoadDefaultBut_clicked)
        self.actionChannel_Set.triggered.connect(self.on_actionChannel_Set_Triggered)
    @pyqtSlot()
    def on_StartButton_clicked(self):
        if(check_ip(self.AFG_IP.text())!=True or check_ip(self.OSC_IP.text())!=True):
            WarningBox("Check IP of AFG/OSC")
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

    @pyqtSlot()
    def on_SaveDefaultBut_clicked(self):
        with open(".\\temp\\state.csv","w") as state:
            if(self.SyncTriggerEnable.isChecked()==True):
                state.write("SyncTriggerEnable=True\r")
            else:
                state.write("SyncTriggerEnable=False\r")
            state.write("AFG_IP="+self.AFG_IP.text()+"\r")
            state.write("OSC_IP="+self.OSC_IP.text()+"\r")
            state.write("Excition="+str(self.AFG_Excition.currentIndex())+"\r")
            state.write("Sync="+str(self.AFG_Sync.currentIndex())+"\r")
            state.write("Amp="+self.Amplitude.text()+"\r")
            state.write("Input="+str(self.OSC_Input.currentIndex())+"\r")
            state.write("Output="+str(self.OSC_Output.currentIndex())+"\r")
            state.write("SyncCh="+str(self.OSC_Sync.currentIndex())+"\r")
            state.write("Sample="+str(self.SampleMode.currentIndex())+"\r")
            state.write("Average="+self.AverageTimes.text()+"\r")
            state.write("StartFrequency="+self.StartFrequency.text()+"\r")
            state.write("StopFrequency="+self.StopFrequency.text()+"\r")
            state.write("Point="+self.Points.text()+"\r")
            state.write("PlotInput="+str(self.PlotInput.currentIndex())+"\r")
            state.write("PlotOutput="+str(self.PlotOutput.currentIndex())+"\r")
            state.close()
        WarningBox("Current State Saved")

    @pyqtSlot()
    def on_LoadDefaultBut_clicked(self):
        with open(".\\temp\\state.csv","r") as state:
            lines = state.readlines()
            for line in lines:
                name = line.split("=")[0]
                value = line.split("=")[1].replace("\n","")
                if(name =="SyncTriggerEnable"):
                    if(value == "True"):
                        self.SyncTriggerEnable.setChecked(True)
                    else:
                        self.SyncTriggerEnable.setChecked(False)
                    self.on_SyncTriggerEnable_clicked()
                if(name == "AFG_IP"):
                    self.AFG_IP.setText(value)
                if(name =="OSC_IP"):
                    self.OSC_IP.setText(value)
                if(name =="Excition"):
                    self.AFG_Excition.setCurrentIndex(int(value))
                if(name =="Sync"):
                    self.AFG_Sync.setCurrentIndex(int(value))
                if(name =="Amp"):
                    self.Amplitude.setText(value)
                if(name =="Input"):
                    self.OSC_Input.setCurrentIndex(int(value))
                if(name =="Output"):
                    self.OSC_Output.setCurrentIndex(int(value))
                if(name =="SyncCh"):
                    self.OSC_Sync.setCurrentIndex(int(value))
                if(name =="Sample"):
                    self.SampleMode.setCurrentIndex(int(value))
                if(name =="Average"):
                    self.AverageTimes.setValue(int(value))
                if(name =="StartFrequency"):
                    self.StartFrequency.setText(value)
                if(name =="StopFrequency"):
                    self.StopFrequency.setText(value)
                if(name =="Point"):
                    self.Points.setText(value)
                if(name =="PlotOutput"):
                    self.PlotOutput.setCurrentIndex(int(value))
                if(name =="PlotInput"):
                    self.PlotInput.setCurrentIndex(int(value))
            state.close()
        WarningBox("Load Current State")

    @pyqtSlot()
    def on_actionChannel_Set_Triggered(self):
        self.actionChannelProcess = subprocess.Popen("python channelSet_GUI.py --osc-ip "+self.OSC_IP.text()+" --afg-ip "+self.AFG_IP.text())

    @pyqtSlot()
    def on_Replot_clicked(self):
        self.plot2html()
        self.loadHtml()

    def plot2html(self):
        self.df = pd.DataFrame({}, columns=['freq', 'gain', 'phase'])
        if(self.PlotInput.currentText()!="Excite"):
            InputPos = self.PlotInput.currentIndex()+1
        else:
            InputPos = 5
        

        if(self.PlotOutput.currentText()!="Excite"):
            OutputPos = self.PlotOutput.currentIndex()+1
        else:
            OutputPos = 5
            
        print(InputPos,OutputPos)
        with open(".\\temp\\datafilename.txt","r") as f:
            datafilename=f.readline()
            f.close()
        with open(".\\ExampleData\\"+datafilename,"r") as f:
            datalines = f.readlines()
            f.close()
            for line in datalines:
                lineSplit = line.split(",")
                # print(lineSplit)
                # print(float(lineSplit[0]),float(lineSplit[InputPos]),float(lineSplit[OutputPos]))
                self.df.loc[len(self.df.index)]=[float(lineSplit[0]),\
                                                 20*math.log(float(lineSplit[OutputPos])/float(lineSplit[InputPos])),\
                                                float(lineSplit[4])]
        if(OutputPos!=6 and InputPos!=6):
            fig = make_subplots(rows = 2,cols = 1)
            fig.add_trace(go.Scatter(x=self.df['freq'], y=self.df['gain'], mode='lines', name='Gain'), row = 1, col = 1)
            fig.add_trace(go.Scatter(x=self.df['freq'], y=self.df['phase'], mode='lines', name='Phase'), row = 2, col = 1)
            fig.update_xaxes(type="log", exponentformat="power")
            plotly.offline.plot(fig, filename=os.path.abspath(os.path.join(os.path.dirname(__file__), "name_x.html")), auto_open=False)
        else:
            fig = make_subplots(rows = 1,cols = 1)
            fig.add_trace(go.Scatter(x=self.df['freq'], y=self.df['gain'], mode='lines', name='Gain'), row = 1, col = 1)
            # fig.add_trace(go.Scatter(x=self.df['freq'], y=self.df['phase'], mode='lines', name='Phase'), row = 2, col = 1)
            fig.update_xaxes(type="log", exponentformat="power")
            plotly.offline.plot(fig, filename=os.path.abspath(os.path.join(os.path.dirname(__file__), "name_x.html")), auto_open=False)
    def loadHtml(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "name_x.html"))
        self.plotyWidget.load(QUrl.fromLocalFile(file_path))

    def lifecheck(self):
        if not self.pyBode_cmd_process.poll()==None:
            self.checkLifeTimer.stop()
            self.plot2html()
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
    icon = QIcon(".\\Resource\\PyBode.ico")
    # app.setWindowIcon(icon)
    mainc=mainCode()
    mainc.setWindowIcon(icon)
    if(sys.platform == "win32"):
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'myappid')
    mainc.show()
    mainc.loadHtml()
    sys.exit(app.exec_())