from django.shortcuts import render
from django.views.generic.base import View
from datetime import datetime

from .models import Category, Post

class HomeView(View):
	'''Home page'''
	def get(self, request):
		category_list = Category.objects.all()
		posts = Post.objects.filter(published=True, published_date__lte=datetime.now())
		return render(request, 'blog/post_list.html', {'categories': category_list, 'posts': posts})

	def post(self, request):
		pass

class PostDetailView(View):
	'''Вывод полной статьи'''
	def get(self, request, category, slug):
		category_list = Category.objects.all()
		post = Post.objects.get(slug=slug)
		return render(request, 'blog/post_detail.html', {'categories': category_list, 'post': post})

class CategoryView(View):
	'''Вывод статей категории'''
	def get(self, request, cat_name):
		category = Category.objects.get(slug=cat_name)
		return render(request, 'blog/post_list.html', {'category': category})
