def inception_dream(num_dream_lvl):
    return 1 + int(inception_dream(num_dream_lvl - 1))

# lab6 Question 3 & 4 
def save_game(winner, hero_name = "", num_stars=0):
    with open("save.txt", "a") as file:
        if winner == "hero":
            file.write(f"hero {hero_name} has killed the monster and gained {num_stars},\n")
        elif winner == "monster":
            file.write(f"Monster killed the {hero_name}.\n")
            file.close()

# lab6 question 5a


def load_game():
    try:
        with open("save.txt", "r") as file:
            print("    |    Loading from saved file ..")
            lines =file.readlines()
            if lines:
                last_line = lines[-1].strip()
                return last_line
    except FileNotFoundError:
        print("    |    No pre game found. Start again")
        return None


# lab6 question 5b