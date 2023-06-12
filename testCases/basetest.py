import pytest


# this base class should be inherited in every test scripts for launching browser
from utilities.customLogger import LogGen


@pytest.mark.usefixtures("chrome_init")
# @pytest.mark.usefixtures("driver_init")
class Baseclass:
    logger = LogGen.loggen()
    pass
