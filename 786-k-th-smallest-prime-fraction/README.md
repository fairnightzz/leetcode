This one I did O(n^2), but the better solution is to use binary search.

I was stumped because I was unsure on what to binary search on, but if you decide to set a fraction with bounds 
0 to 1, and then calculate everything less than 0.5, it can be done in linear time. It works by incrementing denominator slowly, since the number will get smaller and then every denominator to the right is smaller. Then, increase the numerator where you may need to increase the denominator again. This part was tricky to realize.