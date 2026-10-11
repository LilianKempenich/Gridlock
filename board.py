
def _index(i: int, j: int):
    assert 0 <= i <= 8
    assert 0 <= j <= 8
    return i*9 + j


class Board:
    """A possibly incomplete Sudoku board, 0-indexed by row and column"""
    def __init__(self):
        self.contents = [None] * 81


    def put(self, value: int, i: int, j: int):
        """Place a number at this square"""
        assert 1 <= value <= 9
        index = _index(i, j)
        self.contents[index] = value


    def is_complete(self) -> bool:
        """Is every square of this sudoku board filled in?"""
        return all(x is not None for x in self.contents)


    def is_valid(self) -> bool:
        """Are the Sudoku constraints satisfied by this board?"""
        assert False
