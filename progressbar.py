# _*_coding: UTF-8_*_
# 开发作者 ：TXH
# 开发时间 ：2020-09-08 10:20
# 文件名称 ：Qt_Processbar.py
# 开发工具 ：Python 3.7 + Pycharm IDE
 
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit, QProgressBar, \
    QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QDialogButtonBox
from PyQt5.QtCore import Qt, QBasicTimer, QThread,QRect
import sys
 

class ProgressBar(QDialog):
    def __init__(self,  parent=None):
        super(ProgressBar, self).__init__(parent)
 
        # Qdialog窗体的设置
        self.resize(500, 32) # QDialog窗的大小
        self.setFixedSize(500,32)
        # 创建并设置 QProcessbar
        self.progressBar = QProgressBar(self) # 创建
        self.progressBar.setMinimum(0) #设置进度条最小值
        self.progressBar.setMaximum(100)  # 设置进度条最大值
        self.progressBar.setValue(0)  # 进度条初始值为0
        self.progressBar.setGeometry(QRect(1, 3, 499, 28)) # 设置进度条在 QDialog 中的位置 [左，上，右，下]
        self.show()
 
    def setValue(self,current_frequency, value): # 设置总任务进度和子任务进度
        label = "Current Frequency:"+current_frequency+"Hz"
        self.setWindowTitle(self.tr(label)) # 顶部的标题
        self.progressBar.setValue(value)
 
class pyqtbar():
    '''
    task_number和 total_task_number都为 0 时，不显示当前进行的任务情况
    task_number<total_task_number 都为整数，错误的设置将出现错误显示，暂未设置报错警告
    
    # 使用示例
    import time
    bar = pyqtbar() # 创建实例
    total_number=10
    # 任务1
    task_id=1
    for process in range(1, 100):
        time.sleep(0.05)
        bar.set_value(task_id,total_number,process) # 刷新进度条
    # 任务2
    task_id = 2
    for process in range(1, 100):
        time.sleep(0.05)
        bar.set_value(task_id, total_number,process)
    bar.close # 关闭 bar 和 app
    '''
    def __init__(self):
        self.progressbar = ProgressBar() # 初始化 ProcessBar实例
 
    def set_value(self,current_frequency,i):
        self.progressbar.setValue(str(current_frequency), i)  # 更新进度条的值
        # QApplication.processEvents()  # 实时刷新显示
 
    @property
    def close(self):
        self.progressbar.close()  # 关闭进度条
 
if __name__ == '__main__':
 
    import time
    # 使用示例
    bar=pyqtbar() # 创建实例
    total_number=10 # 总任务数
    # 任务1
    task_id=1 # 子任务序号
    for process in range(1, 100):
        time.sleep(0.05)
        bar.set_value(task_id,total_number,process) # 刷新进度条
 
    bar.close # 关闭 bar 和 app