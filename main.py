import argparse
import matplotlib.pyplot as plt
from project import config
from project.data_loader import load_trajectory
from project.optimizer import MassOptimizer
from project.integrator import integrate_trajectory
from project.plotter import plot_trajectory
from project.utils import calculate_metrics


def main():
    parser = argparse.ArgumentParser(description="Rocket Payload Est")
    parser.add_argument("--plot", action="store_true", help="Show plot after calc")
    parser.add_argument(
        "--data",
        type=str,
        default="data/tr_gosk-AUT3st.txt",
        help="Path to file",
    )
    parser.add_argument(
        "--velocity-weight",
        type=float,
        default=0.0,
        help="Velocity error weight (default: 0.0 - consider only coordinates)",
    )
    args = parser.parse_args()

    reference = load_trajectory(args.data)
    optimizer = MassOptimizer(reference, velocity_weight=args.velocity_weight)
    m_opt, cost = optimizer.find_optimal_mass()

    print(f"Calculated weight m_кон: {m_opt:.2f}")
    print(
        f"Functionality (accounting for speeds with weight {args.velocity_weight}): {cost:.4f}"
    )

    result = integrate_trajectory(m_opt, config.INITIAL_STATE)

    metrics = calculate_metrics(reference, result)
    print(f"RMSE: {metrics['RMSE']:.2f} m")
    print(f"Max deviation: {metrics['Max deviation']:.2f} m")
    print(f"End deviation: {metrics['End deviation']:.2f} m")

    if args.plot:
        plot_trajectory(reference, result)


if __name__ == "__main__":
    main()
