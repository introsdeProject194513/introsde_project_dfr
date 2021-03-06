from django.conf.urls import url
from rest_framework.documentation import include_docs_urls
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'patients', views.PatientList, basename='Patient')
router.register(r'drugs', views.DrugList, basename='Drug')
router.register(r'prescriptions', views.PrescriptionList, basename='Prescription')
router.register(r'patient_diseases', views.PatientDiseaseList, basename='Patient diseases')
router.register(r'measurements', views.MeasurementList, basename='Measurement')
router.register(r'alerts', views.AlertList, basename='Alert')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
