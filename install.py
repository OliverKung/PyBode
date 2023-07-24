import os,sys
def warning(warn_info):
    print("\033[0;31;40m"+warn_info+"\033[0m")
if __name__=="__main__":
    system_platform = sys.platform
    if(system_platform == "win32"):
        python_version = sys.version_info
        if(python_version>=(3,10)):
            print("Python Check Successfully")
        else:
            warning("WARNING:PyBode Recommend Verision is >3.10")
            exit()
        print("install pandas,numpy")
        os.system("pip install numpy pandas")
        print("install vxi11")
        os.system("pip install python-vxi11")
        print("install PyQt5 with WebEngine")
        os.system("pip install PyQt5 PyQtWebEngine")
        print("install pyqtgraph")
        os.system("pip install pyqtgraph")
        print("install tqdm,plotly")
        os.system("pip install tqdm plotly")
        print("install FINISH, try boot pyBode GUI")
        os.system("python pyBode_GUI.py")
    if(system_platform == "linux"):
        python_version = sys.version_info
        if(python_version>=(3,10)):
            print("Python Check Successfully")
        else:
            warning("WARNING:PyBode Recommend Verision is >3.10")
            exit()
        print("install pandas,numpy")
        os.system("pip3 install numpy pandas")
        print("install vxi11")
        os.system("pip3 install python-vxi11")
        print("install PyQt5 with WebEngine")
        os.system("pip3 install PyQt5 PyQtWebEngine")
        print("install pyqtgraph")
        os.system("pip3 install pyqtgraph")
        print("install tqdm,plotly")
        os.system("pip3 install tqdm plotly")
        print("install FINISH, try boot pyBode GUI")
        os.system("python3 pyBode_GUI.py")