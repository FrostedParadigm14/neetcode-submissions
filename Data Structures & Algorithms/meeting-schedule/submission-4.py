"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        start, end = [],[]

        for i in intervals:
            start.append(i.start)
            end.append(i.end)

        start.sort()
        end.sort()

        p1, p2, groups =1,0,0
        while p1 < len(intervals):
            if start[p1] < end[p2]:
                return False
            p1+=1
            p2+=1
        
        return True

        #                 ----
        #             ----
        #         ----
        #      ---
        # -------------
        # 0   10  20  30  40  50  



