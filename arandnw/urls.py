from django.urls import path
from .views import NewsList, NewsDetail, Search, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='newsdetail'),
    path('search/', Search.as_view()),
    path('add/', PostCreateView.as_view(), name='add'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='add'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='delete')

]