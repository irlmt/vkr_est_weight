from .datatypes import TrajectoryPoint


def load_trajectory(filepath: str) -> list[TrajectoryPoint]:
    trajectory = []
    with open(filepath, "r") as file:
        file.readline()  # пропуск заголовка
        for line in file:
            values = list(map(float, line.strip().split()))
            if len(values) >= 7:
                trajectory.append(
                    TrajectoryPoint(
                        t=values[0],
                        x=values[1],
                        y=values[2],
                        z=values[3],
                        vx=values[4],
                        vy=values[5],
                        vz=values[6],
                    )
                )
    return trajectory
