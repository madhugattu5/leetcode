from collections import deque
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        container = deque()

        iterNode = head

        while iterNode is not None:
            container.append(iterNode.val)
            iterNode = iterNode.next

        result = 0

        while container:
            front = container.popleft()
            back = container.pop()
            result = max(result, front + back)
        return result