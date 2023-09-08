from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    
    
    
class Add_new_section_choicesForm(forms.Form):
    new_choice = forms.CharField(max_length=50, label='نام رشته جدید : ')