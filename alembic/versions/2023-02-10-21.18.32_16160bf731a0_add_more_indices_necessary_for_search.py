"""add more indices necessary for search

Revision ID: 16160bf731a0
Revises: ff5f73b01a7a
Create Date: 2023-02-10 21:18:32.405130

"""
import sqlalchemy as sa

import mealie.db.migration_types
from alembic import op

# revision identifiers, used by Alembic.
revision = "16160bf731a0"
down_revision = "ff5f73b01a7a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f("ix_recipe_instructions_text"), "recipe_instructions", ["text"], unique=False)
    op.create_index(op.f("ix_recipes_description"), "recipes", ["description"], unique=False)
    op.create_index(op.f("ix_recipes_ingredients_note"), "recipes_ingredients", ["note"], unique=False)
    op.create_index(
        op.f("ix_recipes_ingredients_original_text"), "recipes_ingredients", ["original_text"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_recipes_ingredients_original_text"), table_name="recipes_ingredients")
    op.drop_index(op.f("ix_recipes_ingredients_note"), table_name="recipes_ingredients")
    op.drop_index(op.f("ix_recipes_description"), table_name="recipes")
    op.drop_index(op.f("ix_recipe_instructions_text"), table_name="recipe_instructions")
    # ### end Alembic commands ###
