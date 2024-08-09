

from src.players.base_player import BasePlayer
from src.minigames.maze import Maze
from src.minigames.speed_challenge import SpeedChallenge

MAZE, SPEED_CHALLENGE = MAZE, 'speed_challenge'


class Player(BasePlayer):

    def __init__(self):

        self.mazes, self.speed_challenges, self.minigames = [], [], []

        self.minigame_start_map = {
            MAZE: self._start_maze_challenge(),
            SPEED_CHALLENGE: self._start_speed_challenge()
        }
        self.current_minigame_name = None

    def _assign_to_minigame(self, minigame_name: str) -> None:
        if minigame_name not in self._get_minigame_names():
            raise ValueError(f'Please match an appropriate minigame name: Minigame names: {self._get_minigame_names()}')
        self._start_minigame(minigame_name)


    def _start_speed_challenge(self):
        self._set_minigame_name('speed challenge')
        self._add_maze()

    def _start_maze_challenge(self):
        self._set_minigame_name('maze')
        self._add_speed_challenge()

    def _start_minigame(self, minigame_name) -> (Maze, SpeedChallenge): self._get_minigame_start_map()[minigame_name]()


    def _create_speed_challenge(self) -> SpeedChallenge: return SpeedChallenge() #Add parameters
    def _create_maze(self) -> Maze: return Maze() #Add parameters


    def _get_current_minigame_name(self) -> str: return self.current_minigame_name
    def _get_current_maze(self): return self._get_mazes()[-1]
    def _get_current_speed_challenge(self): return self._get_speed_challenges()[-1]
    def _get_current_minigame(self) -> (Maze, SpeedChallenge):
        match self._get_current_minigame_name():
            case MAZE: return self._get_current_maze()
            case SPEED_CHALLENGE: self._get_current_speed_challenge()

    def _get_minigame_names(self) -> set: return {minigame_name for minigame_name, _ in self._get_minigame_start_map().items()}
    def _get_mazes(self) -> list[Maze]: return self.mazes
    def _get_speed_challenges(self) -> list[SpeedChallenge]: return self.speed_challenges
    def _get_minigames(self) -> list[Maze, SpeedChallenge]: return self.minigames


    def _get_minigame_start_map(self) -> dict: return self.minigame_start_map


    def _set_minigame_name(self, minigame_name: str = None) -> None: self.current_minigame_name = minigame_name


    def _add_maze(self) -> None:
        new_maze = self._create_maze()
        self._get_mazes().append(new_maze), self._get_minigames().append(new_maze)

    def _add_speed_challenge(self) -> None:
        new_speed_challenge = self._create_speed_challenge()
        self._get_speed_challenges().append(new_speed_challenge), self._get_minigames(new_speed_challenge)

    def _add_minigame(self, minigame: (Maze, SpeedChallenge)) -> None: self._get_minigames().append(minigame)



