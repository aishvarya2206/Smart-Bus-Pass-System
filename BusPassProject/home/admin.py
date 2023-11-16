from django.contrib import admin
from home.models import College , Manager , Route , Student , Pass, AuthUser
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

"""
# Define an inline admin descriptor for AuthUser model
# which acts a bit like a singleton
class AuthUserInline(admin.StackedInline):
    model = AuthUser
    can_delete = False
    verbose_name_plural = "Auth users"
    
# Define a new User admin
class CustomizedUserAdmin(UserAdmin):
    inlines = [AuthUserInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
"""
# Register your models here.
admin.site.register(College)
admin.site.register(Manager)
admin.site.register(Route)
admin.site.register(Student)
admin.site.register(Pass)
admin.site.register(AuthUser)