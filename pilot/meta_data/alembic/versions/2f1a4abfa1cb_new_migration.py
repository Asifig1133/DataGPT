"""New migration

Revision ID: 2f1a4abfa1cb
Revises: b70cf2b9906e
Create Date: 2024-05-23 13:35:16.167546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f1a4abfa1cb'
down_revision: Union[str, None] = 'b70cf2b9906e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###