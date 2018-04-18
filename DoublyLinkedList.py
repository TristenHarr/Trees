# class DoubleNode(object):
#
#     def __init__(self, value, parent):
#         self.contents = {"UP":None, "DOWN":None, "LEFT":None, "RIGHT":None, "VALUE":value, }
#
# class SuperLinkedList(object):
#
#     def __init__(self):
#         self.node = "node"

my_list_layer_1 = []

my_list = [[
            [
                [1],[2],[   [3],
                            [4],
                            [   [[2],
                                 [3],
                                 [4]],
                            [5]        ]
                                        ]
            ],

            [6],
            [7] ]]
print(my_list[0])

my_stuff = "*-1"
def lookup(item, the_list):
    item = item.replace("*", "1")
    stuff = list(map(lambda z: int(z)-1, item.split('-')))
    testing = list(map(lambda x: the_list[stuff[x]], range(len(stuff))))
    print(testing)
    return testing.pop()
x = lookup(my_stuff, my_list)
print(x)

"""Given a list such that:
1
    2
        0   4
            0   0   2   3
            0   3   4   5   6
                3  +4  +5   +6

Sum of the row is how many children will be in the next row.
                """