from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(verbose_name="Name", max_length=128)
    calories = models.FloatField(verbose_name="Calories (kcal)", default=0.0)
    total_fat = models.FloatField(verbose_name="Total Fat (g)", default=0.0)
    saturated_fat = models.FloatField(verbose_name="Saturated Fat (g)", default=0.0)
    cholesterol = models.FloatField(verbose_name="Cholesterol (mg)", default=0.0)
    sodium = models.FloatField(verbose_name="Sodium (mg)", default=0.0)
    total_carbohydrate = models.FloatField(verbose_name="Total Carbohydrate (g)", default=0.0)
    dietary_fibre = models.FloatField(verbose_name="Dietary Fibre (g)", default=0.0)
    sugar = models.FloatField(verbose_name="Sugar (g)", default=0.0)
    protein = models.FloatField(verbose_name="Protein (g)", default=0.0)

    def __str__(self):
        return "%s" % self.name

class Meal(models.Model):
	BREAKFAST = 1
	MORNING_SNACK = 2
	LUNCH = 3
	AFTERNOON_SNACK = 4
	DINNER = 5
	EVENING_SNACK = 6

	MEAL_TIME_TYPES = (
		(BREAKFAST, "Breakfast"),
		(MORNING_SNACK, "Morning Snack"),
		(LUNCH, "Lunch"),
		(AFTERNOON_SNACK, "Afternoon Snack"),
		(DINNER, "Dinner"),
		(EVENING_SNACK, "Evening Snack")
	)

	food = models.ForeignKey(Food, verbose_name="Food" , on_delete = models.CASCADE)
	serving_size = models.IntegerField(verbose_name="Serving Size")
	meal_time = models.IntegerField(verbose_name="Meal Time", choices=MEAL_TIME_TYPES)

	def __str__(self):
		return "%s" % self.food

	def get_total_calories(self):
		return self.serving_size * self.food.calories

	def get_total_fat(self):
		return self.serving_size * self.food.total_fat

	def get_saturated_fat(self):
		return self.serving_size * self.food.saturated_fat
	
	def get_cholesterol(self):
		return self.serving_size * self.food.cholesterol

	def get_sodium(self):
		return self.serving_size * self.food.sodium

	def get_total_carbohydrate(self):
		return self.serving_size * self.food.total_carbohydrate

	def get_dietary_fibre(self):
		return self.serving_size * self.food.dietary_fibre

	def get_sugar(self):
		return self.serving_size * self.food.sugar

	def get_protein(self):
		return self.serving_size * self.food.protein