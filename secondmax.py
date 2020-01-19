def second_max(arr):
		arr = sorted(list(dict.fromkeys(arr)))
		print(arr)
		print("Maximum : ", arr[-1])
		print("Second Maximum : ", arr[-2])

second_max([2, 3, 6, 6, 5])
second_max([2, 34, 23, 100, 3])
