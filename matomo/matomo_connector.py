#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard


class MatomoConnector(object):

    def __init__(self, endpoint: str, token: str, id_site: str = 'all'):
        self.endpoint = endpoint
        self.token = token
        self.id_site = id_site
