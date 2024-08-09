
'''
Main script to run the game.
'''

from real_src import Player


def exit_game(key: str):
    if key == 'EXIT':
        return False


def run(minigame):
    while True:
        selected_key = input()
        if exit_game(selected_key):
            break
        minigame.clicked_key(selected_key)
        minigame.show_game()
        print(f'Score: {minigame.get_score()}')
        if minigame.check_won():
            break


def main():
    player = Player()
    while True:
        player.pick_game(
            input('Choose a game ("maze" or "speed challenge"): '))
        minigame = player.get_current_minigame()
        run(minigame)


if __name__ == '__main__':

    main()
