name = input("What is your name?")
file = "name.txt"
out_file = open(file, "w")

print(("Your name is", name), file=out_file)

out_file.close()