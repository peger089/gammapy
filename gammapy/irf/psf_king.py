# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
from astropy.table import Table
from astropy.units import Quantity
from astropy.coordinates import Angle
from ..utils.energy import Energy

__all__ = ['PSFKing']


class PSFKing(object):
    """
    King profile analytical PSF depending on energy and theta.
    """
    def __init__(self, name):
        self.name = name

