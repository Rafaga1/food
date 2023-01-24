insert
into
food_category(category_name, is_publish)
values
('первое', True),
('второе', True)

INSERT
INTO
topping(name)
VALUES('перец'),
('майонез');

insert
into
food(food_name, description, price, is_special, is_vegan, is_publish, category_id)
values
('суп', 'Очень вкусный суп', 100, True, True, True, 1),
('Картошка', 'Жачераня, свежая', 90, True, True, True, 1),
('Мясо', 'Слабой прожарки', 110, True, FALSE, True, 2),
('Шашлык', 'Шашлычек на костре', 150, True, FALSE, True, 2)

insert into topping_food (topping, food)
values (1, 1),
		(2, 1),
		(1, 2)