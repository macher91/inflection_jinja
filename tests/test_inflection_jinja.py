#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `inflection_jinja` package."""


import unittest

from jinja2 import Environment
from inflection import *

from inflection_jinja import inflection_jinja


class TestInflectionJinjaTestCase(unittest.TestCase):
    """Tests for `inflection_jinja` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

        self.env = Environment(extensions=[inflection_jinja.InflectionExtension])

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_camelize(self):
        """Test camelize"""

        test_text = 'device_type'
        camelize_value = self.env.from_string('{{ "' + test_text + '" | camelize}}')
        self.assertEqual(camelize(test_text), camelize_value.render())

    def test_dasherize(self):
        """Test dasherize"""

        test_text = 'puni_puni'
        dasherize_value = self.env.from_string('{{ "' + test_text + '" | dasherize}}')
        self.assertEqual(dasherize(test_text), dasherize_value.render())

    def test_humanize(self):
        """Test humanize"""

        test_text = 'employee_salary'
        humanize_value = self.env.from_string('{{ "' + test_text + '" | humanize}}')
        self.assertEqual(humanize(test_text), humanize_value.render())

    def test_ordinal(self):
        """Test ordinal"""

        test_text = '1002'
        ordinal_value = self.env.from_string('{{ "' + test_text + '" | ordinal}}')
        self.assertEqual(ordinal(test_text), ordinal_value.render())

    def test_ordinalize(self):
        """Test ordinalize"""

        test_text = '1003'
        ordinalize_value = self.env.from_string('{{ "' + test_text + '" | ordinalize}}')
        self.assertEqual(ordinalize(test_text), ordinalize_value.render())

    def test_parameterize(self):
        """Test parameterize"""

        test_text = 'Donald E. Knuth'
        parameterize_value = self.env.from_string('{{ "' + test_text + '" | parameterize}}')
        self.assertEqual(parameterize(test_text), parameterize_value.render())

    def test_pluralize(self):
        """Test pluralize"""

        test_text = 'cat'
        pluralize_value = self.env.from_string('{{ "' + test_text + '" | pluralize}}')
        self.assertEqual(pluralize(test_text), pluralize_value.render())

    def test_singularize(self):
        """Test singularize"""

        test_text = 'dogs'
        singularize_value = self.env.from_string('{{ "' + test_text + '" | singularize}}')
        self.assertEqual(singularize(test_text), singularize_value.render())

    def test_tableize(self):
        """Test tableize"""

        test_text = 'DogsAndCats'
        tableize_value = self.env.from_string('{{ "' + test_text + '" | tableize}}')
        self.assertEqual(tableize(test_text), tableize_value.render())

    def test_titleize(self):
        """Test titleize"""

        test_text = 'dogs dont\'t like cats'
        titleize_value = self.env.from_string('{{ "' + test_text + '" | titleize}}')
        self.assertEqual(titleize(test_text), titleize_value.render())

    def test_transliterate(self):
        """Test transliterate"""

        test_text = 'Ążćźó'
        transliterate_value = self.env.from_string('{{ "' + test_text + '" | transliterate}}')
        self.assertEqual(transliterate(test_text), transliterate_value.render())

    def test_underscore(self):
        """Test underscore"""

        test_text = 'DogsAndCats'
        underscore_value = self.env.from_string('{{ "' + test_text + '" | underscore}}')
        self.assertEqual(underscore(test_text), underscore_value.render())
