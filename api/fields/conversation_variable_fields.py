from flask_restful import fields

from libs.helper import TimestampField

conversation_variable_fields = {
    "id": fields.String,
    "name": fields.String,
    "value_type": fields.String(attribute="value_type.value"),
    "value": fields.String,
    "description": fields.String,
    "created_at": TimestampField,
    "updated_at": TimestampField,
}

paginated_conversation_variable_fields = {
    "page": fields.Integer,
    "limit": fields.Integer,
    "total": fields.Integer,
    "has_more": fields.Boolean,
    "data": fields.List(fields.Nested(conversation_variable_fields), attribute="data"),
}

conversation_variable_infinite_scroll_pagination_fields = {
    "limit": fields.Integer,
    "has_more": fields.Boolean,
    "data": fields.List(fields.Nested(conversation_variable_fields)),
}
