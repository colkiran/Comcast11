
"""
1. local
2. global
3. non local
"""


# global scope
glbX = 100

def fun(y):                 # local variable
    global glbX             # global variable
    print(f"y :{y}")
    glbX = 250
    print(f"Inside fun :{glbX}")


print(f"Before fun :{glbX}")

fun(50)

print(f"After fun :{glbX}")
