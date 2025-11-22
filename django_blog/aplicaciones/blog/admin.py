from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion',)
    resource_class = CategoriaResource

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'correo']
    list_display = ('nombres', 'apellidos', 'correo', 'estado', 'fecha_creacion',)
    resource_class = AutorResource

# ----------------------------------------------------
# NUEVA CLASE PARA AÑADIR EL CSS DE CORRECCIÓN
# ----------------------------------------------------
class PostAdmin(admin.ModelAdmin):
    # Puedes añadir aquí opciones de list_display, search_fields, etc., si las necesitas.
    # Por ahora, solo añadimos la clase Media:
    class Media:
        css = {
            # La ruta es relativa a la carpeta 'static' dentro de tu aplicación 'blog'.
            # Django buscará en: aplicaciones/blog/static/admin/css/ckeditor_fix.css
            'all': ('admin/css/ckeditor_fix.css',) 
        }

# ----------------------------------------------------
# ACTUALIZACIÓN DEL REGISTRO
# ----------------------------------------------------
# admin.site.register(Post) # <-- ELIMINA ESTA LÍNEA (línea 26)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
# Reemplaza el registro simple por el que usa tu nueva clase PostAdmin
admin.site.register(Post, PostAdmin)