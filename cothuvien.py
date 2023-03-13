class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Student:
    def __init__(self, name, id, avg_grade):
        self.name = name
        self.id = id
        self.avg_grade = avg_grade

    def __lt__(self, other):
        return self.avg_grade < other.avg_grade

    def __gt__(self, other):
        return self.avg_grade > other.avg_grade

    def __eq__(self, other):
        return self.avg_grade == other.avg_grade

    def __str__(self):
        return f"{self.name} ({self.id}): {self.avg_grade}"
# tao cay su dung ctdl PST
class PrioritySearchTree:
    # khoi tao cay tim kiem uu tien
    def __init__(self, root=None):
        self.root = root
    # chen gia tri moi vao cay
    def insert(self, value):
        # kiem tra nut goc co ton tai khong
        if not self.root:
            self.root = Node(value)
            return
        # khoi tao nut voi nut cha ban dau la None
        node = self.root
        parent = None

        while node:
            parent = node
            if value < node.value:
                node = node.left
            else:
                node = node.right

        if value < parent.value:
            parent.left = Node(value)
        else:
            parent.right = Node(value)
# ham search_range de tim kiem nhung hoc sinh co diem trung binh trong khoang
    def search_range(self, start, end):
        result = []
        self._search_range_helper(self.root, start, end, result)
        return result
# am search_range_helper dung de ho tro tim kiem trong khoang
    def _search_range_helper(self, node, start, end, result):
        if not node:
            return

        if start <= node.value.avg_grade <= end:
            result.append(node.value)

        if start < node.value.avg_grade:
            self._search_range_helper(node.left, start, end, result)

        if end > node.value.avg_grade:
            self._search_range_helper(node.right, start, end, result)
# ham test 
students = [
    Student("Alice", 1, 7.5),
    Student("Bob", 2, 8.0),
    Student("Charlie", 3, 6.0),
    Student("David", 4, 7.8),
    Student("Eve", 5, 9.2),
    Student("Frank", 6, 7.1)
]

tree = PrioritySearchTree()
for student in students:
    tree.insert(student)

result = tree.search_range(7, 8)
for student in result:
    print(student)
