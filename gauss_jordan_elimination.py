class GaussJodanElimination():
    def __init__(self, matrix):
        self.matrix = matrix
        self.cols = len(matrix[0])
        self.rows = len(matrix)

        self.row_echelon_form()
    
    def row_echelon_form(self):
        for self.index in range(self.rows):
            self.non_zero()
            self.first_one()
            self.zeros_under_one()
        self.round_matrix ()

    def non_zero(self):
        index = 1
        while (self.matrix[self.index][self.index] == 0
                and index < self.rows):
            if self.matrix[self.index + index][self.index] != 0:
                # swap rows
                self.row_swap(self.index, self.index+index)
            index += 1

    def first_one(self):
        dividing_number = self.matrix[self.index][self.index]
        for i in range(self.index, self.cols):
            self.matrix[self.index][i] /= dividing_number
        
    def zeros_under_one(self):
        for i in range(self.rows):
            if i == self.index:
                continue
            minus_number = self.matrix[i][self.index] * -1
            for j in range(self.index, self.cols):
                self.matrix[i][j] += self.matrix[self.index][j] * minus_number
                
    def item_switch_swap(self, x, y):
        temp_1 = (self.matrix[x][y],
        self.matrix[y][x])
        
        temp_2 = (self.matrix[y][x],
        self.matrix[x][y])
        
        (self.matrix[x][y],
        self.matrix[y][x]) = temp_2
        
        (self.matrix[y][x],
        self.matrix[x][y]) = temp_1

    def row_swap(self, row_1, row_2):
        temp_1 = (self.matrix[row_1],
        self.matrix[row_2])
        
        temp_2 = (self.matrix[row_2],
        self.matrix[row_1])
        
        (self.matrix[row_1],
        self.matrix[row_2]) = temp_2
        
        (self.matrix[row_2],
        self.matrix[row_1]) = temp_1
    
    def round_matrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = round(self.matrix[i][j], 5)

    def get_answers(self):
        answers = []
        for i in range(self.rows):
            answers.append(self.matrix[i][-1])
        return answers


test_amatrix = [[2, 1, -2, 15],
                [2, 3, 1, 20],
                [3, 2, 2, 28]]

test = GaussJodanElimination(test_amatrix)
print(test.matrix)