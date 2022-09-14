from typing import Optional


class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Given two sorted linked lists, merge them together in ascending order and return a reference to the merged list 

    Example: Given the following lists...

    list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
    list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
    list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null
    """
    def __init__(self):
        self.head = None

    def insert(self, val: int):
        """
        Insert a new value into the linked list.

        Args:
            val: The value to insert into the linked list.

        Returns: 
            None
        """

        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head

        while last.next is not None:
            last = last.next
        
        last.next = new_node


    

    def merge_linked_lists(self, list1: Optional[ListNode], list2:Optional[ListNode])->ListNode:
        """
        Merge two sorted linked lists.

        Args: 
            list1: A sorted linked list.
            list2: A sorted linked list.

        Returns:
            A sorted linked list the merges the two linked lists provided as inputs.
        """

        if list1 is None:
            return list2

        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
            temp = list1
            temp.next = self.merge_linked_lists(list1.next, list2)
        
        else:
            temp = list2
            temp.next = self.merge_linked_lists(list2.next, list1)
        
        return temp

if __name__ == "__main__":
    # vals = [[[1,2,3],[4,5,6]][[1,3,5][2,4,6]],[[4,4,7],[1,5,6]]]
    vals = [[1,2,3],[4,5,6]]

    l1_n1 = ListNode(vals[0][0])
    l1_n2 = ListNode(vals[0][1])
    l1_n3 = ListNode(vals[0][2])
    
    l1_n1.next = l1_n2
    l1_n2.next = l1_n3

    l2_n1 = ListNode(vals[1][0])
    l2_n2 = ListNode(vals[1][1])
    l2_n3 = ListNode(vals[1][2])

    l2_n1.next = l2_n2
    l2_n2.next = l2_n3

    solution = Solution()
    
    # node1 = solution.insert(val=vals[0][0])
    # for val in vals:
    #     l1 = Solution()
    #     l2 = Solution()
    #     l1.insert(val=val[0])
    #     l2.insert(val=val[1])
    #     print([sol for sol in solution.merge_linked_lists(l1, l2)])

    result = solution.merge_linked_lists(l1_n1, l2_n1)
    
    while result is not None:
        print(result.val)
        result = result.next
