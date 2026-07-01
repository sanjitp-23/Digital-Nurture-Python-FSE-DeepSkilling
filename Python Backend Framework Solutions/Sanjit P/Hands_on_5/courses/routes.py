from flask import Blueprint, jsonify, request
from courses import db
from courses.models import Course

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)


def make_response_json(data, status_code=200):
    return jsonify({
        "status": "success",
        "data": data
    }), status_code


@courses_bp.route("/", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return make_response_json([course.to_dict() for course in courses])


@courses_bp.route("/<int:id>", methods=["GET"])
def get_course(id):
    course = Course.query.get_or_404(id)
    return make_response_json(course.to_dict())


@courses_bp.route("/", methods=["POST"])
def create_course():

    data = request.get_json()

    if not data:
        return jsonify({"message": "JSON body required"}), 400

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"],
        department_id=data.get("department_id")
    )

    db.session.add(course)
    db.session.commit()

    return make_response_json(course.to_dict(), 201)


@courses_bp.route("/<int:id>", methods=["PUT"])
def update_course(id):

    course = Course.query.get_or_404(id)

    data = request.get_json()

    course.name = data.get("name", course.name)
    course.code = data.get("code", course.code)
    course.credits = data.get("credits", course.credits)

    db.session.commit()

    return make_response_json(course.to_dict())


@courses_bp.route("/<int:id>", methods=["DELETE"])
def delete_course(id):

    course = Course.query.get_or_404(id)

    db.session.delete(course)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Course deleted"
    })