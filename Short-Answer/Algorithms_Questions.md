# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

```python
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```python
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

First count the floors and find the middle, if it's an even number include both middles in the upper part and middle would be the first from the pair.

Second throw 2 eggs, for odd n one from mid and one from mid - 1 for even n one from top mid and one from lower mid.

Third analyse result from both eggs and start with step one from new boundries.

whenever you find a pair where one egg breaks and the inmidiate below doesn't then you know that the one that broke is f
