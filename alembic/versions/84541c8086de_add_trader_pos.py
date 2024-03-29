"""Add trader pos

Revision ID: 84541c8086de
Revises: a68bb495de52
Create Date: 2024-02-25 02:33:26.801744

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84541c8086de'
down_revision: Union[str, None] = 'a68bb495de52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trader_position',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('trader_id', sa.Integer(), nullable=False),
    sa.Column('x', sa.Float(), nullable=False),
    sa.Column('y', sa.Float(), nullable=False),
    sa.Column('z', sa.Float(), nullable=False),
    sa.Column('x_dir', sa.Float(), nullable=False),
    sa.Column('y_dir', sa.Float(), nullable=False),
    sa.Column('z_dir', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['trader_id'], ['game.trader.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema='game'
    )
    op.create_index(op.f('ix_game_trader_position_id'), 'trader_position', ['id'], unique=False, schema='game')
    op.create_index(op.f('ix_game_trader_position_trader_id'), 'trader_position', ['trader_id'], unique=False, schema='game')
    op.create_table('trader_inventory',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('trader_id', sa.Integer(), nullable=False),
    sa.Column('skin_name', sa.String(), nullable=False),
    sa.Column('vest_id', sa.Integer(), nullable=False),
    sa.Column('backpack_id', sa.Integer(), nullable=False),
    sa.Column('top_id', sa.Integer(), nullable=False),
    sa.Column('belt_id', sa.Integer(), nullable=False),
    sa.Column('legs_id', sa.Integer(), nullable=False),
    sa.Column('head_id', sa.Integer(), nullable=False),
    sa.Column('face_id', sa.Integer(), nullable=False),
    sa.Column('eyes_id', sa.Integer(), nullable=False),
    sa.Column('gloves_id', sa.Integer(), nullable=False),
    sa.Column('feet_id', sa.Integer(), nullable=False),
    sa.Column('armband_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['armband_id'], ['game.items.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['backpack_id'], ['game.items.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['belt_id'], ['game.items.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['eyes_id'], ['game.items.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['face_id'], ['game.items.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['feet_id'], ['game.items.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['gloves_id'], ['game.items.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['head_id'], ['game.items.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['legs_id'], ['game.items.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['top_id'], ['game.items.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['trader_id'], ['game.trader.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['vest_id'], ['game.items.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema='game'
    )
    op.create_index(op.f('ix_game_trader_inventory_id'), 'trader_inventory', ['id'], unique=False, schema='game')
    op.create_index(op.f('ix_game_trader_inventory_trader_id'), 'trader_inventory', ['trader_id'], unique=False, schema='game')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_game_trader_inventory_trader_id'), table_name='trader_inventory', schema='game')
    op.drop_index(op.f('ix_game_trader_inventory_id'), table_name='trader_inventory', schema='game')
    op.drop_table('trader_inventory', schema='game')
    op.drop_index(op.f('ix_game_trader_position_trader_id'), table_name='trader_position', schema='game')
    op.drop_index(op.f('ix_game_trader_position_id'), table_name='trader_position', schema='game')
    op.drop_table('trader_position', schema='game')
    # ### end Alembic commands ###
