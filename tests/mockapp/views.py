from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

from drf_haystack.filters import (
    HaystackFilter,
)
from drf_haystack.mixins import FacetMixin, MoreLikeThisMixin
from drf_haystack.viewsets import HaystackViewSet

from .models import MockPerson
from .serializers import MockPersonFacetSerializer, MoreLikeThisSerializer, SearchSerializer


class BasicPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"


class BasicLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class SearchPersonFacetViewSet(FacetMixin, HaystackViewSet):
    index_models = [MockPerson]
    pagination_class = BasicLimitOffsetPagination
    serializer_class = SearchSerializer
    filter_backends = [HaystackFilter]

    # Faceting
    facet_serializer_class = MockPersonFacetSerializer


class SearchPersonMLTViewSet(MoreLikeThisMixin, HaystackViewSet):
    index_models = [MockPerson]
    serializer_class = MoreLikeThisSerializer
