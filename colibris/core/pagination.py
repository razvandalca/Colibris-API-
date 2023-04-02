from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ColibrisDefaultPaginator(PageNumberPagination):
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'next_page': self.page.next_page_number() if self.page.has_next() else None,
            'previous_page': self.page.previous_page_number() if self.page.has_previous() else None,
            'results': data
        })
