
st = "hello world"
print(f"st :{st}")
print(type(st))

# print(dir(st))
print(f"st :{st}")
print(st[0])
# strings are stored like lists in python
print(st[6])
print(st[10])

# st[0] = "H"
# strings are immutable

# slicing
print(f"st :{st}")
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[0:] :{st[0:]}")
print(f"st[:] :{st[:]}")

# reverse indexing
print('-' * 40)
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")
# slicing
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

print('-' * 40)
st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")

res = st.replace("fox", "tiger")
print(f"res :{res}")

print(dir(st))
