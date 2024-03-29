from PyQt5 import QtCore, QtGui, QtWidgets
from . import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_preview = QtWidgets.QVBoxLayout()
        self.verticalLayout_preview.setObjectName("verticalLayout_preview")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 640, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_image = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_image.setMinimumSize(QtCore.QSize(0, 0))
        self.label_image.setText("")
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.verticalLayout_2.addWidget(self.label_image)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_preview.addWidget(self.scrollArea)
        self.horizontalLayout_rendering_settings = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rendering_settings.setObjectName("horizontalLayout_rendering_settings")
        self.spinBox_scale = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_scale.setMaximumSize(QtCore.QSize(56, 16777215))
        self.spinBox_scale.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox_scale.setAutoFillBackground(False)
        self.spinBox_scale.setWrapping(False)
        self.spinBox_scale.setFrame(True)
        self.spinBox_scale.setKeyboardTracking(True)
        self.spinBox_scale.setSuffix("%")
        self.spinBox_scale.setMaximum(800)
        self.spinBox_scale.setProperty("value", 100)
        self.spinBox_scale.setObjectName("spinBox_scale")
        self.horizontalLayout_rendering_settings.addWidget(self.spinBox_scale)
        self.label_filename = QtWidgets.QLabel(self.centralwidget)
        self.label_filename.setObjectName("label_filename")
        self.horizontalLayout_rendering_settings.addWidget(self.label_filename, 0, QtCore.Qt.AlignLeft)
        self.checkBox_render = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_render.setObjectName("checkBox_render")
        self.horizontalLayout_rendering_settings.addWidget(self.checkBox_render)
        self.verticalLayout_preview.addLayout(self.horizontalLayout_rendering_settings)
        self.horizontalLayout_2.addLayout(self.verticalLayout_preview)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_resolution = QtWidgets.QVBoxLayout()
        self.verticalLayout_resolution.setObjectName("verticalLayout_resolution")
        self.label_resolution = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_resolution.setFont(font)
        self.label_resolution.setObjectName("label_resolution")
        self.verticalLayout_resolution.addWidget(self.label_resolution)
        self.horizontalLayout_resolution = QtWidgets.QHBoxLayout()
        self.horizontalLayout_resolution.setObjectName("horizontalLayout_resolution")
        self.label_width = QtWidgets.QLabel(self.centralwidget)
        self.label_width.setObjectName("label_width")
        self.horizontalLayout_resolution.addWidget(self.label_width)
        self.spinBox_width = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_width.setMinimumSize(QtCore.QSize(100, 0))
        self.spinBox_width.setMinimum(1)
        self.spinBox_width.setMaximum(1023)
        self.spinBox_width.setProperty("value", 100)
        self.spinBox_width.setObjectName("spinBox_width")
        self.horizontalLayout_resolution.addWidget(self.spinBox_width)
        self.label_height = QtWidgets.QLabel(self.centralwidget)
        self.label_height.setObjectName("label_height")
        self.horizontalLayout_resolution.addWidget(self.label_height)
        self.spinBox_height = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_height.setMinimumSize(QtCore.QSize(100, 0))
        self.spinBox_height.setMinimum(1)
        self.spinBox_height.setMaximum(1023)
        self.spinBox_height.setProperty("value", 100)
        self.spinBox_height.setObjectName("spinBox_height")
        self.horizontalLayout_resolution.addWidget(self.spinBox_height)
        self.verticalLayout_resolution.addLayout(self.horizontalLayout_resolution)
        self.verticalLayout.addLayout(self.verticalLayout_resolution)
        self.verticalLayout_displaymode = QtWidgets.QVBoxLayout()
        self.verticalLayout_displaymode.setObjectName("verticalLayout_displaymode")
        self.label_displaymode = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_displaymode.setFont(font)
        self.label_displaymode.setObjectName("label_displaymode")
        self.verticalLayout_displaymode.addWidget(self.label_displaymode)
        self.displaymode_group = QtWidgets.QButtonGroup()
        self.radioButton_fillarea = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_fillarea.setChecked(True)
        self.radioButton_fillarea.setObjectName("radioButton_fillarea")
        self.displaymode_group.addButton(self.radioButton_fillarea)
        self.verticalLayout_displaymode.addWidget(self.radioButton_fillarea)
        self.radioButton_saveproportions = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_saveproportions.setObjectName("radioButton_saveproportions")
        self.displaymode_group.addButton(self.radioButton_saveproportions)
        self.verticalLayout_displaymode.addWidget(self.radioButton_saveproportions)
        self.verticalLayout.addLayout(self.verticalLayout_displaymode)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_filesize = QtWidgets.QLabel(self.centralwidget)
        self.label_filesize.setObjectName("label_filesize")
        self.horizontalLayout.addWidget(self.label_filesize)
        self.pushButton_convert = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_convert.setObjectName("pushButton_convert")
        self.horizontalLayout.addWidget(self.pushButton_convert, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuColors = QtWidgets.QMenu(self.menubar)
        self.menuColors.setObjectName("menuColors")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuImage = QtWidgets.QMenu(self.menubar)
        self.menuImage.setObjectName("menuImage")
        self.menuColor_mode = QtWidgets.QMenu(self.menuImage)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuColor_mode.setIcon(icon1)
        self.menuColor_mode.setObjectName("menuColor_mode")

        self.actionColorModeGroup = QtWidgets.QActionGroup(self)
        self.actionColorModeGroup.setObjectName("actionColorModeGroup")

        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon4)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setShortcut("")
        self.actionQuit.setObjectName("actionQuit")
        self.actionBrighthess_Contrast = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/brightness.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBrighthess_Contrast.setIcon(icon5)
        self.actionBrighthess_Contrast.setObjectName("actionBrighthess_Contrast")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon6)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon7)
        self.actionRedo.setObjectName("actionRedo")
        self.action24bit = QtWidgets.QAction(MainWindow)
        self.action24bit.setObjectName("action24bit")
        self.action24bit.setCheckable(True)
        self.action24bit.setChecked(True)
        self.actionColorModeGroup.addAction(self.action24bit)
        self.actionRRRGGGBBB = QtWidgets.QAction(MainWindow)
        self.actionRRRGGGBBB.setObjectName("actionRRRGGGBBB")
        self.actionRRRGGGBBB.setCheckable(True)
        self.actionColorModeGroup.addAction(self.actionRRRGGGBBB)
        self.actionRGBXXX = QtWidgets.QAction(MainWindow)
        self.actionRGBXXX.setObjectName("actionRGBXXX")
        self.actionRGBXXX.setCheckable(True)
        self.actionColorModeGroup.addAction(self.actionRGBXXX)
        self.actionXXX = QtWidgets.QAction(MainWindow)
        self.actionXXX.setObjectName("actionXXX")
        self.actionXXX.setCheckable(True)
        self.actionColorModeGroup.addAction(self.actionXXX)
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon8)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/installing-updates.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpdate.setIcon(icon9)
        self.actionUpdate.setObjectName("actionUpdate")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuColors.addAction(self.actionBrighthess_Contrast)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuColor_mode.addAction(self.action24bit)
        self.menuColor_mode.addAction(self.actionRRRGGGBBB)
        self.menuColor_mode.addAction(self.actionRGBXXX)
        self.menuColor_mode.addAction(self.actionXXX)
        self.menuImage.addAction(self.menuColor_mode.menuAction())
        self.menuSettings.addAction(self.actionPreferences)
        self.menuSettings.addAction(self.actionUpdate)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuImage.menuAction())
        self.menubar.addAction(self.menuColors.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "E2img img2eimg"))
        self.spinBox_scale.setToolTip(_translate("MainWindow", "Image scale."))
        self.spinBox_scale.setSuffix(_translate("MainWindow", "%"))
        self.label_filename.setText(_translate("MainWindow", "None"))
        self.checkBox_render.setText(_translate("MainWindow", "Render"))
        self.label_resolution.setText(_translate("MainWindow", "Digital screen resolution:"))
        self.label_width.setText(_translate("MainWindow", "Width:"))
        self.spinBox_width.setSuffix(_translate("MainWindow", " px"))
        self.label_height.setText(_translate("MainWindow", "Height:"))
        self.spinBox_height.setSuffix(_translate("MainWindow", " px"))
        self.label_displaymode.setText(_translate("MainWindow", "Display mode:"))
        self.radioButton_fillarea.setText(_translate("MainWindow", "Fill area"))
        self.radioButton_saveproportions.setText(_translate("MainWindow", "Save image proportions"))
        self.label_filesize.setText(_translate("MainWindow", "Size image: None"))
        self.pushButton_convert.setToolTip(_translate("MainWindow", "The image conversion process starts."))
        self.pushButton_convert.setText(_translate("MainWindow", "Convert"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuColors.setTitle(_translate("MainWindow", "Colors"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuImage.setTitle(_translate("MainWindow", "Image"))
        self.menuColor_mode.setTitle(_translate("MainWindow", "Color mode"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setIconText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionQuit.setText(_translate("MainWindow", "Quit", "123"))
        self.actionBrighthess_Contrast.setText(_translate("MainWindow", "Brighthess-Contrast"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.action24bit.setText(_translate("MainWindow", "24 Bit (Recommended)"))
        self.actionRRRGGGBBB.setText(_translate("MainWindow", "RRRGGGBBB"))
        self.actionRGBXXX.setText(_translate("MainWindow", "RGBXXX"))
        self.actionXXX.setText(_translate("MainWindow", "XXX"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))