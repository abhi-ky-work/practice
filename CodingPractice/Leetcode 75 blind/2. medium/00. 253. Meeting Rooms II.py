""" 
253. Meeting Rooms II 
https://leetcode.com/problems/meeting-rooms-ii?q=2402%3A+Meeting+Rooms+III

https://www.lintcode.com/problem/919/


Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

https://www.youtube.com/watch?v=FdzJmTCVyJU

 """

from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        start = []
        end = []
        s, e = 0, 0
        res, count = 0, 0
        for item in intervals:
            start.append(item.start)
            end.append(item.end)
        start = sorted(start)
        end = sorted(end)
        while(s < len(intervals)):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res

       """  
/**
 * Definition of Interval:
 * public class Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

public class Solution {
    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
    public int minMeetingRooms(List<Interval> intervals) {
        // Write your code here
        List<Integer> start = new ArrayList();
        List<Integer> end = new ArrayList();
        int count = 0;
        int res = 0;
        int s = 0;
        int e = 0;

   
        for(int i = 0; i < intervals.size() ; i++){
            start.add(intervals.get(i).start);
            end.add(intervals.get(i).end);
        };
        start.sort((a,b) -> Integer.compare(a, b));
        end.sort((a,b) -> Integer.compare(a, b));

        while(s < start.size()){
            if( start.get(s) < end.get(e)){
                s++;
                count++;
            }else{
                e++;
                count--;
            }
            res = Math.max(res, count);
        }
        return res;
    }
} """