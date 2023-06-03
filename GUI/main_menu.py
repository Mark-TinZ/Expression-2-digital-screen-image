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

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.verticalLayout_preview = QtWidgets.QVBoxLayout()
        self.verticalLayout_preview.setObjectName("verticalLayout_preview")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 430, 527))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_image = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_image.setMinimumSize(QtCore.QSize(0, 0))
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
        self.spinBox_scale.setMaximum(999)
        self.spinBox_scale.setMinimum(1)
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
        self.horizontalLayout_4.addLayout(self.verticalLayout_preview)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.checkBox_change = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_change.setObjectName("checkBox_change")
        self.verticalLayout.addWidget(self.checkBox_change)

        self.gridLayout_shift = QtWidgets.QGridLayout()
        self.gridLayout_shift.setObjectName("gridLayout_shift")

        self.label_xshift = QtWidgets.QLabel(self.centralwidget)
        self.label_xshift.setObjectName("label_xshift")
        self.gridLayout_shift.addWidget(self.label_xshift, 0, 0, 1, 1)

        self.spinBox_xshift = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_xshift.setMinimumSize(QtCore.QSize(75, 0))
        self.spinBox_xshift.setMaximum(1023)
        self.spinBox_xshift.setObjectName("spinBox_xshift")
        self.gridLayout_shift.addWidget(self.spinBox_xshift, 0, 1, 1, 1)

        self.label_yshift = QtWidgets.QLabel(self.centralwidget)
        self.label_yshift.setObjectName("label_yshift")
        self.gridLayout_shift.addWidget(self.label_yshift, 0, 2, 1, 1)

        self.spinBox_yshift = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_yshift.setMinimumSize(QtCore.QSize(75, 0))
        self.spinBox_yshift.setMaximum(1023)
        self.spinBox_yshift.setObjectName("spinBox_yshift")
        self.gridLayout_shift.addWidget(self.spinBox_yshift, 0, 3, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_shift)

        self.checkBox_resolution = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_resolution.setTabletTracking(False)
        self.checkBox_resolution.setChecked(True)
        self.checkBox_resolution.setObjectName("checkBox_resolution")
        self.verticalLayout.addWidget(self.checkBox_resolution)

        self.gridLayout_image_resolution = QtWidgets.QGridLayout()
        self.gridLayout_image_resolution.setObjectName("gridLayout_image_resolution")

        self.label_width = QtWidgets.QLabel(self.centralwidget)
        self.label_width.setObjectName("label_width")
        self.gridLayout_image_resolution.addWidget(self.label_width, 0, 0, 1, 1)

        self.spinBox_width = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_width.setMinimumSize(QtCore.QSize(75, 0))
        self.spinBox_width.setMaximum(1023)
        self.spinBox_width.setObjectName("spinBox_width")
        self.gridLayout_image_resolution.addWidget(self.spinBox_width, 0, 1, 1, 1)

        self.label_height = QtWidgets.QLabel(self.centralwidget)
        self.label_height.setObjectName("label_height")
        self.gridLayout_image_resolution.addWidget(self.label_height, 0, 2, 1, 1)

        self.spinBox_height = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_height.setMinimumSize(QtCore.QSize(75, 0))
        self.spinBox_height.setMaximum(1023)
        self.spinBox_height.setObjectName("spinBox_height")
        self.gridLayout_image_resolution.addWidget(self.spinBox_height, 0, 3, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_image_resolution)

        self.checkBox_square = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_square.setObjectName("checkBox_square")
        self.verticalLayout.addWidget(self.checkBox_square)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.checkBox_advanced = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_advanced.setObjectName("checkBox_advanced")
        self.verticalLayout.addWidget(self.checkBox_advanced)

        self.verticalLayout_advanced = QtWidgets.QVBoxLayout()
        self.verticalLayout_advanced.setObjectName("verticalLayout_advanced")

        self.verticalLayout_digi_resolution = QtWidgets.QVBoxLayout()
        self.verticalLayout_digi_resolution.setObjectName("verticalLayout_digi_resolution")

        self.label_redolution = QtWidgets.QLabel(self.centralwidget)
        self.label_redolution.setObjectName("label_redolution")
        self.verticalLayout_digi_resolution.addWidget(self.label_redolution)

        self.gridLayout_digi_resolution = QtWidgets.QGridLayout()
        self.gridLayout_digi_resolution.setObjectName("gridLayout_digi_resolution")

        self.label_width_digi = QtWidgets.QLabel(self.centralwidget)
        self.label_width_digi.setObjectName("label_width_digi")
        self.gridLayout_digi_resolution.addWidget(self.label_width_digi, 0, 0, 1, 1)

        self.spinBox_width_digi = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_width_digi.setMinimumSize(QtCore.QSize(75, 0))
        self.spinBox_width_digi.setMaximum(1023)
        self.spinBox_width_digi.setObjectName("spinBox_width_digi")
        self.gridLayout_digi_resolution.addWidget(self.spinBox_width_digi, 0, 1, 1, 1)

        self.label_height_digi = QtWidgets.QLabel(self.centralwidget)
        self.label_height_digi.setObjectName("label_height_digi")
        self.gridLayout_digi_resolution.addWidget(self.label_height_digi, 0, 2, 1, 1)

        self.spinBox_height_digi = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_height_digi.setMinimumSize(QtCore.QSize(75, 0))
        self.spinBox_height_digi.setMaximum(1023)
        self.spinBox_height_digi.setObjectName("spinBox_height_digi")
        self.gridLayout_digi_resolution.addWidget(self.spinBox_height_digi, 0, 3, 1, 1)

        self.verticalLayout_digi_resolution.addLayout(self.gridLayout_digi_resolution)
        self.verticalLayout_advanced.addLayout(self.verticalLayout_digi_resolution)

        self.horizontalLayout_alignment = QtWidgets.QHBoxLayout()
        self.horizontalLayout_alignment.setObjectName("horizontalLayout_alignment")

        self.label_alignment = QtWidgets.QLabel(self.centralwidget)
        self.label_alignment.setObjectName("label_alignment")
        self.horizontalLayout_alignment.addWidget(self.label_alignment)

        self.comboBox_alignment = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_alignment.setObjectName("comboBox_alignment")
        self.comboBox_alignment.addItem("")
        self.comboBox_alignment.addItem("")
        self.comboBox_alignment.addItem("")
        self.comboBox_alignment.addItem("")
        self.comboBox_alignment.addItem("")
        self.comboBox_alignment.addItem("")
        self.comboBox_alignment.addItem("")
        self.comboBox_alignment.addItem("")
        self.comboBox_alignment.addItem("")
        self.horizontalLayout_alignment.addWidget(self.comboBox_alignment)

        self.verticalLayout_advanced.addLayout(self.horizontalLayout_alignment)
        self.verticalLayout.addLayout(self.verticalLayout_advanced)

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
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

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

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.menuColor_mode = QtWidgets.QMenu(self.menuImage)
        self.menuColor_mode.setIcon(icon1)
        self.menuColor_mode.setObjectName("menuColor_mode")

        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")

        MainWindow.setMenuBar(self.menubar)

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setIcon(icon3)
        self.actionSave_As.setObjectName("actionSave_As")

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setShortcut("")
        self.actionQuit.setObjectName("actionQuit")

        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/brightness.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionBrighthess_Contrast = QtWidgets.QAction(MainWindow)
        self.actionBrighthess_Contrast.setIcon(icon4)
        self.actionBrighthess_Contrast.setObjectName("actionBrighthess_Contrast")

        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setIcon(icon5)
        self.actionUndo.setObjectName("actionUndo")

        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setIcon(icon6)
        self.actionRedo.setObjectName("actionRedo")

        self.actionColorModeGroup = QtWidgets.QActionGroup(self)
        self.actionColorModeGroup.setObjectName("actionColorModeGroup")

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

        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setIcon(icon7)
        self.actionPreferences.setObjectName("actionPreferences")

        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/installing-updates.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setIcon(icon8)
        self.actionUpdate.setObjectName("actionUpdate")

        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setIcon(icon9)
        self.actionSave.setObjectName("actionSave")

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

        self.checkBox_change.setToolTip(_translate("MainWindow", "The shift of the image along the X and Y axis."))
        self.checkBox_change.setText(_translate("MainWindow", "Allow change"))

        self.label_xshift.setText(_translate("MainWindow", "X shift"))

        self.spinBox_xshift.setSuffix(_translate("MainWindow", " px"))

        self.label_yshift.setText(_translate("MainWindow", "Y shift"))

        self.spinBox_yshift.setSuffix(_translate("MainWindow", " px"))

        self.checkBox_resolution.setToolTip(_translate("MainWindow", "Automatically adjusts the image for correct output to the digital screen."))
        self.checkBox_resolution.setText(_translate("MainWindow", "Auto resolution"))

        self.label_width.setText(_translate("MainWindow", "Width"))

        self.spinBox_width.setSuffix(_translate("MainWindow", " px"))

        self.label_height.setText(_translate("MainWindow", "Height"))

        self.spinBox_height.setSuffix(_translate("MainWindow", " px"))

        self.checkBox_square.setToolTip(_translate("MainWindow", "Makes the image square for correct display on a digital screen. (recommended)"))
        self.checkBox_square.setText(_translate("MainWindow", "Square image"))

        self.checkBox_advanced.setText(_translate("MainWindow", "Advanced Rendering settings"))

        self.label_redolution.setText(_translate("MainWindow", "Digital screen resolution:"))

        self.label_width_digi.setText(_translate("MainWindow", "Width"))

        self.spinBox_width_digi.setSuffix(_translate("MainWindow", " px"))

        self.label_height_digi.setText(_translate("MainWindow", "Height"))

        self.spinBox_height_digi.setSuffix(_translate("MainWindow", " px"))

        self.label_alignment.setText(_translate("MainWindow", "Alignment"))

        self.comboBox_alignment.setItemText(0, _translate("MainWindow", "Left, Top"))
        self.comboBox_alignment.setItemText(1, _translate("MainWindow", "Left, Center"))
        self.comboBox_alignment.setItemText(2, _translate("MainWindow", "Left, Bottom"))
        self.comboBox_alignment.setItemText(3, _translate("MainWindow", "Center, Top"))
        self.comboBox_alignment.setItemText(4, _translate("MainWindow", "Center, Center"))
        self.comboBox_alignment.setItemText(5, _translate("MainWindow", "Center, Bottom"))
        self.comboBox_alignment.setItemText(6, _translate("MainWindow", "Right, Top"))
        self.comboBox_alignment.setItemText(7, _translate("MainWindow", "Right, Center"))
        self.comboBox_alignment.setItemText(8, _translate("MainWindow", "Right, Bottom"))

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
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

        self.actionSave_As.setText(_translate("MainWindow", "Save As…"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))

        self.actionQuit.setText(_translate("MainWindow", "Quit"))

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