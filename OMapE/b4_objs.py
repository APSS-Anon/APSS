# bloom4, each tree is a lsh

from treelib import Node, Tree
import math, os, sys
import pickle
from Crypto.Util.Padding import pad, unpad


class node_data(object):
    def __init__(self, value, children, left_max_child=None):
        self.value = value
        self.children = children
        self.max_children = None
        self.left_max_children = left_max_child

    def __reduce__(self):
        return self.__class__, (self.value, self.children, self.left_max_children)

    def __str__(self):
        return str(self.value)

    def add_child(self, child):
        # child is node identifier number
        self.children.append(child)

    def get_children(self):
        return self.children

    def add_children_data(self, lchild, rchild):
        if type(rchild) is tuple and len(rchild) > 0:
            self.max_children = rchild[0]

        if type(lchild) is tuple and len(lchild) > 0:
            if self.max_children is None:
                self.max_children = lchild[0]

            self.left_max_children = lchild[0]

        else:
            if rchild is not None and rchild.max_children is not None:
                self.max_children = rchild.max_children
            else:
                self.max_children = lchild.max_children
            self.left_max_children = lchild.max_children