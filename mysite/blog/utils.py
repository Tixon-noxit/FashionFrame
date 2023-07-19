from blog.models import CategoryBlog
from main.models import BackgroungImage


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['Category_Article'] = CategoryBlog.objects.all()
        context['backgroung_photo'] = BackgroungImage.objects.filter(id=1).first()
        context['heading'] = 'Блог'
        return context
