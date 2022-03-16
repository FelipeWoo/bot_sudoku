import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import copy
import pyautogui as pg

class SolveSudoku:
    def __init__(self,url) -> None:
        self.__url = url

    def get_sudoku_problem(self):
        return self.__board_problem
        
    def get_sudoku_solution(self):
        return self.__board_solution
    
    def get_validation(self):
        self.validate_dimension()
        self.validate_rows()
        self.validate_columns()
        self.validate_squares()
        

    
    def validate_dimension(self):
        """
        Validar que la dimensión del tablero sea de 9 x 9.
        """
        
        assert len(self.__board) == 9, "El tablero no es de 9 x 9"
        for row in self.__board:
            assert len(row) == 9, "El tablero no es de 9 x 9"
       

    def validate_rows(self,board ="new__board"):
        """
        Validar que no se repitan los números del 1 al 9 en ninguna fila.
        """
        

        if board == "new__board":
            board = self.__board

        for row in board:
            for element in row:
                if element != 0:
                    assert row.count(element) == 1, "El tablero tiene números repetidos."
       

    def validate_columns(self):
        """
        Validar que no se repitan los números del 1 al 9 en ninguna columna.
        """
        zipped_rows = zip(*self.__board)
        transpose__board = [list(row) for row in zipped_rows]
        self.validate_rows(transpose__board)

    def validate_squares(self):
        """
        Validar que no se repitan los números del 1 al 9 en ningún cuadro de 3 x 3.
        """
        board_reordered = self.__new_matrix()
        self.validate_rows(board_reordered)

    def __new_matrix(self): 
        # Acomoda las listas de los cuadros en orden para armar una nueva matriz. 
        matrix = [
            self.__square2row(self.__board,0,3,0,3),
            self.__square2row(self.__board,3,6,0,3),
            self.__square2row(self.__board,6,9,0,3),


            self.__square2row(self.__board,0,3,3,6),
            self.__square2row(self.__board,3,6,3,6),
            self.__square2row(self.__board,6,9,3,6),

            self.__square2row(self.__board,0,3,6,9),
            self.__square2row(self.__board,3,6,6,9),
            self.__square2row(self.__board,6,9,6,9),
        ]
        return matrix
        

    def __square2row(self,matrix,a,b,c,d):
        # Extrae cada cuadro de la matriz.
        sq = [row[a:b] for row in matrix][c:d]
        square_reordered=list()
        # Acomoda todos los elementos del cuadro en una lista.
        for row in sq:
            for element in row:
                square_reordered.append(element)

        return square_reordered  

    def possible(self,y,x,n):
        for i in range(0,9):
            if self.__board[y][i]==n:
                return False
        for i in range(0,9):
            if self.__board[i][x]==n:
                return False
        x0 = (x//3)*3
        y0 = (y//3)*3

        for i in range(0,3):
            for j in range(0,3):
                if self.__board[y0+i][x0+j]==n:
                    return False
        return True

    def solve(self):
        for y in range(0,9):
            for x in range(0,9):
                if self.__board[y][x]==0:
                    for n in range(1,10):
                        if self.possible(y,x,n):
                            self.__board[y][x] = n
                            self.solve()
                            self.__board[y][x] = 0
                    return
        self.__board_solution = copy.deepcopy(self.__board)



    def get_sudoku(self,difficulty="hard"):
        options = Options()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    
        url = self.__url + difficulty
        driver.get(url)
        driver.implicitly_wait(0.5)


        sudoku_dict = {} 

        grid = driver.find_elements(By.CLASS_NAME, 'su-board')
        for e in grid:
            elements = e.find_elements(By.TAG_NAME, 'div')
            for element in elements:
                cell = element.get_attribute("data-cell")
                value = element.get_attribute("aria-label")
                if cell is None or value is None:
                    continue
                sudoku_dict[int(cell)] = 0 if value == 'empty' else int(value)

        sudoku_list = []
    
        for i in range(0,81):
            if i/9.0 == i//9.0:
                sudoku_list.append([])

            sudoku_list[i//9].append(sudoku_dict[i])

        self.__board = copy.deepcopy(sudoku_list)
        self.__board_problem = copy.deepcopy(sudoku_list)

    def set_solution(self):
        
        new_line = ['down']+['left' for i in range(0,9)]
        for i in range(0,9):
            for j in range(0,9):
                pg.typewrite(str(self.__board_solution[i][j]))
                pg.typewrite(['right'])

            if i != 8 : pg.typewrite(new_line)



sudoku = SolveSudoku("https://www.nytimes.com/puzzles/sudoku/")
sudoku.get_sudoku()
sudoku.get_validation()
print("Sudoku Problem from New York Times")
print(np.matrix(sudoku.get_sudoku_problem()))
sudoku.solve()
print("Sudoku Solution")
print(np.matrix(sudoku.get_sudoku_solution()))
sudoku.set_solution()
