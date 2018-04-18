"""
Author: Tristen Harr
Date: 3/31/2017

The Tree object creates a tree with methods of manipulation. The object handles tree traversal by nesting hash-maps,
and linking values to their parent node. The linked values can also be objects.

FUTURE TODO:

    Create additional methods to manipulate the structure.

    Create methods to implement algorithms inherently

    EX:
        my_tree.shortest_path()

    ***Create Object that extends Tree titled Graph.
        Create methods to implement common graph algorithms.


"""


class Tree(object):
    # TODO: Add better error handling descriptions
    @staticmethod
    def __curerror():
        """
        Internal method raises an error when the requested subtree path does not exist

        :return:    AttributeError
        """
        raise AttributeError("The specified path does not exist")

    @staticmethod
    def __deptherror():
        """
        Internal method that raises an error when the requested subtree path exceeds subtree depth by more than 1
        or path already exists

        :return:    AttributeError
        """
        raise AttributeError("The requested path exceeds the current trees depth by more than 1"
                             "or the path already exists")

    def __init__(self, root="ROOT"):
        """
        The base Tree object

        :param root: Root Value *optional
        """
        self.root = root
        self.dirs = {"*": {"VALUE": root}} #[]

    def __curlook(self, path):
        """
        Internal Method that returns the specified branch by path

        EX:
        my_tree = tree()
        my_tree.make_children("*",[1,2,3])
        my_tree.__curlook("*")   -->  {'VALUE': 'ROOT', '*-1': {'VALUE': 1}, '*-2': {'VALUE': 2}, '*-3': {'VALUE': 3}}
        !IMPORTANT! .__curlook() is an internal method, and may not work if external call is attempted

        :param path:    Accepts path such as "*"
        :return:        Subtree in form of dictionary
        """
        my_pathlist = []
        items = list(path)
        for i in range(1, len(items)+1, 2):
            my_pathlist.append("".join(items[0:i]))
        curdir = self.dirs[my_pathlist[0]]
        for itemp in my_pathlist[1:]:
            curdir = curdir[itemp]
        return curdir

    def __path_check(self, path):
        """
        Wraps __curlook() for error handling

        :param path:    Accepts path such as "*"
        :return:        Subtree in form of dictionary or error
        """
        try:
            item1 = self.__curlook(path)
            return item1
        except KeyError:
            error_handle = False
            return error_handle

    def make_children(self, path, children=None):
        """
        Creates children nodes on parent path
        *ADDITIONAL INFORMATION* Children values can be objects

        :param path:        Path key  EX: "*"
        :param children:    Children Values   EX: ["Value1", "Value2"]
        :return:            None or Error
        """
        curdir = self.__path_check(path)
        if curdir:
            curdir.update({"{}-{}".format(path, i): {"VALUE": children[i-1]} for i in range(1, len(children)+1)})
        else:
            self.__deptherror()

    def value_lookup(self, path):
        """
        Returns the value associated with the specified path

        :param path:    Path Key EX: "*"
        :return:        Path Value
        """
        curdir = self.__path_check(path)
        if curdir:
            return curdir["VALUE"]
        else:
            self.__curerror()

    def value_update(self, path, value):
        """
        Updates the value currently associated with the path
        *ADDITIONAL INFORMATION* Values can be objects

        :param path:    Path Key EX: "*"
        :param value:   New Value  EX: "The Value"
        :return:        None or Error
        """
        curdir = self.__path_check(path)
        if curdir:
            curdir["VALUE"] = value
        else:
            self.__curerror()

    def add_children(self, path, children):
        """
        Adds additional nodes to the parent path
        *ADDITIONAL INFORMATION* Children values can be objects

        :param path:        Path Key  EX: "*"
        :param children:    Children Values   EX: ["Value1", "Value2"]
        :return:            None or Error
        """
        curdir = self.__path_check(path)
        if curdir:
            curdir.update({"{}-{}".format(path, i+len(list(curdir.keys()))):
                          {"VALUE": children[i]} for i in range(len(children))})
        else:
            self.__curerror()

    def subtree(self, path):
        """
        Returns the subtree of the specified path
        *IMPORTANT* Exactly the same as .__curlook() with error handling and ACCESSIBLE TO USER

        :param path:
        :return:
        """
        curdir = self.__path_check(path)
        if curdir:
            return curdir
        else:
            self.__curerror()

    def tree_section(self, tree=None):
        if tree:
            tree = self.dirs
        my_list = []

        def keygetter(subtree):
            my_dicts = {}
            for key in subtree.keys():
                if type(subtree[key]) == dict:
                    try:
                        my_dicts["KEY{}".format(key.count("-"))].append(key)
                    except KeyError:
                        my_dicts["KEY{}".format(key.count("-"))] = [key]
                    keygetter(subtree[key])
            itemx = [*my_dicts.values()]
            if itemx:
                my_list.append(*itemx)
                return sorted(my_list)
        final = keygetter(tree)
        return final

    def tree_layer(self, partition=False):
        """
        Returns a dictionary with the Integer keys from 0 to the depth of the tree, with values in the form of a list
        with the Tree's parent keys contained within the list.
        *IF PARTITION IS TRUE* The values list is partitioned by parent keys

        :param partition:   Boolean specifies whether lists should be partitioned
        :return:            A dictionary with parent keys
        """
        # TODO: add parameter to allow tree_layer to be chosen by path
        tree = None
        if tree is None:
            tree = self.tree_section(self.dirs)
        my_dict = {}
        items = list(map(lambda z: {z[0].count('-'): z}, tree))
        if partition:
            for diction in items:
                try:
                    my_dict["{}".format(*diction.keys())] += list(diction.values())
                except KeyError:
                    my_dict["{}".format(*diction.keys())] = list(diction.values())
            return my_dict
        else:
            for diction in items:
                try:
                    my_dict["{}".format(*diction.keys())] += list(*diction.values())
                except KeyError:
                    my_dict["{}".format(*diction.keys())] = list(*diction.values())
            return my_dict

    def rekey(self, tree):
        orig = self.__path_check(tree)
        print(list(map(lambda z: len(z[1]) > 1, list(self.__path_check(tree).items())[1:])))
        print(list(map(lambda z: z, list(self.__path_check(tree).items()))))
        vals = self.tree_section(orig)
        # print(vals)
        newvals = list(map(lambda z: z[0:z.rfind('-')]+"-{}", vals[0]))
        fnewvals = ["VALUE"]+list(map(lambda z: newvals[z].format(z+1), range(len(newvals))))
        dictup = dict(zip(fnewvals, [*orig.values()]))
        orig.clear()
        orig.update(dictup)
        vals.pop(0)
        for itemx in orig.items():
            if itemx[0] != "VALUE":
                if len(itemx[1]):
                    if len(itemx[1].keys()) > 1:
                        print(itemx)

    def swap_children(self, child1, child2):
        # TODO: Build function as specified in docstring
        """
        Switches the subtrees location in the main tree and re-keys the items.

        :param child1:        Parent key of subtree 1
        :param child2:        Parent key of subtree 2
        :return:              None or Error
        """
        pass
        # TODO: Extend the re-orienation on method to be made in destroy_subtree to allow for path re-ordering

    def destroy_subtree(self, path):
        """
        Destroys specified subtree

        :param path:    Parent path to destroy
        :return:        None or Error
        """
        curdir = self.__path_check(path[0:len(path)-2])
        curdir.pop(path)
        # TODO: create a way to reset the path keys shifting them all towards root when a path is removed

    def walk(self, orientation="Left", item="Values"):
        """
        This method walks the path in the specified orientation, and returns the specified item
        :param orientation:
        :param item:
        :return:
        """
        pass



