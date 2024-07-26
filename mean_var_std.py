import numpy as np

def calculate(list):

    if len(list)!=9:
        raise ValueError("La lista debe contener nueve números")
    matrix=np.array(list).reshape(3,3)
    calculations={
        "Mean":[np.mean(matrix,axis=0).tolist(),np.mean(matrix,axis=1).tolist(),
                np.mean(matrix).tolist()],
        "Variance":[np.var(matrix,axis=0).tolist(),np.var(matrix,axis=1).tolist(),
                    np.var(matrix).tolist()],
        "Sum":[np.sum(matrix,axis=0).tolist(),np.sum(matrix,axis=1).tolist(),
               np.sum(matrix).tolist()],
        "Standar Deviation":[np.std(matrix,axis=0).tolist(),np.std(matrix,axis=1).tolist(),
                             np.std(matrix).tolist()],
        "Máximum":[np.max(matrix,axis=0).tolist(),np.max(matrix,axis=1).tolist(),
                   np.max(matrix).tolist()],
        "Minimum":[np.min(matrix,axis=0).tolist(),np.min(matrix,axis=1).tolist(),
                   np.min(matrix).tolist()]
        }

    return calculations
try:

    print(calculate((1,2,3,4,5,6,7,8,9)))
  
except ValueError as error:
    print("error:",error)


    return calculations