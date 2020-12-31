from marshmallow import Schema, fields, post_load
from football_api.models.season import Season


class SeasonSchema(Schema):
    """
    Season Marshmallow Schema

    Marshmallow schema used for loading/dumping Seasons
    """

    year = fields.Integer(allow_none=False)

    @post_load
    def make_season(self, data, **kwargs):
        return Season(**data)
