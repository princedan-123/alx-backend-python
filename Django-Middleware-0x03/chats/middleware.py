from .models import User
from datetime import time, datetime, timedelta
from django.utils import timezone
from django.http import HttpResponseForbidden
from django.core.cache import cache

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        """Implements a logging feature that logs data to a file."""
        user = request.user
        print(f'{datetime.now()} - User: {user} - Path: {request.path}')
        with open('./requests.log', 'w', encoding='utf-8') as file:
            file.write(f'{datetime.now()} - User: {user} - Path: {request.path}')
        return self.get_response(request)

class RestrictAccessByTimeMiddleware:
    """
        A middleware that restricts access to the app during certain hours
        of the day.
    """
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        current_server_time_date = timezone.now()
        current_server_date = current_server_time_date.date()
        nine_pm = datetime.combine(current_server_date, time(21, 0,0))
        six_pm = datetime.combine(current_server_date, time(18,00))
        nine_pm_aware = timezone.make_aware(
            nine_pm, timezone.get_current_timezone()
            )
        six_pm_aware = timezone.make_aware(
            six_pm, timezone.get_current_timezone()
            )
        if current_server_time_date > nine_pm_aware:
            return HttpResponseForbidden(
                '403 forbidden you can only used this app between 6-9pm'
                )
        if current_server_time_date < six_pm_aware:
            return HttpResponseForbidden(
                '403 forbidden you can only used this app between 6-9pm'
                )
        return self.get_response(request)

class RolepermissionMiddleware:
    """A middleware that grants access to only admin users."""
    def __init__(self, get_response):
        """Initializes the middleware class."""
        self.get_response = get_response
    
    def __call__(self, request):
        """Inspects the request object to check the users role."""
        user = request.user
        if user.is_staff or user.is_superuser:
            return self.get_response(request)
        return HttpResponseForbidden('403 Forbidden: you are not admin')

class OffensiveLanguageMiddleware:
    """A middleware that restricts access to users makes execessive request."""
    def __init__(self, get_response):
        """Initializes the middleware."""
        self.get_response = get_response
    
    def __call__(self, request):
        """implements restriction on number of request per minutes."""
        ip_address = request.META.get('REMOTE_ADDR')
        http_method = request.method
        current_time = datetime.now()
        if http_method == 'POST':
            cache_result = cache.get(ip_address)
            if cache_result is None:
                cache_result = []
                cache_result.append(current_time)                
                cache.set(ip_address, cache_result)
                return self.get_response(request)
            number_of_request = len(cache_result)
            elapse_time = min(cache_result) + timedelta(minutes=1)
            maximum_duration = max(cache_result)
            if maximum_duration >= elapse_time and number_of_request >= 5:
                return HttpResponseForbidden('403 FORBIDDEN exceeded 5 request per minute')
            cache_result.append(current_time)
            cache.set(ip_address, cache_result)
        return self.get_response(request)
        