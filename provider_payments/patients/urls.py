from django.conf.urls import include, url
from django.contrib import admin
import oauth2_provider.views as oauth2_views
from django.conf import settings
from . import views
from .views import ApiEndpoint

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    url(r'^authorize/$', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    url(r'^token/$', oauth2_views.TokenView.as_view(), name="token"),
    url(r'^revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token˓→"), ]
if settings.DEBUG:
# OAuth2 Application Management endpoints
    oauth2_endpoint_views += [
        url(r'^applications/$', oauth2_views.ApplicationList.as_view(), name="list"),
        url(r'^applications/register/$', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        url(r'^applications/(?P<pk>\d+)/$', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        url(r'^applications/(?P<pk>\d+)/delete/$', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        url(r'^applications/(?P<pk>\d+)/update/$', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]
# OAuth2 Token Management endpoints
oauth2_endpoint_views += [
    url(r'^authorized-tokens/$', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
    url(r'^authorized-tokens/(?P<pk>\d+)/delete/$', oauth2_views.AuthorizedTokenDeleteView.as_view(), name="authorized-token-delete"),
]

urlpatterns = [
    url(r'^o/', include(oauth2_endpoint_views, namespace="oauth2_provider")),
    url(r'^api/hello', ApiEndpoint.as_view()), # an example resource endpoint
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
