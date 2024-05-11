# main.py
import sys
from PyQt6 import QtWidgets
from gui import VoteMenu
from logic import print_votes

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    vote_menu = VoteMenu()

    app.aboutToQuit.connect(print_votes)

    vote_menu.show()
    sys.exit(app.exec())
