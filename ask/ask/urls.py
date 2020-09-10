"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from django.views.defaults import page_not_found
from .views import page_test

urlpatterns = [
	path('/', page_test),
	path('login/', page_test),
	path('signup/', page_test),
	path('question/', include('qa.urls')),
	path('ask/', page_test),
	path('popular/', page_test),
	path('new/', page_test),
]
