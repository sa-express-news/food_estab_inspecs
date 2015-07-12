from django import forms 

class SearchForm(forms.ModelForm):
    search_query = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'search-form'}))