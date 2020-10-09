__author__ = 'John Evans'
__copyright__ = 'Copyright 2020 John Evans'
__credits__ = ['John Evans']
__license__ = 'Apache License 2.0'
__version__ = '0.0.1'
__maintainer__ = 'John Evans'
__email__ = 'thejevans@gmail.com'
__status__ = 'Development'

"""
Docstring
"""

from typing import Dict, List, Union, Optional

import time

from pynput import keyboard

Board = Dict[
    Optional[str],
    str,
    int,
    int,
    Optional[str],
    List[int],
    List[int],
    int,
    bool,
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

ROTATE_INT = {'0': 0, 'R': 1, '2': 2, 'L': 3}
INT_ROTATE = ('0', 'R', '2', 'L')
TETROMINO_INT = {'I': 0, 'J': 1, 'L': 2, 'O': 3, 'S': 4, 'T': 5, 'Z': 6}
DIRECTION_INT = {'clockwise': 1, 'counterclockwise': -1}

KEYMAP = { # TODO: change the keys to the correct strings
    'up': 'up',
    'down': 'down',
    'left': 'left',
    'right': 'right',
    'clockwise': 'clockwise',
    'counterclockwise': 'counterclockwise',
    'store': 'store',
}

def display(board_state: Board) -> None:
    """Displays the current board state.

    TODO: currently simply printing to console. update to use curses.

    Args:
        board_state: Dictionary containing the board state.
    """
    # TODO: write this function

def true_rotate(board_state: Board, new_rotation: str = '0') -> List[int]:
    """Rotates a given tetromino clockwise and returns the rotated one.

    Args:
        board_state: 
        new_rotation: 

    Returns:
        A list representation of the rotated tetromino

    Raises:
        AssertionError: 
    """

    # This nested function returns the new index for a given index after a
    # clockwise rotation.
    def rot(idx: int, dim: int) -> int:
        return (dim - 1 - (idx % dim))*dim + idx//dim

    tetromino_idx = TETROMINO_INT[board_state['tetromino']]
    tetromino = TETROMINOES[tetromino_idx]
    current_rotation_idx = ROTATE_INT[board_state['rotation']]
    new_rotation_idx = ROTATE_INT[new_rotation]

    iterations = (4 + new_rotation_idx - current_rotation_idx) % 4

    assert(iterations != 2)

    dim = int(len(tetromino)**0.5)

    for _ in range(iterations):
        tetromino = [tetromino[rot(i, dim)] for i in tetromino]

    return tetromino

def collision(board_state: Board) -> bool:
    """Checks if given board results in a collision.

    Args:
        board_state: 

    Returns:
        True if there is a collision, False if there is not.
    """
    # TODO: write this function
    pass


def kick(board_state: Board,
         rotated_board_state: Board,
         k: int,
) -> Union[bool, Board]:
    """Translates the rotated board using the offset tables.

    Returns the kicked board if there is a kick available. Otherwise, returns
    False.

    Args:
        board_state: 
        rotated_board_state: 
        k: The offset index to use.

    Returns:
        
    """

    i_rotate = ROTATE_INT[board_state['rotation']]
    f_rotate = ROTATE_INT[rotated_board_state['rotation']]

    if board_state['tetromino'] == 'O':
        if k != 0:
            return False
        i_offset = O_OFFSETS[i_rotate]
        f_offset = O_OFFSETS[f_rotate]

    elif ~(0 <= k <= 4):
        return False

    elif board_state['tetromino'] == 'I':
        i_offset = I_OFFSETS[i_rotate*5 + k]
        f_offset = I_OFFSETS[f_rotate*5 + k]

    else:
        i_offset = OFFSETS[i_rotate*5 + k]
        f_offset = OFFSETS[f_rotate*5 + k]

    x_kick = f_offset[0] - i_offset[0]
    y_kick = f_offset[1] - i_offset[1]

    kicked_board_state = rotated_board_state.copy()

    kicked_board_state['x'] += x_kick
    kicked_board_state['y'] += y_kick

    return kicked_board_state

def rotate(board_state: Board, direction: str = 'clockwise') -> Board:
    """Attempts to rotate the current piece in the given direction.

    Args:
        board_state:
        direction:

    Returns:
        A new board state.
    """

    rotate_offset = DIRECTION_INT[direction]
    current_rotate = ROTATE_INT[Board['rotation']]
    new_rotate = (current_rotate + rotate_offset) % 4

    rotated_board_state = board_state.copy()
    rotated_board_state['rotation'] = INT_ROTATE[new_rotate]

    k = 0
    kicked_board_state = kick(board_state, rotated_board_state, k)

    while collision(kicked_board_state):
        k += 1
        if kicked_board_state := kick(board_state, rotated_board_state, k):
            continue
        else:
            return board_state

    return kicked_board_state

def translate(board_state: Board, direction: str = 'down') -> Board:
    """Attempts to translate the current piece in the given direction.

    Args:
        board_state:
        direction:

    Returns:
        A new board state.
    """
    # TODO: write this function
    pass

def store(board_state: Board) -> Board:
    """Attempt to store the current piece.

    Args:
        board_state:

    Returns:
        A new board state.
    """
    # TODO: write this function
    pass

def lock(board_state: Board) -> Union[bool, Board]:
    """Checks to see if the current piece should be locked.

    If the piece should not be locked, returns False. Otherwise, returns the
    new board state with the locked piece.

    Args:
        board_state:

    Returns:
        
    """
    # TODO: make sure to clear lines
    # TODO: update score
    # TODO: write this function
    pass

def pop(board_state: Board) -> Board:
    # TODO: make sure to reset the store flag
    # TODO: write this function
    pass

def initialize_board() -> Board:
    """

    """
    board_state = {
        'tetromino': None,
        'rotation': '0',
        'x': 0,
        'y': 0,
        'stored': None,
        'stack': [],
        'queue': [],
        'score': 0,
        'store_flag': False,
    }
    
    # TODO: initialize stack
    # TODO: initialize queue

    return board_state

def game_over(board_state: Board) -> bool:
    # TODO: write this function
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
        if board_state['tetromino'] is None:
            return pop(board_state)

        translated_board_state = translate(board_state, key)

        if locked_board_state := lock(translated_board_state):
            return locked_board_state
        return translate(board_state, key)

    elif key in rotations:
        return rotate(board_state, key)

    else: # elif key == 'store':
        return store(board_state)

if __name__ == '__main__':
    TICK = 0.5
    board = initialize_board()

    with keyboard.Events() as events:
        t_i = time.perf_counter()
        while ~game_over(board):
            event = events.get(TICK)

            if event is not None:
                board = move(board, KEYMAP[event])
                display(board)

            if (time.perf_counter() - t_i) > TICK:
                t_i = time.perf_counter()
                board = move(board)
                display(board)

    print('GAME OVER')
    input("Press the <ENTER> key to continue...")
