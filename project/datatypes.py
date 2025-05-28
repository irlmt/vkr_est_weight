from dataclasses import dataclass


@dataclass
class TrajectoryPoint:
    t: float
    x: float
    y: float
    z: float
    vx: float
    vy: float
    vz: float
