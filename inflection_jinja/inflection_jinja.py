# -*- coding: utf-8 -*-

"""Main module."""

from inflection import *
from jinja2.ext import Extension


class InflectionExtension(Extension):
    def __init__(self, environment):
        super(InflectionExtension, self).__init__(environment)
        inflection_filters = dict(
            camelize=camelize,
            dasherize=dasherize,
            humanize=humanize,
            ordinal=ordinal,
            ordinalize=ordinalize,
            parameterize=parameterize,
            pluralize=pluralize,
            singularize=singularize,
            tableize=tableize,
            titleize=titleize,
            transliterate=transliterate,
            underscore=underscore,
            )
        environment.filters.update(inflection_filters)
