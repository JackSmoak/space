# 2 ** 4 = 2 * 2 * 2 * 2

def pot(b, e):

	if e == 0:
		return 1
	return b * pot(b, e - 1)

print(pot(2, 10))
