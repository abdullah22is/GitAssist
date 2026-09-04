"""Tests for localization."""

import unittest
from gitassist.localization.texts import get_text
from gitassist.config import settings


class TestLocalization(unittest.TestCase):
    def setUp(self):
        self.original_lang = settings.LANGUAGE

    def tearDown(self):
        settings.LANGUAGE = self.original_lang

    def test_english_text(self):
        settings.LANGUAGE = "en"
        self.assertEqual(get_text("welcome"), "Welcome to GitAssist!")

    def test_arabic_text(self):
        settings.LANGUAGE = "ar"
        self.assertEqual(get_text("welcome"), "مرحبًا بك في GitAssist!")

    def test_missing_key_fallback(self):
        settings.LANGUAGE = "en"
        self.assertEqual(get_text("non_existent_key"), "non_existent_key")

    def test_formatting(self):
        settings.LANGUAGE = "en"
        self.assertEqual(get_text("current_branch", branch="main"), "Current branch: main")


if __name__ == "__main__":
    unittest.main()