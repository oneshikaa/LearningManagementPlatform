from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

app_name='certificates'
urlpatterns = [
    path('certificates/', views.certificate_list, name='certificate_list'),
    path('certificates/add/', views.add_certificate, name='add_certificate'),
    path('certificates/delete/<int:certificate_id>/', views.delete_certificate, name='delete_certificate'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)