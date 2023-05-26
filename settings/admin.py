from django.contrib import admin
from .models import Setting, Tours, Days, Photo, Video
# Register your models here.
admin.site.register(Setting)
admin.site.register(Tours)
admin.site.register(Days)
admin.site.register(Photo)
admin.site.register(Video)