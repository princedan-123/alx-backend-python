from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class delete_user(viewsets.ViewSet):
    def destroy(self, request, pk=None):
        """Deletes a user by id"""
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(
                {'deleted': f'user with id {pk} deleted successfully'},
                status=status.HTTP_204_NO_CONTENT
                )
        except User.DoesNotExist:
            return Response(
                {'Error': f'User with id {pk} not found'},
                status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            return Response(
                {'An error occured': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
