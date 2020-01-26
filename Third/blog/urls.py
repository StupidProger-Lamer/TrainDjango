from django.urls import path

from . import views

urlpatterns = [
	path('', views.HomeView.as_view()),
	path('<slug:cat_name>/', views.CategoryView.as_view(), name='category'),
	path('<slug:category>/<slug:slug>/', views.PostDetailView.as_view(), name='detail_post')
]

