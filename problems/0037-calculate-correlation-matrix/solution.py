import numpy as np

def calculate_correlation_matrix(X, Y=None):
    if Y is None:
        return np.corrcoef(X, rowvar=False)

    p = X.shape[1]
    return np.corrcoef(X, Y, rowvar=False)[:p, p:]