from .models import User
from datetime import datetime

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
