import numpy as np


def calc_disp(values: list[float]) -> float:
    if len(values):
        return sum(values) / len(values)


def calculate_metrics(reference, model):
    x_ref = np.array([p.x for p in reference])
    y_ref = np.array([p.y for p in reference])
    x_model = model.y[0]
    y_model = model.y[2]

    min_len = min(len(x_ref), len(x_model))
    x_ref, y_ref = x_ref[:min_len], y_ref[:min_len]
    x_model, y_model = x_model[:min_len], y_model[:min_len]

    mse = np.mean((x_ref - x_model) ** 2 + (y_ref - y_model) ** 2)
    rmse = np.sqrt(mse)
    max_dev = np.max(np.sqrt((x_ref - x_model) ** 2 + (y_ref - y_model) ** 2))
    end_dev = np.sqrt((x_ref[-1] - x_model[-1]) ** 2 + (y_ref[-1] - y_model[-1]) ** 2)

    return {"RMSE": rmse, "Max deviation": max_dev, "End deviation": end_dev}
