from LinkedList import *


def fibonacci_llist(n):
    """
    Iterative generation of a linked list containing the first n fibonacci numbers
    :param n: number of fibonacci numbers the linked list should contain
    :return: linked list with the fibonacci sequence from 0 to n-1
    """
    if n < 0:
        print("Input values needs to be positive.")
    fibo_llist = LinkedList()
    if n >= 0:
        fibo_minus_two = 0
        fibo_llist.add_end(0)
    if n >= 1:
        fibo_minus_one = 1
        fibo_llist.add_end(1)
    if n >= 2:
        for i in range(2, n):
            fibo = fibo_minus_two + fibo_minus_one
            fibo_llist.add_end(fibo)
            fibo_minus_two = fibo_minus_one
            fibo_minus_one = fibo

    return fibo_llist


def reverse_order_llist(llist):
    """
    Creates linked list in reverse order by iterating along the linked list while
    adding the data always at the root of a new linked list.
    :param llist: linked list for which the order is to be reversed
    :return: linked list with reversed order
    """
    reverse_llist = LinkedList()
    current_node = llist.get_root()
    for i in range(llist.length):
        reverse_llist.add_root(current_node.get_data())
        current_node = current_node.get_next()
    return reverse_llist


if __name__ == "__main__":
    fibo_llist = fibonacci_llist(100)
    fibo_llist.print()
    fibo_llist_reversed = reverse_order_llist(fibo_llist)
    fibo_llist_reversed.print()
