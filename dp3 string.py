# -*- coding: utf-8 -*-
#32. Longest Valid Parentheses (*) - reverse 1D

#87. Scramble String (*) - not the same as sorted(s1)==sorted(s2)

#97. Interleaving String (*) - similar to edit distance
#dp[i+1][j+1]:表示s1[0...i]与s2[0...j]能否交替形成s3[0...i+j+1]部分.
#dp[i+1][j+1] = (dp[i][j+1] && s1[i] == s3[i+j+1]) | (dp[i+1][j] && s2[j] == s3[i+j+1]);

#115. Distinct Subsequences (*)

#132 Palindrome Partitioning II (*)





