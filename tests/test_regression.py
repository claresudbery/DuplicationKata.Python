import unittest

from approvaltests.approvals import verify
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
from kata.Song import Song


class RegressionTest(unittest.TestCase):
    def setUp(self):
        self.reporter = GenericDiffReporterFactory().get("DiffMerge")

    def test_cat(self):
        from kata.Lesson1Straight import Lesson1Straight
        song = Lesson1Straight()
        song.sing_cat_song()
        verify(song.song, self.reporter)

    def test_beer(self):
        from kata.Lesson2Variable import Lesson2Variable
        song = Lesson2Variable()
        song.sing_beer_song()
        verify(song.song, self.reporter)

    def test_names(self):
        from kata.Lesson21 import Lesson21
        song = Lesson21()
        names = ["Llewellyn", "Samatha", "Tomas", "Emilia"]
        song.sing_song(1, names)
        song.sing_song(2, names)
        song.sing_song(3, names)
        verify(song.song, self.reporter)

    def test_primes(self):
        from kata.Lesson3HigherOrderFunctions import Lesson3HigherOrderFunctions
        song = Lesson3HigherOrderFunctions()
        song.sing_song()
        verify(song.song, self.reporter)

    def test_names3(self):
        from kata.Lesson31 import Lesson31
        song = Lesson31()
        names = ["Llewellyn", "Samatha", "Tomas", "Emilia"]
        song.sing_song(1, names)
        song.sing_song(2, names)
        song.sing_song(3, names)
        verify(song.song, self.reporter)
