# unordered linked list

class Node:
    def __init__(self, init_node = None):
        self.init_node = init_node
        self.next_node = None

    def get_head_node(self):
        return self.init_node

    def get_next_node(self):
        return self.next_node

    def add_head_node(self, node):
        self.init_node = node
        return self.init_node

    def add_next_node(self, node):
        self.next_node = node
        return self.next_node


class UnorderedList:
    def __init__(self):
        self.head_node = None
        self.undo_list = []
        self.redo_list = []

    def add_node(self, elem):
        node = Node(elem)
        node.add_next_node(self.head_node)
        self.head_node = node
        self.undo_list.append(self.head_node)
        self.redo_list.clear()

    def print_list(self):
        iterate = self.head_node
        linked = ""
        while iterate != None:
            linked += str(iterate.init_node) + "==>"
            iterate = iterate.next_node

        return f"linked list [{linked}]"

    def length_list(self):
        count = 0
        counting = self.head_node

        while counting != None:
            count += 1
            counting = counting.get_next_node()
        return count

    def remove_node(self, item):
        current = self.head_node
        previous = None
        found = False
        while found:
            if current == item:
                found = True

            else:
                previous = current
                current = current.get_next_node()

        if previous == None:
            self.head_node = current.get_next_node()
            self.undo_list.append(self.head_node)
            self.redo_list.clear()
        else:
            previous.add_next_node(current.get_next_node())
            self.undo_list.append(previous)
            self.redo_list.clear()

    def insert_node_data(self, index, data):
        if index < 0 or index >= self.length_list():
            print("index out of list length")

        else:
            if index == 0:
                self.head_node.init_node = data

            else:
                itr = self.head_node
                count = 0
                while itr != None:
                    if count == index:
                        itr.init_node = data
                        return
                    else:
                        itr = itr.next_node
                        count += 1

    def undo_command(self):
        if len(self.undo_list) == 0:
            print("Undo stack is empty, it is not possible to undo again")

        else:
            undo_item = self.undo_list.pop(len(self.undo_list) - 1)
            self.redo_list.append(undo_item)

            undo_print = ""
            while undo_item != None:
                undo_print += str(undo_item.init_node) + "==>"
                undo_item = undo_item.next_node

            print(undo_print)

    def redo_command(self):
        if len(self.redo_list) == 0:
            print("Redo stack is empty, it is not possible to redo again")

        else:
            redo_item = self.redo_list.pop(len(self.redo_list) - 1)
            self.undo_list.append(redo_item)

            redo_print = ""
            while redo_item != None:
                redo_print += str(redo_item.init_node) + "==>"
                redo_item = redo_item.next_node

            print(redo_print)


    # def insert_node_end(self, data):
    #     if self.head_node == None:
    #         self.head_node = Node(data)
    #
    #     else:
    #         itr = self.head_node
    #         while itr.next_node != None:
    #             itr = itr.next_node
    #
    #         itr.next_node = Node(data)
    #
    # def insert_values(self, values):
    #     self.head_node = None
    #     for data in values:
    #         self.insert_node_end(data)

    # def undo(self):
    #     """
    #     this undo method will remove element at the begining of the list
    #     because they are the ones to be inserted lastly
    #     :return:
    #     """
    #     itr = self.head_node
    #     next = None
    #     while itr.next_node != None:

my_object = UnorderedList()
my_object.add_node(2)
my_object.add_node(3)
my_object.add_node(4)
my_object.add_node(5)
my_object.remove_node(3)
# print(my_object.print_list())
my_object.remove_node(4)
print(my_object.print_list())
my_object.undo_command()
my_object.undo_command()
my_object.redo_command()
my_object.redo_command()
my_object.redo_command()





