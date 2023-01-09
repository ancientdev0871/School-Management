from wish_teacher import wish
students = {}
print(wish())
s = int(input("What is the strength of your class: "))
for i in range(s):
  n = input("What is the name of the student: ")
  rl =int(input(f"What is the roll number of {n}: "))
  students[rl] = n
marks = []
for o in range(s):
  marks.append({})
for j in range(s):
  print("You are kindly requested to input the marks of the respective students in the roll number wise order.")
  grade = int(input("This is the marks of which student(Roll number): "))
  maths = int(input("Marks in maths: "))
  chem = int(input("Marks in chemistry: "))
  bio = int(input("Marks in biology: "))
  phy = int(input("Marks in physics: "))
  eng1 = int(input("Marks in english language: "))
  eng2 = int(input("Marks in english literature: "))
  hist = int(input("Marks in history: "))
  geo = int(input("Marks in geography: "))
  ca = int(input("Marks in computer application: "))
  hind = int(input("Marks in hindi: "))
  comments = input("Comment on the student's performance: ")
  marks[grade-1]["maths"] = maths
  marks[grade-1]["phy"] = phy
  marks[grade-1]["chem"] = chem
  marks[grade-1]["bio"] = bio
  marks[grade-1]["eng1"] = eng1
  marks[grade-1]["eng2"] = eng2
  marks[grade-1]["hist"] = hist
  marks[grade-1]["geo"] = geo
  marks[grade-1]["ca"] = ca
  marks[grade-1]["hindi"] = hind
  marks[grade-1]["comment"] = comments
end = True
while end:
  ask = int(input("You need the marks of which student(Roll number): "))
  def result(name, math, phy, chem, bio, eng1, eng2, hist, geo, ca, hind, cmt):
    print(f"Student name: {name}")
    print(f"Roll number: {ask}")
    print(f"Mathematics: {math}")
    print(f"Physics: {phy}")
    print(f"Chemistry: {chem}")
    print(f"Biology: {bio}")
    print(f"English language: {eng1}")
    print(f"English literature: {eng2}")
    print(f"History: {hist}")
    print(f"Geography: {geo}")
    print(f"Computer applications: {ca}")
    print(f"Hindi: {hind}")
    total = math + phy + chem + bio + eng1 + eng2 + hist + geo + ca + hind
    aggregrate_percentage = total/1250*100
    print(f"Percentile: {aggregrate_percentage}%")
    print(f"Comment of the teacher: {cmt}")
  result(name=students[ask], math=marks[ask-1]["maths"], phy=marks[ask-1]["phy"], chem=marks[ask-1]["chem"], bio=marks[ask-1]["bio"], eng1=marks[ask-1]["eng1"], eng2=marks[ask-1]["eng2"], hist=marks[ask-1]["hist"], geo=marks[ask-1]["geo"], ca=marks[ask-1]["ca"], hind=marks[ask-1]["hindi"], cmt=marks[ask-1]["comment"])
  # new_result = "\n".join(str(key) + ":" +  str(value) for key, value in marks[ask-1].items())
  # print(new_result)
  e = input("Do you want more results(y or n): ")
  if e == "n":
    end = False
