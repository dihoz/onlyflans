from django.contrib import admin
from .models import Flan, ContactForm


#admin.site.register(Flan)
# Register your models here.
@admin.register(Flan)

class FlanAdmin(admin.ModelAdmin):
    list_display = ('name','description','is_private')
    list_display_links = ('name',)
    search_fields = ('name','description')
    list_per_page = 2

@admin.register(ContactForm)
class ContactForm(admin.ModelAdmin):
    list_display = ('customer_email','customer_name')
    list_display_links = ('customer_email',)
    search_fields = ('customer_email',)
    list_per_page = 2