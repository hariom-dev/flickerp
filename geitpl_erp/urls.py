"""geitpl_erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^', include('user.urls', namespace='user')),
	url(r'^', include('dashboard.urls', namespace='dashboard')),
    # url(r'^', include('department.urls', namespace='department')),
    url(r'^', include('opportunity.urls', namespace='opportunity')),
    url(r'^', include('attendance.urls', namespace='attendance')),
    url(r'^', include('contract.urls', namespace='contract')),
    url(r'^', include('service.urls', namespace='service')),
    url(r'^', include('support.urls', namespace='support')),
    url(r'^admin/', admin.site.urls),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
