from model.util import *

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        nodes = {}
        edges = {}

        if not node:
            return None
        q = []
        new_head = Node(node.val, [])
        for n in node.neighbors:
            q.append((n, new_head))
            node2 = Node(n.val, [])
            nodes[n] = node2
        nodes[node] = new_head
        while len(q) > 0:
            n, head = q[0]
            q.pop(0)
            if n not in nodes:
                new_node = Node(n.val, [])
                nodes[n] = new_node
            new_node = nodes[n]
            head.neighbors.append(new_node)
            #new_node.neighbors.append(head)
            for neighbor in n.neighbors:
                if neighbor not in nodes:
                    q.append((neighbor, new_node))
                    node2 = Node(neighbor.val, [])
                    nodes[neighbor] = node2
                else:
                    new_node.neighbors.append(nodes[neighbor])
        return new_head


