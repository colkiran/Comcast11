
num = 5
inv = 1

try:
    inv = 1 / num

except ZeroDivisionError as z:
    print(z)

except TypeError as t:
    print(t)

except Exception as e:
    print(e)


else:
    print(f"inverse of {num} is {inv}")

finally:
    print("completed the process of dividing numbers......")