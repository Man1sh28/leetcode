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



    