"""Custom paginations are defined here."""
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomizedPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 50,

    def get_paginated_response(self, data):
        """Customizes paginated json response output."""
        pagination_meta_data = {
            'current_page_number' : self.page.number,
            'paginator_count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'next': self.get_next_link(),
            'previous': self.get_previous_link()
        }
        return Response(
            {
                'meta': pagination_meta_data,
                'data': data
            }
        )
