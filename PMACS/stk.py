__author__ = "Justin Panchula"
__copyright__ = "Copyright UC CubeCats"
__credits__ = "Justin Panchula"
__version__ = "1"
__status__ = "Production"
__doc__ = """STK interaction file"""

# Imports
from agi.stk12.stkengine import STKEngine
from agi.stk12.stkobjects import AgESTKObjectType
from datetime import datetime
import numpy as np

# Typing
from agi.stk12.stkengine import AgStkObjectRoot

# Logging
import logging
log = logging.getLogger('PMACS')


class STK():
    """Wrapper to interface with Ansys Orbital STK
    """
    # Class values
    R_EARTH = 6378  # km

    def __init__(self):
        # Launch w/o GUI and create root object
        log.info("Launching STK Engine...")
        stk = STKEngine.StartApplication(noGraphics=True)
        self._root = stk.NewObjectRoot()

        # Set date format
        self._root.UnitPreferences.SetCurrentUnit('DateFormat', 'UTCG')

    def get_orbital_states(self,
                           start_datetime: datetime,
                           end_datetime: datetime,
                           Aa: float = 419,
                           Ap: float = 418,
                           e: float = 0.0001022,
                           i: float = 51.6433,
                           Ω: float = 115.2267,
                           ω: float = 223.6999):
        """Generates a file detailing orbital states over the time specified.

        Args:
            start_datetime (datetime): simulation start datetime (year, month, day, hour, minute, second).
            end_datetime (datetime): simulation end datetime (year, month, day, hour, minute, second).
            Aa (float): altitude of apoapsis.
            Ap (float): altitude of periapsis.
            e (float): eccentricity of the orbit.
            i (float): inclination of the orbit.
            Ω (float): longitude of the ascending node (degrees).
            ω (float): argument of periapsis (degrees).
        """
        # Calculate additional parameters
        za = Aa + STK.R_EARTH
        zp = Ap + STK.R_EARTH
        a = (za + zp)/2

        # Create scenario
        try:
            log.info("Creating scenario \"PMACS\"")
            self._root.NewScenario("PMACS")
            scenario = self._root.CurrentScenario
        except OSError as err:
            # Close old scenario
            log.debug(err)
            log.info("Closing earlier scenario...")
            self._root.CloseScenario()

            # Create scenario
            log.info("Creating scenario \"PMACS\"")
            self._root.NewScenario("PMACS")
            scenario = self._root.CurrentScenario

        # Create CubeSat
        cubesat = scenario.Children.New(AgESTKObjectType.eSatellite, "CubeSat-1")

    # Properties
    @property
    def root(self) -> AgStkObjectRoot:
        return self._root


# Testing
if __name__ == "__main__":
    pass