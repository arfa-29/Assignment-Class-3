# Grading system of XYZ Uniersity

yourMarks = int(input("Enter your marks: "))

if yourMarks >= 880 and yourMarks <= 1000:
    print("""You Got "A1 Grade"
GPA is 4.0
Excellent""")
elif yourMarks >= 810 and yourMarks < 880:
    print("""You Got "A Grade"
GPA is 3.5
Very Good""")
elif yourMarks >= 740 and yourMarks < 810:
    print("""You Got "B Grade"
GPA is 3.0
Good""")
elif yourMarks >= 670 and yourMarks < 740:
    print("""You Got "C Grade"
GPA is 2.5
Average""")
elif yourMarks >= 600 and yourMarks < 670:
    print("""You Got "D Grade"
GPA is 2.0
Below Average""")
else:
    print("""you are failed
course repeat""")
