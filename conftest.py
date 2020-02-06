#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

import pytest

from matomo.matomo_connector import MatomoConnector


@pytest.fixture
def matomo_connector():
    return MatomoConnector('url', 'token')
