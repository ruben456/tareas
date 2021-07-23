from rest_framework import permissions

class IsUserOrReadOnly(permissions.BasePermission):
    """ Clase para el control de permisos sobre los objetos Task """
    def has_object_permission(self, request, view, obj):
        """ Valida que el usuario este relacionado con el objeto para poder editarlo """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user