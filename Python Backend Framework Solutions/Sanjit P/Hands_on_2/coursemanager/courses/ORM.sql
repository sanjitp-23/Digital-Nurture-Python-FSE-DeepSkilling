-- Task 17: Course.objects.filter(department__name="Computer Science")
SELECT courses_course.id, courses_course.name, courses_course.code, courses_course.credits, courses_course.department_id 
FROM courses_course 
INNER JOIN courses_department ON (courses_course.department_id = courses_department.id) 
WHERE courses_department.name = 'Computer Science';

-- Task 18: Department.objects.annotate(course_count=Count("course"))
SELECT courses_department.id, courses_department.name, courses_department.head_of_dept, courses_department.budget, COUNT(courses_course.id) AS course_count 
FROM courses_department 
LEFT OUTER JOIN courses_course ON (courses_department.id = courses_course.department_id) 
GROUP BY courses_department.id, courses_department.name, courses_department.head_of_dept, courses_department.budget;

-- Task 19: Student.objects.select_related("department")
SELECT courses_student.id, courses_student.first_name, courses_student.last_name, courses_student.email, courses_student.department_id, courses_student.enrollment_year, courses_department.id, courses_department.name, courses_department.head_of_dept, courses_department.budget 
FROM courses_student 
INNER JOIN courses_department ON (courses_student.department_id = courses_department.id);

-- Task 20: Department.objects.update(budget=F("budget")*1.1)
UPDATE courses_department 
SET budget = budget * 1.1;
