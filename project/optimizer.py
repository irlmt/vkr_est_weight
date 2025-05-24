import math
from scipy.optimize import minimize_scalar
from . import config, integrator, utils
from .datatypes import TrajectoryPoint


class MassOptimizer:
    def __init__(self, reference: list[TrajectoryPoint]):
        self.reference = reference

    def cost_function(self, m_f: float) -> float:
        result = integrator.integrate_trajectory(m_f, config.INITIAL_STATE)
        points = [0.0]

        for i in range(min(len(result.t), len(self.reference))):
            dx = result.y[0, i] - self.reference[i].x
            dy = result.y[2, i] - self.reference[i].y
            dz = result.y[4, i] - self.reference[i].z
            points.append(dx**2 + dy**2 + dz**2)

        return math.sqrt(utils.calc_disp(points))

    def find_optimal_mass(self):
        result = minimize_scalar(
            self.cost_function, bounds=(config.M_MIN, config.M_MAX), method="bounded"
        )
        return result.x, self.cost_function(result.x)
