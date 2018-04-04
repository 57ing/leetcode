#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 94. Binary Tree Inorder Traversal.py
@time: 2018/4/4 13:29

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        if (root == null) return null;
        stack.push(root);
        while (!stack.empty()){
            TreeNode tmp = stack.peek();
            if (tmp.left != null) {
                stack.push(tmp.left);
                tmp.left = null;
            } else {
                stack.pop();
                list.add(tmp.val);
                if (tmp.right != null) {
                    stack.push(tmp.right);
                    tmp.right = null;
                }
            }
        }
        return list;
    }
}
'''
