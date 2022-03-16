import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import copy
import pyautogui as pg



# Clase para resolver Sudokus.
class SolveSudoku:
    """
    Se solicita la url de la página de origen del sudoku.
    """
    def __init__(self,url) -> None:
        self.__url = url

    # Métodos para obtener datos de la clase.
    def get_sudoku_problem(self):
        """Regresa el valor del tablero sin resolver."""
        return self.__board_problem
        
    def get_sudoku_solution(self):
        """Regresa el valor del tablero con la solución"""
        return self.__board_solution
    
    
    def get_validation(self):
        """
        Método para realizar todas las validaciones del problema.
        """
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

    # Método interno para el ordenamiento de los cuadros internos.
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
        
    # Método interno para cambiar los cuadros a listas.
    def __square2row(self,matrix,a,b,c,d):
        # Extrae cada cuadro de la matriz.
        sq = [row[a:b] for row in matrix][c:d]
        square_reordered=list()
        # Acomoda todos los elementos del cuadro en una lista.
        for row in sq:
            for element in row:
                square_reordered.append(element)

        return square_reordered  

    # Método interno para la evaluación de las posibles soluciones.
    def __possible(self,y,x,n):
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
        """
        Genera el valor de la solución y lo regresa por el método: get_sudoku_solution().
        """
        for y in range(0,9):
            for x in range(0,9):
                if self.__board[y][x]==0:
                    for n in range(1,10):
                        if self.__possible(y,x,n):
                            self.__board[y][x] = n
                            self.solve()
                            self.__board[y][x] = 0
                    return
        self.__board_solution = copy.deepcopy(self.__board)



    def get_sudoku(self,difficulty="hard"):
        """
        Obtiene el tablero de sudoku de la página web introducida como URL.

        Nota: En caso de no utilizar la página del NY Times, modificar el siguiente código.
        """

        #Configuración del Scraper
        options = Options()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    
        url = self.__url + difficulty
        driver.get(url)
        driver.implicitly_wait(0.5)

        # Obtención del tablero de Sudoku de la página web.
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
        # Generación de la matrix de datos.
        sudoku_list = []
    
        for i in range(0,81):
            if i/9.0 == i//9.0:
                sudoku_list.append([])

            sudoku_list[i//9].append(sudoku_dict[i])

        self.__board = copy.deepcopy(sudoku_list)
        self.__board_problem = copy.deepcopy(sudoku_list)

    def set_solution(self):
        """
        Regresa la solución del tablero a la página del NY Times.
        """
        new_line = ['down']+['left' for i in range(0,9)]
        for i in range(0,9):
            for j in range(0,9):
                pg.typewrite(str(self.__board_solution[i][j]))
                pg.typewrite(['right'])

            if i != 8 : pg.typewrite(new_line)


# Se genera el objeto a partir de la clase; instanciamiento.
sudoku = SolveSudoku("https://www.nytimes.com/puzzles/sudoku/")
# Se obtiene el tablero.
sudoku.get_sudoku()
# Se valida.
sudoku.get_validation()
# Si no regresa ningún error todo esta bien.

# Impresión del problea.
print("Sudoku del New York Times")
print(np.matrix(sudoku.get_sudoku_problem()))
# Resolución.
sudoku.solve()
# Impresión del resultado.
print("Solución del Sudoku")
print(np.matrix(sudoku.get_sudoku_solution()))

# Subir el resultado a la página del NY Times.
sudoku.set_solution()