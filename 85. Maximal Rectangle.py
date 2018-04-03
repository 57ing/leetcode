#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 85. Maximal Rectangle.py
@time: 2018/4/3 14:44

import java.util.Stack;

public class Solution {
    public static void main(String args[]) {
        char[][] matrix = {{'1','0','1','1','1'},{'1','0','1','1','1'},{'1','1','1','1','1'},{'1','0','0','1','0'}};
        System.out.println(maximalRectangle(matrix));
    }
    public static int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0) return 0;
        int[][] matrix_int = new int[matrix.length][matrix[0].length];
        for (int i = 0 ; i < matrix.length; i++){
            for (int j = 0; j < matrix[0].length; j++){
                matrix_int[i][j] = Integer.parseInt(""+matrix[i][j]);
            }
        }
        int count =0;
        for (int j = 0 ; j < matrix_int[0].length; j++){
            for (int i = 1; i < matrix_int.length; i++){
                if (matrix_int[i][j] > 0 && matrix_int[i-1][j] > 0){
                    matrix_int[i][j] += matrix_int[i-1][j];
                }
            }
        }
        for (int i =0 ; i < matrix_int.length; i++){
            int tmp = largestRectangleArea(matrix_int[i]);
            if (count < tmp) count = tmp;
        }
        return count;
    }
    static int largestRectangleArea(int[] heights) {
        int n = heights.length;
        int i = 0;
        int tp = 0;
        int tmp = 0, max = 0;
        Stack<Integer> stack = new Stack<>();
        while (i < n){
            if (stack.empty() || heights[stack.peek()] < heights[i]) {
                stack.push(i++);
            }else{
                tp = (Integer) stack.pop();
                tmp = heights[tp] * (stack.empty() ? i : i - stack.peek() - 1);
                if (tmp > max) max = tmp;

            }
        }
        while (!stack.empty()){
            tp = (Integer) stack.pop();
            tmp = heights[tp] * (stack.empty() ? i : i - stack.peek() - 1);
            if (tmp > max) max = tmp;
        }
        return max;
    }
}
'''