item = Tree()
item.make_children("*", [["Items","Items2"], 1, "Stuff"])
print(item.dirs)
item.add_children("*-1", [1,2,3])
item.add_children("*-2", [4,5,6])
item.add_children("*-2-1", [1,2,3])
print(item.dirs)
print(item.tree_layer())
# item.add_children("*-3", ["Root-3-1", "Root-3-2", "Root-3-3"])
# print(item.subtree("*-1"))
# print(item.dirs)
# print(item.tree_layer(), "TREE LAYER")
# print(item.subtree("*-1"))
# print(item.tree_section())
# print(item.tree_layer(partition=True))
# print(item.dirs)
# x = item.subtree_lookup()
# print(x)
item.destroy_subtree("*-2")
# print(item.dirs)
# item.rekey("*-3")
# print(item.dirs)

# print(item.tree_section(test))
# print(item.value_lookup("*-7"))
# item.value_update("*-7", "UPDATED")
# print(item.value_lookup("*-7"))
# print(item.dirs)
# item.make_children("*-1",["Root1-1","Root1-2","Root1-3"])
# print(item.dirs)

# item.make_children("*-2",["Root2-1","Root2-2", "Root2-3","Hey","HELLO","PLEASE"])
# print(item.dirs)
# item.make_children("*-1-1", ["Root1-1-1", "Root1-1-2"])
# item.make_children("*-2-1", ["Root1-2-1", "Root1-2-2"])
# item.make_children("*-2-2", ["Test","Test2"])
# item.make_children("*-2-1-1", ["R","J","K"])
# item.destroy_subtree("*-2-1")
# item.destroy_subtree("*-2-3")
# item.rekey("*-2")
# print(item.dirs)

