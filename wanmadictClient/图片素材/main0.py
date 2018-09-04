from PyQt5 import QtCore, QtGui, QtWidgets
from xincidian import Ui_Form
class My_window(QtWidgets.QWidget, Ui_Form):
	def __init__(self):
		super().__init__() # 初始化父类构造方法
		self.setupUi(self) # 调用父类属性设置方法
        
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv) # 创建主应用对象
	myshow = My_window() # 主窗口对象
	myshow.show() # 显示主窗口
	sys.exit(app.exec_()) # 主应用循环