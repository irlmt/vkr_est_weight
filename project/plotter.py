import matplotlib.pyplot as plt


def plot_trajectory(reference, model):
    x_ref = [p.x for p in reference]
    y_ref = [p.y for p in reference]

    x_model = model.y[0]
    y_model = model.y[2]

    plt.figure(figsize=(10, 6))
    plt.plot(x_ref, y_ref, label="ГОСК", linestyle="--")
    plt.plot(x_model, y_model, label="Модель")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Сравнение траекторий")
    plt.legend()
    plt.grid()
    plt.show()
