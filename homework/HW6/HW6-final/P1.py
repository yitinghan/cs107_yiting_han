class BSTNode:
    
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val}, {self.size})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node: 
            return BSTNode(key, val)
        if key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    @staticmethod
    def _size(node):
        return node.size if node else 0
    
    def _removemin(self, node):
        if node.left == None:
            return node.right
        node.left = self._removemin(node.left)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if  key < node.key:
            node.left = self._remove(node.left,  key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                # Find the node's successor, substitue the node with successor, remove the successor from the right child
                ori_left = node.left
                ori_right = node.right
                node = node.right
                while node.left is not None:
                    node = node.left     
                node.right = self._removemin(ori_right)  
                node.left = ori_left
        
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node;


from enum import Enum

class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        self.idx = 0
        if traversalType == DFSTraversalTypes.PREORDER:
            self.list = self.preorder(tree)
        elif traversalType == DFSTraversalTypes.INORDER:
            self.list = self.inorder(tree)
        else:
            self.list = self.postorder(tree)

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.list):
            val = self.list[self.idx]
            self.idx += 1
            return val
        else:
            raise StopIteration()

    def inorder(self, bst: BSTTable):
        return self._inorder(bst._root)

    def _inorder(self, node: BSTNode):
        list = []
        if node is None:
            return list
        list.extend(self._inorder(node.left))
        list.append(node)
        list.extend(self._inorder(node.right))
        return list

    def preorder(self, bst: BSTTable):
        return self._preorder(bst._root)
    
    def _preorder(self, node: BSTNode):
        list = []
        if node is None:
            return list       
        list.append(node)
        list.extend(self._preorder(node.left)) 
        list.extend(self._preorder(node.right))
        return list

    def postorder(self, bst: BSTTable):
        return self._postorder(bst._root)
    
    
    def _postorder(self, node: BSTNode):
        list = []
        if node is None:
            return list       
        list.extend(self._postorder(node.left)) 
        list.extend(self._postorder(node.right))
        list.append(node)
        return list





            
        


# tree = BSTTable()
# tree.put(0, 'd')
# tree.put(2, 'c')
# tree.put(5, 'a')
# tree.put(1, 'b')
# tree.put(4, 'e')
# print(tree._root)

# print(tree._removemin(tree._root))

# tree.remove(2)
# print(tree)


input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
bst = BSTTable()
for key, val in input_array:
    bst.put(key, val)
traversal = DFSTraversal(bst, DFSTraversalTypes.INORDER)
for node in traversal:
    print(str(node.key) + ', ' + node.val)


