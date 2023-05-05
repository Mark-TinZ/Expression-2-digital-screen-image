from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QDialog, QFileDialog, QDialogButtonBox, QMessageBox
from UI.mainmenu import Main_Menu
from UI.dialog_fileopen import Ui_Dialog_FileOpen
from UI.progressmenu import Ui_ProgressMenu
import numpy as np
import cv2
import sys

class StartFileOpen(QDialog, Ui_Dialog_FileOpen):
    succesfully = pyqtSignal(str)
    def __init__(self, parent=None):
        super(StartFileOpen, self).__init__(parent)
        self.setupUi(self)
        #self.setWindowFlag(Qt.WindowCloseButtonHint, True)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.Path = ""

        self.toolButton.clicked.connect(self.getFile)
        self.buttonBox.button(QDialogButtonBox.Open).clicked.connect(self.buttonOpen)
        self.buttonBox.button(QDialogButtonBox.Close).clicked.connect(self.closeEvent)

        # self.closeEvent = self.closeEvent

    def isImage(self, path):
        img = cv2.imread(path)
        if img is not None:
            return True
        else:
            msg = QMessageBox()
            msg.setWindowTitle("E2img")
            msg.setText("Error!")
            msg.setInformativeText("Image file cannot be identified")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(320, 80)
            msg.exec_()

    def getFile(self):
        image_format = ["PNG (*.png)", "JPEG (*.jpeg *.jpg *.jpe)",
                        "Tagged Image File Format (*.tiff *.tif)", "Windows bitmaps (*.bmp *.dib)",
                        "Portable image format (*.pbm *.pgm *.ppm)", "WebP (*.webp)", "All (*.*)"]
        path = QFileDialog.getOpenFileName(self, "E2img - Image Selection", None, ";;".join(image_format))[0]
        if path:
            if self.isImage(path):
                self.Path = path
                self.lineEdit.setText(path)

    def buttonOpen(self):
        self.succesfully.emit(self.Path)

    def end(self):
        pass

    def closeEvent(self, event):
        QtWidgets.QApplication.quit()


