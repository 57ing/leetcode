#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 96. Unique Binary Search Trees.py
@time: 2018/4/5 12:40
class Solution {
    public static void main(String args[]){
        System.out.println(numTrees(1));
    }
    public static int numTrees(int n) {
        int[] list;
        if (n > 2) {
            list = new int[n];
        }
        else {
            list = new int[3];
        }
        list[0] = 1;
        list[1] = 2;
        list[2] = 5;
        for (int i = 3; i < n; i++){
            list[i] += list[i-1] * 2;
            for (int j = 1; j < (i+1)/2 ; j++){
                list[i] += list[j-1] * list[i-1-j] *2;
            }
            if ((i) % 2 == 0){
                list[i] += list[i/2-1] * list[i/2-1];
            }
        }
        return list[n-1];
    }
}
'''
