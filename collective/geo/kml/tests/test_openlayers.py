import unittest
import doctest

from Testing import ZopeTestCase as ztc

from collective.geo.kml.tests import base

def test_suite():
    return unittest.TestSuite([
        ztc.ZopeDocFileSuite(
            'browser/kml_openlayers.txt', package='collective.geo.kml',
            test_class=base.KmlFunctionalTestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
            ),
        ])
