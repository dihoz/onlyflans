from django import forms
from django.forms import ModelForm
from .models import ContactForm

### esta clase hereda de Form pero se personaliza
class ContactFormForm(forms.Form):  
    customer_email = forms.EmailField(label="Correo")
    customer_name = forms.CharField(max_length=64, label= "Nombre") 
    message = forms.CharField(label="Mensaje")

#### esta clase hereda de ModelForm, basta con indicar qué campos se mostrarán
## en la vista se es necesario invocarlo

class Formulario_Contacto(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']