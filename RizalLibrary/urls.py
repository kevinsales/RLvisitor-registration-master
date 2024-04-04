"""BADproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

# for css
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # for visitor input
    path('', views.visitor_start_page, name='visitor_start_page'),
    # first page for visitor input
    path('upload_visitor_info/', views.upload_visitor_info, name='upload_visitor_info'),
    # second pages for visitor input
    path('partner_library/', views.partner_library_page, name='partner_library_page'),
    path('non_ateneo_affiliated/', views.non_ateneo_affiliated_page, name='non_ateneo_affiliated_page'),
    path('ateneo_affiliated/', views.ateneo_affiliated_page, name='ateneo_affiliated_page'),
    # third page for visitor input
    path('visitor_activities/', views.visitor_activities, name='visitor_activities'),
    # forth page for visitor input
    path('visitor_upload_success/', views.visitor_upload_success, name='visitor_upload_success'),
    # template for visitor input
    path('empty_visitors_input/', views.empty_visitors_input, name='empty_visitors_input'),

    # for event upload
    path('event_upload/', views.event_upload, name='event_upload'),


    # for librarians
    path('visitors/', views.visitors, name='visitors'),
    # for detecting qr code
    path('qrtest/', views.qrtest, name='qrtest')
]
# + STATIC_ROOT = os.path.join(BASE_DIR, 'static')
