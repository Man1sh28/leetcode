nums1 =[]
nums2 =[2]
l2=[]

for i in nums1:
            l2.append(i)
for j in nums2:
            l2.append(j)

l2.sort()
n = len(l2)
if n == 0:
    print (0)
    if l2[0]>0:
        print (l2[0])
    else:
        print (0)
elif n%2==1:
   print ((l2[0] + l2[-1])/2)
else:
    print ((l2[n//2] + l2[n//2 -1])/2)