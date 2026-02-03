from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("", include("blog.urls"), name="blog-urls"),
]