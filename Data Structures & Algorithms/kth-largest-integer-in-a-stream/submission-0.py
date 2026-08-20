class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []

        # Add the initial values using the same logic as add()
        for num in nums:
            self._push(num)

            if len(self.heap) > self.k:
                self._pop_min()

    def add(self, val: int) -> int:
        self._push(val)

        if len(self.heap) > self.k:
            self._pop_min()

        return self.heap[0]

    def _push(self, val: int) -> None:
        """Add a value and restore the min-heap property."""
        self.heap.append(val)
        index = len(self.heap) - 1

        # Sift upward
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[parent] <= self.heap[index]:
                break

            self.heap[parent], self.heap[index] = (
                self.heap[index],
                self.heap[parent],
            )
            index = parent

    def _pop_min(self) -> int:
        """Remove and return the minimum value."""
        minimum = self.heap[0]

        # Move the last element to the root
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._sift_down()

        return minimum

    def _sift_down(self) -> None:
        """Restore the min-heap property after removing the root."""
        index = 0
        n = len(self.heap)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            index = smallest