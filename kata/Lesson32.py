from kata.Song import Song
from enum import Enum


class LineListType(Enum):
    SOURCE_HORIZONTAL = 1
    DESTINATION_HORIZONTAL = 2
    DESTINATION_VERTICAL = 3


class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return f"X: {self.X}, Y: {self.Y}"


class Lesson32:
    def get_segment_index(self, list_type, line_segments, point):
        segment_index = -1

        if list_type == LineListType.SOURCE_HORIZONTAL or list_type == LineListType.DESTINATION_HORIZONTAL:
            for i in range(len(line_segments)):
                line_segment = line_segments[i]
                if (line_segment.generation_point.X == point.X
                        and point.Y >= line_segment.start_point.Y
                        and point.Y <= line_segment.end_point.Y):
                    segment_index = i
                    break
        else:
            for i in range(len(line_segments)):
                line_segment = line_segments[i]
                if (line_segment.generation_point.Y == point.Y
                        and point.X >= line_segment.start_point.X
                        and point.X <= line_segment.end_point.X):
                    segment_index = i
                    break

        return segment_index
