from django.contrib import admin
from tabTrunkApp.models import Tab

class TabAdmin(admin.ModelAdmin):
	fieldsets = [
		('Information',		{'fields':['songTitle','artist', 'tabURL', 'addedDate','ability','content']}),
	]
	
	list_display = ('songTitle','artist', 'addedDate')

admin.site.register(Tab, TabAdmin)




#list_filter = ['pub_date']
#search_fields = ['question']
#date_hierarchy = 'pub_date'
