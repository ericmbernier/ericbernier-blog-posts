from marshmallow import Schema, fields, post_load
from football_api.schemas.player_schema import PlayerSchema
from football_api.schemas.team_schema import TeamSchema
from football_api.models.stats import Stats


class StatsSchema(Schema):
    """
    Stats Marshmallow Schema

    Marshmallow schema used for loading/dumping Stats
    """

    stat_id = fields.Integer()
    player_id = fields.Integer()
    player = fields.Nested(PlayerSchema(), dump_only=True)
    season = fields.Integer(allow_none=False)
    team_id = fields.Integer()
    team = fields.Nested(TeamSchema(), dump_only=True)
    age = fields.Integer()
    games = fields.Integer()
    games_started = fields.Integer()
    completions = fields.Integer()
    pass_attempts = fields.Integer()
    pass_yards = fields.Integer()
    pass_tds = fields.Integer()
    interceptions = fields.Integer()
    rush_attempts = fields.Integer()
    rush_yards = fields.Integer()
    rush_yards_per_attempt = fields.Number()
    rush_tds = fields.Integer()
    targets = fields.Integer()
    receptions = fields.Integer()
    rec_yards = fields.Integer()
    yards_per_reception = fields.Number()
    rec_tds = fields.Integer()
    fumbles = fields.Integer()
    fumbles_lost = fields.Integer()
    fantasy_points = fields.Number()

    @post_load
    def make_stats(self, data, **kwargs):
        return Stats(**data)
