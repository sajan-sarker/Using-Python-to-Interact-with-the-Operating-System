import os
print("Destination: "+os.getcwd())

dest_dir = os.path.join(os.getcwd(), "text1")
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

src_file = os.path.join(os.getcwd(), "Module2", "README.md")
dest_file = os.path.join(os.getcwd(), "test1", "README.md")


os.rename(src_file, dest_file)

print()
print()
