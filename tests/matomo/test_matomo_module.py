#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard


def test_matomo_module_instance(matomo_module):
    assert isinstance(matomo_module, object) is True
    assert hasattr(matomo_module, 'connector') is True
    assert hasattr(matomo_module, 'name') is True
