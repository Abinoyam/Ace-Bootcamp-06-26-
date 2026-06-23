f = open("test_t.txt", "w")
f.write("I like working with codes")
print("File Name is:", f.name)
print("Current Position:", f.tell())
f.close()
with open("test_t.txt", "r") as f:
    print(f.read())
print("File Closed:", f.closed)