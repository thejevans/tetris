__author__ = 'John Evans'
__copyright__ = ''
__credits__ = ['John Evans']
__license__ = 'Apache License 2.0'
__version__ = '0.0.1'
__maintainer__ = 'John Evans'
__email__ = 'thejevans@gmail.com'
__status__ = 'Development'

"""
Docstring
"""

from typing import Dict, List

Board = Dict[
    int,
    Dict[int, int, int, int],
    List[int],
    List[List[int]],
]

TETROMINOES = [
    [ # I
        0, 0, 0, 0,
        1, 1, 1, 1,
        0, 0, 0, 0,
        0, 0, 0, 0,
    ],
    [ # J
        1, 0, 0,
        1, 1, 1,
        0, 0, 0,
    ],
    [ # L
        0, 0, 1,
        1, 1, 1,
        0, 0, 0,
    ],
    [ # O
        0, 1, 1, 0,
        0, 1, 1, 0,
        0, 0, 0, 0,
    ],
    [ # S
        0, 1, 1,
        1, 1, 0,
        0, 0, 0,
    ],
    [ # T
        0, 1, 0,
        1, 1, 1,
        0, 0, 0,
    ],
    [ # Z
        1, 1, 0,
        0, 1, 1,
        0, 0, 0,
    ],
]

KICKS = [
    (0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2), # 0 -> R
    (0, 0), (1, 0), (1, -1), (0, 2), (1, 2), # R -> 0
    (0, 0), (1, 0), (1, -1), (0, 2), (1, 2), # R -> 2
    (0, 0), (-1, 0), (-1, 1), (0, -2), (-1, -2), # 2 -> R
    (0, 0), (1, 0), (1, 1), (0, -2), (1, -2), # 2 -> L
    (0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2), # L -> 2
    (0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2), # L -> 0
    (0, 0), (1, 0), (1, 1), (0, -2), (1, -2), # 0 -> L
]

I_KICKS = [
    (0, 0), (-2, 0), (1, 0), (-2, -1), (1, 2), # 0 -> R
    (0, 0), (2, 0), (-1, 0), (2, 1), (-1, -2), # R -> 0
    (0, 0), (-1, 0), (2, 0), (-1, 2), (2, -1), # R -> 2
    (0, 0), (1, 0), (-2, 0), (1, -2), (-2, 1), # 2 -> R
    (0, 0), (2, 0), (-1, 0), (2, 1), (-1, -2), # 2 -> L
    (0, 0), (-2, 0), (1, 0), (-2, -1), (1, 2), # L -> 2
    (0, 0), (1, 0), (-2, 0), (1, -2), (-2, 1), # L -> 0
    (0, 0), (-1, 0), (2, 0), (-1, 2), (2, -1), # 0 -> L
]

def display(board_state: Board) -> None:
    """Displays the current board state.

    TODO: currently simply printing to console. update to use curses.

    Args:
        board_state: Dictionary containing the board state.
    """

def rotate(tetromino: List[int]) -> List[int]:
    """Rotates a given tetromino clockwise and returns the rotated one.

    Args:
        tetromino: A list representation of the tetromino.

    Returns:
        A list representation of the rotated tetromino
    """

    def rot(idx: int, dim: int) -> int:
        return (dim - 1 - (idx % dim))*dim + idx//dim

    if len(tetromino) == 12:
        return tetromino

    dim = int(len(tetromino)**0.5)
    return [tetromino[rot(i, dim)] for i in tetromino]

def move(board_state: Board, key: str = 'down') -> Board:
    """Attempts to move the active piece based on the key.

    Key presses allowed: 'up', 'down', 'left', 'right', 'store'.

    Args:
        board_state: Dictionary containing the board state.
        key: A strign representation of the key pressed.

    Returns:
        The new board state
    """

    if key == 'up':
        pass
    elif key == 'down':
        pass
    elif key == 'left':
        pass
    elif key == 'right':
        pass
    else: # elif key == 'store':
        pass
