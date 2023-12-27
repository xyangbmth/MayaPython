from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

maya_main_window = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)

class TestDialog(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window):
        super().__init__(parent)
        self.setWindowTitle("test dialog")
        self.setMinimumWidth(200)
        
d = TestDialog()
d.show()
