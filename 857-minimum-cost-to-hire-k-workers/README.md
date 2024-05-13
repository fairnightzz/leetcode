Solution is simple, but to get to the solution is difficult.

The important part is to write out relationships with wage and quality, and you notice that in order 
to maintain the proportion of qualities `(quality[i]/quality[j])`, you need to also maintain `(wage[i]/wage[j])`. Grouping i and j together, you end up getting a ratio of wage/quality which can help in determining the most cost effective workers.

Then, we use a priority queue to keep track of the lowest quality workers. This is because a high quality worker will also 
increase the cost of the total. So whenever we hit k we remove the highest quality worker.

There is some more math to determine the cost which is by keeping track of total quality and then multiplying by the wage to quality ratio to determine a possible total cost.