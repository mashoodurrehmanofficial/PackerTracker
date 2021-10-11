
from django.urls import path
from .views import *
from .views2 import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [ 
    path('', index, name='index'),    
    path('delete/<str:barcode>', delete, name='delete'),    
    path('remove_specific_warning/<str:barcode>', remove_specific_warning, name='remove_specific_warning'),  


    path('upload', upload, name='upload'),    
    path('update', update, name='update'),    
    path('remove_warnings', remove_warnings, name='remove_warnings'),    
    path('generate_latest_report', generate_latest_report, name='generate_latest_report'),    
    path('reset_records', reset_records, name='reset_records'),    
    path('delete_all', delete_all, name='delete_all'),    
    
    
    
    path('charts', charts, name='charts'),    
    path('get_new_data', get_new_data, name='get_new_data'),    
    
    
    
    path('login', login_page, name='login_page'),    
    path('logout', logout_page, name='logout_page'),    
    
    
    
    
    path('reports_dir', reports_dir, name='reports_dir'),    
    path('reports_dir/download/<str:file_name>', report_dir_download, name='report_dir_download'),    
    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

