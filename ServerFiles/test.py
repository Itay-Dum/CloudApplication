def x(y: int):
    print(int(y))


h = {
    "x": x
}
h['x'](5)
