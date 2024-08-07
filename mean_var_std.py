import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convertir la lista de entrada a un arreglo numpy y remodelarlo
    arr = np.array(list).reshape(3, 3)

    # Cálculo de las estadísticas
    calculations = {
        'mean': [
            arr.mean(axis=0).tolist(),  # Media por columnas
            arr.mean(axis=1).tolist(),  # Media por filas
            arr.mean()                  # Media total
        ],
        'variance': [
            arr.var(axis=0).tolist(),   # Varianza por columnas
            arr.var(axis=1).tolist(),   # Varianza por filas
            arr.var()                   # Varianza total
        ],
        'standard deviation': [
            arr.std(axis=0).tolist(),    # Desviación estándar por columnas
            arr.std(axis=1).tolist(),    # Desviación estándar por filas
            arr.std()                    # Desviación estándar total
        ],
        'max': [
            arr.max(axis=0).tolist(),    # Máximo por columnas
            arr.max(axis=1).tolist(),    # Máximo por filas
            arr.max()                    # Máximo total
        ],
        'min': [
            arr.min(axis=0).tolist(),    # Mínimo por columnas
            arr.min(axis=1).tolist(),    # Mínimo por filas
            arr.min()                    # Mínimo total
        ],
        'sum': [
            arr.sum(axis=0).tolist(),     # Suma por columnas
            arr.sum(axis=1).tolist(),     # Suma por filas
            arr.sum()                     # Suma total
        ]
    }

    return calculations
