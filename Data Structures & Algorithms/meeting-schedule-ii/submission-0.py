"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([s.start for s in intervals])
        end = sorted([e.end for e in intervals])

        res, count = 0,0
        first, last = 0,0
        while first < len(intervals):
            if start[ first ] <  end[last]:
                first+=1 
                count += 1

            else:
                last+=1
                count -=1
            res = max(res, count)

        return res


        