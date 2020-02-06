#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard


def test_matomo_connector_instance(matomo_connector):
    assert isinstance(matomo_connector, object) is True
    assert hasattr(matomo_connector, 'endpoint') is True
    assert hasattr(matomo_connector, 'token') is True
    assert hasattr(matomo_connector, 'id_site') is True

    assert matomo_connector.id_site == 'all'


def test_base_url(matomo_connector):
    assert hasattr(matomo_connector, 'base_url') is True
    assert matomo_connector.base_url == 'url/?token_auth=token&module=API&idSite=all'
