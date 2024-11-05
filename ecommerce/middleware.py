from django.utils.deprecation import MiddlewareMixin
from .utils import get_breadcrumb_name

class BreadcrumbMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not hasattr(request, 'breadcrumbs'):
            request.breadcrumbs = []
        
        breadcrumb_name = get_breadcrumb_name(request.path)
        
        # Limpiamos los breadcrumbs anteriores y solo mantenemos el actual
        request.breadcrumbs = [(request.path, breadcrumb_name)]

