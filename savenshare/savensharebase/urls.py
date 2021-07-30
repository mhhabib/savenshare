from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import LinkCreateView, FileCreateView, LinkPostCreateView, home, PostDetailView, SelectToShare
from django.conf import settings
from django.conf.urls.static import static
# from .views import MyView

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/l/', LinkCreateView.as_view(), name='create-link'),
    path('create/f/', FileCreateView.as_view(), name='create-file'),
    path('create/p/', LinkPostCreateView.as_view(), name='create-post'),
    path('<str:author>/<int:pk>/', PostDetailView.as_view(), name='details'),
    path('sharelink/', SelectToShare.as_view(), name='sharelinks'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
