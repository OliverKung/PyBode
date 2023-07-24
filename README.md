# pyBode：基于pyVisa的波特图分析上位机
## Dependancies
python>=3.10.7(developing environment)

numpy>=1.24.2

pandas>=2.0.3

tqdm>=4.65.0

plotly>=5.15.0

PyQt5>=5.15.7
## Installation
首先请确保python版本高于3.10，查看方法为命令行运行
```python
python -v
```
运行
```powershell
pip install pandas numpy python-vxi11 PyQt5 PyQtWebEngine pyqtgraph tqdm plotly 
```
然后运行如下命令查看pyBode是否能正常调用
```python
python pyBode.py -h
```
运行如下命令尝试拉起GUI版本，应当会弹出一个GUI的对话框
```python
python pyBode_GUI.py
```
或者可以尝试自动安装的命令
```python
python install.py
```
按道理说能自动安装
## Usage
对于无GUI的使用，例如将其作为纯后端或者轻量化的测试脚本，直接在命令行当中运行即可
```python
python pyBode.py -h
```
对于需要GUI的用户请运行：
```python
python pyBode_GUI.py
```
~~在此之前，请在pyBode.conf里配置VNC viewer的安装路径，请注意路径当中的空格，等号前后都得来个空格。~~
现在不用设置了，软件的安装目录下直接集成了一个VNC viewer，虽然不那么轻量化但是又不是不能用。
~~启动之后，请首先配置AFG和OSC的IP，暂时没写异常排除，不写IP的话应该会直接闪退~~
已经更新了异常判断，但是警告的窗口还有些许的Bug。
之后配置需要输入输出信号源幅度等功能。
点击Load VNC可以拉起示波器的VNC界面，点击Start可以开始测量。
~~暂时没得进度条后面会加上~~
加了，现在点击Start会自动拉起一个进度条，还会显示当前的扫描频率，老高级了。