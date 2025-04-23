class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0] * numCourses
        queue = deque()
        order = []

        # Build the graph and count incoming edges
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1

        # Add all nodes with no incoming edges to the queue
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)

        # BFS traversal
        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)

        # If all courses are in order, return it; otherwise return []
        if len(order) != numCourses:
            return []

        return order
