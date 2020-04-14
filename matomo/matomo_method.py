#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard


from .matomo_requester import MatomoRequester


class MatomoMethod(object):

    def __init__(self, name, module):
        self.name = name
        self.module = module

    def __str__(self):
        return "{connector}&method={module}.{method}".format(connector=self.module.connector, module=self.module.name,
                                                             method=self.name)

    def __call__(self, *args, **kwargs):
        return MatomoRequester(*args, **kwargs).get_from(str(self))