"""first migration

Revision ID: caf9b023b4d8
Revises: 
Create Date: 2024-06-18 22:42:26.447890

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'caf9b023b4d8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehiculo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehiculo',
    sa.Column('id', mysql.INTEGER(display_width=20), autoincrement=False, nullable=False),
    sa.Column('marca', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('tipo', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('modelo', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('precio', mysql.DOUBLE(asdecimal=True), server_default=sa.text('0'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
