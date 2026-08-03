""" 2402. Meeting Rooms III
https://leetcode.com/problems/meeting-rooms-iii/description/

https://www.youtube.com/watch?v=2VLwjvODQbA&t=2s

You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). 
All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

 

 """

import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x : x[0])
        # meetings.sort()
        print(meetings)
        available = [ x for x in range(n)] 
        used = [] # (end_time, room)
        count = [0] * n
        for start, end in meetings:
            while used and start > used[0][0]:
                end_time, room = heapq.heappop(used) # popping the room which has no meeting at this time and available now
                heapq.heappush(available, room)
            # no room is available, i.e room with closed end_time of next meeting will be the first available one
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + ( end - start )
                heapq.heappush(available, room)

            # a room is available
            room = heapq.heappop(available)
            heapq.heappush(used, [end, room])
            count[room] += 1
        return count.index(max(count))