class BSTNode:
    
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = None
        self.right = None
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
        if node is None:
            new_node = BSTNode(key, val)
            return new_node

        if key < node.key:
            node.left = self._put(node.left, key, val)
            node.size = self._size(node.left) + self._size(node.right) + 1       
        elif key > node.key: 
            node.right = self._put(node.right, key, val)
            node.size = self._size(node.right) + self._size(node.left) + 1   
        else:
            node.val = val
        
        return node         

    def _get(self, node, key):
        if node is None:
            raise KeyError("Node not found")      
        if node.key == key:
            return node.val
        elif (node.key < key):
            return self._get(node.right, key)
        else:
            return self._get(node.left, key)

    @staticmethod
    def _size(node):
        return node.size if node else 0



greektoroman = BSTTable()
greektoroman.put('Athena',    'Minerva')
greektoroman.put('Eros',      'Cupid')
greektoroman.put('Aphrodite', 'Venus')
greektoroman.put('TestGreek', 'TestRoman')
greektoroman.put('B', 'D')
greektoroman.put('Eros', 'Something')
print(greektoroman.get('Eros'))
print(greektoroman.get('Athena'))
print(greektoroman)