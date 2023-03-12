from django.contrib import admin


class HabitAdmin(admin.ModelAdmin):
    list_display = '__all__'
    search_fields = '__all__'
