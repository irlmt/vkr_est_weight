from project import config
from project.data_loader import load_trajectory
from project.optimizer import MassOptimizer
from project.integrator import integrate_trajectory
from project.utils import calculate_metrics
from project.plotter import plot_metric_curve


def main():
    weights = [0.0, 0.1, 0.3, 0.5, 1.0]
    rmse_values = []
    max_dev_values = []
    end_dev_values = []

    reference = load_trajectory("data/tr_gosk-AUT3st.txt")

    for w in weights:
        optimizer = MassOptimizer(reference, velocity_weight=w)
        m_opt, cost = optimizer.find_optimal_mass()
        result = integrate_trajectory(m_opt, config.INITIAL_STATE)
        metrics = calculate_metrics(reference, result)

        rmse_values.append(metrics["RMSE"])
        max_dev_values.append(metrics["Max deviation"])
        end_dev_values.append(metrics["End deviation"])

        print(
            f"w = {w:.2f} | RMSE = {metrics['RMSE']:.2f} | MaxDev = {metrics['Max deviation']:.2f} | EndDev = {metrics['End deviation']:.2f}"
        )

    plot_metric_curve(weights, rmse_values, max_dev_values, end_dev_values)


if __name__ == "__main__":
    main()
