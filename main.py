import argparse
import matplotlib.pyplot as plt
from project import config
from project.data_loader import load_trajectory
from project.optimizer import MassOptimizer
from project.integrator import integrate_trajectory


def plot_trajectory(reference, model):
    x_ref = [p.x for p in reference]
    y_ref = [p.y for p in reference]

    x_model = model.y[0]
    y_model = model.y[2]

    plt.figure(figsize=(10, 6))
    plt.plot(x_ref, y_ref, linestyle="--")
    plt.plot(x_model, y_model, label="Model")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("diff")
    plt.legend()
    plt.grid()
    plt.show()


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

    print(f"Calculated weught m_кон: {m_opt:.2f}")
    print(
        f"Functionality (accounting for speeds with weight {args.velocity_weight}): {cost:.4f}"
    )

    if args.plot:
        result = integrate_trajectory(m_opt, config.INITIAL_STATE)
        plot_trajectory(reference, result)


if __name__ == "__main__":
    main()
