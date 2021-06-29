
from django.contrib import admin
from django.urls import path,include
from contact import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contactapi',views.ContacttModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
