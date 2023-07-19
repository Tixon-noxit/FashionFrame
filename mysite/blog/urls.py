from django.urls import path
from .views import ZhannaBlog, ShowArticle, SearchResultsArticleView, ShowResultsCategoryView

app_name = "blog"

urlpatterns = [
    path('', ZhannaBlog.as_view(), name='blog'),
    path('article/<slug:article_slug>/', ShowArticle.as_view(), name='article'),
    path('result-search/', SearchResultsArticleView.as_view(), name='search_article'),
    path('category/<slug:category_slug>/', ShowResultsCategoryView.as_view(), name='selected_category'),
]

handler404 = "main.views.page_not_found_view"
