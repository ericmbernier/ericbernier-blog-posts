from marshmallow import Schema, fields, post_load
from football_api.models.team import Team


class TeamSchema(Schema):
    """
    Team Marshmallow Schema

    Marshmallow schema used for loading/dumping Teams
    """

    name = fields.String(allow_none=False)
    abbreviation = fields.String(allow_none=False)
    team_id = fields.Integer()

    @post_load
    def make_team(self, data, **kwargs):
        return Team(**data)
