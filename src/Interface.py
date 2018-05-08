import sys
from PyQt5.QtWidgets import *
from MapReader import MapReader
from PyQt5.QtCore import Qt


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.log = ""
        self.sCat = ""
        self.title = 'Rutas mas actuales en Andalucia, GeoJSON'
        self.left = 300
        self.top = 150
        self.width = 700
        self.height = 500
        self.statusBar()

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()
 
    def demobuttonClicked(self):
        if(False):
            QMessageBox.about(self, "ERROR", "Un mensaje de error")
        else:
            self.statusBar().showMessage('Esto indica que ha ocurrido')
            QMessageBox.about(self, "RESULTADO", 'Mensage del resultado')

    def file_choice(self, text):
        QMessageBox.about(self, "RESULTADO", text + ' ha sido descargada')

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
        self.fileChoicer.addItem("motif")
        self.fileChoicer.addItem("Windows")
        self.fileChoicer.addItem("cde")
        self.fileChoicer.addItem("Plastique")
        self.fileChoicer.addItem("Cleanlooks")
        self.fileChoicer.addItem("windowsvista")
        self.tab1.layout.addWidget(self.fileChoicer)

        self.fileChoicer.activated[str].connect(parent.file_choice)
        self.mapView = QGraphicsView()
        map = QGraphicsScene
        self.mapView.setScene(self, map)
        self.tab1.layout.addWidget(self.mapView)

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