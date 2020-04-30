import argparse
from unittest import TestCase, mock
from npmworkon import NpmWorkon

@mock.patch('argparse.ArgumentParser.parse_args',
            return_value = argparse.Namespace(
                environment = None,
                version = None,
                rm = None)
            )
def test_no_options(mock_args):
    npmworkon = NpmWorkon()
    res = npmworkon.run()
    assert res == None # TODO:
