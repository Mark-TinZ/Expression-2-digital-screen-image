from PyQt5 import QtCore
import struct

with open('ResData.dat', 'rb') as file:
    size_qt_resource_data = struct.unpack("I", file.read(4))[0]
    qt_resource_data = file.read(size_qt_resource_data)
    size_qt_resource_name = struct.unpack("I", file.read(4))[0]
    qt_resource_name = file.read(size_qt_resource_name)
    size_qt_resource_struct_v1 = struct.unpack("I", file.read(4))[0]
    qt_resource_struct_v1 = file.read(size_qt_resource_struct_v1)
    size_qt_resource_struct_v2 = struct.unpack("I", file.read(4))[0]
    qt_resource_struct_v2 = file.read(size_qt_resource_struct_v2)

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()