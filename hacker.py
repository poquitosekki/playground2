# i = int(input())
# lis = list(map(int, input().split()))
import timeit

# A little faster than the one below:
def secm(lis):
	lis = sorted(lis)
	z = max(lis)
	while lis[-1] == z:
		lis.remove(lis[-1])	
	return lis[-1] 

def secmn(lis):
	z = max(lis)
	while max(lis) == z:
		lis.remove(max(lis))
	return max(lis)

n = int(input("Select N : "))
arr = [i for i in range(n+1)]

print("Second Maximum : ", secm(arr))
print("Second Max •N : ", secmn(arr))
