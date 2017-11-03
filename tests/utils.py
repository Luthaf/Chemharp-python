# -*- coding=utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import unittest

import chemfiles
from chemfiles import Trajectory, ChemfilesError


class TestErrors(unittest.TestCase):
    def test_last_error(self):
        self.assertEqual(chemfiles.utils._last_error(), "")

        try:
            Trajectory("noextention")
        except ChemfilesError:
            pass
        self.assertEqual(
            chemfiles.utils._last_error(),
            "file at 'noextention' does not have an extension, provide a "
            "format name to read it"
        )

        chemfiles.utils._clear_errors()
        self.assertEqual(chemfiles.utils._last_error(), "")


LAST_MESSAGE = ""


class TestWarnings(unittest.TestCase):
    def test_warning(self):
        def callback(message):
            global LAST_MESSAGE
            LAST_MESSAGE = message

        chemfiles.set_warnings_callback(callback)

        try:
            Trajectory("noextention")
        except ChemfilesError:
            pass

        self.assertEqual(
            LAST_MESSAGE,
            "file at 'noextention' does not have an extension, provide a "
            "format name to read it"
        )

    def test_warning_with_exception(self):
        def callback(message):
            global LAST_MESSAGE
            LAST_MESSAGE = message
            raise Exception(message)

        chemfiles.set_warnings_callback(callback)

        try:
            Trajectory("noextention")
        except ChemfilesError:
            pass

        self.assertEqual(
            LAST_MESSAGE,
            "file at 'noextention' does not have an extension, provide a "
            "format name to read it"
        )


if __name__ == '__main__':
    unittest.main()