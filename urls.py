from django.conf.urls import include, url
from django.contrib import admin
from QA import views

urlpatterns = [
    # url(r'^$', 'QA_Tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^add', views.add, name='new_user'),
    url(r'^edit', views.edit, name='edit_user'),
    url(r'^save', views.save, name='save_user'),
    url(r'^delete', views.delete, name='delete_user'),
]

