from kata.LineSegment import LineListType


class Lesson32:
    @staticmethod
    def get_segment_index(list_type, line_segments, point):
        segment_index = -1

        if list_type == LineListType.SOURCE_HORIZONTAL or list_type == LineListType.DESTINATION_HORIZONTAL:

            point1 = lambda point_1 : point_1.X
            point2 = lambda point_2: point_2.Y

            segment_index = Lesson32.process_segments(line_segments, point, point1, point2, segment_index)

        else:

            point1 = lambda point_1: point_1.Y
            point2 = lambda point_2: point_2.X

            segment_index = Lesson32.process_segments(line_segments, point, point1, point2, segment_index)

        return segment_index

    @staticmethod
    def process_segments(line_segments, point, point1, point2, segment_index):
        for i in range(len(line_segments)):
            line_segment = line_segments[i]
            if (point1(line_segment.generation_point) == point1(point)
                    and point2(line_segment.start_point) <= point2(point) <= point2(line_segment.end_point)):
                segment_index = i
                break
        return segment_index
