"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        interval_map = dict()
        for i in range(len(intervals)):
            if intervals[i].start in interval_map and interval_map[intervals[i].start]:
                return False
            else:
                interval_map[intervals[i].start] = intervals[i].end

        start = [num for num in interval_map.keys()]
        start.sort()


        for i in range(0, len(start)-1):
            if start[i+1] < interval_map[start[i]]:
                return False
            i+=1

        return True

