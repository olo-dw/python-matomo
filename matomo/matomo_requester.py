#!/usr/bin/env python
# -*-coding:UTF-8 -*
#
# Olivier Locard


class MatomoRequester(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @property
    def params(self) -> str:
        k = '&'.join(self._get_kwargs())
        a = '&'.join(self.args)
        if k and a:
            return '{}&{}'.format(k, a)
        return k or a

    def _get_kwargs(self) -> list:
        l = list()
        for arg in self.kwargs:
            l.append("{}={}".format(arg, self.kwargs[arg]))
        return l
