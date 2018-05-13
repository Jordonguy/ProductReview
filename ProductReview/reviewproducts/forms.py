from django import forms
from reviewproducts.models import Review
from reviewproducts.models import Product

class AddProductForm(forms.Form):
	producttitle = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Product Title'}))
	productdesc = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Enter Product Description'}))
	productprice = forms.DecimalField(decimal_places=2,max_digits=6, widget=forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Product Price'}))

class AddReviewForm(forms.Form):
	productid = forms.ChoiceField(choices=[(product.pk, product) for product in Product.objects.all()], widget=forms.Select(attrs={'class' : 'form-control'}))
	reviewtitle = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Review Title'}))
	reviewdesc = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Enter Review Description'}))
	rating = forms.ChoiceField(widget=forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'Select a rating'}), choices=Review.RATING_CHOICES)
	