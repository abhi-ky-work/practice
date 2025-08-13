activity = [
( "a1", 0, 6),
( "a2", 3, 4),
( "a3", 1, 2),
( "a4", 5, 8),
( "a5", 5, 7),
( "a6", 8, 9),
]

'''
n activities, 
with start and finish times, 
select max no. of activi. a person can perform,
a person can perform 1 acti. at a time. 

ans : 4 (a3, a2, a5, a6)

approach >>>>>>>>

[
('a3', 1, 2), 
('a2', 3, 4), 
('a1', 0, 6), 
('a5', 5, 7), 
('a4', 5, 8), 
('a6', 8, 9)]
'''


activity.sort(key=lambda x : x[2])
# print(activity)

prev_act = activity[0]
res = [activity[0]]
count = 1
print(activity[0])
for i in range(1, len(activity)):
    if activity[i][1] >= prev_act[2]:
        prev_act = activity[i]
        print(activity[i])
        count += 1
        res.append(activity[i])


print("Count : ", count)
print("Activities : ", res)