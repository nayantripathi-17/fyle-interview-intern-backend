from marshmallow import Schema, EXCLUDE, fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_enum import EnumField
from core.models.assignments import Assignment, GradeEnum
from core.libs.helpers import GeneralObject
from core.models.users import User
from core.models.teachers import Teacher

class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        unknown = EXCLUDE

    id = auto_field(required=False, allow_none=True)
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)
    user_id = auto_field(dump_only=True)