class Node(object):

    def __init__(self, data, next_node=None):
        """
        Initialize node.
        :param data: data that is stored in the node
        :param next_node: pointer to the next node
        """
        self.data = data
        self.next_node = next_node

    def get_data(self):
        """
        Getter for the data of a node.
        :return: data that is stored in the node
        """
        return self.data

    def set_data(self, data):
        """
        Setter for the data of a node.
        :param data: data that should be stored in the node
        """
        self.data = data

    def get_next(self):
        """
        Getter for the next node.
        :return: node that comes next
        """
        return self.next_node

    def set_next(self, next_node):
        """
        Setter for the next node.
        :param next_node: node that comes next
        """
        self.next_node = next_node


class LinkedList(object):

    def __init__(self, root=None, last_node=None):
        """
        Initialize linked list.
        :param root: root (first) node of the linked list
        :param last_node: last node of the linked list
        """
        self.root = root
        self.last_node = last_node
        self.length = 0

    def get_root(self):
        """
        Getter for the root node.
        :return: root node
        """
        return self.root

    def add_root(self, data):
        """
        Creates a new node and adds it to the linked list at the root.
        :param data: data that is stored in the new node
        """
        new_node = Node(data, self.root)
        self.root = new_node
        if not self.last_node:
            self.last_node = new_node
        self.length += 1

    def add_end(self, data):
        """
        Creates a new node and adds it to the linked list at the end.
        :param data: data that is stored in the new node
        """
        new_node = Node(data)
        if self.last_node:
            self.last_node.set_next(new_node)
        else:
            self.root = new_node
        self.last_node = new_node
        self.length += 1

    def print(self):
        """
        Print the data stored in a linked list separated by blacks.
        """
        output = str()
        current_node = self.root
        for i in range(self.length):
            output += str(current_node.get_data()) + ' '
            current_node = current_node.get_next()
        print(output)
