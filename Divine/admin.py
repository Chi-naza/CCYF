from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Activity, UserBirthday, Comment, Ebook, HomeData, GrowthMaterial, Gallery, AnonymousMessage
from django.contrib.auth.models import User

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'first_name', 'last_name']
       
# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUser)
admin.site.register(UserBirthday)
admin.site.register(HomeData)
admin.site.register(Activity)
admin.site.register(Comment)
admin.site.register(Ebook)
admin.site.register(GrowthMaterial)
admin.site.register(Gallery)
admin.site.register(AnonymousMessage)


