from django.contrib import admin
from ourblog.models import Blog, Blogger, Comment
# Register your models here.

class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = Blog, Blogger, Comment

admin.site.register(Blog, profileAdmin)
admin.site.register(Blogger, profileAdmin)
