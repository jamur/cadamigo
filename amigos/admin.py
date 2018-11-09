from django.contrib import admin

from .models import Telefone, Amigo
# Register your models here.

class FoneInLine(admin.TabularInline):
	model = Telefone
	extra = 1

class AmigoAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 					{'fields': ['nome']}),
		('Data de Nascimento', 	{'fields': ['data_de_nascimento']}),
	]
	inlines = [FoneInLine]
	#list_display = ('nome')
	list_filter = ['data_de_nascimento']
	search_fields = ['nome']

admin.site.register(Amigo, AmigoAdmin)
