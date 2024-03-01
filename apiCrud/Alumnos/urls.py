from django.urls import path
from Alumnos import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('facultad/', views.facultadesApi),
    path('facultad/<int:id>/', views.facultadesApi, name='facultad-detail'),

    path('alumno/', views.alumnosApi),
    path('alumno/<int:id>/', views.alumnosApi, name='alumno-detail'),
]
