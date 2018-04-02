'''
@author: 57ing
@contact: black8clock@gmail.com
@file: 79. Word Search.py
@time: 2018/4/2 14:12
'''
"""
class Solution {
    public boolean exist(char[][] board, String word) {
        int row = board.length;
        int col = board[0].length;
        boolean[][] mark = new boolean[row][col];
        for (int i = 0; i < row; i++){
            for (int j = 0; j <col; j++){
                if ((board[i][j] == word.charAt(0)) && judge(i, j, board, mark, word,0)) return true;
            }
        }
        return false;
    }
    public boolean judge(int i, int j, char[][] board, boolean[][] mark, String word, int po){
        if (!( i >= 0 && j >= 0 && i < board.length && j <board[0].length && (!mark[i][j]) && board[i][j] == word.charAt(po) )){
            return false;
        }
        mark[i][j] = true;
        if (po == word.length() - 1) return true;
        boolean tmp =false;
        if (po < word.length()){
            tmp = judge(i + 1, j, board, mark, word ,po+1) ||
                    judge(i - 1, j, board, mark, word ,po+1) ||
                    judge(i, j + 1, board, mark, word ,po+1) ||
                    judge(i, j - 1, board, mark, word ,po+1);
        }
        mark[i][j] = false;
        return tmp;
    }
}

"""
