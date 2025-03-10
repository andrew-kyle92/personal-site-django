from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('send-mail/', views.send_message, name='send-mail'),
    path('', views.index, name='index'),
    path('email/', views.EmailView.as_view(), name='email'),
    path('email/<message_data>/', views.EmailView.as_view(), name='email'),
]

if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
