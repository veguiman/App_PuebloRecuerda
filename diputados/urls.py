from django.conf.urls import url

from .views import (
    DiputadoList,
    DiputadoDetail,
    DiputadoCreation,
    DiputadoUpdate,
    DiputadoDelete
)


urlpatterns = [
	url(r'^$', DiputadoList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', DiputadoDetail.as_view(), name='detail'),
	url(r'^nuevo$', DiputadoCreation.as_view(), name='new'),
	url(r'^editar/(?P<pk>\d+)$', DiputadoUpdate.as_view(), name='edit'),
	url(r'^borrar/(?P<pk>\d+)$', DiputadoDelete.as_view(), name="delete"),
]