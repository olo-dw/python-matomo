#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

import pytest

from matomo.matomo_connector import MatomoConnector
from matomo.matomo_module import MatomoModule


@pytest.fixture
def matomo_connector():
    return MatomoConnector('url', 'token')


@pytest.fixture
def matomo_module(matomo_connector):
    return MatomoModule('module', matomo_connector)
