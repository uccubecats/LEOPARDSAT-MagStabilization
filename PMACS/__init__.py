# __all__
from PMACS import exceptions
from PMACS.IGRF import IGRF
__all__ = [exceptions, IGRF]

# Configure logging
import logging
import logging.config
import yaml
logging.config.dictConfig(yaml.safe_load(open('logging.yaml', 'r').read()))