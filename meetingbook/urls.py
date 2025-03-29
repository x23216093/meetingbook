from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
 path('meetingbook/<int:id>', views.meetingdetails, name="meetingdetails"),
 path('meetingbook/addmeeting', views.addmeeting, name="addmeeting"),
 path('meetingbook/<int:id>/updatemeeting', views.updatemeeting, name="updatemeeting"),
 path('meetingbook/<int:id>/deletemeeting', views.deletemeeting, name="deletemeeting"),
 
 
 ]