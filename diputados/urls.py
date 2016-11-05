from django.conf.urls import url

from .views import (
    DiputadoList,
    DiputadoDetail,
    DiputadoCreation,
    DiputadoUpdate,
    DiputadoDelete
)


urlpatterns = [
    url(r'^diputados/$', DiputadoList.as_view(), name='list'),
    url(r'^diputados/(?P<pk>\d+)$', DiputadoDetail.as_view(), name='detail'),
    url(r'^diputados/nuevo$', DiputadoCreation.as_view(), name='new'),
    url(r'^diputados/editar/(?P<pk>\d+)$',
        DiputadoUpdate.as_view(), name='edit'),
    url(r'^diputados/borrar/(?P<pk>\d+)$',
        DiputadoDelete.as_view(), name="delete"),
]
