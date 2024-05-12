from PyQt6 import QtWidgets, QtCore
from gui import Ui_Vote_Menu, Ui_Candidate_Menu

# Dictionary for keeping track of votes; much better than separate vars
votes = {"Bianca": 0, "Felicia": 0, "Edward": 0}

class VoteMenu(QtWidgets.QDialog, Ui_Vote_Menu):
    """Class for the main UI"""
    def __init__(self, parent=None) -> None:
        """Init for VoteMenu"""
        super().__init__(parent)
        self.setupUi(self)
        self.Vote_Button.clicked.connect(self.show_candidate_menu)
        self.Exit_Button.clicked.connect(QtWidgets.QApplication.instance().quit)

    def show_candidate_menu(self):
        """Shows the candidate menu"""
        self.hide()
        self.candidate_menu = CandidateMenu(parent=self)
        self.candidate_menu.show()


class CandidateMenu(QtWidgets.QDialog, Ui_Candidate_Menu):
    """Class for the candidate selection menu"""
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

    def vote(self, candidateName) -> None:
        """This function takes care of showing/hiding the UIs, and adding the votes to the dict."""
        try:
            votes[candidateName] += 1
            print(f"Vote for {candidateName} recorded.")
            self.hide()
            parent_widget = self.parent()
            if parent_widget is not None:
                parent_widget.show()
            else:
                print("Error: Parent widget is None.")
        except Exception as e:
            print("An error occurred during voting:", e)


def print_votes() -> None:
    """Small, simple function just to print the final numbers."""
    print("\nFinal Vote Tally:\n")
    for candidate, vote_count in votes.items():
        pluralVotes = "vote" if vote_count == 1 else "votes"
        print(f"{candidate}: {vote_count} {pluralVotes}")
    print("-"*16+f"\nTotal: {sum(votes.values())}")
