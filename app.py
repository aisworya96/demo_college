from flask import Flask, request, jsonify

app = Flask(__name__)


class College:
    def __init__(self):
        self.colleges = [
            {
                "id": 1,
                "name": "Sample College 1",
                "classrooms": []
            },
            {
                "id": 2,
                "name": "Sample College 2",
                "classrooms": []
            }
        ]

    def create_college(self, data):
        if "name" in data:
            new_college = {
                "id": len(self.colleges) + 1,
                "name": data["name"],
                "classrooms": []
            }
            self.colleges.append(new_college)
            return {"message": "College created successfully"}, 201
        else:
            return {"error": "Name is required"}, 400

    def get_all_colleges(self):
        return {"colleges": self.colleges}

    def update_college(self, college_id, data):
        college = next((c for c in self.colleges if c["id"] == college_id), None)
        if college is not None:
            college["name"] = data.get("name", college["name"])
            return {"message": "College updated successfully"}, 200
        else:
            return {"error": "College not found"}, 404

    def delete_college(self, college_id):
        college = next((c for c in self.colleges if c["id"] == college_id), None)
        if college is not None:
            self.colleges.remove(college)
            return {"message": "College deleted successfully"}, 200
        else:
            return {"error": "College not found"}, 404


class Classroom:
    def __init__(self):
        self.classrooms = [
            {
                "id": 1,
                "name": "Classroom A",
                "college_id": 1,
                "floor": "1st Floor",
                "block": "A",
                "students": [],
                "teacher": None
            },
            {
                "id": 2,
                "name": "Classroom B",
                "college_id": 1,
                "floor": "1st Floor",
                "block": "B",
                "students": [],
                "teacher": None
            },
            {
                "id": 3,
                "name": "Classroom C",
                "college_id": 2,
                "floor": "2nd Floor",
                "block": "A",
                "students": [],
                "teacher": None
            },
            {
                "id": 4,
                "name": "Classroom D",
                "college_id": 2,
                "floor": "2nd Floor",
                "block": "B",
                "students": [],
                "teacher": None
            },
            {
                "id": 5,
                "name": "Classroom E",
                "college_id": 3,
                "floor": "3rd Floor",
                "block": "C",
                "students": [],
                "teacher": None
            }
        ]

    def create_classroom(self, data):
        if all(key in data for key in ("name", "college_id", "floor", "block")):
            new_classroom = {
                "id": len(self.classrooms) + 1,
                "name": data["name"],
                "college_id": data["college_id"],
                "floor": data["floor"],
                "block": data["block"],
                "students": [],
                "teacher": None
            }
            self.classrooms.append(new_classroom)
            return {"message": "Classroom created successfully"}, 201
        else:
            return {"error": "Name, college_id, floor, and block are required"}, 400

    def get_all_classrooms(self):
        return {"classrooms": self.classrooms}

    def update_classroom(self, classroom_id, data):
        classroom = next((c for c in self.classrooms if c["id"] == classroom_id), None)
        if classroom is not None:
            classroom["name"] = data.get("name", classroom["name"])
            classroom["floor"] = data.get("floor", classroom["floor"])
            classroom["block"] = data.get("block", classroom["block"])
            return {"message": "Classroom updated successfully"}, 200
        else:
            return {"error": "Classroom not found"}, 404

    def delete_classroom(self, classroom_id):
        classroom = next((c for c in self.classrooms if c["id"] == classroom_id), None)
        if classroom is not None:
            self.classrooms.remove(classroom)
            return {"message": "Classroom deleted successfully"}, 200
        else:
            return {"error": "Classroom not found"}, 404


class Teacher:
    def __init__(self):
        self.teachers = [
            {
                "id": 1,
                "first_name": "John",
                "last_name": "Doe",
                "age": 30,
                "topics": ["Math", "Science"]
            },
            {
                "id": 2,
                "first_name": "Jane",
                "last_name": "Smith",
                "age": 35,
                "topics": ["History", "English"]
            },
            {
                "id": 3,
                "first_name": "Michael",
                "last_name": "Johnson",
                "age": 28,
                "topics": ["Physics", "Chemistry"]
            },
            {
                "id": 4,
                "first_name": "Emily",
                "last_name": "Brown",
                "age": 32,
                "topics": ["Biology", "Geography"]
            },
            {
                "id": 5,
                "first_name": "William",
                "last_name": "Wilson",
                "age": 40,
                "topics": ["Computer Science", "Programming"]
            }
        ]

    def create_teacher(self, data):
        if all(key in data for key in ("first_name", "last_name", "age", "topics")):
            new_teacher = {
                "id": len(self.teachers) + 1,
                "first_name": data["first_name"],
                "last_name": data["last_name"],
                "age": data["age"],
                "topics": data["topics"]
            }
            self.teachers.append(new_teacher)
            return {"message": "Teacher created successfully"}, 201
        else:
            return {"error": "First name, last name, age, and topics are required"}, 400

    def get_all_teachers(self):
        return {"teachers": self.teachers}

    def update_teacher(self, teacher_id, data):
        teacher = next((t for t in self.teachers if t["id"] == teacher_id), None)
        if teacher is not None:
            teacher["first_name"] = data.get("first_name", teacher["first_name"])
            teacher["last_name"] = data.get("last_name", teacher["last_name"])
            teacher["age"] = data.get("age", teacher["age"])
            teacher["topics"] = data.get("topics", teacher["topics"])
            return {"message": "Teacher updated successfully"}, 200
        else:
            return {"error": "Teacher not found"}, 404

    def delete_teacher(self, teacher_id):
        teacher = next((t for t in self.teachers if t["id"] == teacher_id), None)
        if teacher is not None:
            self.teachers.remove(teacher)
            return {"message": "Teacher deleted successfully"}, 200
        else:
            return {"error": "Teacher not found"}, 404



