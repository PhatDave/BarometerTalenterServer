from django.urls import include, path

urlpatterns = [
	path('', include('BarometerTalenter.urls', namespace='talenter')),
]
