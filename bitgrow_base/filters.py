"""

Time: :2023/10/14 12:50:33

Function: Base Filter

"""

from django_filters import rest_framework as drf_filters

from . import models


class OrderFilter(drf_filters.FilterSet):
    kol_name = drf_filters.CharFilter(
        field_name='kol__name', lookup_expr='iexact')
    kol_address = drf_filters.CharFilter(
        field_name='kol__address', lookup_expr='iexact')

    # fans_requirement, area track

    class Meta:
        model = models.Order
        fields = ['order_id', 'task_id', 'kol',
                  'kol_name', 'kol_address', 'status']


class TaskFilter(drf_filters.FilterSet):
    project = drf_filters.CharFilter(
        field_name='project__name', lookup_expr='iexact'
    )

    class Meta:
        model = models.Task
        fields = ['project']


class KOLFilter(drf_filters.FilterSet):
    fans_gt = drf_filters.RangeFilter(
        field_name='connectable_user',
        lookup_expr='gt'
    )

    class Meta:
        model = models.KOL
        fields = ['portrait', 'language', 'area', 'address', 'fans_gt']
