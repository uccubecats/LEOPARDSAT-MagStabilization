#!/usr/bin/env python
"""Computes the International Geomagnetic Reference Field 13, valid between 01-01-2020 and 31-12-2025.
"""
__author__ = "Justin Panchula"
__copyright__ = "Copyright 2024 UC CubeCats"
__credits__ = ["Justin Panchula", "Karl M. Laundal"]
__license__ = "MIT"
__version__ = "0.1.0"
__status__ = "Production"
__maintainer__ = None
__contact__ = None

# Imports
from pathlib import Path
import numpy as np

# Errors
from ..exceptions import IGRFFileNotFoundError

# Logging
import logging
log = logging.getLogger('PMACS')


class IGRF():
    def __init__(self, IGRF_FILE):
        # Validate IGRF_FILE type
        if type(IGRF_FILE) is not Path or type(IGRF_FILE) is not str:
            raise TypeError("\"IGRF_FILE\" is not of \"Path\" type!")

        # Load IGRF data
        try:
            with open(IGRF_FILE, 'r') as f:
                # Create empty array
                self._igrf = np.array([])

                # Read lines
                for newline in f.readlines():
                    # Ignore comment lines
                    if newline[0] == '#':
                        continue

                    # Parse new line
                    line = np.fromstring(newline, sep=' ')
                    print(line)
                    self._igrf = np.append(self._igrf, line)
        except FileNotFoundError:
            IGRFFileNotFoundError()

    @property
    def igrf(self) -> np.ndarray[float]:
        return self._igrf


# Testing
if __name__ == "__main__":
    igrf = IGRF("IGRF13.txt")