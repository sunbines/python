# Python program to explain os.path.join() method

# importing os module
import os

# Path
path = "/home"
# Join various path components
print(os.path.join(path, "User/Desktop", "file.txt"))

# Path
path = "User/Documents"
# Join various path components
print(os.path.join(path, "/home", "file.txt"))

# Path
path = "/User"
# Join various path components
print(os.path.join(path, "Downloads", "file.txt", "/home"))


# Path
path = "/home"
# Join various path components
print(os.path.join(path, "User/Public/", "Documents", ""))


