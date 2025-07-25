"""Custom paginations are defined here."""
from rest_framework.paginations import PageNumberPagination

class CustomizedPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 50
