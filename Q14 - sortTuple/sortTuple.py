"""Q14.

You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]​
"""

# data = [("Tom",19,80),("John",20,90),("Jony",17,91),("Jony",17,93),("Json",21,85),]

# data = []
# n = input("No of tuples: ")

# Seperate Inputs
# for _ in xrange(n):
#   name = raw_input("Name: ")
#   age = int(raw_input("Age: "))
#   height = int(raw_input("Height: "))
#   data.append((name, age, height))

# Comma sep Inputs
# for _ in xrange(n):
#   t = raw_input("Name, Age, Height: ")
#   t = t.split(',')
#   data.append((t[0], int(t[1]), int(t[2])))

data = input("Enter input:\n")

def swap(data, i):
  x = data[i]
  data [i] = data[i + 1]
  data[i + 1] = x

def sortData(data):
  for i in xrange(0, len(data) - 1):
    if data[i][0] > data[i + 1][0]:
      swap(data, i)
      continue
    if data[i][1] > data[i][1]:
      swap(data, i)
      continue
    if data[i][2] > data[i][2]:
      swap(data, i)
      continue
  return data


print sortData(data)
