from django.forms import ModelForm, TextInput, fields
from .models import Composer
from django.forms.utils import ErrorList

class ComposerForm(ModelForm):
    class Meta:
        model = Composer
        fields = ["lastname", "firstname"]
        widgets = {
            'lastname': TextInput(attrs={ 'class': 'form-control' }),
            'firstname': TextInput(attrs={ 'class': 'form-control' }),
        }
        
class ParagraphErrorList(ErrorList):
    def __str__(self) -> str:
        return self.asDiv()
    
    def asDiv(self):
        if not self:
            return ''
        
        return "<div class='text-danger'>%s</div>" % ''.join(['<p class="small text-danger">%s</p>' % e for e in self])