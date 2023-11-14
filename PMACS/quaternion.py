__author__ = "Justin Panchula"
__copyright__ = "Copyright UC CubeCats"
__credits__ = "Justin Panchula"
__version__ = "1"
__status__ = "Production"
__doc__ = """Quaternion abstraction"""

# Imports
from typing import Tuple
import numpy as np
from scipy.spatial.transform import Rotation as R


class Quaternion():
    def Quat_to_Euler(theta: float, alpha: float, psi: float, magnitude: float) -> Tuple[float, float, float]:
        """Given quaternions, returns Euler angles

        Args:
            theta (float): angle about the x-axis, in radians.
            alpha (float): angle about the y-axis, in radians.
            psi (float): angle about the z-axis, in radians.
            magnitude (float): the magnitude.

        Returns:
            Tuple[float, float, float]: the Euler angles
        """
        return R.from_quat(np.array([theta, alpha, psi, magnitude])).as_euler('xyz', False)

    def Euler_to_Quat(theta: float, alpha: float, psi: float) -> Tuple[float, float, float, float]:
        """Given Euler angles, returns quaternion angles.

        Args:
            theta (float): the angle about the x-axis, in radians.
            alpha (float): the angle about the y-axis, in radians.
            psi (float): the angle about the z-axis, in radians.

        Returns:
            Tuple[float, float, float, float]: the quaternions.
        """
        return R.from_euler('xyz', np.array(theta, alpha, psi), False).as_quat(True)


# Test
if __name__ == "__main__":
    print(Quaternion.Euler_to_Quat(10, 10, 10))
    print(Quaternion.Quat_to_Euler(0, 0, 0, 0))