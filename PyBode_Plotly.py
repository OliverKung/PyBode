import pandas as pd
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show_in_window(fig):
    import sys, os
    import plotly.offline
    from PyQt5.QtCore import QUrl
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    from PyQt5.QtWidgets import QApplication
    
    plotly.offline.plot(fig, filename='./name.html', auto_open=False)
    
    app = QApplication(sys.argv)
    web = QWebEngineView()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "name.html"))
    print(file_path)
    web.load(QUrl.fromLocalFile(file_path))
    web.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    df = pd.read_csv('F:\SoftDev\Instruments\inststa\data\\bode_data_plot.csv', skiprows=[0], names=['freq', 'gain', 'phase'])
    fig = make_subplots(rows = 2, cols = 1)
    fig.add_trace(go.Scatter(x=df['freq'], y=df['gain'], mode='lines', name='Gain'), row = 1, col = 1)
    fig.add_trace(go.Scatter(x=df['freq'], y=df['phase'], mode='lines', name='Phase'), row = 2, col = 1)
    fig.update_xaxes(type="log", exponentformat="power")
    fig.update_layout()
    show_in_window(fig)
    # fig.show()
