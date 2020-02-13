#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

from matomo.matomo_requester import MatomoRequester


def test_matomo_requester_instance(matomo_requester):
    assert isinstance(matomo_requester, object) is True


def test_get_kwargs(matomo_requester):
    assert isinstance(matomo_requester._get_kwargs(), list) is True
    assert MatomoRequester(1, 'a', field='test', account='oloc')._get_kwargs() == ['field=test', 'account=oloc']
