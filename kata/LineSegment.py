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


class SegmentList:
    def __init__(self, line_segments):
        self.line_segments = line_segments

    def __str__(self):
        segments_as_strings = map(lambda x: x.indexed_string(self.line_segments.index(x)), self.line_segments)
        return "\n".join(segments_as_strings)


class LineSegment:
    def __init__(self, start_point, end_point, generation_point):
        self.generation_point = generation_point
        self.end_point = end_point
        self.start_point = start_point

    def __str__(self):
        return (f"Start: ({self.start_point.X},{self.start_point.Y}), "
                f"End: ({self.end_point.X},{self.end_point.Y}), "
                f"Generation: ({self.generation_point.X},{self.generation_point.Y})")

    def indexed_string(self, index):
        return f"{index}: {str(self)}"
