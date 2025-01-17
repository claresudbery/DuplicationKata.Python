from kata.LineSegment import LineListType


class Lesson32:
    @staticmethod
    def get_segment_index(list_type, line_segments, point):
        segment_index = -1

        if list_type == LineListType.SOURCE_HORIZONTAL or list_type == LineListType.DESTINATION_HORIZONTAL:
            for i in range(len(line_segments)):
                line_segment = line_segments[i]
                if (line_segment.generation_point.X == point.X
                        and line_segment.start_point.Y <= point.Y <= line_segment.end_point.Y):
                    segment_index = i
                    break
        else:
            for i in range(len(line_segments)):
                line_segment = line_segments[i]
                if (line_segment.generation_point.Y == point.Y
                        and line_segment.start_point.X <= point.X <= line_segment.end_point.X):
                    segment_index = i
                    break

        return segment_index
