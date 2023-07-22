# pyBode：基于pyVisa的波特图分析上位机
## Dependancies
python>=3.10.7(developing environment)

numpy>=1.24.2

pandas>=2.0.3

tqdm>=4.65.0

plotly>=5.15.0

PyQt5>=5.15.7
## Installation
就装下依赖库，然后直接运行
```python
python pyBode.py -h
```
查看用法即可
## Usage
对于无GUI的使用，例如将其作为纯后端或者轻量化的测试脚本，直接在命令行当中运行即可
```python
python pyBode.py -h
```
对于需要GUI的用户请运行：
```python
python pyBode_GUI.py
```
在此之前，请在pyBode.conf里配置VNC viewer的安装路径，请注意路径当中的空格，等号前后都得来个空格。
启动之后，请首先配置AFG和OSC的IP，暂时没写异常排除，不写IP的话应该会直接闪退
之后配置需要输入输出信号源幅度等功能。
点击Load VNC可以拉起示波器的VNC界面，点击Start可以开始测量。暂时没得进度条后面会加上