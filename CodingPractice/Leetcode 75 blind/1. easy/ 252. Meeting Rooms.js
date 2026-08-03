
// 252. Meeting Rooms

// https://www.lintcode.com/problem/920/

// https://www.youtube.com/watch?v=PaJxqZVPhbg

// Description
// Given an array of meeting time intervals consisting of start and end times [(s1,e1),(s2,e2),...] (si < ei), determine if a person could attend all meetings.



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

// public class Solution {
//     /**
//      * @param intervals: an array of meeting time intervals
//      * @return: if a person could attend all meetings
//      */
//     public boolean canAttendMeetings(List<Interval> intervals) {
//         // Write your code here
//             intervals.sort((a, b) -> Integer.compare(a.start, b.start));

//             for(int i = 1 ; i < intervals.size() ; i++){
//                 if( intervals.get(i - 1).end > intervals.get(i).start ){
//                     return false;
//                 };
//             };
//             return true;
//     }
// }


// from typing import (
//     List,
// )
// from lintcode import (
//     Interval,
// )

// """
// Definition of Interval:
// class Interval(object):
//     def __init__(self, start, end):
//         self.start = start
//         self.end = end
// """

// class Solution:
//     """
//     @param intervals: an array of meeting time intervals
//     @return: if a person could attend all meetings
//     """
//     def can_attend_meetings(self, intervals: List[Interval]) -> bool:
//         # Write your code here
//         intervals.sort(key = lambda x : x.start ) 
//         for i in range(1, len(intervals) ):
//             if intervals[i].start < intervals[i - 1].end :
//                 return False
//         return True