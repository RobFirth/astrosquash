from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
player = Table('player', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('played', Integer),
    Column('won', Integer),
    Column('lost', Integer),
    Column('name', String(length=64)),
    Column('photourl', String(length=120)),
    Column('wins', Integer),
    Column('losses', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['player'].columns['losses'].create()
    post_meta.tables['player'].columns['wins'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['player'].columns['losses'].drop()
    post_meta.tables['player'].columns['wins'].drop()
