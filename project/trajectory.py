import numpy as np
import math
from . import config


def thrust(t: float, m_f: float) -> float:
    return (config.M_DOT * config.G0 * config.P_UD) / (
        m_f + config.M_DOT * (config.T_F - t)
    )


def dynamics(t: float, y: list[float], m_f: float) -> np.ndarray:
    x, vx, y_pos, vy, z, vz = y
    r_squared = x**2 + y_pos**2 + z**2
    a_grav = (config.G0 * config.R_Z**2) / r_squared
    v_mag = math.sqrt(vx**2 + vy**2 + vz**2)
    f_thrust = thrust(t, m_f)

    return np.array(
        [
            vx,
            a_grav + f_thrust * (vx / v_mag),
            vy,
            a_grav + f_thrust * (vy / v_mag),
            vz,
            a_grav + f_thrust * (vz / v_mag),
        ]
    )
