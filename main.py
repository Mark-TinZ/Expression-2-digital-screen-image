import math
import numpy as np
import sys, cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDialog
from GUI.main_menu import Ui_MainWindow
from GUI.BriCon import Ui_Dialog
from PyQt5.QtCore import QTimer, Qt

class BriCon(QDialog, Ui_Dialog):
    def __init__(self, Image: cv2.imread, parent=None):
        super(BriCon, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Var
        self.Brightness = 0
        self.Contrast = 1
        self.win = parent
        self.Image = Image

        # Triggered
        self.horizontalSlider_brightess.valueChanged.connect(self.slider_brightness)
        self.horizontalSlider_contrast.valueChanged.connect(self.slider_contrast)
        self.checkBox.stateChanged.connect(self.check_box_preview)
        self.buttonBox.clicked.connect(self.select_image)
        self.buttonBox.rejected.connect(self.close_edit)

    def select_image(self):
        image = self.Image
        image = image.astype(np.float32)  # default: uint8
        image = (self.Contrast * image + self.Brightness)
        image = np.uint8(np.clip(image, 0, 255))
        pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(image, image.shape[1], image.shape[0],
                                                      image.shape[1] * 3, QtGui.QImage.Format_RGB888))
        self.win.Image = image
        self.accept()

    def close_edit(self):
        self.reject()

    def slider_brightness(self, value):
        self.Brightness = value
        _translate = QtCore.QCoreApplication.translate
        self.horizontalSlider_brightess.setToolTip(f"Brightness: {value}")

        self.update_image()

    def slider_contrast(self, value):
        self.Contrast = value / 100
        _translate = QtCore.QCoreApplication.translate
        self.horizontalSlider_contrast.setToolTip(f"Contrast: {value}")

        self.update_image()

    def check_box_preview(self):
        self.update_image()

    def update_image(self):
        image = self.Image
        value = self.win.spinBox_scale.value()
        width = int(image.shape[1] * value / 100)
        height = int(image.shape[0] * value / 100)

        image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

        if self.checkBox.isChecked():
            image = image.astype(np.float32)  # default: uint8
            image = (self.Contrast * image + self.Brightness)
            image = np.uint8(np.clip(image, 0, 255))
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(image, image.shape[1], image.shape[0],
                                                          image.shape[1] * 3, QtGui.QImage.Format_RGB888))
        else:
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(image, image.shape[1], image.shape[0],
                                                          image.shape[1] * 3, QtGui.QImage.Format_RGB888))
        self.win.label_image.setPixmap(pixmap)



