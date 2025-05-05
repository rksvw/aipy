import test_test as tst

import unittest
import doctest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(tst))
    return tests
