#!/usr/bin/python3
""" Unittests : console """
import unittest
from console import HBNBCommand
from io import StringIO
import json
import sys
from unittest.mock import patch
import pep8
import os


class TestConsole(unittest.TestCase):
    """ test the class console """

    def test_all(self):
        """ all method test """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all results")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_show(self):
        """ show method test """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show results")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_create(self):
        """ create method test """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create results")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_update(self):
        """ update method test """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update results")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_destroy(self):
        """ destroy method test """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy results")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_destroy(self):
        """ destroy method test """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy results")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")
