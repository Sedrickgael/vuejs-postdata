from django.contrib import admin

from . import models


class UtilisateurAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'username',
        'password',
        'email',
        'phone',
        'image',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'username',
        'password',
        'email',
        'phone',
        'image',
        'status',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Utilisateur, UtilisateurAdmin)