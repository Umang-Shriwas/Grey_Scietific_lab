from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser,MultiToken


# class CustomUserAdmin(BaseUserAdmin):
#     model = CustomUser
#     list_display = ["email" , "name","user_type","is_active", ] 
#     search_fields = ["email", "name",]
   
#     fieldsets = (
#         ('User Details', {'fields': ('email','password')}),
#         ('Personal Details', {'fields': ('name', 'user_type')}),
#         ('Permission Info', {
#             'classes': ('wide',),
#             'fields': ('is_staff', 'is_active', 'is_superuser','groups', 'user_permissions', 'date_joined',)}
#         )
#     )
    
#     add_fieldsets = (
#         ('Personal Info', {
#             'classes': ('wide',),
#             'fields': ('email', 'name', 'password1', 'password2')}
#         ),
#     )
#     ordering = ('email',)
#     filter_horizontal = ['groups', 'user_permissions']


admin.site.unregister(Group)
# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(MultiToken)

admin.site.register(CustomUser)
