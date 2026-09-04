"""Tests for error analyzer."""

import unittest
from gitassist.errors.analyzer import analyze_error


class TestErrorAnalyzer(unittest.TestCase):
    def test_not_git_repo(self):
        explanation = analyze_error("fatal: not a git repository")
        self.assertIn("Git repository", explanation)

    def test_push_rejected(self):
        explanation = analyze_error("error: failed to push some refs")
        self.assertIn("remote contains commits", explanation)

    def test_unknown_error(self):
        explanation = analyze_error("some unknown error")
        self.assertEqual(explanation, "")


if __name__ == "__main__":
    unittest.main()