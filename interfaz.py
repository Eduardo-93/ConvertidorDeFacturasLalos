import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox, QLabel
from PySide6.QtGui import QPixmap
from xmltocsv import xml_to_csv

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        label = QLabel(self)
        pixmap = QPixmap("lalos.jpg")
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())
        
        self.setWindowTitle("Selector de Archivos")
        self.setGeometry(100, 100, 380, 200)

        self.button = QPushButton("Seleccionar Archivos", self)
        self.button.setGeometry(200, 80, 150, 30)
        self.button.clicked.connect(self.openFileDialog)
    
    def showAlert(self):
        alert = QMessageBox()
        alert.setWindowTitle("Finalizado")
        alert.setText("Arhivos listos")
        alert.setIcon(QMessageBox.Information)
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec()

    def openFileDialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("All files (*.*)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)  # Permitir la selección de varios archivos

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            #print("Archivos seleccionados:")
            for file in selected_files:
                if ".xml" in file:
                    xml_to_csv(file, file.replace(".xml",".csv"))
            self.showAlert()
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
