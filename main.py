import numpy as np
import configparser
import math, sys, cv2

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QUndoCommand, QUndoStack
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMainWindow, QDialog

from GUI.main_menu import Ui_MainWindow
from GUI.BriCon import Ui_Dialog

class BriCon_Dialog(QDialog, Ui_Dialog):
    def __init__(self, image: cv2.imread, parent):
        super(BriCon_Dialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.parent = parent
        self.image = image
        self.brightness = 0
        self.contrast = 1

        self.horizontalSlider_brightess.valueChanged.connect(self.slider_bri)
        self.horizontalSlider_contrast.valueChanged.connect(self.slider_con)
        self.checkBox.stateChanged.connect(self.apply_image)
        self.buttonBox.accepted.connect(self.select_image)
        self.buttonBox.rejected.connect(self.reject)

    def slider_bri(self, value):
        self.brightness = value
        _translate = QtCore.QCoreApplication.translate
        self.horizontalSlider_brightess.setToolTip(f"Brightness: {value}")
        self.apply_image()

    def slider_con(self, value):
        self.contrast = value / 100
        _translate = QtCore.QCoreApplication.translate
        self.horizontalSlider_contrast.setToolTip(f"Contrast: {value}")
        self.apply_image()

    def edit_image(self):
        image = self.image
        image = image.astype(np.uint32)  # default: uint8
        image = (self.contrast * image + self.brightness)

        return np.uint8(np.clip(image, 0, 255))

    def apply_image(self):
        image = self.image
        if self.checkBox.isChecked():
            image = self.edit_image()
        print(self.parent.spinBox_scale.value())
        self.parent.update_pixmap(image, self.parent.spinBox_scale.value())

    def select_image(self):
        image = self.image
        self.parent.image = self.edit_image()
        self.parent.update_pixmap(self.parent.image, self.parent.spinBox_scale.value())
        self.parent.make_undo_command(image)
        self.accept()


class UndoCommand_Image(QUndoCommand):
    def __init__(self, parent, prev_image):
        super().__init__()
        self.parent = parent
        self.prev_image = prev_image
        self.curr_image = parent.image

    def undo(self):
        self.curr_image = self.parent.image
        self.parent.image = self.prev_image
        self.parent.update_pixmap(self.parent.image, self.parent.spinBox_scale.value())

    def redo(self):
        self.parent.image = self.curr_image
        self.parent.update_pixmap(self.parent.image, self.parent.spinBox_scale.value())

class DataFile():
    def __init__(self, file_config):
        self.config = configparser.ConfigParser()
        self.config.read(file_config)

        if "Formats" not in self.config:
            self.config["Formats"] = {}
            self.config["Formats"]["image"] = "Image (*.png *.jpeg *.jpg *.jpe *.tiff *.tif *.bmp *.dib *.pbm *.pgm *.ppm *.webp)"
            self.config["Formats"]["png"] = "PNG (*.png)"
            self.config["Formats"]["jpeg"] = "JPEG (*.jpeg *.jpg *.jpe)"
            self.config["Formats"]["tiff"] = "Tagged Image File Format (*.tiff *.tif)"
            self.config["Formats"]["bitmaps"] = "Windows bitmaps (*.bmp *.dib)"
            self.config["Formats"]["pbm"] = "Portable image format (*.pbm *.pgm *.ppm)"
            self.config["Formats"]["webp"] = "WebP (*.webp)"
            self.config["Formats"]["all"] = "All (*.*)"

        if "Options" not in self.config:
            self.config["Options"] = {}
            self.config["Options"]["path"] = ""
            self.config["Options"]["filepath"] = ""
            self.config["Options"]["e2files"] = "garrysmod\data\e2files"
            self.config["Options"]["expression2"] = "garrysmod\data\expression2"

        self.data_save()

    def data_save(self):
        with open("Data.ini", "w") as file:
            self.config.write(file)

    def get_game_path(self):
        return self.config.get("Options", "path")

    def get_game_e2files(self):
        return self.config.get("Options", "e2files")

    def get_game_expression2(self):
        return self.config.get("Options", "expression2")

    def set_game_path(self, path):
        self.config.set("Options", "path", path)
        self.data_save()

    def get_formats_image(self):
        formats = []
        for form in self.config["Formats"]:
            formats.append(self.config.get("Formats", form))
        return formats

    def get_options_end_path_file(self):
        if self.config.get("Options", "filepath") == "":
            return None
        return self.config.get("Options", "filepath")

    def set_options_end_path_file(self, path):
        self.config.set("Options", "filepath", path)
        self.data_save()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setAcceptDrops(True)

        self.Data = DataFile("Data.ini")
        self.undo_stack = QUndoStack(self)
        self.undo_stack.setUndoLimit(10)
        self.image = cv2.imread
        self.sup_format = self.Data.get_formats_image()
        self.dialog_bricon = None
        self.render_image = np.zeros((self.spinBox_height.value(),
                                      self.spinBox_width.value(), 3), dtype=np.uint8)

        self.actionSave.setEnabled(False)
        self.actionSave_As.setEnabled(False)
        self.menuImage.setEnabled(False)
        self.menuColors.setEnabled(False)
        self.actionUpdate.setEnabled(False)
        self.centralwidget.setEnabled(False)

        self.actionOpen.triggered.connect(self.get_file_FileDialog)
        self.actionUndo.triggered.connect(lambda: self.undo_stack.undo() if not self.checkBox_render.isChecked() else None)
        self.actionRedo.triggered.connect(lambda: self.undo_stack.redo() if not self.checkBox_render.isChecked() else None)
        self.actionBrighthess_Contrast.triggered.connect(self.BriCon)
        self.undo_stack.canUndoChanged.connect(lambda enabled: self.actionUndo.setEnabled(enabled))
        self.undo_stack.canRedoChanged.connect(lambda enabled: self.actionRedo.setEnabled(enabled))
        self.actionQuit.triggered.connect(lambda: quit())

        self.spinBox_scale.valueChanged.connect(self.image_scale)
        self.checkBox_render.stateChanged.connect(self.changed_render)
        self.spinBox_width.valueChanged.connect(self.update_render_image)
        self.spinBox_height.valueChanged.connect(self.update_render_image)
        self.displaymode_group.buttonClicked.connect(lambda: self.update_render_image() if self.checkBox_render.isChecked() else None)

        self.actionUndo.setEnabled(self.undo_stack.canUndo())
        self.actionRedo.setEnabled(self.undo_stack.canRedo())

    def changed_render(self):
        self.menuFile.setEnabled(True)
        self.menuImage.setEnabled(True)
        self.menuColors.setEnabled(True)
        if self.checkBox_render.isChecked():
            self.menuFile.setEnabled(False)
            self.menuImage.setEnabled(False)
            self.menuColors.setEnabled(False)
            self.update_render_image()
            return
        self.update_pixmap(self.image, self.spinBox_scale.value())


    def update_render_image(self):
        mode = self.displaymode_group.checkedButton().objectName()
        width = self.spinBox_width.value()
        height = self.spinBox_height.value()
        match mode:
            case "radioButton_fillarea":
                self.render_image = cv2.resize(self.image, (width, height), interpolation=cv2.INTER_AREA)
            case "radioButton_saveproportions":
                current_height, current_width = self.image.shape[:2]
                aspect_ratio = current_width / current_height
                new_aspect_ratio = width / height

                if new_aspect_ratio > aspect_ratio:
                    new_height = int(round(width / aspect_ratio))
                    resized = cv2.resize(self.image, (width, new_height))
                    border_size = abs((height - new_height) // 2)
                    resized = cv2.copyMakeBorder(resized, top=0, bottom=0, left=border_size, right=border_size,
                                                borderType=cv2.BORDER_CONSTANT, value=(0, 0, 0))
                    self.render_image = cv2.resize(resized, (width, height), interpolation=cv2.INTER_AREA )
                else:
                    # Изменяем размер изображения по высоте
                    new_width = int(round(height * aspect_ratio))
                    resized = cv2.resize(self.image, (new_width, height))

                    # Добавляем границы слева и справа
                    border_size = abs((width - new_width) // 2)
                    resized = cv2.copyMakeBorder(resized, top=border_size, bottom=border_size, left=0, right=0,
                                                borderType=cv2.BORDER_CONSTANT, value=(0, 0, 0))
                    self.render_image = cv2.resize(resized, (width, height), interpolation=cv2.INTER_AREA)


        # radioButton_saveproportions
        # radioButton_fillarea
        self.update_pixmap(self.render_image, self.spinBox_scale.value())

    def BriCon(self):
        self.dialog_bricon = BriCon_Dialog(parent=self, image=self.image)
        self.dialog_bricon.show()

    def make_undo_command(self, image):
        self.undo_stack.push(UndoCommand_Image(self, prev_image=image))

    def get_file_FileDialog(self):
        path_file = QFileDialog.getOpenFileName(self, "E2img - Image Selection", self.Data.get_options_end_path_file(), ";;".join(self.sup_format))[0]
        if path_file:
            self.Data.set_options_end_path_file("/".join(path_file.split("/")[0:-1]))
            self.load_image(path_file)

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QtGui.QDropEvent):
        urls = event.mimeData().urls()
        self.scrollArea.setStyleSheet("")
        if len(urls) == 1 and urls[0].toLocalFile():
            path = urls[0].toLocalFile()
            self.load_image(path)
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QtGui.QDragMoveEvent):
        if self.scrollArea.geometry().contains(event.pos()):
            self.scrollArea.setStyleSheet("background-color: #EFEFEF; border: 2px dashed black;")
            self.scrollAreaWidgetContents.setStyleSheet("border: None;")
            self.label_image.setStyleSheet("border: None;")
            event.acceptProposedAction()
        else:
            self.scrollArea.setStyleSheet("")
            event.ignore()

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

    def load_image(self, path):
        if self.isImage(path):
            image = self.image
            self.image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
            if self.label_image.pixmap() is not None:
                self.make_undo_command(image)
            self.update_pixmap(self.image, self.spinBox_scale.value())

            self.actionSave.setEnabled(True)
            self.actionSave_As.setEnabled(True)
            self.menuImage.setEnabled(True)
            self.menuColors.setEnabled(True)
            self.actionUpdate.setEnabled(True)
            self.centralwidget.setEnabled(True)


    def resize_image(self, image,  value):
        width = int(image.shape[1] * value / 100) or 1
        height = int(image.shape[0] * value / 100) or 1

        return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

    def update_pixmap(self, image, scale):
        # image = self.render_image(image, scale)
        pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(image, image.shape[1], image.shape[0],
                                                      image.shape[1] * 3, QtGui.QImage.Format_RGB888))
        self.label_image.setPixmap(pixmap)

    def image_scale(self, value):
        image = self.image
        if self.checkBox_render.isChecked():
            image = self.render_image
        image = self.resize_image(image, value)
        self.update_pixmap(image, value)

    def wheelEvent(self, event: QtGui.QWheelEvent):
        if self.label_image.pixmap() is not None and event.modifiers() == QtCore.Qt.ControlModifier:
            angle_delta = event.angleDelta().y() / 120.0
            if angle_delta > 0:
                self.spinBox_scale.setValue(math.ceil(self.spinBox_scale.value() * 1.1))
            else:
                self.spinBox_scale.setValue(math.floor(self.spinBox_scale.value() * 0.9))
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

