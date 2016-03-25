from django.contrib import admin
from .models import Subject, Course, Module
# Register your models here.

@admin.register(Subject) #this works the same as admin.site.register()
class SubjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug': ('title',)}

class ModuleInline(admin.StackedInline):
	model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['title', 'created']
	list_filter = ['created', 'subject']
	search_fields = ['title', 'overview']
	prepopulated_fields = {'slug': ('title',)}
	inlines = [ModuleInline]