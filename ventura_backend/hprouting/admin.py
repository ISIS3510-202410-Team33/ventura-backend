from django.contrib import admin

from .models import University, Building, SiteType, Site, SiteAdjacency

# Register your models here.
admin.site.register(University)
admin.site.register(Building)
admin.site.register(SiteType)
admin.site.register(Site)
admin.site.register(SiteAdjacency)
