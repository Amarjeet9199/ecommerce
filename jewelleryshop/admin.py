from multiprocessing.connection import Client
from django.contrib import admin
from .models import *

admin.site.register(Carausal)
admin.site.register(Shop)
admin.site.register(About)
admin.site.register(Offer)
admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(Contact)
admin.site.register(Shopcat)
admin.site.register(Item)
admin.site.register(OrderItem)
