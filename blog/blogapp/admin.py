from django.contrib import admin
from .models import Artigo

# Register your models here.
#admin.site.register(Artigo)
# Abaixo modificamos a forma de vizualizar os objetos do banco de dados no admin
@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ("titulo","slug","autor","data_pub","atualizado")
    # Conforme o titulo é escrito o slug vai sendo preenchido também
    prepopulated_fields = {"slug": ("titulo",)}
    # Precisa da vírgula para ser lida a tupla


