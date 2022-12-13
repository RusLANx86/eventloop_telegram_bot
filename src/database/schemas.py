from marshmallow import Schema, fields, EXCLUDE, pre_load


class RidesSchema(Schema):

    uid = fields.String(allow_none=False, data_key='id')
    creator = fields.String()
    ride_name = fields.String(default='', data_key='Nazvanie_katushki')
    meet_point = fields.String(default='', data_key='Tochka_sbora')
    ride_datetime = fields.String(data_key='Vremya_nachala_katushki')
    meet_time = fields.String()
    description = fields.String(default='', data_key='Opisanie_katushki')

    # @pre_load
    # def convert_datetime(self, data, **kwargs):
    #     dt = data['Vremya_nachala_katushki']
    #     ...

    class Meta:
        unknown = EXCLUDE
        exclude = ("uid",)
