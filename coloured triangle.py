
def triangle(s):
    while len(s) > 1: s= ''.join(({'R', 'G', 'B'} - {a, b}).pop() if a != b else a for a, b in zip(s, s[1:]))
    return s
print(triangle(input()))

