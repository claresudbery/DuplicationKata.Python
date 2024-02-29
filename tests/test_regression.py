import unittest

from approvaltests.approvals import verify
from approvaltests.combination_approvals import verify_all_combinations
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory

from kata.Lesson32 import LineListType
from kata.Song import Song


def get_segment_index(list_type, line_segments, point):
    from kata.Lesson32 import Lesson32
    lesson_32 = Lesson32()
    return lesson_32.get_segment_index(list_type, line_segments, point)


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

    def test_segment_index(self):
        arg1_combinations = (LineListType.SOURCE_HORIZONTAL, LineListType.DESTINATION_HORIZONTAL, LineListType.DESTINATION_VERTICAL)
        arg2_combinations = (4, 5)
        arg3_combinations = ("thing1", "thing2")
        arg_combinations = (arg1_combinations, arg2_combinations, arg3_combinations)
        verify_all_combinations(get_segment_index, arg_combinations)

    def test_combinations(self):
        arg1_combinations = (1, 2)
        arg2_combinations = (4, 5)
        arg3_combinations = ("thing1", "thing2")
        arg_combinations = (arg1_combinations, arg2_combinations, arg3_combinations)
        verify_all_combinations(self.do_a_thing, arg_combinations)

    def do_a_thing(self, int1, int2, string1):
        return str(int1) + ", " + str(int2) + ", " + str(string1)