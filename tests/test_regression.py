import unittest

from approvaltests.approvals import verify
from approvaltests.combination_approvals import verify_all_combinations
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory

from kata.LineSegment import LineListType, Point, SegmentList, LineSegment


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
        self.assertEqual(song.song, "Clare")
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
        arg2_combinations = (SegmentList((
                LineSegment(
                    start_point=Point(9, 8888),
                    end_point=Point(11, 8888),
                    generation_point=Point(7777, 14)),
                LineSegment(
                    start_point=Point(7777, 10),
                    end_point=Point(7777, 12),
                    generation_point=Point(13, 8888)))),
            SegmentList((
                LineSegment(
                    start_point=Point(9, 8887),
                    end_point=Point(11, 8889),
                    generation_point=Point(7777, 14)),
                LineSegment(
                    start_point=Point(7776, 10),
                    end_point=Point(7778, 12),
                    generation_point=Point(13, 8888)))),
            SegmentList((
                LineSegment(
                    start_point=Point(1, 2),
                    end_point=Point(3, 4),
                    generation_point=Point(5, 6)),)),
            SegmentList((
                LineSegment(
                    start_point=Point(9, 8888),
                    end_point=Point(11, 99999),
                    generation_point=Point(7776, 14)),
                LineSegment(
                    start_point=Point(7777, 10),
                    end_point=Point(99999, 12),
                    generation_point=Point(13, 8887)))),
            SegmentList((
                LineSegment(
                    start_point=Point(9, 8888),
                    end_point=Point(11, 999),
                    generation_point=Point(7777, 14)),
                LineSegment(
                    start_point=Point(7777, 10),
                    end_point=Point(999, 12),
                    generation_point=Point(13, 8888)))),
            SegmentList((
                LineSegment(
                    start_point=Point(9, 8889),
                    end_point=Point(11, 99999),
                    generation_point=Point(7777, 14)),
                LineSegment(
                    start_point=Point(7778, 10),
                    end_point=Point(99999, 12),
                    generation_point=Point(13, 8888))))
        )
        arg3_combinations = (Point(7777, 8888),)
        arg_combinations = (arg1_combinations, arg2_combinations, arg3_combinations)

        verify_all_combinations(
            self.get_segment_index,
            arg_combinations,
            formatter=lambda args, output: f"{args[0].name}\n{str(args[1])}\n{str(args[2])}\n => {str(output)}\n")

    def get_segment_index(self, list_type, segment_list, point):
        from kata.Lesson32 import Lesson32
        index_calculator = Lesson32()
        return index_calculator.get_segment_index(list_type, segment_list.line_segments, point)