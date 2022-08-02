from PyQt6.QtWidgets import QApplication, QStackedWidget
from GUI import MainWindow
from sys import exit, argv

def main():
   app = QApplication(argv)
   mainwindow = MainWindow()
   widget = QStackedWidget()
   widget.addWidget(mainwindow)
   widget.setFixedWidth(596)
   widget.setFixedHeight(577)
   widget.setWindowTitle("Пошук точки мінімуму")
   widget.show()

   try:
      exit(app.exec())
   except:
      pass

if __name__ == "__main__":
    main()