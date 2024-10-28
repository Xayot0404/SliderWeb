from django.urls import include, path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',Web_DesignView,name="WebDesign"),
    path('all_designs/', all_web_designs, name='all_web_designs'),
    path('open_pptx/<int:slide_id>/', open_pptx, name='open_pptx'),
    path('designs2/', design2_list, name='design2_list'),
    path('designs3/', design3_list, name='design3_list'),
    path('designs4/', design4_list, name='design4_list'),
    path('designs5/', design5_list, name='design5_list'),
    path('designs6/', design6_list, name='design6_list'),
    path('upload/', presentation_upload, name='presentation_upload'),
    path('presentations/', presentation_list, name='presentation_list'),
    path('view/<int:presentation_id>/', presentation_view, name='presentation_view'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)