from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, Post

class HomeView(View):
	'''Home page'''
	def get(self, request):
		category_list = Category.objects.all()
		posts = Post.objects.all()
		return render(request, 'blog/home.html', {'categories': category_list, 'posts': posts})

	def post(self, request):
		pass

class CategoryView(View):
	'''Вывод статей категории'''
	def get(self, request, slug):
		category = Category.objects.get(slug=slug)
		return render(request, 'blog/post_list.html', {'category': category})
