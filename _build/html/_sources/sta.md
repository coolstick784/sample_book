## This simulates a probability
For 8 cards with two sides that are either blue ("b") or red ("r"), we can determine the probability that the other side is red given that the first side is blue

Import the "random" module


```python
import random
```

Initialize the cards as shown


```python
c1 = ["b", "b"]
c2 = ["b", "b"]
c3 = ["b", "b"]
c4 = ["b", "b"]
c5 = ["b", "b"]
c6 = ["r","b"]
c7 = ["b","r"]
c8 = ["r","b"]
```

Set the choices to 0 or 1 (the front or back of the card)


```python
choices = [0,1]
```

For a million trials, if the front side of the card is blue, add 1 to the total. If the other side is red, add 1 to the red total


```python
cards = [c1, c2, c3, c4, c5, c6, c7, c8]
total = 0
blue = 0
for i in range(1000000):
    cursides = []
    
    for c in cards:
        cur_choice = random.choice(choices)
        
        if cur_choice == 0:
            other_choice = 1
        else:
            other_choice = 0
        
        if c[cur_choice] == "b":
            total += 1
            if c[other_choice] == "r":
                red += 1
                
        
        
```

probability = number of favorable outcomes / number of total outcomes


```python
red/total
```




    0.23076260349319933




```python

```
