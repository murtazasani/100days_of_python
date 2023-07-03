# Some Functions on Set
# Unordered Form
st = {1, 2, 4, 5, 9, 3, 8}
print(st)

''' Not Support Indexing
print(st[1])'''

# Don't allow duplication
st1 = {1, 1, 3, 3.0, "Hello world"}
print(st1)

"Functions of Set"

st2 = {1, 3, 5, 9}
print(st2)

st2.add(2)
print(st2)

st2.update([4, 6, 7, 8])
print(st2)

st2.remove(8)
print(st2)

"Set Operations"
"Union"
a = {0, 1, 3}
b = {4, 5, 6}
print(a | b)

"InterSection"
c = {1, 3, 4, 5}
d = {1, 2, 4, 5, 6}
print(c & d)


