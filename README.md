# BinaryTreeTraversal

## What is a binary tree?

In binary tree datastructures each node has at most two children, which are referred to as the left child and the right child.

___

         1
       /   \
      2     3          This is a binary tree.
     / \     \
    4   5     6          


___

## Depth first order.

There are 3 types of depth first order:
- Pre Order
- In Order
- Post Order

### Pre Order

In Pre Order we:
1. Check if the current node is Empty
2. Display the data part of the root
3. Traverse the left subtree by recursion
4. Traverse the right subtree by recursion.

___

         1
       /   \
      2     3          Pre Order ->  1 , 2 , 4 , 5 , 3 , 6
     / \     \
    4   5     6          


___


### In Order

In Pre Order we:
1. Check if the current node is Empty
2. Traverse the left subtree by recursion
3. Display the data part of the root
4. Traverse the right subtree by recursion.

___

         1
       /   \
      2     3          In Order -> 4 , 2 , 5 , 1 , 3 , 6
     / \     \
    4   5     6          


___


### Pre Order

In Pre Order we:
1. Check if the current node is Empty
2. Traverse the left subtree by recursion
3. Traverse the right subtree by recursion.
4. Display the data part of the root


___

         1
       /   \
      2     3          Pre Order -> 4 , 5 , 2 , 6 , 3 , 1
     / \     \
    4   5     6          


___
