from django.urls import path
from apps.water.views import (
    ArticleListView,
    ArticleCrateView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    About,
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('create', ArticleCrateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
    path('about', About, name='about'),
]