class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.qdialog_bricon = None
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.setStyleSheet("")

        # Var
        self.label_filename_timer = QTimer(self)
        self.label_filename_text = "None"
        self.label_filesize_text = ""
        self.label_filename_curi = 0
        self.label_filename_timer.timeout.connect(self.label_filename_update)
        self.label_filename_timer.start(300)
        self.History_image = []
        self.History_fx = []
        self.Image = cv2.imread
        self.Support_format = ["Image (*.png *.jpeg *.jpg *.jpe *.tiff *.tif *.bmp *.dib *.pbm *.pgm *.ppm *.webp)",
                               "PNG (*.png)", "JPEG (*.jpeg *.jpg *.jpe)",
                               "Tagged Image File Format (*.tiff *.tif)", "Windows bitmaps (*.bmp *.dib)",
                               "Portable image format (*.pbm *.pgm *.ppm)", "WebP (*.webp)", "All (*.*)"]

        # MenuBar
        self.actionSave.setEnabled(False)
        self.actionSave_As.setEnabled(False)
        self.menuEdit.setEnabled(False)
        self.menuImage.setEnabled(False)
        self.menuColors.setEnabled(False)
        self.actionUpdate.setEnabled(False)

        # Widgets
        self.gridLayout_shift_enabled(False)
        self.gridLayout_image_resolution_enabled(False)
        self.verticalLayout_advanced_enabled(False)
        self.spinBox_xshift.setEnabled(False)
        self.scrollArea.setAcceptDrops(True)
        self.spinBox_scale.setEnabled(False)

        # Triggered
        self.actionOpen.triggered.connect(self.open_file)
        # self.actionSave.triggered.connect()
        # self.actionSave_As.triggered.connect()
        self.actionQuit.triggered.connect(QtWidgets.QApplication.quit)

        # self.actionUndo.triggered.connect()
        # self.actionRedo.triggered.connect()
        #
        # self.action24bit.triggered.connect()
        # self.actionRRRGGGBBB.triggered.connect()
        # self.actionRGBXXX.triggered.connect()
        # self.actionXXX.triggered.connect()
        #
        self.actionBrighthess_Contrast.triggered.connect(self.bricon)
        #
        # self.actionPreferences.triggered.connect()
        # self.actionUpdate.triggered.connect()

        self.spinBox_scale.valueChanged.connect(self.image_scale)
        self.checkBox_change.stateChanged.connect(self.checkBox_change_connect)
        self.checkBox_resolution.stateChanged.connect(self.checkBox_resolution_connect)
        self.checkBox_square.stateChanged.connect(self.checkBox_square_connect)
        self.checkBox_advanced.stateChanged.connect(self.checkBox_advanced_connect)

    def gridLayout_shift_enabled(self, Enabled: bool):
        self.label_xshift.setEnabled(Enabled)
        self.spinBox_xshift.setEnabled(Enabled)
        self.label_yshift.setEnabled(Enabled)
        self.spinBox_yshift.setEnabled(Enabled)

    def gridLayout_image_resolution_enabled(self, Enabled: bool):
        self.label_width.setEnabled(Enabled)
        self.spinBox_width.setEnabled(Enabled)
        self.label_height.setEnabled(Enabled)
        self.spinBox_height.setEnabled(Enabled)

    def verticalLayout_advanced_enabled(self, Enabled: bool):
        self.label_redolution.setEnabled(Enabled)
        self.label_width_digi.setEnabled(Enabled)
        self.spinBox_width_digi.setEnabled(Enabled)
        self.label_height_digi.setEnabled(Enabled)
        self.spinBox_height_digi.setEnabled(Enabled)
        self.label_alignment.setEnabled(Enabled)
        self.comboBox_alignment.setEnabled(Enabled)

    def checkBox_change_connect(self):
        if self.checkBox_change.isChecked():
            self.gridLayout_shift_enabled(True)
        else:
            self.gridLayout_shift_enabled(False)

    def checkBox_resolution_connect(self):
        if not self.checkBox_resolution.isChecked():
            self.gridLayout_image_resolution_enabled(True)
        else:
            self.gridLayout_image_resolution_enabled(False)

    def checkBox_square_connect(self):
        if self.checkBox_square.isChecked():
            pass
        else:
            pass

    def checkBox_advanced_connect(self):
        if self.checkBox_advanced.isChecked():
            self.verticalLayout_advanced_enabled(True)
        else:
            self.verticalLayout_advanced_enabled(False)

    def image_scale(self, value):
        width = int(self.Image.shape[1] * value / 100)
        height = int(self.Image.shape[0] * value / 100)

        resized_image = cv2.resize(self.Image, (width, height), interpolation=cv2.INTER_AREA)

        self.update_image(resized_image)
    # func
    def bricon(self):
        self.qdialog_bricon = BriCon(parent=self, Image=self.Image)
        self.qdialog_bricon.show()


    # Load image
    def isImage(self, path):
        img = cv2.imread(path)
        if img is None:
            msg = QMessageBox()
            msg.setWindowTitle("E2img")
            msg.setText("Error!")
            msg.setInformativeText("Image file cannot be identified")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(320, 80)
            msg.exec_()
        else:
            return True

    def update_image(self, image):
        pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(image, image.shape[1], image.shape[0],
                                                      image.shape[1] * 3, QtGui.QImage.Format_RGB888))
        #scaled_pixmap = pixmap.scaled(self.label_image.size(), QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(pixmap)

    def load_image(self, path):
        if self.isImage(path):
            self.Image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
            self.update_image(self.Image)

            self.actionSave.setEnabled(True)
            self.actionSave_As.setEnabled(True)
            self.menuEdit.setEnabled(True)
            self.menuImage.setEnabled(True)
            self.menuColors.setEnabled(True)
            self.actionUpdate.setEnabled(True)
            self.spinBox_scale.setEnabled(True)

            height, width, channels = self.Image.shape
            total_pixels = self.Image.size

            bits_per_pixel = 8 * channels
            file_size_bits = total_pixels * bits_per_pixel
            file_size_bytes = file_size_bits / 8

            if file_size_bytes < 1024:
                file_size = f"{round(file_size_bytes, 2)} bytes"
            elif file_size_bytes < 1024 * 1024:
                file_size = f"{round(file_size_bytes / 1024, 2)} KB"
            else:
                file_size = f"{round(file_size_bytes / (1024 * 1024), 2)} MB"

            self.label_filename_text = f"{path.split('/')[-1]} "
            self.label_filesize_text = f" ({file_size})"

            image = self.Image
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(image, image.shape[1], image.shape[0],
                                                          image.shape[1] * 3, QtGui.QImage.Format_RGB888))


    def open_file(self):
        path_file = QFileDialog.getOpenFileName(self, "E2img - Image Selection", None, ";;".join(self.Support_format))[0]
        if path_file:
            self.load_image(path_file)

    # Events
    def dragEnterEvent(self, event: QtGui.QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QtGui.QDropEvent):
        urls = event.mimeData().urls()
        self.scrollArea.setStyleSheet("")
        if len(urls) == 1 and urls[0].toLocalFile():
            path = urls[0].toLocalFile()
            print(path)
            # pixmap = QtGui.QPixmap(path)
            # self.label_image.setPixmap(pixmap)
            self.load_image(path)
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QtGui.QDragMoveEvent):
        if self.scrollArea.geometry().contains(event.pos()):
            self.scrollArea.setStyleSheet("background-color: #EFEFEF; border: 2px dashed black;")
            self.scrollAreaWidgetContents.setStyleSheet("border: None;")
            self.label_image.setStyleSheet("border: None;")
            # self.scrollAreaWidgetContents.setStyleSheet("background-color: #EFEFEF; border: 1px dashed black;")
            # self.label_image.setStyleSheet("background-color: #EFEFEF; border: 1px dashed black;")
            event.acceptProposedAction()
        else:
            self.scrollArea.setStyleSheet("")
            event.ignore()

    def wheelEvent(self, event: QtGui.QWheelEvent):
        if self.label_image.pixmap() is not None and event.modifiers() == QtCore.Qt.ControlModifier:
            angle_delta = event.angleDelta().y() / 120.0
            if angle_delta > 0:
                self.spinBox_scale.setValue(math.ceil(self.spinBox_scale.value() * 1.1))
            else:
                self.spinBox_scale.setValue(math.floor(self.spinBox_scale.value() * 0.9))
        else:
            event.ignore()

    def label_filename_update(self):
        if len(self.label_filename_text) > 24:
            if self.label_filename_curi == 0:
                self.label_filename_timer.stop()
                QTimer.singleShot(4000, self.label_filename_start_update)

            self.label_filename.setText((self.label_filename_text[self.label_filename_curi:]+self.label_filename_text[:self.label_filename_curi])[:24] + self.label_filesize_text)
            self.label_filename_curi = (self.label_filename_curi + 1) % len(self.label_filename_text)
        else:
            self.label_filename.setText(self.label_filename_text + self.label_filesize_text)

    def label_filename_start_update(self):
        self.label_filename_timer.start(300)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
