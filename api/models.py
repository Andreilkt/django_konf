from tastypie.resources import ModelResource
from shop.models import Category, Course


class CategoryResource(ModelResource):
    class meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']




# /api/v1/categories
# /api/v1/courses

