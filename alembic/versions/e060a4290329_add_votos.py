"""add votos

Revision ID: e060a4290329
Revises: e77c9fe0895a
Create Date: 2025-06-11 09:45:19.709843

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'e060a4290329'
down_revision: Union[str, None] = 'e77c9fe0895a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('credenciales', 'tipo_usuario',
               existing_type=mysql.ENUM('Usu', 'Admin'),
               type_=sa.Enum('Usuario', 'Admin', name='tipousuario'),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('credenciales', 'tipo_usuario',
               existing_type=sa.Enum('Usuario', 'Admin', name='tipousuario'),
               type_=mysql.ENUM('Usu', 'Admin'),
               existing_nullable=True)
    # ### end Alembic commands ###
