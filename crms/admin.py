from django.contrib import admin
from .models import User,Customer,Address,Regcenter,DeathReg


# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Regcenter)
admin.site.register(DeathReg)
