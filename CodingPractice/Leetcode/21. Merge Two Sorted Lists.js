/**
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
var mergeTwoLists = function(list1, list2) {
    let head

    if(list1 == null) return list2
    if(list2 == null) return list1
    else{
        if(list1.val < list2.val){
            head = list1
            list1 = list1.next
        }else{
            head = list2
            list2 = list2.next
        }
    }
    let tail = head
    while(list1 && list2){
        if(list1.val < list2.val){
            tail.next = list1
            list1 = list1.next
        }else{
            tail.next = list2
            list2 = list2.next
        }
        tail = tail.next
    }
    if(list1 ){
        tail.next = list1
        // list1.next = list2
    }
    if(list2){
        tail.next = list2
        // list2.next = list1
    }
    console.log(head)
    return head
};