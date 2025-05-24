from .datatypes import TrajectoryPoint


def load_trajectory(filepath: str) -> list[TrajectoryPoint]:
    trajectory = []
    with open(filepath, "r") as file:
        file.readline()
        for line in file:
            values = list(map(float, line.strip().split()))
            if len(values) >= 4:
                trajectory.append(
                    TrajectoryPoint(values[0], values[1], values[2], values[3])
                )
    return trajectory
