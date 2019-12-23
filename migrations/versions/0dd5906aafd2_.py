"""empty message

Revision ID: 0dd5906aafd2
Revises: 29097876c7e6
Create Date: 2019-12-22 22:56:14.005273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0dd5906aafd2"
down_revision = "29097876c7e6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("email_validation_messages", sa.Boolean(), nullable=True)
    )
    op.execute(""" UPDATE users SET email_validation_messages  = false """)
    op.alter_column("users", "email_validation_messages", nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "email_validation_messages")
    # ### end Alembic commands ###
