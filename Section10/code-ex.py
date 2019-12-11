present_students = dict()
with open('attendance.csv', 'r') as attendance:
    header = attendance.readline()
    header_list = header.split(";")
    column_number = header_list.index('4') #list
    line = attendance.readline() #string
    while line != '':
        student_info = line.split(";") #list
        attendance_info = student_info[column_number]
        if attendance_info == 'yes':
            present_students[student_info[0]] = student_info[header_list.index('Email')]
        line = attendance.readline()
    attendance.close()

file_name = 'students_in_section_4.txt'
while True:
    try:
        with open(file_name, 'x') as my_file:
            for student in present_students:
                my_file.write(student + ';' + present_students[student] + '\n')
            my_file.close()
            break
    # I don't want to overwrite existing file
    except FileExistsError:
        print("This file already exists, I am creating a file with a different name")
        file_name = file_name[:file_name.index('.txt')] + '1.txt'
