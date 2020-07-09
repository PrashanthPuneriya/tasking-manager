"""empty message

Revision ID: 46626c2a76cf
Revises: 5053c01cb170
Create Date: 2020-07-07 18:53:18.637148

"""
from alembic import op
import geoalchemy2


# revision identifiers, used by Alembic.
revision = "46626c2a76cf"
down_revision = "5053c01cb170"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "projects",
        "geometry",
        existing_type=geoalchemy2.types.Geometry(
            geometry_type="MULTIPOLYGON",
            srid=4326,
            from_text="ST_GeomFromEWKT",
            name="geometry",
        ),
        nullable=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "projects",
        "geometry",
        existing_type=geoalchemy2.types.Geometry(
            geometry_type="MULTIPOLYGON",
            srid=4326,
            from_text="ST_GeomFromEWKT",
            name="geometry",
        ),
        nullable=True,
    )
    # ### end Alembic commands ###
