#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard


def test_matomo_requester_instance(matomo_requester):
    assert isinstance(matomo_requester, object) is True
