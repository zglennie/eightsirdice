import argparse
import random
import time

die_faces = list(range(1, 7))
default_players = ('PLAYER_ONE', 'PLAYER_TWO')

ONE = [
    ' ███████ ',
    '█████████',
    '████ ████',
    '█████████',
    ' ███████ ',
]

TWO = [
    ' ███████ ',
    '██ ██████',
    '█████████',
    '██████ ██',
    ' ███████ ',
]

THREE = [
    ' ███████ ',
    '██ ██████',
    '████ ████',
    '██████ ██',
    ' ███████ ',
]

FOUR = [
    ' ███████ ',
    '██ ███ ██',
    '█████████',
    '██ ███ ██',
    ' ███████ ',
]

FIVE = [
    ' ███████ ',
    '██ ███ ██',
    '████ ████',
    '██ ███ ██',
    ' ███████ ',
]

SIX = [
    ' ███████ ',
    '██ █ █ ██',
    '█████████',
    '██ █ █ ██',
    ' ███████ ',
]

die_glyphs = {
    1: ONE,
    2: TWO,
    3: THREE,
    4: FOUR,
    5: FIVE,
    6: SIX,
}

def spinner(seconds, width=12):
    left = 0
    moving_right = True
    start = time.time()
    while True:
        right = width - left - 1
        print(left * ' ' + 'O' + right * ' ', end='', flush=True)
        time.sleep(0.025)
        print('\r', end='', flush=True)
        if time.time() > start + seconds:
            break
        if moving_right:
            left += 1
            if left == width - 1:
                moving_right = False
        else:
            left -= 1
            if left == 0:
                moving_right = True

    print(' ' * width, end='\n', flush=True)


class DiceRoller:

    def __init__(self, players=default_players, graphical=False):
        self.players = list(players)
        self.graphical = graphical

        self.rolls = 0
        self.doubles = 0

        self.player_statistics = {
            player: {
                'rolls': 0,
                'doubles': 0,
            } for player in self.players
        }

    def roll(self):
        player = self.players[self.rolls % len(self.players)]
        print("{} is rolling the dice.".format(player))
        spinner(0.75)
        dice = [
            random.choice(die_faces),
            random.choice(die_faces),
        ]
        self.rolls += 1
        self.player_statistics[player]['rolls'] += 1
        if dice[0] == dice[1]:
            self.doubles += 1
            self.player_statistics[player]['doubles'] += 1
        print(dice)
        if self.graphical:
            print()
            first = die_glyphs[dice[0]]
            second = die_glyphs[dice[1]]
            assert len(first) == len(second)
            for i, first_part in enumerate(first):
                line = '    ' + first_part + '    ' + second[i]
                print(line)
            print()

    def print_statistics(self):
        print("Total Rolls: %s" % self.rolls)
        print("Total Doubles: %s (of %s)" % (self.doubles, self.rolls))
        print()
        for player in self.players:
            print("%s Rolls: %s" % (player,
                                    self.player_statistics[player]['rolls']))
            print("%s Doubles: %s (of %s)" % (player,
                                              self.player_statistics[player]['doubles'],
                                              self.player_statistics[player]['rolls']))
            print()


def main():
    argparser = argparse.ArgumentParser("Roll dice based on the supplied random seed. Good for backgammon.")

    print()
    players_str = input("Enter the names of the players, separated by commas (default: PLAYER_ONE, PLAYER_TWO):\n")
    if not players_str.strip():
        players = default_players
    else:
        players = tuple([element.strip() for element in players_str.split(',')])
    print("Players are: %s" % (players,))

    print()
    seed = input("Enter a seed for random number generation (text or number, default: 26860):\n")
    if not seed.strip():
        # This happens to produce four consecutive 6,1 rolls, which should alert the user
        # that they're on the default seed.
        seed = 26860
    elif seed.isdigit():
        # Parse as an integer if possible.
        seed = int(seed)
    print("Random seed is: %r" % seed)
    random.seed(a=seed)

    print()
    graphical_yesno = input("Graphical mode? Enter 'Y' or 'N' (default: 'N'):\n")
    if graphical_yesno.upper() == 'Y':
        graphical = True
    elif graphical_yesno.upper() == 'N' or graphical_yesno.strip() == '':
        graphical = False
    else:
        _ = input("Invalid choice.")
        exit()

    print()
    print("Commands:")
    print("  - Q: quit")
    print("  - S: print statistics")
    print("  - anything else: just roll the dice!")
    print()

    dice_roller = DiceRoller(players=players, graphical=graphical)

    while True:
        print()
        entry = input("> ")
        if entry.upper() == 'Q':
            exit()
        elif entry.upper() == 'S':
            dice_roller.print_statistics()
        else:
            dice_roller.roll()


if __name__ == '__main__':
    main()
