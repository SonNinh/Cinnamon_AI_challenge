'''
Chalenge Owner: Cinamon AI LAb Vietnam
Developer: SonNinh@github.com
Time: 10pm
Date: Dec 21st, 2019 (UTC +7)
'''

class Node():
    def __init__(self):
        # parent's name
        self.parent = None

        #list of child's name
        self.child = []

    def add_child(self, node):
        self.child.append(node)


def find_path(net, start, end):
    '''
    find shortest path from start_word to end_word, using Dijkstra's algorithm
    '''

    cur_layer = [start]

    while cur_layer:
        new_layer = []
        # loop nodes which just are reached
        for node in cur_layer:
            for child in net[node].child:
                # if the node has been not reached so far.
                if net[child].parent is None:
                    net[child].parent = node
                    new_layer.append(child)
                # if end_word is found
                if child == end:
                    return True
                    
        cur_layer = new_layer
        new_layer = []

    # if can not fine end_word
    return False


def check(pet1, pet2):
    '''
    check if 2 words are diiferrent at only one character
    '''
    diff = 0
    for c1, c2 in zip(pet1, pet2):
        if c1 != c2:
            diff += 1
            if diff == 2:
                return False
    
    return True


def build_net(pets):
    '''
    build a net whose keys are name of given words and vallues are connected words
    '''
    net = {}
    for pet in pets:
         net[pet] = Node()

    for i, pet1 in enumerate(pets, start=1):
        for pet2 in pets[i:]:
            if check(pet1, pet2):
                net[pet1].add_child(pet2)
                net[pet2].add_child(pet1)

    return net


def main():
    pets = ['cat', 'dog', 'nop', 'fat', 'dop', 'dot', 'dat', 'son']

    # build the connection between each word
    net = build_net(pets)
    
    start = pets[0]
    end = pets[2]

    # update net. If output is False, stop and return None
    if not find_path(net, start, end):
        return None
    # else
    res = [end]
    while end != start:
        # loop backward the net, using parent's name of each node to fine the path
        end = net[end].parent
        res.append(end)
    
    return res[::-1]


if __name__ == "__main__":
    print(main())
