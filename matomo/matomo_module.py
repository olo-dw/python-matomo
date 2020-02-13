#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard

from .matomo_method import MatomoMethod


class MatomoModule(object):

    def __init__(self, name: str, connector):
        self.name = name
        self.connector = connector

    def __getattr__(self, item: str) -> MatomoMethod:
        return MatomoMethod(item, self)
