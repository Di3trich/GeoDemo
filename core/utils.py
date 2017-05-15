from rest_framework.pagination import PageNumberPagination


class PositionSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'size'
    max_page_size = 1000000
