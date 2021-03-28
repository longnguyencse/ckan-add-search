# encoding: utf-8

import ckan.lib.base as base

CACHE_PARAMETERS = ['__cache', '__no_cache__']


class SearchAdvController(base.BaseController):

    def index(self):
        return base.render('search/index.html', cache_force=True)
