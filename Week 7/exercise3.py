import csv
import random as random
import platform
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url
    
    def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        avg_grade = sum(grades)/len(grades)
        return avg_grade    
    
    
    
    
class DataSheet():
    def __init__(self, courses = []):
        self.courses = courses    
    
    def get_grades_as_list(self):
        grades = []
        for course in self.courses:
            grades.append(course.grade)
        return grades    
    
      
class Course():
    def __init__(self, name, teacher, classroom, ects, grade):
        self.name = name
        self.teacher = teacher
        self.classroom = classroom
        self.ects = ects
        self.grade = grade    
    
    
def random_student(n):
    
    m_names = ['Harald Blaatand','Jens Jensen','Emil Hansen','Ole Olsen','Per Pallesen','Hans Hansen']
    f_names = ['Yrsa Hansen','Jane Jansen','Bolette Nielsen','Ea Andersen','Jette Jespersen','Kristine Holm']
        
    with open('students.csv', 'w', newline='') as output_file:
        output_writer = csv.writer(output_file)
        #output_writer.writerow(['NAME','COURSENAME','TEACHER','ECTS','CLASSROOM','GRADE','IMGURL'])
        output_writer.writerow(['stud_name','course_name','teacher','ects','classroom','grade','img_url'])        
        
        for i in range(n):
            
            course_1 = Course('English','Birgitte Kofoed','1.021',random.randrange(10,30),random.choice([2,4,7,10,12]))
            course_2 = Course('Danish','Per Holm','1.022',random.randrange(10,30),random.choice([2,4,7,10,12]))
            course_3 = Course('Math','Erik Agerhoff','1.023',random.randrange(10,30),random.choice([2,4,7,10,12]))
            course_4 = Course('Spanish','Dorte Jensen','1.024',random.randrange(10,30),random.choice([2,4,7,10,12]))
            courses = [course_1,course_2,course_3,course_4]    
    
            gender = random.choice(['Male','Female'])
            
            if gender is 'Male':
                name = random.choice(m_names)
            else:
                name = random.choice(f_names)
                     
            data_sheet = DataSheet(random.sample(courses,1))
            
            student = Student(name,gender,data_sheet,'www.image.com')
            
            output_writer.writerow([student.name,student.data_sheet.courses[0].name,
            student.data_sheet.courses[0].teacher,student.data_sheet.courses[0].ects,
            student.data_sheet.courses[0].classroom,student.data_sheet.courses[0].grade,student.image_url])               
                
                   
def read_students():
    students = []
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader,None)
        for row in reader:
            data_sheet = DataSheet([Course(row[1],row[4],row[2],row[3],int(row[5]))])
            stud = Student(row[0],'N/A',data_sheet,row[6])
            students.append(stud)
            students.sort(key=lambda s: s.get_avg_grade(), reverse=True)
       # for stud in students:
            #print(stud.name + ' - ' + stud.image_url + ' - ' + str(stud.get_avg_grade()))
    return students    


def student_ects_sort():
    students = read_students()

    for s in students:
        Ectssum = 9
        for course in s.data_sheet.courses:
            Ectssum += int(course.ects)
        print(s.name + ': ' + str(round((Ectssum/150)*100, 2))+'%' + '  ' + s.image_url)

        
def student_plotter():
    students = read_students()
    avg_grade = []
    names = []
    for s in students:
        names.append(s.name)
        avg_grade.append(s.get_avg_grade())


    plt.bar(names, avg_grade, width=0.6, align='center')
    plt.ylabel('Avg-Grade')
    plt.xlabel('Name')
    plt.title('Students avg-grade')
    plt.show()        
        
        
        
student_ects_sort()
#student_plotter()