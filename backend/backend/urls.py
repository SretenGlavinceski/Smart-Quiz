from django.contrib import admin
from django.urls import path
from application.views import get_sections, get_questions_by_section
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sections/', get_sections),
    path('api/sections/<int:section_id>/questions/', get_questions_by_section),
]
