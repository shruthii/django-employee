from django import forms
from EmpDetails.models import EmpDetailsModel

class EmpDetailsForm(forms.ModelForm):

   GENDER_CHOICES = ('Male', 'Female')
   class Meta():
       model = EmpDetailsModel
       fields = ('EmployeeId','FullName', 'DOB', 'PermanentAddress', 'Dateofjoining', 'Designation', 'Department', 'EmailId', 'Gender', 'Phonenumber', 'Status')

       widgets={
            'EmployeeId': forms.TextInput(attrs={'class':'textinputclass', 'type':'number'}),
            'FullName': forms.TextInput(attrs={'class':'textinputclass'}),
            'DOB': forms.DateInput(format='%d/%m/%Y', attrs={'type':'date'}),
            'PermanentAddress': forms.TextInput(attrs={'class':'textinputclass'}),
            'Dateofjoining': forms.DateInput(format='%d/%m/%Y', attrs={'type':'date'}),
            'Designation': forms.TextInput(attrs={'class':'textinputclass'}),
            'EmailId': forms.TextInput(attrs={'class':'textinputclass'}),
            'Gender': forms.TextInput(attrs={'class':'textinputclass'}),
            'Phonenumber': forms.TextInput(attrs={'class':'textinputclass'}),
            'Status': forms.TextInput(attrs={'class':'textinputclass'}),
       }
