def fibonacci(n):
	count = 1
	m = [1, 1]
	while count < n:
		m.append(m[len(m) - 1] + m[len(m) - 2])
		count += 1
	return m
number = int(input("请输入计算的层级："))
print(list(fibonacci(number)))
