from rest_framework.pagination import PageNumberPagination


class Paginator(PageNumberPagination):
    """ Number of objects displayed per page """

    page_size = 20
    page_query_param = 'page_size'
