#!/usr/bin/env python3
# change to use python3-pyqt5 from yocto meta-qt5
import sys
import logging
import signal
# usePyside = False
# if usePyside:
#     import PySide2 as PyQt5
# QPushButton, QLabel, QLineEdit,
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QMessageBox
# QWebEngineView
from PySide2.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    """
    MainWindow class contains html canvas.
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Web Browser')
        self.setGeometry(300, 300, 800, 600)
        self.setWindowIcon(QtGui.QIcon('web.png'))
        self.create_menu()
        self.create_main_frame()
        self.create_status_bar()
        self.show()
        print("loading html")
        self.file_reload()
        # file_exit on keyboard interrupt
        signal.signal(signal.SIGINT, signal.SIG_DFL)

    def create_menu(self):
        self.file_menu = self.menuBar().addMenu("&File")
        # self.file_menu.addAction("&Open", self.file_open, QtCore.Qt.CTRL + QtCore.Qt.Key_O)
        # self.file_menu.addAction("&Save", self.file_save, QtCore.Qt.CTRL + QtCore.Qt.Key_S)
        # reload
        self.file_menu.addAction("&Reload", self.file_reload, QtCore.Qt.CTRL + QtCore.Qt.Key_R)
        self.file_menu.addAction("&Exit", self.file_exit, QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.help_menu = self.menuBar().addMenu("&Help")
        self.help_menu.addAction("&About", self.about)
        # no margin or border
        self.menuBar().setStyleSheet("""
            QMenuBar {
                background-color: #eee;
                border: 0px;
                margin: 0px;
                padding: 0px;
                }
                """)

    def file_reload(self):
        """
        load index.html in current directory
        :return:
        """
        self.web_view.load(QtCore.QUrl.fromLocalFile(QtCore.QDir.currentPath() + "/index.html"))
        self.web_view.reload()

    def create_main_frame(self):
        self.main_frame = QWidget()
        self.setCentralWidget(self.main_frame)
        # set layout
        self.main_frame.setLayout(QVBoxLayout())
        self.create_web_view()
        self.main_frame.layout().setContentsMargins(0, 0, 0, 0)
        self.main_frame.layout().setSpacing(0)
        self.main_frame.setContentsMargins(0, 0, 0, 0)

    def create_web_view(self):
        self.web_view = QWebEngineView()
        self.main_frame.layout().addWidget(self.web_view)

    def create_status_bar(self):
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Ready")

    def about(self):
        QMessageBox.about(
            self,
            "About Web Browser",
            """<b>Web Browser</b> v1.0
            <p>Copyright &copy; 2017
            <p>This is a simple web browser.
            <p>Python %s - PySide2 %s - Qt %s on %s""" %
            (sys.version, "unknown", QtCore.qVersion(),  QtCore.QSysInfo.prettyProductName())
        )

    def file_exit(self):
        self.close()


def main():
    """
    Main function
    :return:
    """
    logging.basicConfig(level=logging.DEBUG)
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()