from django.contrib import admin

# Register your models here.


from .models import Post


class PostModelAdmin(admin.ModelAdmin):
	ca

admin.site.register(Post)