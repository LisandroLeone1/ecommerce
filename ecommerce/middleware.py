from django.utils.deprecation import MiddlewareMixin
from .utils import get_breadcrumb_name

class BreadcrumbMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not hasattr(request, 'breadcrumbs'):
            request.breadcrumbs = [('/', 'Inicio')]  # Iniciar con 'Inicio'

        # Obtener el nombre del breadcrumb actual para la URL
        breadcrumb_name = get_breadcrumb_name(request.path)
        
        # Si la URL no está en la lista de breadcrumbs, agregarla
        if request.path not in [path for path, name in request.breadcrumbs]:
            request.breadcrumbs.append((request.path, breadcrumb_name))


