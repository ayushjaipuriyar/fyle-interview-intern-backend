from flask import Blueprint
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from core.apis import decorators
from core.apis.teachers.schema import TeacherSchema


principal_teachers_resources = Blueprint("principal_teachers_resources", __name__)


@principal_teachers_resources.route("/teachers", methods=["GET"], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of assignments"""
    teachers_list = Teacher.get_list_of_teachers()
    teachers_list_dump = TeacherSchema().dump(teachers_list, many=True)
    return APIResponse.respond(data=teachers_list_dump)
