from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
association = Table('association', pre_meta,
    Column('left_id', INTEGER),
    Column('right_id', INTEGER),
)

playee = Table('playee', post_meta,
    Column('winner_id', Integer),
    Column('loser_id', Integer),
)

fixtures = Table('fixtures', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('timestamp', DATETIME),
    Column('winner_id', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['association'].drop()
    post_meta.tables['playee'].create()
    pre_meta.tables['fixtures'].columns['winner_id'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['association'].create()
    post_meta.tables['playee'].drop()
    pre_meta.tables['fixtures'].columns['winner_id'].create()
