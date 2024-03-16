class Matrix(object):
    def __init__(self,mat = None):
        self.mat = mat
    
    def get_matrix(self) -> list:
        return self.mat
        
    def transpose(self) -> list:
        if self.mat:
            try:
                return list(zip(*self.mat))
            except Exception as e:
                return f"Failed to convert transpose because {e}"
mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    
matrix_obj = Matrix(mat)
print(f"Original Matrix is : \n {matrix_obj.get_matrix()}")
print(f"Transpose of above matrix is : \n {matrix_obj.transpose()}")
