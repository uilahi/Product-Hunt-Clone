from django.contrib import admin
from Python_Django.Product_Hunt_Clone.products import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
