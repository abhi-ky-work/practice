/**
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/description/?envType=problem-list-v2&envId=psz78mq6&favoriteSlug=&difficulty=EASY
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    
    if( head == null){
        return false
    }
    let node = head
    if(node.next == null){
        return false
    }
    while(node != null && node.val != "X"){
        node.val = "X"
        node = node.next
    }
    if( node == null ) {
        return false
    }
    if(node.val == "X"){
        return true
    }


};