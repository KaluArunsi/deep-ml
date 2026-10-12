import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    matrix = np.array(matrix)
    det = np.linalg.det(matrix)
    matrix_inv = (1/det) * np.array([[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]])

    return None if det == 0 else matrix_inv.round(1).tolist() 