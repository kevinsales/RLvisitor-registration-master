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
    # for event upload
    path('event_upload/', views.event_upload, name='event_upload'),
    # template for visitor input
    path('empty_visitors_input/', views.empty_visitors_input, name='empty_visitors_input'),


    # for librarians
    # for template for librarian
    path('empty_librarian/', views.empty_librarian, name='empty_librarian'),
    # for checking visitor requests
    path('librarian_check_request/', views.librarian_check_request, name='librarian_check_request'),
    path('approve_visitor/<int:pk>/', views.approve_visitor, name='approve_visitor'),
    path('reject_visitor/<int:pk>/', views.reject_visitor, name='reject_visitor'),
    # dashboard
    path('librarian_dashboard/', views.librarian_dashboard, name='librarian_dashboard'),
    # visitor record
    path('librarian_visitor_record/', views.librarian_visitor_record, name='librarian_visitor_record'),
    # event record
    path('librarian_event_record/', views.librarian_event_record, name='librarian_event_record'),
    # for detecting qr code
    path('qrtest/', views.qrtest, name='qrtest'),

    # old code dont use this
    path('visitors', views.visitors, name='visitors'),

    # for login
    # path('login/', views.login, name='login'),
    # /login to login
    # /logout to logout 
    path('', include('django.contrib.auth.urls')),
    
    # edit visitor
    path('edit_visitor/<int:pk>/', views.edit_visitor, name='edit_visitor'),

    # for admin
    path('adminDashboard/', views.adminDashboard, name='adminDashboard'),
    # create user
    path('create_user/', views.create_user, name='create_user'),


]
# + STATIC_ROOT = os.path.join(BASE_DIR, 'static')
