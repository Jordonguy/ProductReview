from django.db import models
from django.utils import timezone
from django.db.models import F

# Create your models here.
class Product(models.Model):
	producttitle = models.CharField(max_length=20)
	productdesc = models.TextField()
	productprice = models.DecimalField(decimal_places=2,max_digits=6)
	productimage = models.TextField(null=True, blank=True)

	def __str__(self):
		return '<Producttitle: {}, ID: {}>'.format(self.producttitle, self.id)

class Review(models.Model):
	RATING_CHOICES = (
		(1, '1'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5'),
		)
	reviewtitle = models.CharField(max_length=20)
	reviewdesc = models.TextField()
	rating = models.IntegerField(choices=RATING_CHOICES)
	date_added = models.DateTimeField(default=timezone.now)
	productid = models.IntegerField()

	def __str__(self):
		return '<ReviewTitle: {}, ID: {}, Rating: {}, Productid: {}>'.format(self.reviewtitle, self.id, self.rating, self.productid)