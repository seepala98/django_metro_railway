from django.conf.urls import url

from booking import views


app_name = 'booking'

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^stationinfo/$', views.stationinfo, name='stationinfo'),
    
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login'),
    url(r'^logout_user/$', views.logout_user, name='logout'),
    url(r'^search/', views.search_results, name='search'),
    url(r'^booking/', views.book_ticket, name='book_ticket'),
    url(r'^ticket/(?P<pk>[0-9]+)/$', views.GetTicket.as_view(), name='get_ticket'),
    url(r'^ticketdetails/(?P<ticket_id>[0-9]+)/$', views.ticketdetails, name='ticketdetails'),
]
