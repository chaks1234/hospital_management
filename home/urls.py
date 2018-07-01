from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
	url(r'^$',views.IndexView.as_view(), name = 'index'),

	url(r'^patient/$',views.Patient_view.as_view(), name = 'patient'),

	url(r'^register/$',views.PatientCreate.as_view(), name = 'patient-add'),

	url(r'^(?P<pk>[0-9]+)/$',views.PatientView.as_view(), name = 'signup'),


	url(r'doctor/add/$',views.DoctorCreate.as_view(),name= 'doctor-add'),


	#update user
	url(r'doctor/(?P<pk>[0-9]+)/$', views.DoctorUpdate.as_view(), name='doctor-update'),

	#delete user
	url(r'doctor/delete/(?P<pk>[0-9]+)/$', views.DoctorDelete.as_view(), name='doctor-delete'),

	url(r'patient/delete/(?P<pk>[0-9]+)/$', views.PatientDelete.as_view(), name='patient-delete'),
	]
