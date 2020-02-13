#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

from matomo.matomo_method import MatomoMethod


def test_matomo_module_instance(matomo_module):
    assert isinstance(matomo_module, object) is True
    assert hasattr(matomo_module, 'connector') is True
    assert hasattr(matomo_module, 'name') is True


def test_getattr(matomo_module):
    assert isinstance(matomo_module.method, MatomoMethod) is True
