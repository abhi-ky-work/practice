/**
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    if(head && head.next){
        let tail = head
        let current = head.next
        tail.next = null
        while(current.next){
            let temp = current.next
            current.next = tail
            tail = current
            current = temp
        }
        current.next = tail
        return current
    }return head
};
