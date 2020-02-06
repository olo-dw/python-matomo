#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

from .matomo_module import MatomoModule


class MatomoConnector(object):

    def __init__(self, endpoint: str, token: str, id_site: str = 'all'):
        self.endpoint = endpoint
        self.token = token
        self.id_site = id_site

    @property
    def base_url(self):
        return "{endpoint}/?token_auth={token}&module=API&idSite={id_site}".format(endpoint=self.endpoint,
                                                                                   token=self.token,
                                                                                   id_site=self.id_site)

    def __getattr__(self, item: str) -> MatomoModule:
        return MatomoModule(item, self)

    def __str__(self):
        return self.base_url