class Main(QtWidgets.QMainWindow, Main_Menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.start_file_open = StartFileOpen(parent=self)
        self.start_file_open.succesfully.connect(self.checkFile)
        self.start_file_open.show()

        self.actionOpen.triggered.connect(self.getFile)
        self.actionSave_As.triggered.connect(self.saveFile)
        self.actionQuit.triggered.connect(self.close)
        self.Slider_Brightness.valueChanged.connect(self.on_brightness_slider_changed)
        self.Slider_Contrast.valueChanged.connect(self.on_contrast_slider_changed)
        self.checkBox_Square.stateChanged.connect(self.on_square_checkbox_changed)

        self.Image = cv2.imread
        self.Brightness = 0
        self.Contrast = 0
        self.Square = True
        self.Render_Image = cv2.imread

        self.menubar.setEnabled(False)
        self.centralwidget.setEnabled(False)
        self.statusbar.setEnabled(False)
        # self.closeEvent = self.closeEvent

    def on_brightness_slider_changed(self, value):
        _translate = QtCore.QCoreApplication.translate
        #self.Slider_Brightness.setToolTip(_translate("MainWindow", f"Brightness: {value}"))
        self.statusbar.showMessage(f"Brightness: {value}", 1000)
        self.Brightness = value
        self.select_Filter()

    def on_contrast_slider_changed(self, value):
        _translate = QtCore.QCoreApplication.translate
        #self.Slider_Contrast.setToolTip(_translate("MainWindow", f"Сontrast: {value}"))
        self.statusbar.showMessage(f"Сontrast: {value}", 1000)
        self.Contrast = value
        self.select_Filter()

    def on_square_checkbox_changed(self, state):
        if self.checkBox_Square.isChecked():
            self.Square = True
        else:
            self.Square = False

        self.select_Filter()

    def select_Filter(self):
        self.Render_Image = self.setBrightness(self.Image, self.Brightness)
        self.Render_Image = self.setContrast(self.Render_Image, self.Contrast)
        if self.Square:
            self.Render_Image = self.make_square(self.Render_Image)
        self.loadImage()

    def setBrightness(self, image, Brightness):
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        h, s, v = cv2.split(hsv)

        if Brightness > 0:
            lim = 255 - Brightness
            v[v > lim] = 255
            v[v <= lim] += Brightness
        else:
            lim = abs(Brightness)
            v[v < lim] = 0
            v[v >= lim] -= lim

        final_hsv = cv2.merge((h, s, v))
        final_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB)
        return final_img

    def setContrast(self, image, Сontrast):
        alpha = (100 - Сontrast) / 127.0
        beta = 127.0 * (1 - alpha)
        adjusted_img = cv2.addWeighted(image, alpha, image, 0, beta)
        return adjusted_img

    # def setSharpness(self, image, Sharpness):
    #     pass


    def saveFile(self):
        image_format = ["PNG (*.png)", "JPEG (*.jpeg *.jpg *.jpe)",
                        "Tagged Image File Format (*.tiff *.tif)", "Windows bitmaps (*.bmp *.dib)",
                        "Portable image format (*.pbm *.pgm *.ppm)", "WebP (*.webp)", "All (*.*)"]
        path = QFileDialog.getSaveFileName(self, "E2img - Saving an image", None, ";;".join(image_format))[0]
        img = cv2.cvtColor(self.Render_Image, cv2.COLOR_RGB2BGR)
        cv2.imwrite(path, img)

    def isImage(self, path):
        img = cv2.imread(path)
        if img is not None:
            return True
        else:
            msg = QMessageBox()
            msg.setWindowTitle("E2img")
            msg.setText("Error!")
            msg.setInformativeText("Image file cannot be identified")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(320, 80)
            msg.exec_()

    def getFile(self):
        image_format = ["PNG (*.png)", "JPEG (*.jpeg *.jpg *.jpe)",
                        "Tagged Image File Format (*.tiff *.tif)", "Windows bitmaps (*.bmp *.dib)",
                        "Portable image format (*.pbm *.pgm *.ppm)", "WebP (*.webp)", "All (*.*)"]
        path = QFileDialog.getOpenFileName(self, "E2img - Image Selection", None, ";;".join(image_format))[0]
        if path:
            if self.isImage(path):
                img = cv2.imread(path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                self.Image = img
                self.Render_Image = self.make_square(self.Image)
                self.loadImage()
                self.select_Filter()


    def checkFile(self, path):
        if path:
            self.menubar.setEnabled(True)
            self.centralwidget.setEnabled(True)
            self.statusbar.setEnabled(True)
            img = cv2.imread(path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.Image = img
            self.Render_Image = self.make_square(self.Image)
            self.loadImage()
        else:
            self.start_file_open.show()

    def make_square(self, image):
        height, width, channels = image.shape
        if height == width:
            return image
        elif height < width:
            border_size = (width - height) // 2
            border = cv2.copyMakeBorder(image, top=border_size, bottom=border_size, left=0, right=0,
                                        borderType=cv2.BORDER_CONSTANT, value=(0, 0, 0))
            return border
        else:
            border_size = (height - width) // 2
            border = cv2.copyMakeBorder(image, top=0, bottom=0, left=border_size, right=border_size,
                                        borderType=cv2.BORDER_CONSTANT, value=(0, 0, 0))
            return border

    def loadImage(self):
        pixmap = QPixmap.fromImage(QImage(self.Render_Image, self.Render_Image.shape[1], self.Render_Image.shape[0], self.Render_Image.shape[1] * 3, QImage.Format_RGB888))
        scaled_pixmap = pixmap.scaled(self.Label_Image.size(), Qt.KeepAspectRatio)
        self.Label_Image.setPixmap(scaled_pixmap)

class ProgressMenu(QtWidgets.QMainWindow, Ui_ProgressMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())