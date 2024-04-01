from signLanguage.logger import logging
from signLanguage.exception import SignException
import sys

#logging.info("Welcome in the world of data logging")


# Exception Test

try:
    a = 7 / '9'

except Exception as e:
    raise SignException(e, sys) from e