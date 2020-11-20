from PyQt5 import QtCore, QtGui, QtWidgets


class GUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1205, 760)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:1,stop:0 rgba(42,44,111,255),stop:0.521368 rgba(28,29,73,255));                      \n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.main_stacked = QtWidgets.QStackedWidget(self.centralwidget)
        self.main_stacked.setObjectName("main_stacked")
        self.login_page_page = QtWidgets.QWidget()
        self.login_page_page.setObjectName("login_page_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.login_page_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.login_page_page)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.title = QtWidgets.QLabel(self.frame_3)
        self.title.setGeometry(QtCore.QRect(300, -10, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(0, 223, 223);\n"
"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:1,stop:0 rgba(42,44,126,255),stop:0.521368 rgba(28,35,73,255));                      \n"
"")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(70, 80, 981, 611))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet("background-color: rgb(0, 0, 61);\n"
"border-radius: 40px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.login_label = QtWidgets.QLabel(self.frame_4)
        self.login_label.setGeometry(QtCore.QRect(20, 20, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("color: rgb(0, 223, 223);")
        self.login_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_label.setObjectName("login_label")
        self.username_label = QtWidgets.QLabel(self.frame_4)
        self.username_label.setGeometry(QtCore.QRect(70, 140, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(27)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color: rgb(0, 223, 223);")
        self.username_label.setObjectName("username_label")
        self.username_sign_in = QtWidgets.QLineEdit(self.frame_4)
        self.username_sign_in.setGeometry(QtCore.QRect(260, 150, 501, 42))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.username_sign_in.setFont(font)
        self.username_sign_in.setStyleSheet("QLineEdit{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.username_sign_in.setObjectName("username_sign_in")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(70, 240, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(27)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 223, 223);")
        self.label_3.setObjectName("label_3")
        self.password_sign_in = QtWidgets.QLineEdit(self.frame_4)
        self.password_sign_in.setGeometry(QtCore.QRect(260, 250, 501, 42))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.password_sign_in.setFont(font)
        self.password_sign_in.setStyleSheet("QLineEdit{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.password_sign_in.setObjectName("password_sign_in")
        self.login_button = QtWidgets.QPushButton(self.frame_4)
        self.login_button.setGeometry(QtCore.QRect(380, 350, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(31)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(0, 0, 204);\n"
"    color: rgb(0, 216, 216);\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(0, 0, 98);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.login_button.setObjectName("login_button")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(120, 470, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(27)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 223, 223);")
        self.label_4.setObjectName("label_4")
        self.link_sign_up = QtWidgets.QPushButton(self.frame_4)
        self.link_sign_up.setGeometry(QtCore.QRect(470, 473, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(31)
        self.link_sign_up.setFont(font)
        self.link_sign_up.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(0, 0, 204);\n"
"    color: rgb(0, 216, 216);\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(0, 0, 107);\n"
"}\n"
"")
        self.link_sign_up.setObjectName("link_sign_up")
        self.gridLayout_4.addWidget(self.frame_3, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.main_stacked.addWidget(self.login_page_page)
        self.sign_up_page = QtWidgets.QWidget()
        self.sign_up_page.setObjectName("sign_up_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.sign_up_page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.sign_up_page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(110, 100, 981, 581))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.frame_5.setFont(font)
        self.frame_5.setStyleSheet("background-color: rgb(0, 0, 61);\n"
"border-radius: 40px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.username_label_2 = QtWidgets.QLabel(self.frame_5)
        self.username_label_2.setGeometry(QtCore.QRect(50, 140, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(27)
        self.username_label_2.setFont(font)
        self.username_label_2.setStyleSheet("color: rgb(0, 223, 223);")
        self.username_label_2.setObjectName("username_label_2")
        self.sign_up_user = QtWidgets.QLineEdit(self.frame_5)
        self.sign_up_user.setGeometry(QtCore.QRect(260, 150, 501, 42))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.sign_up_user.setFont(font)
        self.sign_up_user.setStyleSheet("QLineEdit{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.sign_up_user.setObjectName("sign_up_user")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(50, 220, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(27)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 223, 223);")
        self.label_5.setObjectName("label_5")
        self.sign_up_password = QtWidgets.QLineEdit(self.frame_5)
        self.sign_up_password.setGeometry(QtCore.QRect(260, 230, 501, 42))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.sign_up_password.setFont(font)
        self.sign_up_password.setStyleSheet("QLineEdit{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.sign_up_password.setObjectName("sign_up_password")
        self.sign_up_button = QtWidgets.QPushButton(self.frame_5)
        self.sign_up_button.setGeometry(QtCore.QRect(390, 410, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(31)
        self.sign_up_button.setFont(font)
        self.sign_up_button.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(0, 0, 204);\n"
"    color: rgb(0, 216, 216);\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(0, 0, 98);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.sign_up_button.setObjectName("sign_up_button")
        self.login_label_2 = QtWidgets.QLabel(self.frame_5)
        self.login_label_2.setGeometry(QtCore.QRect(20, 30, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.login_label_2.setFont(font)
        self.login_label_2.setStyleSheet("color: rgb(0, 223, 223);")
        self.login_label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.login_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.login_label_2.setObjectName("login_label_2")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setGeometry(QtCore.QRect(50, 310, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(27)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 223, 223);")
        self.label_6.setObjectName("label_6")
        self.sign_up_email = QtWidgets.QLineEdit(self.frame_5)
        self.sign_up_email.setGeometry(QtCore.QRect(260, 310, 501, 42))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.sign_up_email.setFont(font)
        self.sign_up_email.setStyleSheet("QLineEdit{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.sign_up_email.setObjectName("sign_up_email")
        self.title_2 = QtWidgets.QLabel(self.frame_2)
        self.title_2.setGeometry(QtCore.QRect(320, 0, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.title_2.setFont(font)
        self.title_2.setStyleSheet("color: rgb(0, 223, 223);\n"
"border-radius: 20px;\n"
"")
        self.title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_2.setObjectName("title_2")
        self.back_button = QtWidgets.QPushButton(self.frame_2)
        self.back_button.setGeometry(QtCore.QRect(0, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(0, 0, 217);\n"
"}")
        self.back_button.setObjectName("back_button")
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.main_stacked.addWidget(self.sign_up_page)
        self.control_panel_page = QtWidgets.QWidget()
        self.control_panel_page.setObjectName("control_panel_page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.control_panel_page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_6 = QtWidgets.QFrame(self.control_panel_page)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.main_username_label = QtWidgets.QLabel(self.frame_6)
        self.main_username_label.setGeometry(QtCore.QRect(310, 0, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.main_username_label.setFont(font)
        self.main_username_label.setStyleSheet("color: rgb(0, 223, 223);\n"
"border-radius: 20px;\n"
"")
        self.main_username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_username_label.setObjectName("main_username_label")
        self.main_username_label_2 = QtWidgets.QLabel(self.frame_6)
        self.main_username_label_2.setGeometry(QtCore.QRect(10, 100, 511, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.main_username_label_2.setFont(font)
        self.main_username_label_2.setStyleSheet("color: rgb(0, 223, 223);\n"
"border-radius: 20px;\n"
"")
        self.main_username_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.main_username_label_2.setObjectName("main_username_label_2")
        self.upload_files_button = QtWidgets.QPushButton(self.frame_6)
        self.upload_files_button.setGeometry(QtCore.QRect(40, 200, 491, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.upload_files_button.setFont(font)
        self.upload_files_button.setMouseTracking(False)
        self.upload_files_button.setTabletTracking(False)
        self.upload_files_button.setAutoFillBackground(False)
        self.upload_files_button.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 40px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.upload_files_button.setObjectName("upload_files_button")
        self.view_files_button = QtWidgets.QPushButton(self.frame_6)
        self.view_files_button.setGeometry(QtCore.QRect(40, 320, 491, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.view_files_button.setFont(font)
        self.view_files_button.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 40px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}")
        self.view_files_button.setObjectName("view_files_button")
        self.share_files_button = QtWidgets.QPushButton(self.frame_6)
        self.share_files_button.setGeometry(QtCore.QRect(40, 440, 491, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.share_files_button.setFont(font)
        self.share_files_button.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 40px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}")
        self.share_files_button.setObjectName("share_files_button")
        self.open_shared_button = QtWidgets.QPushButton(self.frame_6)
        self.open_shared_button.setGeometry(QtCore.QRect(40, 570, 491, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.open_shared_button.setFont(font)
        self.open_shared_button.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 40px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}")
        self.open_shared_button.setObjectName("open_shared_button")
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setGeometry(QtCore.QRect(620, 90, 451, 580))
        self.frame_8.setStyleSheet("background-color: rgb(0, 0, 61);\n"
"border-radius: 40px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_circle1 = QtWidgets.QFrame(self.frame_8)
        self.frame_circle1.setGeometry(QtCore.QRect(100, 30, 250, 250))
        self.frame_circle1.setMinimumSize(QtCore.QSize(250, 250))
        self.frame_circle1.setMaximumSize(QtCore.QSize(250, 250))
        self.frame_circle1.setStyleSheet("QFrame{\n"
"    border: 5px solid rgb(60, 231, 195);\n"
"    border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_circle1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_circle1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_circle1.setObjectName("frame_circle1")
        self.label = QtWidgets.QLabel(self.frame_circle1)
        self.label.setGeometry(QtCore.QRect(60, 40, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("border: none;\n"
"color: rgb(60, 231, 195);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.frame_circle1)
        self.label_8.setGeometry(QtCore.QRect(20, 70, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border: none;\n"
" color: rgb(128, 102, 168);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.memory_used_label = QtWidgets.QLabel(self.frame_circle1)
        self.memory_used_label.setGeometry(QtCore.QRect(40, 130, 181, 64))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(60)
        self.memory_used_label.setFont(font)
        self.memory_used_label.setStyleSheet("border: none;\n"
"color: ;\n"
"color: rgb(0, 255, 30);\n"
"")
        self.memory_used_label.setAlignment(QtCore.Qt.AlignCenter)
        self.memory_used_label.setObjectName("memory_used_label")
        self.frame_circle2 = QtWidgets.QFrame(self.frame_8)
        self.frame_circle2.setGeometry(QtCore.QRect(100, 310, 250, 250))
        self.frame_circle2.setMinimumSize(QtCore.QSize(250, 250))
        self.frame_circle2.setMaximumSize(QtCore.QSize(250, 250))
        self.frame_circle2.setStyleSheet("QFrame{\n"
"    border: 5px solid rgb(60, 231, 195);\n"
"    border-radius: 125px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 5px solid rgb(105, 95, 148);\n"
"}")
        self.frame_circle2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_circle2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_circle2.setObjectName("frame_circle2")
        self.label_9 = QtWidgets.QLabel(self.frame_circle2)
        self.label_9.setGeometry(QtCore.QRect(50, 40, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border: none;\n"
"color: rgb(60, 231, 195);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_circle2)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border: none;\n"
" color: rgb(128, 102, 168);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.network_transfer_label = QtWidgets.QLabel(self.frame_circle2)
        self.network_transfer_label.setGeometry(QtCore.QRect(29, 120, 191, 64))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(60)
        self.network_transfer_label.setFont(font)
        self.network_transfer_label.setStyleSheet("border: none;\n"
"color: ;\n"
"color: rgb(0, 255, 30);\n"
"")
        self.network_transfer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.network_transfer_label.setObjectName("network_transfer_label")
        self.logout_button = QtWidgets.QPushButton(self.frame_6)
        self.logout_button.setGeometry(QtCore.QRect(0, 0, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet("QPushButton{\n"
"background-color:rgb(170, 0, 0);\n"
"border-radius: 10px;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(0, 0, 255);\n"
"}")
        self.logout_button.setObjectName("logout_button")
        self.gridLayout_5.addWidget(self.frame_6, 0, 0, 1, 1)
        self.main_stacked.addWidget(self.control_panel_page)
        self.open_files_page = QtWidgets.QWidget()
        self.open_files_page.setObjectName("open_files_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.open_files_page)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_7 = QtWidgets.QFrame(self.open_files_page)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.view_files_username_label = QtWidgets.QLabel(self.frame_7)
        self.view_files_username_label.setGeometry(QtCore.QRect(190, 0, 771, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.view_files_username_label.setFont(font)
        self.view_files_username_label.setStyleSheet("color: rgb(0, 223, 223);\n"
"border-radius: 20px;\n"
"")
        self.view_files_username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.view_files_username_label.setObjectName("view_files_username_label")
        self.commands_line_edit = QtWidgets.QLineEdit(self.frame_7)
        self.commands_line_edit.setGeometry(QtCore.QRect(70, 680, 891, 42))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.commands_line_edit.setFont(font)
        self.commands_line_edit.setStyleSheet("QLineEdit{\n"
"    background-color:rgb(0, 0, 117);\n"
"    border-radius: 10px;\n"
"    color: rgb(0, 223, 223);\n"
"\n"
"}\n"
"QLineEdit: hover{\n"
"    broder: 2px rgb(105, 95, 148);\n"
"}")
        self.commands_line_edit.setObjectName("commands_line_edit")
        self.back_button_2 = QtWidgets.QPushButton(self.frame_7)
        self.back_button_2.setGeometry(QtCore.QRect(0, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.back_button_2.setFont(font)
        self.back_button_2.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(0, 0, 217);\n"
"}")
        self.back_button_2.setObjectName("back_button_2")
        self.files_listing_stacked_obj = QtWidgets.QStackedWidget(self.frame_7)
        self.files_listing_stacked_obj.setGeometry(QtCore.QRect(60, 80, 1071, 591))
        self.files_listing_stacked_obj.setObjectName("files_listing_stacked_obj")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_9 = QtWidgets.QFrame(self.page)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(17)
        self.frame_9.setFont(font)
        self.frame_9.setStyleSheet("background-color: rgb(0, 0, 61);\n"
"border-radius: 40px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.page_index_in_pages = QtWidgets.QLabel(self.frame_9)
        self.page_index_in_pages.setGeometry(QtCore.QRect(350, 530, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.page_index_in_pages.setFont(font)
        self.page_index_in_pages.setStyleSheet("color: rgb(0, 223, 223);")
        self.page_index_in_pages.setObjectName("page_index_in_pages")
        self.next_page_button = QtWidgets.QPushButton(self.frame_9)
        self.next_page_button.setGeometry(QtCore.QRect(490, 530, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.next_page_button.setFont(font)
        self.next_page_button.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 117);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 3px solid rgb(0, 0, 217);\n"
"}")
        self.next_page_button.setObjectName("next_page_button")
        self.no_files_yet_label = QtWidgets.QLabel(self.frame_9)
        self.no_files_yet_label.setGeometry(QtCore.QRect(330, 240, 431, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(20)
        self.no_files_yet_label.setFont(font)
        self.no_files_yet_label.setStyleSheet("color: rgb(0, 223, 223);")
        self.no_files_yet_label.setObjectName("no_files_yet_label")
        self.reload_button = QtWidgets.QPushButton(self.frame_9)
        self.reload_button.setGeometry(QtCore.QRect(620, 530, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.reload_button.setFont(font)
        self.reload_button.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 117);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 3px solid rgb(0, 0, 217);\n"
"}")
        self.reload_button.setObjectName("reload_button")
        self.gridLayout_7.addWidget(self.frame_9, 0, 1, 1, 1)
        self.files_listing_stacked_obj.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.files_listing_stacked_obj.addWidget(self.page_2)
        self.apply_button = QtWidgets.QPushButton(self.frame_7)
        self.apply_button.setGeometry(QtCore.QRect(970, 680, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.apply_button.setFont(font)
        self.apply_button.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(0, 0, 217);\n"
"}")
        self.apply_button.setObjectName("apply_button")
        self.gridLayout_6.addWidget(self.frame_7, 0, 1, 1, 1)
        self.main_stacked.addWidget(self.open_files_page)
        self.share_files_page = QtWidgets.QWidget()
        self.share_files_page.setObjectName("share_files_page")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.share_files_page)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_10 = QtWidgets.QFrame(self.share_files_page)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.share_files_username_label = QtWidgets.QLabel(self.frame_10)
        self.share_files_username_label.setGeometry(QtCore.QRect(210, 0, 771, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.share_files_username_label.setFont(font)
        self.share_files_username_label.setStyleSheet("color: rgb(0, 223, 223);\n"
"border-radius: 20px;\n"
"")
        self.share_files_username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.share_files_username_label.setObjectName("share_files_username_label")
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setGeometry(QtCore.QRect(90, 125, 981, 531))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.frame_11.setFont(font)
        self.frame_11.setStyleSheet("background-color: rgb(0, 0, 61);\n"
"border-radius: 40px;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.username_label_3 = QtWidgets.QLabel(self.frame_11)
        self.username_label_3.setGeometry(QtCore.QRect(10, 110, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(27)
        self.username_label_3.setFont(font)
        self.username_label_3.setStyleSheet("color: rgb(0, 223, 223);")
        self.username_label_3.setObjectName("username_label_3")
        self.submit_share_button = QtWidgets.QPushButton(self.frame_11)
        self.submit_share_button.setGeometry(QtCore.QRect(260, 370, 491, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.submit_share_button.setFont(font)
        self.submit_share_button.setMouseTracking(False)
        self.submit_share_button.setTabletTracking(False)
        self.submit_share_button.setAutoFillBackground(False)
        self.submit_share_button.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 40px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.submit_share_button.setObjectName("submit_share_button")
        self.username_label_4 = QtWidgets.QLabel(self.frame_11)
        self.username_label_4.setGeometry(QtCore.QRect(10, 220, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(27)
        self.username_label_4.setFont(font)
        self.username_label_4.setStyleSheet("color: rgb(0, 223, 223);")
        self.username_label_4.setObjectName("username_label_4")
        self.share_code_line_edit = QtWidgets.QLineEdit(self.frame_11)
        self.share_code_line_edit.setGeometry(QtCore.QRect(210, 220, 711, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.share_code_line_edit.setFont(font)
        self.share_code_line_edit.setStyleSheet("QLineEdit{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.share_code_line_edit.setObjectName("share_code_line_edit")
        self.frame_16 = QtWidgets.QFrame(self.frame_11)
        self.frame_16.setGeometry(QtCore.QRect(200, 30, 120, 80))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.files_list_share = QtWidgets.QComboBox(self.frame_11)
        self.files_list_share.setGeometry(QtCore.QRect(210, 110, 711, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.files_list_share.setFont(font)
        self.files_list_share.setStyleSheet("QComboBox{\n"
"    background-color:rgb(0, 0, 98);\n"
"    border-radius:10px;\n"
"    color: rgb(0, 223, 223);\n"
"    \n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 4px solid rgb(0, 0, 217)\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox QListView{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QScrollBar{\n"
"    width:0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView { \n"
"selection-background-color: rgb(0, 0, 98);\n"
"outline: none;\n"
"    \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.files_list_share.setMaxVisibleItems(5)
        self.files_list_share.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.files_list_share.setPlaceholderText("")
        self.files_list_share.setObjectName("files_list_share")
        self.back_button_3 = QtWidgets.QPushButton(self.frame_10)
        self.back_button_3.setGeometry(QtCore.QRect(0, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.back_button_3.setFont(font)
        self.back_button_3.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(0, 0, 217);\n"
"}")
        self.back_button_3.setObjectName("back_button_3")
        self.gridLayout_8.addWidget(self.frame_10, 0, 0, 1, 1)
        self.main_stacked.addWidget(self.share_files_page)
        self.open_shared_page = QtWidgets.QWidget()
        self.open_shared_page.setObjectName("open_shared_page")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.open_shared_page)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_12 = QtWidgets.QFrame(self.open_shared_page)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.open_share_username_label = QtWidgets.QLabel(self.frame_12)
        self.open_share_username_label.setGeometry(QtCore.QRect(330, -10, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.open_share_username_label.setFont(font)
        self.open_share_username_label.setStyleSheet("color: rgb(0, 223, 223);\n"
"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:1,stop:0 rgba(42,44,126,255),stop:0.521368 rgba(28,35,73,255));                      \n"
"")
        self.open_share_username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.open_share_username_label.setObjectName("open_share_username_label")
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setGeometry(QtCore.QRect(110, 100, 981, 571))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.frame_13.setFont(font)
        self.frame_13.setStyleSheet("background-color: rgb(0, 0, 61);\n"
"border-radius: 40px;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.username_label_5 = QtWidgets.QLabel(self.frame_13)
        self.username_label_5.setGeometry(QtCore.QRect(30, 110, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(27)
        self.username_label_5.setFont(font)
        self.username_label_5.setStyleSheet("color: rgb(0, 223, 223);")
        self.username_label_5.setObjectName("username_label_5")
        self.file_code_line_edit = QtWidgets.QLineEdit(self.frame_13)
        self.file_code_line_edit.setGeometry(QtCore.QRect(260, 110, 661, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.file_code_line_edit.setFont(font)
        self.file_code_line_edit.setStyleSheet("QLineEdit{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.file_code_line_edit.setObjectName("file_code_line_edit")
        self.save_files_button = QtWidgets.QPushButton(self.frame_13)
        self.save_files_button.setGeometry(QtCore.QRect(260, 430, 491, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.save_files_button.setFont(font)
        self.save_files_button.setMouseTracking(False)
        self.save_files_button.setTabletTracking(False)
        self.save_files_button.setAutoFillBackground(False)
        self.save_files_button.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 40px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.save_files_button.setObjectName("save_files_button")
        self.username_label_6 = QtWidgets.QLabel(self.frame_13)
        self.username_label_6.setGeometry(QtCore.QRect(20, 310, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(27)
        self.username_label_6.setFont(font)
        self.username_label_6.setStyleSheet("color: rgb(0, 223, 223);")
        self.username_label_6.setObjectName("username_label_6")
        self.radioButton_1 = QtWidgets.QRadioButton(self.frame_13)
        self.radioButton_1.setGeometry(QtCore.QRect(290, 310, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setStyleSheet("QRadioButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QRadioButton:hover{\n"
"    border: 1px solid rgb(0, 0, 217);\n"
"}\n"
"")
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_13)
        self.radioButton_2.setGeometry(QtCore.QRect(450, 310, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("QRadioButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QRadioButton:hover{\n"
"    border: 1px solid rgb(0, 0, 217);\n"
"}\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_13)
        self.radioButton_3.setGeometry(QtCore.QRect(610, 310, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("QRadioButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QRadioButton:hover{\n"
"    border: 1px solid rgb(0, 0, 217);\n"
"}\n"
"")
        self.radioButton_3.setObjectName("radioButton_3")
        self.username_label_7 = QtWidgets.QLabel(self.frame_13)
        self.username_label_7.setGeometry(QtCore.QRect(20, 210, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(27)
        self.username_label_7.setFont(font)
        self.username_label_7.setStyleSheet("color: rgb(0, 223, 223);")
        self.username_label_7.setObjectName("username_label_7")
        self.file_name_line_edit = QtWidgets.QLineEdit(self.frame_13)
        self.file_name_line_edit.setGeometry(QtCore.QRect(260, 210, 661, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.file_name_line_edit.setFont(font)
        self.file_name_line_edit.setStyleSheet("QLineEdit{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.file_name_line_edit.setObjectName("file_name_line_edit")
        self.back_button_4 = QtWidgets.QPushButton(self.frame_12)
        self.back_button_4.setGeometry(QtCore.QRect(0, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.back_button_4.setFont(font)
        self.back_button_4.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(0, 0, 217);\n"
"}")
        self.back_button_4.setObjectName("back_button_4")
        self.gridLayout_9.addWidget(self.frame_12, 0, 0, 1, 1)
        self.main_stacked.addWidget(self.open_shared_page)
        self.upload_files_page = QtWidgets.QWidget()
        self.upload_files_page.setObjectName("upload_files_page")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.upload_files_page)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frame_14 = QtWidgets.QFrame(self.upload_files_page)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.upload_files_username_label = QtWidgets.QLabel(self.frame_14)
        self.upload_files_username_label.setGeometry(QtCore.QRect(340, 0, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.upload_files_username_label.setFont(font)
        self.upload_files_username_label.setStyleSheet("color: rgb(0, 223, 223);\n"
"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:1,stop:0 rgba(42,44,126,255),stop:0.521368 rgba(28,35,73,255));                      \n"
"")
        self.upload_files_username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.upload_files_username_label.setObjectName("upload_files_username_label")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setGeometry(QtCore.QRect(100, 90, 981, 571))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.frame_15.setFont(font)
        self.frame_15.setStyleSheet("background-color: rgb(0, 0, 61);\n"
"border-radius: 40px;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.username_label_8 = QtWidgets.QLabel(self.frame_15)
        self.username_label_8.setGeometry(QtCore.QRect(20, 40, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(27)
        self.username_label_8.setFont(font)
        self.username_label_8.setStyleSheet("color: rgb(0, 223, 223);")
        self.username_label_8.setObjectName("username_label_8")
        self.file_path_line_edit = QtWidgets.QLineEdit(self.frame_15)
        self.file_path_line_edit.setGeometry(QtCore.QRect(170, 40, 550, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.file_path_line_edit.setFont(font)
        self.file_path_line_edit.setStyleSheet("QLineEdit{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 20px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.file_path_line_edit.setObjectName("file_path_line_edit")
        self.browse_files_button = QtWidgets.QPushButton(self.frame_15)
        self.browse_files_button.setGeometry(QtCore.QRect(740, 40, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.browse_files_button.setFont(font)
        self.browse_files_button.setMouseTracking(False)
        self.browse_files_button.setTabletTracking(False)
        self.browse_files_button.setAutoFillBackground(False)
        self.browse_files_button.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.browse_files_button.setObjectName("browse_files_button")
        self.username_label_10 = QtWidgets.QLabel(self.frame_15)
        self.username_label_10.setGeometry(QtCore.QRect(10, 160, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(27)
        self.username_label_10.setFont(font)
        self.username_label_10.setStyleSheet("color: rgb(0, 223, 223);")
        self.username_label_10.setText("")
        self.username_label_10.setObjectName("username_label_10")
        self.username_label_11 = QtWidgets.QLabel(self.frame_15)
        self.username_label_11.setGeometry(QtCore.QRect(20, 170, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(27)
        self.username_label_11.setFont(font)
        self.username_label_11.setStyleSheet("color: rgb(0, 223, 223);")
        self.username_label_11.setObjectName("username_label_11")
        self.name_file_line_edit = QtWidgets.QLineEdit(self.frame_15)
        self.name_file_line_edit.setGeometry(QtCore.QRect(270, 170, 661, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.name_file_line_edit.setFont(font)
        self.name_file_line_edit.setStyleSheet("QLineEdit{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.name_file_line_edit.setObjectName("name_file_line_edit")
        self.upload_button = QtWidgets.QPushButton(self.frame_15)
        self.upload_button.setGeometry(QtCore.QRect(250, 370, 491, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.upload_button.setFont(font)
        self.upload_button.setMouseTracking(False)
        self.upload_button.setTabletTracking(False)
        self.upload_button.setAutoFillBackground(False)
        self.upload_button.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 40px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 5px solid rgb(0, 0, 217);\n"
"}\n"
"\n"
"\n"
"")
        self.upload_button.setObjectName("upload_button")
        self.back_button_5 = QtWidgets.QPushButton(self.frame_14)
        self.back_button_5.setGeometry(QtCore.QRect(0, 0, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.back_button_5.setFont(font)
        self.back_button_5.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 98);\n"
"    color: rgb(0, 223, 223);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(0, 0, 217);\n"
"}")

        self.back_button_5.setObjectName("back_button_5")
        self.gridLayout_10.addWidget(self.frame_14, 0, 0, 1, 1)
        self.main_stacked.addWidget(self.upload_files_page)
        self.gridLayout.addWidget(self.main_stacked, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_stacked.setCurrentIndex(1)
        self.files_listing_stacked_obj.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Dumay\'s Cloud Application"))
        self.login_label.setText(_translate("MainWindow", "Login To Your Acount"))
        self.username_label.setText(_translate("MainWindow", "Username:"))
        self.username_sign_in.setPlaceholderText(_translate("MainWindow", "Your Username"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.password_sign_in.setPlaceholderText(_translate("MainWindow", "Your Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.label_4.setText(_translate("MainWindow", "Don\'t have an acount?"))
        self.link_sign_up.setText(_translate("MainWindow", "Sign Up"))
        self.username_label_2.setText(_translate("MainWindow", "Username:"))
        self.sign_up_user.setPlaceholderText(_translate("MainWindow", "Your Username Here"))
        self.label_5.setText(_translate("MainWindow", "Password:"))
        self.sign_up_password.setPlaceholderText(_translate("MainWindow", "Your Password Here"))
        self.sign_up_button.setText(_translate("MainWindow", "Sign Up"))
        self.login_label_2.setText(_translate("MainWindow", "Sign Up"))
        self.label_6.setText(_translate("MainWindow", "Your Email:"))
        self.sign_up_email.setPlaceholderText(_translate("MainWindow", "Your Email Here, Use Real Emails Only"))
        self.title_2.setText(_translate("MainWindow", "Dumay\'s Cloud Application"))
        self.back_button.setText(_translate("MainWindow", "Back ←"))
        self.main_username_label.setText(_translate("MainWindow", "{username}\'s - Control Panel"))
        self.main_username_label_2.setText(_translate("MainWindow", "What would you like to do?"))
        self.upload_files_button.setText(_translate("MainWindow", "Upload Files"))
        self.view_files_button.setText(_translate("MainWindow", "View Your Files"))
        self.share_files_button.setText(_translate("MainWindow", "Share Files"))
        self.open_shared_button.setText(_translate("MainWindow", "Open Shared Files"))
        self.label.setText(_translate("MainWindow", "MEMORY USED"))
        self.label_8.setText(_translate("MainWindow", "0MB Used From 1GB"))
        self.memory_used_label.setText(_translate("MainWindow", "0%"))
        self.label_9.setText(_translate("MainWindow", "NETWORK TRANSFER"))
        self.label_10.setText(_translate("MainWindow", "0MB Used From 2GB"))
        self.network_transfer_label.setText(_translate("MainWindow", "0%"))
        self.logout_button.setText(_translate("MainWindow", " Logout ←"))
        self.view_files_username_label.setText(_translate("MainWindow", "{username} - View Your Files"))
        self.commands_line_edit.setPlaceholderText(_translate("MainWindow", "Commands here, availeble: run python files, apt-get install, ls -la and more!"))
        self.back_button_2.setText(_translate("MainWindow", "Back ←"))
        self.page_index_in_pages.setText(_translate("MainWindow", "Page 1 out of 1"))
        self.next_page_button.setText(_translate("MainWindow", "Next Page"))
        self.no_files_yet_label.setText(_translate("MainWindow", "You currently have no files saved!"))
        self.reload_button.setText(_translate("MainWindow", "Reload ↻"))
        self.apply_button.setText(_translate("MainWindow", "Apply"))
        self.share_files_username_label.setText(_translate("MainWindow", "{username} - Share Your Files To Others"))
        self.username_label_3.setText(_translate("MainWindow", "Select File:"))
        self.submit_share_button.setText(_translate("MainWindow", "Share File"))
        self.username_label_4.setText(_translate("MainWindow", "Share Code:"))
        self.share_code_line_edit.setPlaceholderText(_translate("MainWindow", "Set custom share code, default is 6 random letters(optional)"))
        self.back_button_3.setText(_translate("MainWindow", "Back ←"))
        self.open_share_username_label.setText(_translate("MainWindow", "{username} - Open Shared Files"))
        self.username_label_5.setText(_translate("MainWindow", "File code:"))
        self.file_code_line_edit.setPlaceholderText(_translate("MainWindow", "File Code Here"))
        self.save_files_button.setText(_translate("MainWindow", "Save File"))
        self.username_label_6.setText(_translate("MainWindow", "Where to save:"))
        self.radioButton_1.setText(_translate("MainWindow", "Your PC"))
        self.radioButton_2.setText(_translate("MainWindow", "Your Cloud"))
        self.radioButton_3.setText(_translate("MainWindow", "Both"))
        self.username_label_7.setText(_translate("MainWindow", "Name The File:"))
        self.file_name_line_edit.setPlaceholderText(_translate("MainWindow", "Name your file and than leave a dot (e.g : {file}. )"))
        self.back_button_4.setText(_translate("MainWindow", "Back ←"))
        self.upload_files_username_label.setText(_translate("MainWindow", "{username} - Upload Files"))
        self.username_label_8.setText(_translate("MainWindow", "File Path:"))
        self.file_path_line_edit.setPlaceholderText(_translate("MainWindow", "File path here, each file separated with \"||\""))
        self.browse_files_button.setText(_translate("MainWindow", "Browse Files..."))
        self.username_label_11.setText(_translate("MainWindow", "Name The File:"))
        self.name_file_line_edit.setPlaceholderText(_translate("MainWindow", "Name your files e.g file1||file2|| etc (optional)"))
        self.upload_button.setText(_translate("MainWindow", "Upload"))
        self.back_button_5.setText(_translate("MainWindow", "Back ←"))

