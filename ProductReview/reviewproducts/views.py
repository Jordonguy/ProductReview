from django.shortcuts import render, redirect
from django.views import generic
from reviewproducts.models import Product
from reviewproducts.models import Review
from reviewproducts.forms import AddProductForm
from reviewproducts.forms import AddReviewForm
# Create your views here.
def index(request):
	products = Product.objects.order_by('-id')

	context = {'products' : products}

	return render(request, 'reviewproducts/index.html', context)

def addproduct(request):
	if request.method == 'POST':
		form = AddProductForm(request.POST)
		if form.is_valid():
			new_product = Product(producttitle=request.POST['producttitle'], productdesc=request.POST['productdesc'], productprice=request.POST['productprice'])
			new_product.save()
			return redirect('index')
	else:
		form = AddProductForm()

	form = AddProductForm()

	context = {'form' : form}

	return render(request, 'reviewproducts/addproduct.html', context)

def addreview(request):
	if request.method == 'POST':
		form = AddReviewForm(request.POST)
		if form.is_valid():
			new_review = Review(productid=request.POST['productid'], reviewtitle=request.POST['reviewtitle'], reviewdesc=request.POST['reviewdesc'], rating=request.POST['rating'])
			new_review.save()
			return redirect('addreview')
	else:
		form = AddReviewForm()

	products = Product.objects.order_by('-id')
	reviews = Review.objects.order_by('-id')
	form = AddReviewForm()

	context = {'reviews' : reviews, 'form' : form, 'products' : products}

	return render(request, 'reviewproducts/addreview.html', context)

class ProductDetailView(generic.DetailView):
	model = Product
	template_name = 'reviewproducts/product.html'

class ReviewDetailView(generic.DetailView):
	model = Review
	templete_name = 'reviewproduct/review.html'
