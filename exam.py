class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None

class PrioritySearchTree:
    def __init__(self, points):
        self.root = self.build_tree(points)

    def build_tree(self, points):
        if not points:
            return None
        else:
            points.sort(key=lambda x: x[0])
            mid = len(points) // 2
            node = Node(points[mid])
            node.left = self.build_tree(points[:mid])
            node.right = self.build_tree(points[mid+1:])
            return node

    def add_node(self, point, node):
        if not node:
            return Node(point)
        elif point[0] < node.point[0]:
            node.left = self.add_node(point, node.left)
        else:
            node.right = self.add_node(point, node.right)
        return node

    def search_range(self, x1, x2, node, results):
        if not node:
            return
        if node.point[0] < x1:
            self.search_range(x1, x2, node.right, results)
        elif node.point[0] > x2:
            self.search_range(x1, x2, node.left, results)
        else:
            results.append(node.point)
            self.search_range(x1, x2, node.left, results)
            self.search_range(x1, x2, node.right, results)

# Example usage
points = [(1, 4), (3, 1), (6, 5), (8, 3), (9, 9), (12, 6)]
pst = PrioritySearchTree(points)
results = []
pst.search_range(3, 8, pst.root, results)
print(results)  # Output
