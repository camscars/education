from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class Subject(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		ordering = ('title',)

	def __str__(self):
		return self.title

class Course(models.Model):
	title = models.CharField(max_length=250)
	owner = models.ForeignKey(User, related_name='courses_created')
	subject = models.ForeignKey(Subject, related_name='courses')
	slug= models.SlugField(max_length=200, unique=True)
	overview = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.title

class Module(models.Model):
	course = models.ForeignKey(Course, related_name='modules')
	title = models.CharField(max_length=250)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.title

class Content(models.Model):  
	model = models.ForeignKey(Module, related_name='contents')
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	item = GenericForeignKey('content_type', 'object_id')

class ItemBase(models.Model): #class to allow site to store diverse content for courses: text, files, pictures, etc
	owner = models.ForeignKey(User, related_name='%(class)s_related')
	title = models.CharField(max_length=250)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta: #abstract class, wont make its own table but all subclasses will
		abstract = True

	def __str__(self):
		return self.title

class Text(ItemBase):
	content = models.TextField()

class File(ItemBase):
	file = models.FileField(upload_to='files')

class Image(ItemBase):
	file = models.FileField(upload_to='images')

class Video(ItemBase):
	url = models.URLField()
	
