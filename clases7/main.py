# Definamos una matriz de 3x3
# matriz: list[list[int]] = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for fila in matriz:
#     for elemento in fila:
#         print(elemento, end=" ")
#     print()  # Nueva línea después de cada fila

# Agregar elementos a una posicion especifica
# matriz[1].insert(1, 99)  # Insertar 99 en

from enum import Enum

class PieceType(Enum):
    X = "X"
    O = "O"

# Tres en ray o gato. Deben existir piezas X y O en posiciones lineales
# para poder ganar. Juegas dos jugadores.

class Player:
    def __init__(self, name: str = ""):
        self.name: str = name

    def __str__(self):
        return f"Soy {self.name}"

class GamePiece:
    def __init__(self, piece_type: PieceType, X: int, Y: int):
        self.__piece_type: PieceType = piece_type  # 'X' u 'O'
        self.__X = X
        self.__Y = Y
    # Identificar el tipo de pieza (X u O)
    def get_piece_type(self) -> PieceType:
        return self.__piece_type
    
    # Especificar la posicion en la matriz
    def get_X(self) -> int:
        return self.__X
    
    def get_Y(self) -> int:
        return self.__Y

class Board:
    def __init__(self):
        # Debe tener una matriz de 3x3
        self.__matrix: list[list[GamePiece | None]] = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
    
    # Debe tener metodo para agregar piezas
    def add_piece(self, piece: GamePiece) -> None:
        if self.__matrix[piece.get_X()][piece.get_Y()] is None:
            self.__matrix[piece.get_X()][piece.get_Y()] = piece
        else:
            raise ValueError("La posicion ya esta ocupada")
        
    # Informar si hay pieza en una posicion y que pieza es
    def get_piece_at(self, X: int, Y: int) -> GamePiece | None:
        return self.__matrix[X][Y]
    
    # Limpiar tablero
    def clear_board(self) -> None:
        self.__matrix = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

class Game:
    def __init__(self, player1: Player, player2: Player):
        # Inicializar el juego
        # Los jugadores
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.__current_turn = player1

    # Los turnos
    def play_turn(self, X: int, Y: int) -> None:
        game_piece = None
        gamer = self.__current_turn

        if self.__current_turn == self.player1:
            self.__current_turn = self.player2
            game_piece = GamePiece(PieceType.X, X, Y)
        else:
            self.__current_turn = self.player1
            game_piece = GamePiece(PieceType.O, X, Y)

        self.board.add_piece(game_piece)

    # Validar si hay ganador
    def check_winner(self) -> Player | None:
        # Revisar filas, columnas y diagonales
        # Retornar el jugador ganador o None si no hay ganador
        pass

    # Reiniciar el juego
    def reset_game(self) -> None:
        self.board.clear_board()
        self.__current_turn = self.player1

    # Terminar el juego. Al terminar el juego mostrar el ganador (Scoreboard)
    

player1 = Player()
player1.name = "Juan"
print(player1)

tablero = Board()
piezaX = GamePiece(PieceType.X, 0, 0)
piezaY = GamePiece(PieceType.O, 1, 1)
tablero.add_piece(piezaX)
tablero.add_piece(piezaY)