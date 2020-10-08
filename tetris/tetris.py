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

from typing import Dict, List, Union

Board = Dict[
    int,
    Dict[int, int, int, int],
    List[int],
    List[List[int]],
]

TETROMINOES = [
    [ # I
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 1, 1, 1, 1,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
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
        0, 1, 1,
        0, 1, 1,
        0, 0, 0,
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

OFFSETS = [
    (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), # 0
    (0, 0), (1, 0), (1, -1), (0, 2), (1, 2), # R
    (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), # 2
    (0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2), # L
]

I_OFFSETS = [
    (0, 0), (-1, 0), (2, 0), (-1, 0), (2, 0), # 0
    (-1, 0), (0, 0), (0, 0), (0, 1), (0, -2), # R
    (-1, 1), (1, 1), (-2, 1), (1, 0), (-2, 0), # 2
    (0, 1), (0, 1), (0, 1), (0, -1), (0, 2), # L
]

O_OFFSETS = [
    (0, 0), # 0
    (0, -1), # R
    (-1, -1), # 2
    (-1, 0), # L
]

ROTATE_MAP = {'0': 0, 'R': 1, '2': 2, 'L': 3}
TETROMINO_MAP = {'I': 0, 'J': 1, 'L': 2, 'O': 3, 'S': 4, 'T': 5, 'Z': 6}
DIRECTION_MAP = {'clockwise': 1, 'counterclockwise': -1}

def display(board_state: Board) -> None:
    """Displays the current board state.

    TODO: currently simply printing to console. update to use curses.

    Args:
        board_state: Dictionary containing the board state.
    """

def true_rotate(tetromino: List[int]) -> List[int]:
    """Rotates a given tetromino clockwise and returns the rotated one.

    Args:
        tetromino: A list representation of the tetromino.

    Returns:
        A list representation of the rotated tetromino
    """
    
    # This nested function returns the new index for a given index after a
    # clockwise rotation.
    def rot(idx: int, dim: int) -> int:
        return (dim - 1 - (idx % dim))*dim + idx//dim

    dim = int(len(tetromino)**0.5)
    return [tetromino[rot(i, dim)] for i in tetromino]

def collision(board_state: Board, tetromino: List[int]) -> bool:
    """Checks if given board results in a collision.

    Args:
        board_state:
        tetromino:

    Returns:
        True if there is a collision, False if there is not.
    """
    pass

def rotate(board_state: Board, direction: str = 'clockwise') -> Board:
    """Attempts to rotate the current piece in the given direction.

    Args:
        board_state:
        direction:
    
    Returns:
        A new board state.
    """
    pass

def translate(board_state: Board, direction: str = 'down') -> Board:
    """Attempts to translate the current piece in the given direction.

    Args:
        board_state:
        direction:

    Returns:
        A new board state.
    """
    pass

def store(board_state: Board) -> Board:
    """Attempt to store the current piece.

    Args:
        board_state:

    Returns:
        A new board state.
    """
    pass

def lock(board_state: Board) -> Union[bool, Board]:
    """Checks to see if the current piece should be locked.

    If the piece should not be locked, returns False. Otherwise, returns the
    new board state with the locked piece.

    Args:
        board_state:

    Returns:
        
    """
    pass

def move(board_state: Board, key: str = 'down') -> Board:
    """Attempts to move the active piece based on the key.

    Key presses allowed: 'up', 'down', 'left', 'right', 'clockwise',
    'counterclockwise', 'store'.

    Args:
        board_state: Dictionary containing the board state.
        key: A strign representation of the key pressed.

    Returns:
        The new board state
    """
    
    translations = set('up', 'down', 'left', 'right')
    rotations = set('clockwise', 'counterclockwise')

    if key in translations:
        return translate(board_state, key)
    elif key in rotations:
        return rotate(board_state, key)
    else: # elif key == 'store':
        pass
