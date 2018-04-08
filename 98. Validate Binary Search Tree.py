#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 98. Validate Binary Search Tree.py
@time: 2018/4/8 20:56
import java.util.Stack;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
 }
class Solution {
    public static void main(String args[]){
        TreeNode node1 = new TreeNode(5);
        TreeNode node2 = new TreeNode(14);
        TreeNode node3 = new TreeNode(1);
        node1.left = node2;
        node2.left = node3;
        System.out.println(isValidBST(node1));
    }
        public static boolean isValidBST(TreeNode root) {
            Stack<TreeNode> stack = new Stack<>();
            TreeNode current = root;
            TreeNode pre = null;
            while ((current != null || !stack.empty())){
                while (current != null){
                    stack.push(current);
                    current =current.left;
                }
                current = stack.pop();
                if(pre != null && current.val <= pre.val) return false;
                pre = current;
                current = current.right;
            }
            return true;
        }
}
'''
