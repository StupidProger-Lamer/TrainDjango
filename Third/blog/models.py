from django.db import models

class Category(models.Model):
	'''Модель категорий'''
	name = models.CharField('Имя', max_length=100)
	slug = models.SlugField('url', max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

class Tag(models.Model):
	'''Модель Тегов'''
	name = models.CharField('Имя', max_length=100)
	slug = models.SlugField('url', max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Тег'
		verbose_name_plural = 'Теги'

class Post(models.Model):
	'''Модель постов'''
	title = models.CharField('Имя', max_length=100)
	mini_text = models.TextField('Мини-текст', max_length=150)
	text = models.TextField('Текст', max_length=2500)
	published = models.DateTimeField('Дата публикации')
	slug = models.SlugField('url', max_length=100)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'

class Comment(models.Model):
	'''Модель комментариев'''
	text = models.TextField('Текст')
	published = models.DateTimeField('Дата публикации')
	moderation = models.BooleanField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'