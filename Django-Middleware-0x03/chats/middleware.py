from .models import User
from datetime import time, datetime
from django.utils import timezone
from django.http import HttpResponseForbidden

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        """Implements a logging feature that logs data to a file."""
        user = request.user
        print(f'{datetime.now()} - User: {user} - Path: {request.path}')
        with open('requests.log', 'w', encoding='utf-8') as file:
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
        six_pm - datetime.combine(current_server_date, time(18,00))
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
