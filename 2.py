l1 = [2,4,3]
l2 = [5,6,4]
result1 = 0
result2 = 0
for x in l2[::-1]:
    result1 = result1 * 10 + x
for y in l1[::-1]:
    result2 = result2 * 10 + y
result = [int (d) for d in str(result2+result1)]
print(result[::-1])
# didnt work cause the output is not in the form of linked list

# correct code with the  same approach

     arr1 = []
        while l1:
            arr1.append(l1.val)
            l1 = l1.next

        arr2 = []
        while l2:
            arr2.append(l2.val)
            l2 = l2.next

        result1 = 0
        for y in arr1[::-1]:
            result1 = result1 * 10 + y

        result2 = 0
        for x in arr2[::-1]:
            result2 = result2 * 10 + x

        result = [int(d) for d in str(result1 + result2)][::-1]

        dummy = ListNode(0)
        curr = dummy
        for d in result:
            curr.next = ListNode(d)
            curr = curr.next

        return dummy.next



