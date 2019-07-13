from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_book$', views.add_book),
    url(r'^book_info/(?P<book_id>\d+)$', views.book_info),
    url(r'^authors$', views.authors),
    url(r'^add_author$', views.add_author),
    url(r'^author_info/(?P<author_id>\d+)$', views.author_info),
]
