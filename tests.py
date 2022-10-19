import unittest
from Four_In_Line import CuatroInLine, FullColumn, OutOfBoard

class TestCuatroInLine(unittest.TestCase):
    def test_create_board(self):
        InLine = CuatroInLine() 
        self.assertEqual(len(InLine.board), 8)
        self.assertEqual(len(InLine.board[0]), 8)

    def test_change_turn(self):
        InLine = CuatroInLine()
        InLine.change_turn()
        self.assertEqual(InLine.turn, "1")

    def test_insert_toke(self):
        InLine = CuatroInLine()
        InLine.insert_token(1)
        self.assertEqual(InLine.board[7][1], "0")

    def test_insert_toke_1(self):
        InLine = CuatroInLine()
        InLine.insert_token(2)
        InLine.insert_token(2)
        InLine.insert_token(1)
        self.assertEqual(InLine.board[7][1], "0")
        self.assertEqual(InLine.board[6][2], "1")

    def test_not_winner_initial(self):
       InLine = CuatroInLine()
       self.assertEqual(InLine.winner(), False)

    def test_not_winer_horizontal_outside_board(self):
        InLine = CuatroInLine()
        InLine.insert_token(5)
        InLine.insert_token(5)
        InLine.insert_token(6)
        InLine.insert_token(1)
        InLine.insert_token(7)
        self.assertEqual(InLine.winner(), False)

    def test_not_winer_horizontal_not_token(self):
        InLine = CuatroInLine()
        InLine.insert_token(0)
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(1)
        InLine.insert_token(2)
        InLine.insert_token(2)
        InLine.insert_token(4)
        self.assertEqual(InLine.winner(), False)

    def test_winer_horizontal(self):
        InLine = CuatroInLine()
        InLine.insert_token(0)
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(1)
        InLine.insert_token(2)
        InLine.insert_token(2)
        InLine.insert_token(3)
        self.assertEqual(InLine.winner(), True)

    def test_not_winer_vertical_outside_board(self):
        InLine = CuatroInLine()
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(0)
        InLine.insert_token(1)
        self.assertEqual(InLine.winner(), False)
    
    def test_not_winer_vertical_not_token(self):
        InLine = CuatroInLine()
        InLine.insert_token(0)
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(0)
        self.assertEqual(InLine.winner(), False)

    def test_winer_vertical(self):
        InLine = CuatroInLine()
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(0)
        self.assertEqual(InLine.winner(), True)

    def test_not_winer_diagonal_up_outside_board(self):
        InLine = CuatroInLine()
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(1)
        InLine.insert_token(0)
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(1)
        InLine.insert_token(0)
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(1)
        InLine.insert_token(2)
        InLine.insert_token(0)
        InLine.insert_token(2)
        InLine.insert_token(1)
        self.assertEqual(InLine.winner(), False)

    def test_not_winer_diagonal_up_not_token(self):
        InLine = CuatroInLine()
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(1)
        InLine.insert_token(2)
        InLine.insert_token(2)
        InLine.insert_token(3)
        InLine.insert_token(2)  
        self.assertEqual(InLine.winner(), False)

    def test_winer_diagonal_up(self):
        InLine = CuatroInLine()
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(1)
        InLine.insert_token(2)
        InLine.insert_token(2)
        InLine.insert_token(3)
        InLine.insert_token(2)  
        InLine.insert_token(3)
        InLine.insert_token(3)
        InLine.insert_token(4)
        InLine.insert_token(3)
        self.assertEqual(InLine.winner(), True)

    def test_not_winer_diagonal_down_outside_board(self):
        InLine = CuatroInLine()
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(2)
        InLine.insert_token(0)
        self.assertEqual(InLine.winner(), False)

    def test_not_winer_diagonal_down_not_token(self):
        InLine = CuatroInLine()
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(2)
        InLine.insert_token(0)
        InLine.insert_token(0)
        InLine.insert_token(2)
        InLine.insert_token(3)
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(1)
        self.assertEqual(InLine.winner(), False)

    def test_winer_diagonal_down(self):
        InLine = CuatroInLine()
        InLine.insert_token(0)
        InLine.insert_token(1)
        InLine.insert_token(2)
        InLine.insert_token(0)
        InLine.insert_token(0)
        InLine.insert_token(2)
        InLine.insert_token(4)
        InLine.insert_token(3)
        InLine.insert_token(1)
        InLine.insert_token(1)
        InLine.insert_token(3)
        InLine.insert_token(0)
        self.assertEqual(InLine.winner(), True)

    def test_Full_Column(self):
        InLine = CuatroInLine()
        InLine.insert_token(0)
        InLine.insert_token(0)
        InLine.insert_token(0)
        InLine.insert_token(0)
        InLine.insert_token(0)
        InLine.insert_token(0)
        InLine.insert_token(0)
        InLine.insert_token(0)
        with self.assertRaises(FullColumn):
            self.assertEqual(InLine.turn, "0")
            InLine.insert_token(0)
        self.assertEqual(InLine.turn, "0")
        InLine.insert_token(1)
        self.assertEqual(InLine.turn, "1")

    def test_Out_Of_Board(self):
        InLine = CuatroInLine()
        with self.assertRaises(OutOfBoard):
            self.assertEqual(InLine.turn, "0")
            InLine.insert_token(10)
        self.assertEqual(InLine.turn, "0")
        InLine.insert_token(1)
        self.assertEqual(InLine.turn, "1")

    def test_not_empate(self):
        InLine = CuatroInLine()
        InLine.insert_token(1)
        InLine.insert_token(2)
        InLine.insert_token(1)
        InLine.insert_token(2)
        InLine.insert_token(1)
        InLine.insert_token(2)
        InLine.insert_token(1)
        self.assertEqual(InLine.empate(),False)
    
    def test_empate(self):
        InLine = CuatroInLine()
        for i in range(3):
            for x in range(8):
                InLine.insert_token(x)
        for x in range(2):
            InLine.insert_token(1)
            InLine.insert_token(2)
            InLine.insert_token(5)
            InLine.insert_token(0)
            InLine.insert_token(3)
            InLine.insert_token(6)
            InLine.insert_token(7)
            InLine.insert_token(4)
        for i in range(3):
            for x in range(8):
                InLine.insert_token(x)
        self.assertEqual(InLine.empate(),True)

 
if __name__ == "__main__":
    unittest.main()