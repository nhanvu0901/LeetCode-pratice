class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

   dummy = ListNode(0)
   current = dummy
   carry = 0

   while l1 or l2 or carry:
       x = l1.val if l1 else 0
       y = l2.val if l2 else 0

       total = x + y + carry
       carry = total // 10
       digit = total % 10

       current.next = ListNode(digit)
       current = current.next

       l1 = l1.next if l1 else None
       l2 = l2.next if l2 else None

   return dummy.next


# Helper function to create linked list from array
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert linked list to array for easy viewing
def linkedListToArray(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
test_cases = [
    ([2, 4, 3], [5, 6, 4]),
    ([0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])
]

for l1_arr, l2_arr in test_cases:
    l1 = createLinkedList(l1_arr)
    l2 = createLinkedList(l2_arr)
    result = addTwoNumbers(l1, l2)
    print(f"Input: l1 = {l1_arr}, l2 = {l2_arr}")
    print(f"Output: {linkedListToArray(result)}")
    print()