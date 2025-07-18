from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date", "email", "phone", "birth_date", "gender")
  
admin.site.register(Member, MemberAdmin)

# Register your models here.
