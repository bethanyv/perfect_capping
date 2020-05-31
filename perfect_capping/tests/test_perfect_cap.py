"""
Nose tests for perfect_cap_calc.py

"""
import perfect_cap_calc

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_normal_200():
	'''
	Tests are hard for this lol
	'''
	assert perfect_cap_calc.calculate_honor(100)
