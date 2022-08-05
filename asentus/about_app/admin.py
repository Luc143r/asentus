from django.contrib import admin
from .models import Latest_product, Subscription, About_us, Team, Contact, Feedback

# Register your models here.

admin.site.register(Latest_product)
admin.site.register(Subscription)
admin.site.register(About_us)
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(Feedback)