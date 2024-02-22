from django import forms
from website.models import Publication as pub 

class PubForm(forms.ModelForm):
    class Meta:
        model = pub 
        exclude = ['slug', 'writter', 'view_number']
        
        
