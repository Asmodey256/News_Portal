from django.urls import path
from .views import NewsList, NewsDetail, Search, PostCreateView, PostUpdateView, PostDeleteView, UserDetailView, BaseRegisterView, upgrade_me
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='newsdetail'),
    path('search/', Search.as_view()),
    path('add/', PostCreateView.as_view(), name='add'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='add'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='delete'),
    path('user/', UserDetailView.as_view(), name='news_detail'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', BaseRegisterView.as_view(template_name='signup.html'), name='signup'),
    path('upgrade/', upgrade_me, name='upgrade')
]