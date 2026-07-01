from courses import db


class Department(db.Model):

    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    head_of_dept = db.Column(db.String(100), nullable=False)

    budget = db.Column(db.Float, nullable=False)

    courses = db.relationship(
        "Course",
        back_populates="department",
        lazy=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "head_of_dept": self.head_of_dept,
            "budget": self.budget
        }

class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    enrollments = db.relationship(
        "Enrollment",
        back_populates="student",
        lazy=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

class Enrollment(db.Model):

    __tablename__ = "enrollments"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )

    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )

    student = db.relationship(
        "Student",
        back_populates="enrollments"
    )

    course = db.relationship("Course")

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "course_id": self.course_id
        }

class Course(db.Model):

    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    code = db.Column(db.String(20), unique=True, nullable=False)

    credits = db.Column(db.Integer, nullable=False)

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id"),
        nullable=False
    )

    department = db.relationship(
        "Department",
        back_populates="courses"
    )
    enrollments = db.relationship(
    "Enrollment",
    lazy=True
)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "credits": self.credits,
            "department_id": self.department_id
        }

