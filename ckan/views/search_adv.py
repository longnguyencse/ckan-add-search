# encoding: utf-8

from flask import Blueprint

import ckan.lib.base as base

CACHE_PARAMETERS = [u'__cache', u'__no_cache__']

search_adv = Blueprint(u'search_adv', __name__)


def index():
    return base.render(u'search/index.html', extra_vars={})

util_rules = [
    (u'/search-adv', index),
]
for rule, view_func in util_rules:
    search_adv.add_url_rule(rule, view_func=view_func)
