from django.conf.urls import url
from main import views


urlpatterns = [
    url(r'^$', views.BookList.as_view(), name='book_list'),
    url(r'^new$', views.BookCreate.as_view(), name='book_new'),
    url(r'^seach/$', views.ESearchView.as_view(), name='search'),
    url(r'^edit/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
    url(r'^(?P<slug>[-\w]+)/$', views.BookDetailView.as_view(), name='book_detail')
]
