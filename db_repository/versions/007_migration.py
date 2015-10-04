from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
player = Table('player', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('played', INTEGER),
    Column('won', INTEGER),
    Column('lost', INTEGER),
    Column('name', VARCHAR(length=64)),
    Column('photourl', VARCHAR(length=120)),
    Column('losses', INTEGER),
    Column('wins', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['player'].columns['losses'].drop()
    pre_meta.tables['player'].columns['wins'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['player'].columns['losses'].create()
    pre_meta.tables['player'].columns['wins'].create()
