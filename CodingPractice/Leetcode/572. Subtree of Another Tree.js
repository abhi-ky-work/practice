/**
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function(root, subRoot) {
    if( subRoot == null) return true
    if( root == null) return false
    let same = isSame(root, subRoot)
    if( same ) return true;
    return (isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot) )
};

function isSame(root, subroot){
    if( root == null && subroot == null ) return true
    if( root && subroot && root.val == subroot.val) return (isSame(root.left, subroot.left) && isSame(root.right, subroot.right))
    return false
}