from marshmallow import Schema, fields


class RidesSchema(Schema):

    uid = fields.String(allow_none=False)
    creator = fields.String()
    ride_name = fields.String(default='')
    meet_point = fields.String(default='')
    ride_datetime = fields.String()
    meet_time = fields.String()
    description = fields.String(default='')
