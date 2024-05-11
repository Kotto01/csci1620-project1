# logic.py
votes = {"Bianca": 0, "Felicia": 0, "Edward": 0}

def print_votes():
    print("Final Vote Tally:")
    for candidate, vote_count in votes.items():
        print(f"{candidate}: {vote_count} votes")
