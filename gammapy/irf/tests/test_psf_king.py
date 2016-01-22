# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals
from ...utils.testing import requires_dependency, requires_data
from ...datasets import gammapy_extra
from ...irf import PSFKing


@requires_dependency('scipy')
@requires_data('gammapy-extra')
def test_PSFKing():
    filename = gammapy_extra.filename('test_datasets/irf/hess/pa/hess_psf_king_023523.fits.gz')
    # psf = PSFKing.read(filename)
    psf = PSFKing()
    assert psf.name == 'Peter'


