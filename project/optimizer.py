import math
from scipy.optimize import minimize_scalar
from . import config, integrator, utils
from .datatypes import TrajectoryPoint


class MassOptimizer:
    def __init__(self, reference: list[TrajectoryPoint], velocity_weight: float = 0.0):
        self.reference = reference
        self.velocity_weight = velocity_weight

    def cost_function(self, m_f: float) -> float:
        result = integrator.integrate_trajectory(m_f, config.INITIAL_STATE)
        position_errors = []
        velocity_errors = []

        for i in range(min(len(result.t), len(self.reference))):
            dx = result.y[0, i] - self.reference[i].x
            dy = result.y[2, i] - self.reference[i].y
            dz = result.y[4, i] - self.reference[i].z

            position_errors.append(dx**2 + dy**2 + dz**2)

            if self.velocity_weight > 0.0:
                dvx = result.y[1, i]
                dvy = result.y[3, i]
                dvz = result.y[5, i]
                velocity_errors.append(dvx**2 + dvy**2 + dvz**2)

        position_disp = utils.calc_disp(position_errors)
        velocity_disp = utils.calc_disp(velocity_errors) if velocity_errors else 0.0

        total_cost = math.sqrt(position_disp + self.velocity_weight * velocity_disp)
        return total_cost

    def find_optimal_mass(self):
        result = minimize_scalar(
            self.cost_function,
            bounds=(config.M_MIN, config.M_MAX),
            method="bounded",
        )
        return result.x, self.cost_function(result.x)
