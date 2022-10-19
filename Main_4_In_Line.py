from Four_In_Line import CuatroInLine, FullColumn, OutOfBoard

class MainFourInLine:
    
    def __init__(self):
        self.game = CuatroInLine()
        self.running = True
    
    def board(self):
        for x in range(1,9):
            print(f"  ({x}) ", end="")
        print("\n")
        print(" -----------------------------------------------")
        for x in range(8):
            print('-', end="")
            for y in range(8):
                print(f"  {self.game.board[x][y]}  -", end="")
            print("\n")
        print(" -----------------------------------------------")

    def run(self):
        while self.running:
                self.board()
                col = int(input(f"Turno del jugador {self.game.turn} --> En que columna quiere insertar la ficha: "))-1
                try:
                    self.game.insert_token(col)
                    if self.game.winner() or self.game.empate():
                        self.board()
                        self.running = False
                except OutOfBoard:
                    print("\n")
                    print('-------Columna fuera del tablero-------')
                    print("Ingrese una columna nuevamente")
                    print("\n")
                except FullColumn:
                    print("\n")
                    print('-------Columna llena-------')
                    print("Ingrese una columna nuevamente")
                    print("\n")
        self.game.change_turn()
        if self.game.winner():
            print("\n")
            print(f"El ganador es el jugador: {self.game.turn}")
        if self.game.empate():
            print('Empate')

MainFourInLine().run()
