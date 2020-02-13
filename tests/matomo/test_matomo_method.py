#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard


def test_matomo_method_instance(matomo_method):
    assert isinstance(matomo_method, object) is True
    assert hasattr(matomo_method, 'name') is True
    assert hasattr(matomo_method, 'module') is True


def test_str(matomo_method):
    assert str(matomo_method) == 'url/?token_auth=token&module=API&idSite=all&method=module.method'
