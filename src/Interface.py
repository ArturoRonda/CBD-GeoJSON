import sys
from PyQt5.QtWidgets import *
from MapReader import MapReader
from PyQt5.QtCore import Qt
import geojsonio
import webbrowser

def lookForMaps():
    from os import walk
    f = []
    for (dirpath, dirnames, filenames) in walk("maps/"):
        f.extend(filenames)
        break
    return f

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.log = ""
        self.sCat = ""
        self.title = 'HIKER :: Rutas mas actuales en Andalucia'
        self.left = 150
        self.top = 75
        self.width = 600
        self.height = 250
        self.statusBar()
        self.selected = ""

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()
 
    def demobuttonClicked(self):
        if(self.selected == ""):
            QMessageBox.about(self, "ERROR", "Seleccione una ruta")
        else:
            f = open('index.html', 'w')

            message = """<!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="utf-8" />
            <title>Hiker app</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <link rel="stylesheet" href="style.css" />
            <link rel="stylesheet" href="leaflet.css" crossorigin=""/>
            <script src="leaflet.js" crossorigin=""></script>
            </head>
            <body>
            <div id="mapid"></div>
            </body>
            <script src="script.js" map=""" + '"' + self.selected + '"' + """></script>
            </html>"""

            f.write(message)
            f.close()

            # Change path to reflect file location
            webbrowser.open_new_tab("index.html")
            # geojsonio.display(self.selected)

    def file_choice(self, text):
        self.selected="maps/" + text

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Salir del programa',
                                     "¿Está seguro de salir?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Inicialización de elementos de la ventana
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tabs.resize(700, 500)

        # Anadir pestañas a la ventana
        self.tabs.addTab(self.tab1, "Seleciona Ruta")

        # Primera pestana
        self.tab1.layout = QVBoxLayout(self)
        self.label = QLabel("Seleccione una ruta: ",self)
        self.tab1.layout.addWidget(self.label)

        self.fileChoicer = QComboBox(self)
        for mapname in lookForMaps():
            self.fileChoicer.addItem(mapname)

        self.tab1.layout.addWidget(self.fileChoicer)

        self.fileChoicer.activated[str].connect(parent.file_choice)
        # self.mapView = QGraphicsView()
        # map = QGraphicsScene
        # self.mapView.setScene(self, map)
        # self.tab1.layout.addWidget(self.mapView)

        self.readyButton = QPushButton("Ver en navegador",self)
        self.tab1.layout.addWidget(self.readyButton)
        self.readyButton.clicked.connect(lambda: parent.demobuttonClicked())

        # self.pushButton2 = QPushButton("Entrenar el modelo con la división seleccionada: ", self)
        # self.tab1.layout.addWidget(self.pushButton2)
        # self.pushButton2.clicked.connect(lambda: parent.buttonClicked2())

        self.tab1.setLayout(self.tab1.layout)
        self.tab1.setGeometry(300, 300, 250, 150)
        self.show()

        # Añadir pestañas al widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())