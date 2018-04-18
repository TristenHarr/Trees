#
# dict1 = {"A":{"A1":{"A2":{"A3":5, "A3A":4}}}, "B":{"B1":[3,4]}}
# # the_key = {'*': {'VALUE': 'ROOT', '*-1': {'VALUE': 'Root1', '*-1-1': {'VALUE': 'Root1-1', '*-1-1-1': {'VALUE': 'Root1-1-1'}, '*-1-1-2': {'VALUE': 'Root1-1-2'}}, '*-1-2': {'VALUE': 'Root1-2'}, '*-1-3': {'VALUE': 'Root1-3'}}, '*-2': {'VALUE': 'Root2', '*-2-1': {'VALUE': 'Root2-1', '*-2-1-1': {'VALUE': 'Root1-2-1'}, '*-2-1-2': {'VALUE': 'Root1-2-2'}}, '*-2-2': {'VALUE': 'Root2-2'}, '*-2-3': {'VALUE': 'Root2-3'}}, '*-3': {'VALUE': 'Root3'}}}
# the_key = {'VALUE': 'Root3', '*-3-1': {'VALUE': 'Root-3-1'}, '*-3-2': {'VALUE': 'Root-3-2'}, '*-3-3': {'VALUE': 'Root-3-3'}}
# print(the_key)
# print(list(the_key.keys())[1][0:len(list(the_key.keys())[1])-2])
#
# """
#
# Function(x,y):      x is new root,   y is sub-tree     (In this case x is "*-2" and y is the_key)  --> Function("*-2", the_key)
#
#     the_root_key = list(y.values())
#     Get Values from The_Key in order
#
#     Make branch from values with root key of x
#
#
# """


"""
*-1
   \
    \_____> *-1-1
    |
    |_____> *-1-2
    |
    |_____> *-1-3

*-1 holds keys *-1-n

*-1-n values are made via *-1

All *-1-n values can be collected and there must be a path walking algorithm to allow for easy walking of a path to
work with tree migration


*-1 --> [*-1-1, *-1-2, ... *-1-n]

        *-1-n_i --> [*-1-n_i-1, *-1-n_i-2, ...]

Walk the left side, and then at the last branch split until their are no more keys.

                                                *
                                           ____/|\____
                                          /     |     \
                                        *-1    *-2    *-3
                                         |      |      |
                                        / \    / \    / \
                                       /   \
                                      *-1-1 *-1-2   ...

A 4 Layer-Deep Manual Approach   ***THIS ALGORITHM EXISTS, (possibly K-nearest neighbors or something, look it up!)

CURRENT: None                   *
                                |
CURRENT: *                      *-1
                                |
CURRENT: *-1                    *-1-1 <---------\
                                |               |
CURRENT: *-1-1                  *-1-1-1         |
                                |               |
CURRENT: RETURN *-1-1           |_ LAYER END ---/
                                |               |
CURRENT: *-1-1                  *-1-1-2         |
                                |               |
CURRENT: RETURN *-1-1           |_LAYER END ----/
                                |
                                |
                                .....

*
*-1
*-1-1
*-1-2
*-1-2-1
*-1-2-2
*-1-2-3
BREAK *-1-2
*-1-3

2 STACKS?

CURRENT and MAIN?

[*, *-1, *-1-1, ...] Stack on keys until the maximum depth-1 is reached.
the_list = []
the_list.append([*-n, [VALUE1, VALUE2, VALUE3]])
for i in range(len( (DICT:*-n).keys() ) ):

AS LONG AS I KEEP WALKING LEFT.
"""

# x = "*-1-2-1-2-3-1"
# my_list = list(map(lambda z: x[0:z], range(1, len(x),2)))
# print(my_list)
x = ["*", "*-1", "*-2"]
my_keys_that_change = {"0":"1-2-3", "1":"4-5-6"}
my_items = {my_keys_that_change["0"]:"A", my_keys_that_change["1"]:"B"}
print(my_items)
my_keys_that_change["0"] = "CHANGED"
print(my_items)
