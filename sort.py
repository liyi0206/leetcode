#I, Bucket Sort (*)
#164. Maximum Gap - o(n) time/space.
#WA: sort and calc diff, that o(nlgn+n) time.
#AC: get size/max/min in o(n), and bucket_range=int((max-min)/(size-1)),
#then put elem to each bucket in o(n), and keep track of bucket[min,max] in o(2n) space,
#then calc gap of each bucket[max] and next non empty bucket[min] in o(n), and get max gap.


#II, array/linked-list sort
#147    Insertion Sort List ()
#148    Sort List ()

#III, string sort - read lecture


#IV, meeting rooms
#252. Meeting Rooms (locked)
#253. Meeting Rooms II (locked)
#296. Best Meeting Point (locked)