class TreeBuilder:
    def __init__(self):
        self._structure = {0: []}
        self._level = 0

    def structure(self):
        return self._structure[0]

    def add(self, item):
        self._structure[self._level].append(item)

    def __enter__(self):
        self._level += 1
        self._structure.update({self._level: []})
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        level = self._level
        self._level -= 1

        if self._structure[level]:
            self._structure[self._level].append(self._structure[level])
            del self._structure[level]
        return True


# tree = TreeBuilder()
# print(tree.structure())
#
# tree.add('1st')
# print(tree.structure())

# with tree:
#     tree.add('2nd')
#     with tree:
#         tree.add('3rd')
#     tree.add('4th')
#     with tree:
#         pass
#
# print(tree.structure())

# tree = TreeBuilder()
#
# with tree:
#     tree.add(1)
#     tree.add(2)
#     with tree:
#         tree.add(3)
#         with tree:
#             tree.add(4)
#     with tree:
#         tree.add(5)
#
# print(tree.structure())


# TEST_6:
# tree = TreeBuilder()
#
# tree.add('root')
# with tree:
#     tree.add('first child')
#     tree.add('second child')
#     with tree:
#         tree.add('grandchild')
#     tree.add('bastard')
#     with tree:
#         pass
#     tree.add('another bastard')
#
# print(tree.structure())

# ['root', ['first child', 'second child', ['grandchild'], 'bastard', 'another bastard']]

tree = TreeBuilder()

tree.add('1st')

with tree:
    with tree:
        with tree:
            with tree:
                tree.add('5th')

print(tree.structure())

# ['1st', [[[['5th']]]]]

