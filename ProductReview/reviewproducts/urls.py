from django.urls import path
from django.conf.urls import url
from reviewproducts import views
from . import views


urlpatterns = [
	path('', views.index, name='index'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('addreview/', views.addreview, name='addreview'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProductDetailView.as_view(), name='product'),
    ]