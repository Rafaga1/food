import sqlalchemy

metadata = sqlalchemy.MetaData()

food_category = sqlalchemy.Table(
    "food_category",
    metadata,
    sqlalchemy.Column("category_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("category_name", sqlalchemy.String(50)),
    sqlalchemy.Column("is_publish", sqlalchemy.Boolean)
)

topping_food = sqlalchemy.Table(
    "topping_food",
    metadata,
    sqlalchemy.Column("topping", sqlalchemy.ForeignKey('topping.id'), primary_key=True),
    sqlalchemy.Column("food", sqlalchemy.ForeignKey('food.food_id'), primary_key=True)
)

topping = sqlalchemy.Table(
    "topping",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(50)),
)



food = sqlalchemy.Table(
    "food",
    metadata,
    sqlalchemy.Column("food_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("category_id", sqlalchemy.ForeignKey(food_category.c.category_id), nullable=True),
    sqlalchemy.Column("food_name", sqlalchemy.String(50)),
    sqlalchemy.Column("description", sqlalchemy.String(100)),
    sqlalchemy.Column("price", sqlalchemy.Float()),
    sqlalchemy.Column("is_special", sqlalchemy.Boolean),
    sqlalchemy.Column("is_vegan", sqlalchemy.Boolean),
    sqlalchemy.Column("is_publish", sqlalchemy.Boolean),
)
