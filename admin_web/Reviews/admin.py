from django.contrib import admin
from .models import Reviews_model


@admin.register(Reviews_model)
class ReviewsAdmin(admin.ModelAdmin):
    pass
