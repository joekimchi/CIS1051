#1 
infile = open("input.txt", "r")
outfile = open("output.txt", "w")
count = 0

line = infile.readline()
while line != "":
    value = str(line)
    count = count + 1
    outfile.write(count + value + "\n")
    line.infile.readline()
    
outfile.close()
infile.close()

#2
infile = open("input.txt", 'r')

num_lines = len(feed.splitlines())
num_words = 0
num_chars = 0

for line in lines:
    num_words += len(line.split())

#3
import turtle 
alex = turtle.Turtle()
alex.shape("turtle")
alex.up()

for i in range(10):
    if i%2 == 0:
        alex.color("blue")
    else:
        alex.color("red")
    alex.stamp()
    alex.forward(20)
