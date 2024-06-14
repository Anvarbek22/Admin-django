from config.views import *
from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePage),
    path('news/',ShopsPage),
    path('news/<int:name>',ShopsBuyPage),
    path("login/add/<str:UN>/<str:PN>/<str:TS>/<str:CM>/<str:P>/<str:M>",loginPage)
    # path('administrator/76435667666574364324343sdjfnaervireugiberuefgyerubrurf3489t394u9hdfueh3487ty3h97f3r/',AdminPage.as_view()),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)