"""New migration

Revision ID: a59f7e7bef64
Revises: f7ec3eb2871c
Create Date: 2024-06-17 09:29:02.685275

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a59f7e7bef64'
down_revision: Union[str, None] = 'f7ec3eb2871c'
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
