from django import forms
from home.models import CheckoutModel
from home.models import Idea
class checkout(forms.ModelForm):
    class Meta:
        model=CheckoutModel
        fields='__all__'
        labels = {
        "name": "Student Name","title": "Project Title","phno": "Contact Number", "Email": "Email ID"
    }

class IdeaForm(forms.ModelForm):
    class Meta:
        model=Idea
        fields='__all__'
        labels = {
        "name": "Student Name","message": "Message","phno": "Contact Number", "Email": "Email ID", "diagram":"Block Diagram (Optional)"
        }
