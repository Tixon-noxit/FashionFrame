from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from main.models import Shooting, Gallery, Category, BackgroungImage

# обработка главной страницы 
class ZhannaIndex(ListView):
    model = Shooting
    extra_context = {'latest': Shooting.objects.all()[:9]}
    template_name = 'main/index.html'
    context_object_name = 'shooting'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Show_Category'] = Category.objects.annotate(
                                            one=Count('shooting')).filter(one__gt=0).values('slug', 'title').distinct()
        context['backgroung_photo'] = BackgroungImage.objects.filter(id=1).first()
        return context

# обработка страницы проекта
class ShowShooting(DetailView):
    model = Shooting
    template_name = 'main/shooting.html'
    slug_url_kwarg = 'shooting_slug'
    context_object_name = 'shooting'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = Shooting.objects.filter(title=self.object).first()
        context['Show_Photo'] = Gallery.objects.filter(shooting_id=self.get_object())
        context['All_Photo'] = Shooting.objects.all()
        return context

# обработка страницы 404
def page_not_found_view(request, exception):
    return render(request, 'main/page_404.html', status=404)
