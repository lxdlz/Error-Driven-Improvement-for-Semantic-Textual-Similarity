from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import mean_squared_error
import numpy as np


def calculate_pearson(y_true, y_pred):
    return pearsonr(y_true, y_pred)[0]


def calculate_spearman(y_true, y_pred):
    return spearmanr(y_true, y_pred)[0]


def calculate_mse(y_true, y_pred):
    return mean_squared_error(y_true, y_pred)


def calculate_rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))


def evaluate_all(y_true, y_pred):
    return {
        "pearson": calculate_pearson(y_true, y_pred),
        "spearman": calculate_spearman(y_true, y_pred),
        "mse": calculate_mse(y_true, y_pred),
        "rmse": calculate_rmse(y_true, y_pred),
    }