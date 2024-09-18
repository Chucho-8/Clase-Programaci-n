from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

class Ventana (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proyecto")
        self.setFixedSize(500,300)

def main():
    #print("Dentro de main")
    app=QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()