from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @property
    @abstractmethod
    def symbol(self):
        pass

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def set_position(self, new_postion):
        # 
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    pass


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        return [(r, c) for r, c in moves if 0 < r <= 8 and 0 < c <= 8]
    
    @property
    def symbol(self):
        return '♞' if self.color == "black" else '♘'

    def __str__(self):
        return f'Knight({self.symbol}) at position {self.position}'


class Bishop(Piece):
    pass


class Rook(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass


if __name__ == "__main__":
    piece = Knight("white", (1, 2))
    print(piece)
    print(piece.possible_moves())
