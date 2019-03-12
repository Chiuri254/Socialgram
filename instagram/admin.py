from django.contrib import admin
from .models import Profile,Posts,Like,Follow

# Register your models here.
admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(Like)
admin.site.register(Follow)

