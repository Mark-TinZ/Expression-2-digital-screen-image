# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\QDialog_FileOpen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_FileOpen(object):
    def setupUi(self, Dialog_FileOpen):
        Dialog_FileOpen.setObjectName("Dialog_FileOpen")
        Dialog_FileOpen.resize(400, 80)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog_FileOpen)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog_FileOpen)
        self.label.setMinimumSize(QtCore.QSize(40, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog_FileOpen)
        self.lineEdit.setInputMask("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(Dialog_FileOpen)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_FileOpen)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Open)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog_FileOpen)
        self.buttonBox.accepted.connect(Dialog_FileOpen.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog_FileOpen.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_FileOpen)

    def retranslateUi(self, Dialog_FileOpen):
        _translate = QtCore.QCoreApplication.translate
        Dialog_FileOpen.setWindowTitle(_translate("Dialog_FileOpen", "E2img - Image Selection"))
        self.label.setText(_translate("Dialog_FileOpen", "Path:"))
        self.lineEdit.setText(_translate("Dialog_FileOpen", "File path..."))
        self.toolButton.setText(_translate("Dialog_FileOpen", "..."))