from django.contrib import admin
from django.urls import include, path  # Ensure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),
]