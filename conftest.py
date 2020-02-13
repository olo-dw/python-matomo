#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

import pytest

from matomo.matomo_connector import MatomoConnector
from matomo.matomo_method import MatomoMethod
from matomo.matomo_module import MatomoModule
from matomo.matomo_requester import MatomoRequester


@pytest.fixture
def fixture_url():
    return 'https://localhost'


@pytest.fixture
def matomo_connector(fixture_url):
    return MatomoConnector(fixture_url, 'token')


@pytest.fixture
def matomo_method(matomo_module):
    return MatomoMethod('method', matomo_module)


@pytest.fixture
def matomo_module(matomo_connector):
    return MatomoModule('module', matomo_connector)


@pytest.fixture
def matomo_requester():
    return MatomoRequester()
