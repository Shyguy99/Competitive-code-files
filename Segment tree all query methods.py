n=int(input())
m=int(input())
c=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.min = float("inf")
        self.max = float("-inf")
        self.leftEdge = None
        self.rightEdge = None


class SegmentTree:
    def __init__(self):

        self.partial_overlap = "Partial overlap"
        self.no_overlap = "No overlap"
        self.complete_overlap = "Complete overlap"

    def get_overlap(self, x1, y1, x2, y2):

        if (x1 == x2 and y1 == y2) or (x1 >= x2 and y1 <= y2):
            overlap = self.complete_overlap
        elif (y1 < x2) or (x1 > y2):
            overlap = self.no_overlap
        else:
            overlap = self.partial_overlap
        return overlap

    def construct_segment_tree(self, array, start, end):

        if end - start <= 0 or len(array) == 0:
            return None
        if end - start == 1:
            node = Node()
            node.min = array[start]
            node.max = array[start]
            node.sum = array[start]
            node.leftEdge = start
            node.rightEdge = end - 1
            return node
        else:
            node = Node()
            mid = start + (end - start) // 2
            node.left = self.construct_segment_tree(array, start=start, end=mid)
            node.right = self.construct_segment_tree(array, start=mid, end=end)
            if node.left is None and node.right is None:
                node.sum = 0
                node.leftEdge = start
                node.rightEdge = start
                node.min = float("inf")
                node.max = float("-inf")
            elif node.left is None:
                node.leftEdge = node.right.leftEdge
                node.rightEdge = node.right.rightEdge
                node.min = node.right.min
                node.max = node.right.max
            elif node.right is None:
                node.leftEdge = node.left.leftEdge
                node.rightEdge = node.left.rightEdge
                node.min = node.left.min
                node.max = node.left.max
            else:
                node.min = min(node.left.min, node.right.min)
                node.max = max(node.left.max, node.right.max)
                node.leftEdge = node.left.leftEdge
                node.rightEdge = node.right.rightEdge
            return node


    def get_minimum(self, head, left, right):

        overlap = self.get_overlap(head.leftEdge, head.rightEdge, left, right)
        if overlap == self.complete_overlap:
            return head.min
        elif overlap == self.no_overlap:
            return float("inf")
        elif overlap == self.partial_overlap:
            left_min = self.get_minimum(head=head.left, left=left, right=right)
            right_min = self.get_minimum(head=head.right, left=left, right=right)
            return min(left_min, right_min)

    def get_maximum(self, head, left, right):

        overlap = self.get_overlap(head.leftEdge, head.rightEdge, left, right)
        if overlap == self.complete_overlap:
            return head.max
        elif overlap == self.no_overlap:
            return float("-inf")
        elif overlap == self.partial_overlap:
            left_max = self.get_maximum(head=head.left, left=left, right=right)
            right_max = self.get_maximum(head=head.right, left=left, right=right)
            return max(left_max, right_max)



st = SegmentTree()
root = st.construct_segment_tree(array=arr, start=0, end=len(arr))
i=0
j=m-1
count=0
while j<n:

    temp_min=(st.get_minimum(head=root, left=i, right=j))
    temp_max=(st.get_maximum(head=root, left=i, right=j))
    if temp_max-temp_min<=c:
        count+=1
    i+=1
    j+=1
print(count)
