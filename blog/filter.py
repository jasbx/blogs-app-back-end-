import django_filters
from .models import Blogse
class Oreder(django_filters.FilterSet):
    pass
    class Meta:
        model=Blogse
        fields=['card']