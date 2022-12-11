from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "CCYF Admin"
admin.site.index_title = "Christ Church Youth Fellowship"
admin.site.site_title = "Welcome"

urlpatterns = [
    path('ccyf/admin/', admin.site.urls),
    # path('', include('Accounts.urls')),
    path('', include('Divine.urls')),
    path('dashboard/', include('Dashboard.urls')),
    # path('voting/', include('Voting.urls'))
]


if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
