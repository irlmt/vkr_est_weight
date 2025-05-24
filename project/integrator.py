import numpy as np
from scipy.integrate import solve_ivp
from . import config, trajectory


def integrate_trajectory(m_f: float, begin_cond: list[float]):
    return solve_ivp(
        lambda t, y: trajectory.dynamics(t, y, m_f),
        [config.T_S, config.T_F],
        begin_cond,
        t_eval=np.arange(config.T_S, config.T_F, config.H_PRINT),
        rtol=config.EPS,
        atol=config.EPS,
    )
