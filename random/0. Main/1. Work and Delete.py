class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Step 1: Find the middle using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev, curr = None, slow.next
        slow.next = None  # Cut off first half
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next  # Store next pointers
            first.next = second  # Merge node from second half
            second.next = temp1  # Connect back to first half
            first, second = temp1, temp2  # Move to next pair


# Example Usage
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print_list(head)
sol = Solution()
sol.reorderList(head)
print_list(head)  # Output: 1 -> 5 -> 2 -> 4 -> 3 -> None
