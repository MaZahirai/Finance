import numpy as np

def RSE(pred, true):
    return np.sqrt(np.sum((true-pred)**2)) / np.sqrt(np.sum((true-true.mean())**2))

def CORR(pred, true):
    u = ((true-true.mean(0))*(pred-pred.mean(0))).sum(0) 
    d = np.sqrt(((true-true.mean(0))**2*(pred-pred.mean(0))**2).sum(0))
    return (u/d).mean(-1)

def MAE(pred, true):
    return np.mean(np.abs(pred-true))

def MSE(pred, true):
    return np.mean((pred-true)**2)

def RMSE(pred, true):
    return np.sqrt(MSE(pred, true))

def MAPE(pred, true):
    return np.mean(np.abs((pred - true) / true))

def MSPE(pred, true):
    return np.mean(np.square((pred - true) / true))



def directional_accuracy(actual: np.ndarray, predicted: np.ndarray):

    return np.mean((np.sign(actual[1:] - actual[:-1]) == np.sign(predicted[1:] - predicted[:-1])).astype(int))*100




# Example usage:
#actual_values = [100.0, 105.0, 98.0, 102.0, 110.0]  # Actual values over time
#predicted_values = [98.0, 106.0, 99.0, 101.0, 112.0]  # Predicted values over time

#da = directional_accuracy(actual_values, predicted_values)
#print(f"Directional Accuracy: {da:.2f}%")


def metric(pred, true):
    mae = MAE(pred, true)
    mse = MSE(pred, true)
    rmse = RMSE(pred, true)
    mape = MAPE(pred, true)
    mspe = MSPE(pred, true)
    da = directional_accuracy(true,pred)
    
    return mae,mse,rmse,mape,mspe, da