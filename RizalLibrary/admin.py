from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Location)
admin.site.register(Account)
admin.site.register(Visitor)
admin.site.register(PartnerLibrary)
admin.site.register(AteneoAffiliated)
admin.site.register(NonAteneoAffiliated)
admin.site.register(Event)
admin.site.register(VisitRequest)
admin.site.register(VisitRequestDay)
admin.site.register(Activity)
admin.site.register(AccountVisitRequest)
admin.site.register(LocationVisitRequest)