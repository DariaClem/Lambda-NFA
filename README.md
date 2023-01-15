### Formal Languages and Automata theory :computer_mouse:
# Lambda-NFA (λ-NFA)

**Assignment**: Write an algorithm that has as input a lambda-NFA and a list of strings. Display YES/NO for each word, if it is accepted or not. If the answear is YES, display a path that can be used to reach a destination node. 

The symbol for lambda is #, therefore it cannot be used as a transition symbol with another meaning.

## How to use
We read from file date.in:

n (number of states), m (number of transition)

m transition (start node, destination node, transition)

source node

number of final nodes, final nodes

number of strings

the strings.


> _Example_

_Input_
``` python
5 8
0 0 0
0 1 #
1 2 #
2 2 0
2 1 1
1 3 0
3 3 1
3 4 0
0
1 4
5
01110
11111
0000
01011
11
```

_Output_
``` python
YES
Route: 0 1 3 3 3 3 4
_________________________
NO
_________________________
YES
Route: 0 0 0 1 3 4
_________________________
NO
_________________________
NO
_________________________
```
