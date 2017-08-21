from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/patients/(?P<pk>[0-9]+)$',
        views.get_delete_update_patient,
        name='get_delete_update_patient'
    ),
    url(
        r'^api/v1/patients/$',
        views.get_post_patients,
        name='get_post_patients'
    )
]
