#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - code will run once no matter what the size of n is and will only repeat once the while loop starts - the code is linear

---
b) 0(nlog(n))

 sum = 0
    for i in range(n):                  ***o(n)
      j = 1
      while j < n:
        j *= 2                          *** O(log n) since j is doubling each iteration
        sum += 1
                                        O(n * (log n)) = O(n log n)
```

c) 0(n) - Recursion call and the algorithm will always execute "bunnies" number of times (linear time). 

## Exercise II

I would use a binary search where I start in the middle floor then drop an egg.  if egg_broken = true, proceed half of remaining downward and repeat. If egg_broken = false (after drop) process half way upward remaining and repeat. This is O(log n).

