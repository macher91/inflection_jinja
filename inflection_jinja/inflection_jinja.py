# -*- coding: utf-8 -*-

"""Main module."""


from jinja2.ext import Extension
from inflection import *


class InflectionExtension(Extension):

    def __init__(self, environment):
        super(InflectionExtension, self).__init__(environment)
        environment.filters['camelize'] = camelize
        environment.filters['dasherize'] = dasherize
        environment.filters['humanize'] = humanize
        environment.filters['ordinal'] = ordinal
        environment.filters['ordinalize'] = ordinalize
        environment.filters['parameterize'] = parameterize
        environment.filters['pluralize'] = pluralize
        environment.filters['singularize'] = singularize
        environment.filters['tableize'] = tableize
        environment.filters['titleize'] = titleize
        environment.filters['transliterate'] = transliterate
        environment.filters['underscore'] = underscore
