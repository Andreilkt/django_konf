from django.contrib import admin
from .models import Course, Category

admin.site.site_header = "Заголовок"
admin.site.site_title = "Парапланерный сервис"
admin.site.index_title = "Описание услуг"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')

class CoursesInline(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        # ('Dates', {
        #     'fields': ['title'],
        #     'classes': ['collapse']
        # }
        #  )

    ]

    inlines = [CoursesInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)

