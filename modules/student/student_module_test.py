#this python files is to test all functionality inside student class
#in future the class will be used to real senerio

from student import StudentClass


#step : student registeretion test

email = input ("enter your email")
password= input ("enter your password")


s1 = StudentClass()
s1.username_and_password(email, password)



#student details test
phone_number = input("enter your phone number")
full_name = input("enter your full name")
dob = input("enter your date of birth")
gender = input("enter your gender")
preferred_language = input("enter your preferred language")
school_college_name = input("enter your school or college name")
class_grade = input("enter your class or grade")
board_curriculum = input("enter your board or curriculum")
accademic_year = input("enter your academic year")

s1.set_student_details(full_name, dob, gender, phone_number, preferred_language, school_college_name, class_grade, board_curriculum, accademic_year)
