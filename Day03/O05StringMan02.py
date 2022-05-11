
st = "hello world"
print(f"st :{st}")

# uppercase
res = st.upper()
print(res)

# title
res = st.title()
print(res)

print('-' * 40)
emp = "EMP-001, John Slater, Male, MGR, HR, 850000"
print(f"emp :{emp}")
print(type(emp))

# converting the string into a list - split(delimiter)
emplst = emp.split(", ")
print(f"emplst :{emplst}")
print(type(emplst))
print(f"Name  :{emplst[1]}")
print(f"Desig :{emplst[3]}")

# convert the list into a string - join(delimiter)
empstr = ", ".join(emplst)
print(f"empstr :{empstr}")
print(type(empstr))

print("maketrans".center(40, "-"))
# maketrans, translate
st = "hello world"
print(f"st :{st}")
a = "helowrd"
b = "HELOWRD"
# the length of a and b should be the same

trnsTbl = st.maketrans(a,b)
print(f"trnsTbl :{trnsTbl}")

print("{:-^40}".format("translate"))
res = st.translate(trnsTbl)
print(f"res :{res}")

print("strip".center(40, "-"))
st = "************hello world****************"
print(f"st :{st}")

# remove from the RHS
res = st.rstrip("*")
print(f"res :{res}")

# remove * from LHS
res = st.lstrip("*")
print(f"res :{res}")

# remove * from both sides
res = st.strip("*")
print(f"res :{res}")
