#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard


class MatomoRequester(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def _get_kwargs(self) -> list:
        l = list()
        for arg in self.kwargs:
            l.append("{}={}".format(arg, self.kwargs[arg]))
        return l
