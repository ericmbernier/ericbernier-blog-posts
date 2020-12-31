from marshmallow import Schema, fields, post_load
from football_api.models.player import Player


class PlayerSchema(Schema):
    """
    Player Marshmallow Schema

    Marshmallow schema used for loading/dumping Players
    """

    name = fields.String(allow_none=False)
    position = fields.String(allow_none=False)
    player_id = fields.Integer()

    @post_load
    def make_player(self, data, **kwargs):
        return Player(**data)
