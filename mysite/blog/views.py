from django.views.generic import DetailView, ListView
from .models import Article
from django.db.models import Q
from .utils import *


class ZhannaBlog(DataMixin, ListView):
    model = Article
    extra_context = {'latest': Article.objects.all()[:9]}
    template_name = 'blog/blog.html'
    context_object_name = 'blog'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context()
        context['Article_All'] = Article.objects.order_by('-time_create')[:3]
        return dict(list(context.items()) + list(mixin.items()))


class SearchResultsArticleView(DataMixin, ListView):
    paginate_by = 2
    model = Article
    template_name = 'blog/search_results.html'
    context_object_name = 'search_article'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Article.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(short_description__icontains=query)
        )
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context()
        context['Article_All'] = Article.objects.order_by('-time_create')[:3]
        return dict(list(context.items()) + list(mixin.items()))


class ShowResultsCategoryView(DataMixin, ListView):
    model = Article
    template_name = 'blog/selected_category.html'
    context_object_name = 'selected_category'
    slug_url_kwarg = 'category_slug'

    def get_queryset(self):  # новый
        object_list = Article.objects.filter(category__slug__icontains=self.kwargs['category_slug'])
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context()
        context['Article_All'] = Article.objects.all()
        return dict(list(context.items()) + list(mixin.items()))


class ShowArticle(DetailView):
    model = Article
    template_name = 'blog/article.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = Article.objects.filter(title=self.object).first()
        context['Show_Article'] = Article.objects.filter(title=self.get_object())
        return context
