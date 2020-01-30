from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.utils import timezone
from django.urls import reverse

class Category(MPTTModel):
	'''Модель категорий'''
	name = models.CharField('Имя', max_length=100)
	slug = models.SlugField('url', max_length=100)
	discription = models.TextField('Описание', max_length=1000, default='', blank=True)
	parent = TreeForeignKey(
		'self',
		verbose_name='Родительская категория',
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		related_name='children'
	)
	template = models.CharField('Шаблон', max_length=500, default='blog/post_list.html')
	published = models.BooleanField('Отображать?', default=True)
	paginated = models.PositiveIntegerField('Количество новостей на странице', default=5)
	sort = models.PositiveIntegerField('Порядок', default=0)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

class Tag(models.Model):
	'''Модель Тегов'''
	name = models.CharField('Имя', max_length=100, unique=True)
	slug = models.SlugField('url', max_length=100, unique=True)
	published = models.BooleanField('Отображать?', default=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Тег'
		verbose_name_plural = 'Теги'

class Post(models.Model):
	'''Модель постов'''
	title = models.CharField('Имя', max_length=100)
	mini_text = models.TextField('Краткое содержание', max_length=150)
	text = models.TextField('Содержание', max_length=2500)
	subtitle = models.CharField('Подзаголовок', max_length=500, blank=True, null=True)
	created = models.DateTimeField('Дата публикации', auto_now_add=True)
	slug = models.SlugField('url', max_length=100, unique=True)
	tags = models.ManyToManyField(Tag, verbose_name='Тег', blank=True, related_name='tag')
	category = models.ForeignKey(
		Category, 
		verbose_name='Категория',
		on_delete=models.CASCADE,
		null=True
	)
	published_date = models.DateTimeField(
		'Дата публикации',
		default=timezone.now,
		blank=True,
		null=True
	)
	edit_date = models.DateTimeField(
		'Дата редактирования',
		default=timezone.now,
		blank=True,
		null=True
	)
	author = models.ForeignKey(
		User, 
		verbose_name='Автор',
		on_delete=models.SET_NULL,
		null=True,
		blank=True
	)
	image = models.ImageField('Главная фотография', upload_to='post/', null=True, blank=True)
	template = models.CharField('Шаблон', max_length=500, default='blog/post_detail.html')
	published = models.BooleanField('Отображать?', default=True)
	viewed = models.PositiveIntegerField('Просмотрено', default=0)
	status = models.BooleanField('Для зарегистрированных', default=False)
	sort = models.PositiveIntegerField('Порядок', default=0)

	def get_tags(self):
		return self.tags.all()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail_post', kwargs={'category': self.category.slug, 'slug': self.slug})

	def get_comments_count(self):
		return self.comments.count()

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'

class Comment(models.Model):
	'''Модель комментариев'''
	text = models.TextField('Текст')
	published = models.DateTimeField('Дата публикации')
	moderation = models.BooleanField()
	post = models.ForeignKey(Post, related_name='comments', verbose_name='Статья', on_delete=models.CASCADE)
	author = models.ForeignKey(
		User, 
		verbose_name='Автор',
		on_delete=models.CASCADE
	)

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'