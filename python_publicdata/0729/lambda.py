# 1번
students = [('Alice', 3.9, 20160303),
            ('Bob',	3.0, 20160302),
            ('Charlie',	4.3, 20160301)]

# 학번으로 >> 오름차순으로
sorted_students1 = sorted(students, key= lambda s: s[2])
print(sorted_students1)

# 학점으로 >> 내림차순으로
sorted_students2 = sorted(students, key= lambda s: s[1], reverse=True)
print(sorted_students2)

#---------------------------------------------------------------------
# 2번

class Student:
    def	__init__(self,	name,	grade,	number):
        self.name =	name
        self.grade = grade
        self.number = number

    def	__repr__(self):
        return f'({self.name}, {self.grade}, {self.number})'

students = [Student('홍길동', 3.9, 20240303),
            Student('김유신', 3.0, 20240302),
            Student('박문수', 4.3, 20240301)]

print(students[0])

sorted_list= sorted(students, key=lambda s:s.name)
print(sorted_list)