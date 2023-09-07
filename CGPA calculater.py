#CGPA calculater
def cgpacal():
    totscore=0
    gradegot=0
    coursesNo = int(input("Enter the no of subjects: "))
    print("*************************************************")
    for x in range(coursesNo):
        coursenum = int(input("Enter the subject code: "))
        score = int(input("Enter the mark: "))
        print("*********************************************")
        totscore += coursesNo*100
        
        if (score>=70):
            grade = 5
        elif (score<70 and score>=60):
            grade = 4
        elif (score <60 and score>=50):
            grade = 3
        elif (score < 50 and score>=45):
            grade = 2
        elif (score < 45 and score>=40):
            grade = 1
        else:
            grade = 0
            gradegot += grade
            cgpa = float((gradegot/totscore)*5)
            print("Your CGPA IS: " + str(cgpa))
            cgpacal()