class Student:
    def __init__(self):
        self.students = [
            {
                "id": 1,
                "first_name": "Alice",
                "last_name": "Smith",
                "age": 18,
                "standard": "12th"
            },
            {
                "id": 2,
                "first_name": "Bob",
                "last_name": "Johnson",
                "age": 17,
                "standard": "11th"
            },
            {
                "id": 3,
                "first_name": "Charlie",
                "last_name": "Brown",
                "age": 16,
                "standard": "10th"
            },
            {
                "id": 4,
                "first_name": "David",
                "last_name": "Wilson",
                "age": 17,
                "standard": "11th"
            },
            {
                "id": 5,
                "first_name": "Emma",
                "last_name": "Davis",
                "age": 15,
                "standard": "9th"
            },
            {
                "id": 6,
                "first_name": "Frank",
                "last_name": "Lee",
                "age": 16,
                "standard": "10th"
            },
            {
                "id": 7,
                "first_name": "Grace",
                "last_name": "Martinez",
                "age": 18,
                "standard": "12th"
            },
            {
                "id": 8,
                "first_name": "Hannah",
                "last_name": "Jackson",
                "age": 15,
                "standard": "9th"
            },
            {
                "id": 9,
                "first_name": "Isabella",
                "last_name": "Harris",
                "age": 17,
                "standard": "11th"
            },
            {
                "id": 10,
                "first_name": "Jack",
                "last_name": "Taylor",
                "age": 16,
                "standard": "10th"
            }
        ]

    def create_student(self, data):
        if all(key in data for key in ("first_name", "last_name", "age", "standard")):
            new_student = {
                "id": len(self.students) + 1,
                "first_name": data["first_name"],
                "last_name": data["last_name"],
                "age": data["age"],
                "standard": data["standard"]
            }
            self.students.append(new_student)
            return {"message": "Student created successfully"}, 201
        else:
            return {"error": "First name, last name, age, and standard are required"}, 400

    def get_all_students(self):
        return {"students": self.students}

    def update_student(self, student_id, data):
        student = next((s for s in self.students if s["id"] == student_id), None)
        if student is not None:
            student["first_name"] = data.get("first_name", student["first_name"])
            student["last_name"] = data.get("last_name", student["last_name"])
            student["age"] = data.get("age", student["age"])
            student["standard"] = data.get("standard", student["standard"])
            return {"message": "Student updated successfully"}, 200
        else:
            return {"error": "Student not found"}, 404

    def delete_student(self, student_id):
        student = next((s for s in self.students if s["id"] == student_id), None)
        if student is not None:
            self.students.remove(student)
            return {"message": "Student deleted successfully"}, 200
        else:
            return {"error": "Student not found"}, 404


college_handler = College()
classroom_handler = Classroom()
teacher_handler = Teacher()
student_handler = Student()


@app.route('/colleges', methods=['POST'])
def create_college():
    data = request.get_json()
    response, status_code = college_handler.create_college(data)
    return jsonify(response), status_code


@app.route('/colleges', methods=['GET'])
def get_all_colleges():
    return jsonify(college_handler.get_all_colleges())


@app.route('/colleges/<int:college_id>', methods=['PUT'])
def update_college(college_id):
    data = request.get_json()
    response, status_code = college_handler.update_college(college_id, data)
    return jsonify(response), status_code


@app.route('/colleges/<int:college_id>', methods=['DELETE'])
def delete_college(college_id):
    response, status_code = college_handler.delete_college(college_id)
    return jsonify(response), status_code


@app.route('/classrooms', methods=['POST'])
def create_classroom():
    data = request.get_json()
    response, status_code = classroom_handler.create_classroom(data)
    return jsonify(response), status_code


@app.route('/classrooms', methods=['GET'])
def get_all_classrooms():
    return jsonify(classroom_handler.get_all_classrooms())


@app.route('/classrooms/<int:classroom_id>', methods=['PUT'])
def update_classroom(classroom_id):
    data = request.get_json()
    response, status_code = classroom_handler.update_classroom(classroom_id, data)
    return jsonify(response), status_code


@app.route('/classrooms/<int:classroom_id>', methods=['DELETE'])
def delete_classroom(classroom_id):
    response, status_code = classroom_handler.delete_classroom(classroom_id)
    return jsonify(response), status_code


@app.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.get_json()
    response, status_code = teacher_handler.create_teacher(data)
    return jsonify(response), status_code


@app.route('/teachers', methods=['GET'])
def get_all_teachers():
    return jsonify(teacher_handler.get_all_teachers())


@app.route('/teachers/<int:teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
    data = request.get_json()
    response, status_code = teacher_handler.update_teacher(teacher_id, data)
    return jsonify(response), status_code


@app.route('/teachers/<int:teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
    response, status_code = teacher_handler.delete_teacher(teacher_id)
    return jsonify(response), status_code


@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    response, status_code = student_handler.create_student(data)
    return jsonify(response), status_code


@app.route('/students', methods=['GET'])
def get_all_students():
    return jsonify(student_handler.get_all_students())


@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    response, status_code = student_handler.update_student(student_id, data)
    return jsonify(response), status_code


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    response, status_code = student_handler.delete_student(student_id)
    return jsonify(response), status_code


if __name__ == '__main__':
    app.run(debug=True)
