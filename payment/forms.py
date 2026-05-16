from django import forms
from . models import ShippingAddress

class ShippingForm(forms.ModelForm):
     full_name  = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),required=False)
     email  = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),required=False)
     address1  = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address1'}),required=False)
     address2  = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address2'}),required=False)
     city  = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),required=False)
     state  = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'State'}),required=False)
     zipcode  = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Zipcode'}),required=False)
     country  = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}),required=False)
     
     class Meta:
        model = ShippingAddress
        fields = ['full_name','email','address1','address2','city','state','zipcode','country']
        
        exclude = ['user',]
    
    
class PaymentForm(forms.Form):
    card_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name On Card'}),required=False)
    card_number = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Card Number'}),required=False)
    card_expiry_date = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Expiry Date'}),required=False)
    card_cvv_number = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'CVV'}),required=False)
   #  card_address1 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),required=False)
   #  card_address2 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),required=False)
   #  card_city = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),required=False)
   #  card_state = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),required=False)
   #  card_zipcode = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),required=False)
   #  card_country = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),required=False)
   
       