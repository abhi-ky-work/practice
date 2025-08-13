function preOrderTraversal(root){
    if(root == null) console.log("Tree is Empty")
        else{
            console.log(root.val)
            preOrderTraversal(root.left)
            preOrderTraversal(root.right)
    }
}

