// Here is a DSA problem that we will solve. It's about meeting rooms. There are N meeting rooms, and there is an error in the meetings, which will have the values as a list of integer values for the starting hour of the meeting and the closing time. For example, here in the meetings, the first element in the list has two elements: 0 and 10. That means the meeting starts at 0 and finishes at 10. The same is true for the second one: the meeting starts at 1 and ends at 5.

// The area of meetings will be like this. For example, when we try to assign a meeting room to the first meeting, it will go to the first meeting room from 0 to 10. For the next meeting, we need to assign a room. It will go to the second room because it is available, and there is already a meeting allocated to meeting room 1.

// When we need to assign the third meeting timings, this will go to the meeting room that is available at the earliest. For example, the next meeting that starts at 2 will be given to meeting room number 2 because it is finishing first. It is finishing at, say, 5:00, and the meeting in room number 1 is finishing at 10:00. This meeting has to start at 2:00, and there is available space in room number 2 at the earliest because it's available after 5:00. The next meeting will go to room number 2.

// The timings will be like this: because it needs 5 hours, 2:00 to 7:00, the next meeting would be allotted from 5:00 to 10:00. In the same way, we will allocate the rest of the meetings. As a result, we have to return which meeting room has the maximum number of meetings, and we just have to return the number of meetings, like the maximum number of meetings in whichever meeting rooms 


n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]] [10,11]

1- [0,10] [10,11]
2 - [1,5] [5,10 ] [10,11]

Max no of meetings assigned a room 



timeMap = []
earliestAvail = [1,0 ] //room, earliestHr

for(i = 0 ; i < n; i++){
	timeMap.push([i+1,0,0])
}

meetings.forEach(slot =>{

earliestAvail = [1, earliestAvail[1] + (slot[1] - slot[0] )]

timeMap[ earliestAvail[0] ] = [earliestAvail[0] , earliestAvail[1]  , timeMap[2] +1 ]
 
})






Class Tree {
Int val ; 
Tree left; 
Tree right; 
}

indexSet = ()

traverse(root, index = 0 ){
	
	if(root == null){
	return []
	}
	if( ! indexSet.has(index) ){

	console.log([index, root.val])
	indexSet.add(index)
    }
	traverse(root.left, index -1)
	traverse(root.right, index + 1)

}
