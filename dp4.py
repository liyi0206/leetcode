##I, memorization
#329. Longest Increasing Path in a Matrix (**)
#(1) DFS (similar to word search) - time exceeds
#(2) DFS+DP (memorization) - scan once.
#iterate elems, keep val 1 if no larger neighbor, otherwise dfs larger neighbors first (deep dive until get 1 and add back). if elem already populated, skip. [dp matrix is for the memorization]


#II, Coin Change
#322. Coin Change - look forward
#backward,timeout: f(n)=min(f(n-1)+1,f(n-2)+1,etc)


#UVA 675. Coin Change -
#backward1: g(n)=sum(f(n,m))=sum(sum(f(n-c(m),i)))
#backward2: f[i,v] = f[i-1,v]+f[i,v-c[i]] - could simplify to 1d
#forward is similar, skip a few points.

#279. Perfect Squares (*) - forward/backward


#VI. DP design
#303. Range Sum Query - Immutable
#304. Range Sum Query 2D - Immutable (*) - consider edge case when row1==0 or col1==0