import random

die_faces = list(range(1, 7))

def main():
    seed = 0
    while True:
        random.seed(seed)
        first_roll = [
            random.choice(die_faces),
            random.choice(die_faces),
        ]
        second_roll = [
            random.choice(die_faces),
            random.choice(die_faces),
        ]
        third_roll = [
            random.choice(die_faces),
            random.choice(die_faces),
        ]
        fourth_roll = [
            random.choice(die_faces),
            random.choice(die_faces),
        ]
        if first_roll == second_roll == third_roll == fourth_roll == [6, 1]:
            print("Seed %s produces the desired rolls." % seed)
            exit()
        seed += 1


if __name__ == "__main__":
    main()
