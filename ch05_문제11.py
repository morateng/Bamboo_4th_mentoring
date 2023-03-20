def test(x, y):
    tmp = x
    x = y
    y = tmp
    return y.append(x)  # y = ['y', ['x']] 새로운 값임


x = ["y"]
y = ["x"]
test(x, y)
print(y)
