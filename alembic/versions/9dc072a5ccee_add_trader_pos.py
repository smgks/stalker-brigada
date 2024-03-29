"""Add trader pos

Revision ID: 9dc072a5ccee
Revises: 84541c8086de
Create Date: 2024-02-25 02:55:08.024961

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9dc072a5ccee'
down_revision: Union[str, None] = '84541c8086de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('trader_inventory', 'vest_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='game')
    op.alter_column('trader_inventory', 'backpack_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='game')
    op.alter_column('trader_inventory', 'top_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='game')
    op.alter_column('trader_inventory', 'belt_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='game')
    op.alter_column('trader_inventory', 'legs_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='game')
    op.alter_column('trader_inventory', 'head_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='game')
    op.alter_column('trader_inventory', 'face_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='game')
    op.alter_column('trader_inventory', 'eyes_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='game')
    op.alter_column('trader_inventory', 'gloves_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='game')
    op.alter_column('trader_inventory', 'feet_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='game')
    op.alter_column('trader_inventory', 'armband_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='game')
    op.drop_constraint('trader_inventory_armband_id_fkey', 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint('trader_inventory_backpack_id_fkey', 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint('trader_inventory_face_id_fkey', 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint('trader_inventory_feet_id_fkey', 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint('trader_inventory_legs_id_fkey', 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint('trader_inventory_vest_id_fkey', 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint('trader_inventory_belt_id_fkey', 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint('trader_inventory_head_id_fkey', 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint('trader_inventory_top_id_fkey', 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint('trader_inventory_gloves_id_fkey', 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint('trader_inventory_eyes_id_fkey', 'trader_inventory', schema='game', type_='foreignkey')
    op.create_foreign_key(None, 'trader_inventory', 'items', ['gloves_id'], ['id'], source_schema='game', referent_schema='game', ondelete='SET NULL')
    op.create_foreign_key(None, 'trader_inventory', 'items', ['feet_id'], ['id'], source_schema='game', referent_schema='game', ondelete='SET NULL')
    op.create_foreign_key(None, 'trader_inventory', 'items', ['belt_id'], ['id'], source_schema='game', referent_schema='game', ondelete='SET NULL')
    op.create_foreign_key(None, 'trader_inventory', 'items', ['top_id'], ['id'], source_schema='game', referent_schema='game', ondelete='SET NULL')
    op.create_foreign_key(None, 'trader_inventory', 'items', ['head_id'], ['id'], source_schema='game', referent_schema='game', ondelete='SET NULL')
    op.create_foreign_key(None, 'trader_inventory', 'items', ['armband_id'], ['id'], source_schema='game', referent_schema='game', ondelete='SET NULL')
    op.create_foreign_key(None, 'trader_inventory', 'items', ['vest_id'], ['id'], source_schema='game', referent_schema='game', ondelete='SET NULL')
    op.create_foreign_key(None, 'trader_inventory', 'items', ['backpack_id'], ['id'], source_schema='game', referent_schema='game', ondelete='SET NULL')
    op.create_foreign_key(None, 'trader_inventory', 'items', ['eyes_id'], ['id'], source_schema='game', referent_schema='game', ondelete='SET NULL')
    op.create_foreign_key(None, 'trader_inventory', 'items', ['legs_id'], ['id'], source_schema='game', referent_schema='game', ondelete='SET NULL')
    op.create_foreign_key(None, 'trader_inventory', 'items', ['face_id'], ['id'], source_schema='game', referent_schema='game', ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint(None, 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint(None, 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint(None, 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint(None, 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint(None, 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint(None, 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint(None, 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint(None, 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint(None, 'trader_inventory', schema='game', type_='foreignkey')
    op.drop_constraint(None, 'trader_inventory', schema='game', type_='foreignkey')
    op.create_foreign_key('trader_inventory_eyes_id_fkey', 'trader_inventory', 'items', ['eyes_id'], ['id'], source_schema='game', referent_schema='game', ondelete='CASCADE')
    op.create_foreign_key('trader_inventory_gloves_id_fkey', 'trader_inventory', 'items', ['gloves_id'], ['id'], source_schema='game', referent_schema='game', ondelete='CASCADE')
    op.create_foreign_key('trader_inventory_top_id_fkey', 'trader_inventory', 'items', ['top_id'], ['id'], source_schema='game', referent_schema='game', ondelete='CASCADE')
    op.create_foreign_key('trader_inventory_head_id_fkey', 'trader_inventory', 'items', ['head_id'], ['id'], source_schema='game', referent_schema='game', ondelete='CASCADE')
    op.create_foreign_key('trader_inventory_belt_id_fkey', 'trader_inventory', 'items', ['belt_id'], ['id'], source_schema='game', referent_schema='game', ondelete='CASCADE')
    op.create_foreign_key('trader_inventory_vest_id_fkey', 'trader_inventory', 'items', ['vest_id'], ['id'], source_schema='game', referent_schema='game', ondelete='CASCADE')
    op.create_foreign_key('trader_inventory_legs_id_fkey', 'trader_inventory', 'items', ['legs_id'], ['id'], source_schema='game', referent_schema='game', ondelete='CASCADE')
    op.create_foreign_key('trader_inventory_feet_id_fkey', 'trader_inventory', 'items', ['feet_id'], ['id'], source_schema='game', referent_schema='game', ondelete='CASCADE')
    op.create_foreign_key('trader_inventory_face_id_fkey', 'trader_inventory', 'items', ['face_id'], ['id'], source_schema='game', referent_schema='game', ondelete='CASCADE')
    op.create_foreign_key('trader_inventory_backpack_id_fkey', 'trader_inventory', 'items', ['backpack_id'], ['id'], source_schema='game', referent_schema='game', ondelete='CASCADE')
    op.create_foreign_key('trader_inventory_armband_id_fkey', 'trader_inventory', 'items', ['armband_id'], ['id'], source_schema='game', referent_schema='game', ondelete='CASCADE')
    op.alter_column('trader_inventory', 'armband_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='game')
    op.alter_column('trader_inventory', 'feet_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='game')
    op.alter_column('trader_inventory', 'gloves_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='game')
    op.alter_column('trader_inventory', 'eyes_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='game')
    op.alter_column('trader_inventory', 'face_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='game')
    op.alter_column('trader_inventory', 'head_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='game')
    op.alter_column('trader_inventory', 'legs_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='game')
    op.alter_column('trader_inventory', 'belt_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='game')
    op.alter_column('trader_inventory', 'top_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='game')
    op.alter_column('trader_inventory', 'backpack_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='game')
    op.alter_column('trader_inventory', 'vest_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='game')
    # ### end Alembic commands ###
