from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
playee = Table('playee', pre_meta,
    Column('winner_id', INTEGER),
    Column('loser_id', INTEGER),
)

fixtures = Table('fixtures', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('timestamp', DateTime),
    Column('winner_id', Integer),
    Column('loser_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['playee'].drop()
    post_meta.tables['fixtures'].columns['loser_id'].create()
    post_meta.tables['fixtures'].columns['winner_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['playee'].create()
    post_meta.tables['fixtures'].columns['loser_id'].drop()
    post_meta.tables['fixtures'].columns['winner_id'].drop()
