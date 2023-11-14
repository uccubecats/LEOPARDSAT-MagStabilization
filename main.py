__author__ = "Justin Panchula"
__copyright__ = "Copyright UC CubeCats"
__credits__ = "Justin Panchula, Bridget Sciartelli, Madison Coyne, Brynn Giffin"
__version__ = "1"
__status__ = "Production"
__doc__ = """Main file for the PMACS simulation"""

# Imports
from PMACS import STK
from datetime import datetime

# main
if __name__ == "__main__":
    stk = STK()
    stk.get_orbital_states(datetime(2023, 8, 1, 16, 00, 00), datetime(2023, 8, 2, 16, 00, 00))