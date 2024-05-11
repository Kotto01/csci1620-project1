# gui.py
from PyQt6 import QtCore, QtWidgets
from logic import votes


class Ui_Candidate_Menu(object):
    def setupUi(self, Candidate_Menu):
        Candidate_Menu.setObjectName("Candidate_Menu")
        Candidate_Menu.resize(245, 289)
        self.Bianca_Button = QtWidgets.QPushButton(Candidate_Menu)
        self.Bianca_Button.setGeometry(QtCore.QRect(80, 130, 75, 23))
        self.Bianca_Button.setObjectName("Bianca_Button")
        self.Felicia_Button = QtWidgets.QPushButton(Candidate_Menu)
        self.Felicia_Button.setGeometry(QtCore.QRect(80, 190, 75, 23))
        self.Felicia_Button.setObjectName("Felicia_Button")
        self.Edward_Button = QtWidgets.QPushButton(Candidate_Menu)
        self.Edward_Button.setGeometry(QtCore.QRect(80, 160, 75, 23))
        self.Edward_Button.setObjectName("Edward_Button")
        self.Candidate_Menu_Label = QtWidgets.QLabel(Candidate_Menu)
        self.Candidate_Menu_Label.setGeometry(QtCore.QRect(50, 10, 180, 51))
        self.Candidate_Menu_Label.setObjectName("Candidate_Menu_Label")

        # Connect buttons to vote function
        self.Bianca_Button.clicked.connect(lambda: self.vote("Bianca"))
        self.Felicia_Button.clicked.connect(lambda: self.vote("Felicia"))
        self.Edward_Button.clicked.connect(lambda: self.vote("Edward"))

        self.retranslateUi(Candidate_Menu)
        QtCore.QMetaObject.connectSlotsByName(Candidate_Menu)

    def retranslateUi(self, Candidate_Menu):
        _translate = QtCore.QCoreApplication.translate
        Candidate_Menu.setWindowTitle(_translate("Candidate_Menu", "Candidate Menu"))
        self.Bianca_Button.setText(_translate("Candidate_Menu", "Vote Bianca"))
        self.Felicia_Button.setText(_translate("Candidate_Menu", "Vote Felicia"))
        self.Edward_Button.setText(_translate("Candidate_Menu", "Vote Edward"))
        self.Candidate_Menu_Label.setText(_translate("Candidate_Menu",
                                                     "<html><head/><body><p><span style=\" font-size:16pt;\">Candidate Menu</span></p></body></html>"))


class Ui_Vote_Menu(object):
    def setupUi(self, Vote_Menu):
        Vote_Menu.setObjectName("Vote_Menu")
        Vote_Menu.resize(237, 288)
        self.Vote_Button = QtWidgets.QPushButton(Vote_Menu)
        self.Vote_Button.setGeometry(QtCore.QRect(20, 190, 75, 23))
        self.Vote_Button.setObjectName("Vote_Button")
        self.Exit_Button = QtWidgets.QPushButton(Vote_Menu)
        self.Exit_Button.setGeometry(QtCore.QRect(140, 190, 75, 23))
        self.Exit_Button.setObjectName("Exit_Button")
        self.Vote_Menu_label = QtWidgets.QLabel(Vote_Menu)
        self.Vote_Menu_label.setGeometry(QtCore.QRect(60, 20, 111, 71))
        self.Vote_Menu_label.setObjectName("Vote_Menu_label")

        self.retranslateUi(Vote_Menu)
        QtCore.QMetaObject.connectSlotsByName(Vote_Menu)

    def retranslateUi(self, Vote_Menu):
        _translate = QtCore.QCoreApplication.translate
        Vote_Menu.setWindowTitle(_translate("Vote_Menu", "Vote Menu"))
        self.Vote_Button.setText(_translate("Vote_Menu", "Vote"))
        self.Exit_Button.setText(_translate("Vote_Menu", "Exit"))
        self.Vote_Menu_label.setText(_translate("Vote_Menu",
                                                "<html><head/><body><p><span style=\" font-size:16pt;\">Vote Menu</span></p></body></html>"))


class VoteMenu(QtWidgets.QDialog, Ui_Vote_Menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.Vote_Button.clicked.connect(self.show_candidate_menu)
        self.Exit_Button.clicked.connect(QtWidgets.QApplication.instance().quit)

    def show_candidate_menu(self):
        self.hide()
        self.candidate_menu = CandidateMenu(parent=self)  # Pass self as the parent
        self.candidate_menu.show()


class CandidateMenu(QtWidgets.QDialog, Ui_Candidate_Menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def vote(self, candidateName):
        try:
            votes[candidateName] += 1
            print(f"Vote for {candidateName} recorded.")
            self.hide()  # Hide the Candidate Menu
            parent_widget = self.parent()
            if parent_widget is not None:
                parent_widget.show()  # Show the Vote Menu
            else:
                print("Error: Parent widget is None.")
        except Exception as e:
            print("An error occurred during voting:", e)
