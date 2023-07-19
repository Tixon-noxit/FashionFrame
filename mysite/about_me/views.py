from django.views.generic import ListView

from main.models import BackgroungImage
from .models import About


class AboutMe(ListView):
    model = About
    template_name = 'about_me/aboutMe.html'
    context_object_name = 'about_me'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Обо мне'
        context['Show_About'] = About.objects.filter(id=1)
        context['backgroung_photo'] = BackgroungImage.objects.filter(id=1).first()
        return context
