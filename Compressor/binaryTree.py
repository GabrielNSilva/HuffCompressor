class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left = None
        self.right = None

    def insert_right(self, new_node):
        if isinstance(new_node, BinaryTree):
            self.right = new_node
        else:
            self.right = BinaryTree(new_node)

    def insert_left(self, new_node):
        if isinstance(new_node, BinaryTree):
            self.left = new_node
        else:
            self.left = BinaryTree(new_node)

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_val(self, obj):
        self.key = obj

    def get_val(self, ):
        return self.key

    def is_leaf(self):
        return ((not self.left) and (not self.right))

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.key)
        if self.right:
            self.right.in_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.key)

    def pre_order(self):
        print(self.key)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def leaves_in_order(self):
        if self.left:
            self.left.in_order()
        if ((not self.left) and (not self.right)):
            print(self.key, 'is a leaf =', self.is_leaf())
        if self.right:
            self.right.in_order()

    def leaves_post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        if ((not self.left) and (not self.right)):
            print(self.key)

    def leaves_pre_order(self):
        if ((not self.left) and (not self.right)):
            print(self.key)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
