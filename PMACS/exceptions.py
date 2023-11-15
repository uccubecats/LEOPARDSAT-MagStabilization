#!/usr/bin/env python
"""Custom exceptions for Passive Magnetic Attitude Control Simulation.
"""
__author__ = "Justin Panchula"
__copyright__ = "Copyright 2024 UC CubeCats"
__credits__ = ["Justin Panchula"]
__license__ = "MIT"
__version__ = "1.0.0"
__status__ = "Production"
__maintainer__ = None
__contact__ = None


class PMACSBaseException(Exception):
    def __init__(self, msg):
        """Base exception class for the PMACS module
        """
        super().__init__(msg)


class IGRFFileNotFoundError(PMACSBaseException):
    def __init__(self, msg="IGRF file not found!"):
        """Raised when the IGRF file is not found

        Args:
            msg (str, optional): the message to display. Defaults to "IGRF file not found!".
        """
        super().__init__(msg)