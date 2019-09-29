from . import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from ckeditor_uploader import views as ckviews
from django.views.decorators.cache import never_cache
from django.conf.urls import url


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('cycles/', include('cycles.urls')),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('payments/', include('payments.urls')),

    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),

    path('ckeditor/upload/', ckviews.upload, name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(ckviews.browse), name='ckeditor_browse'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'oauth/', include('social_django.urls', namespace='social')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
