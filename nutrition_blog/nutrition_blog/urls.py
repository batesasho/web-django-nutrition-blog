from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('nutrition_blog.web.urls')),
        path('accounts/', include('nutrition_blog.accounts.urls')),
        path('email/', include('nutrition_blog.email_client.urls')),


]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
