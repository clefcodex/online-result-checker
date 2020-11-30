from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Complain, Course
 
class AccountAdmin(UserAdmin):
	list_display = ('matric_number', 'first_name', 'last_name', 'department', 'study_level', 'academic_session')
	filter_horizontal = ()
	filter_vertical = ('courses',)
	list_filter = ()
	fieldsets = ()


# admin.site.register(Account, AccountAdmin)
admin.site.register(Account)
admin.site.register(Complain)
admin.site.register(Course)
