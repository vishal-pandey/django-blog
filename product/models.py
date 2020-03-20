from django.db import models




class Product(models.Model):
	name = models.CharField(blank=False, max_length=50)
	weight = models.CharField(blank=False, max_length=50)
	price = models.IntegerField(blank=False)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.name)
