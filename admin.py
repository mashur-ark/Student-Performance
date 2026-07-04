from django.contrib import admin
from .models import Dataset


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'dataset_name',
        'uploaded_at',
    )

    search_fields = (
        'dataset_name',
    )

    list_filter = (
        'uploaded_at',
    )