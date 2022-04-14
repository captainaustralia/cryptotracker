from django.contrib import admin

# Register your models here.
from core.models import User, Portfolio, Coin

admin.site.register(User)
admin.site.register(Portfolio)
admin.site.register(Coin)
