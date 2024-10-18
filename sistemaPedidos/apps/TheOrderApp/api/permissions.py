from rest_framework.permissions import BasePermission

class Mipermiso (BasePermission):
    def has_object_permission(self, request, view):
        if request.method == 'GET':
            return True
        else: 
            return request.user.is_staff
       