import matplotlib.pyplot as plt


def plot_trajectory(reference, model):
    x_ref = [p.x for p in reference]
    y_ref = [p.y for p in reference]

    x_model = model.y[0]
    y_model = model.y[2]

    plt.figure(figsize=(10, 6))
    plt.plot(x_ref, y_ref, label="Исходная", linestyle="--")
    plt.plot(x_model, y_model, label="Модель")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Сравнение траекторий")
    plt.legend()
    plt.grid()
    plt.show()


import matplotlib.pyplot as plt


def plot_metric_curve(weights, rmse_values, max_dev_values, end_dev_values):
    plt.figure(figsize=(10, 6))

    plt.plot(weights, rmse_values, label="RMSE", marker="o")
    plt.plot(weights, max_dev_values, label="Max deviation", marker="o")
    plt.plot(weights, end_dev_values, label="End deviation", marker="o")

    plt.xlabel("Velocity weight")
    plt.ylabel("Metric value (m)")
    plt.title("Metric vs Velocity Weight")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()
