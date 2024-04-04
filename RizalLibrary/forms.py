from django import forms
from .models import *

class VisitorForm(forms.ModelForm):
    error_css_class= 'error-field'
    required_css_class= 'required-field'
    
    class Meta:
        model = Visitor
        fields = ['lastName', 'firstName', 'middleName', 'visitorEmail', 'idNumber', 'affiliation', 'visitorType']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   

        # add this for apply css class in form
        for field in self.fields:
            css_format ={
            'class':"form-control",
            'placeholder' :"Type Here",
            # 'id':"name", 
            }
            if field == 'visitorType':
                css_format ={
                'class':"selectpicker bg-white border border-1 rounded mb-4",
                'title' :"select visitor type",
                'data-width' :"100%"
                # 'id':"name", 
                }
            self.fields[field].widget.attrs.update(
                css_format
            )

class PartnerLibraryForm(forms.ModelForm):

    class Meta:
        model = PartnerLibrary
        fields = ['plVisitorID','librarianName', 'requestorName', 'requestorEmail', 'representativeName', 'representativeEmail', 'representativeID']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        
        for field in self.fields:
            css_format ={
            'class':"form-control",
            'placeholder' :"Type Here",
            # 'id':"name", 
            }
            if field == 'visitorType':
                css_format ={
                'class':"selectpicker bg-white border border-1 rounded mb-4",
                'title' :"select visitor type",
                'data-width' :"100%"
                # 'id':"name", 
                }
            self.fields[field].widget.attrs.update(
                css_format
            )

class AteneoAffiliatedForm(forms.ModelForm):
    class Meta:
        model = AteneoAffiliated
        fields = ['aaType', 'aaYear', 'aaIDPhoto', 'aaCourse', 'aaLastSem', 'aaPaymentConfirmation']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   

    # add this for apply css class in form
        for field in self.fields:
            css_format ={
            'class':"form-control",
            'placeholder' :"Type Here",
            # 'id':"name", 
            }
            if field == 'aaType':
                css_format ={
                'class':"selectpicker bg-white border border-1 rounded mb-4",
                'title' :"select visitor type",
                'data-width' :"100%"
                # 'id':"name", 
                }
            self.fields[field].widget.attrs.update(
                css_format
            )



class NonAteneoAffiliatedForm(forms.ModelForm):
    class Meta:
        model = NonAteneoAffiliated
        fields = ['naaType', 'naaCompanions', 'naaInvitation', 'naaPaymentConfirmation']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   

        # add this for apply css class in form
        for field in self.fields:
            css_format ={
            'class':"form-control",
            'placeholder' :"Type Here",
            # 'id':"name", 
            }
            if field == 'naaType':
                css_format ={
                'class':"selectpicker bg-white border border-1 rounded mb-4",
                'title' :"select visitor type",
                'data-width' :"100%"
                # 'id':"name", 
                }
            self.fields[field].widget.attrs.update(
                css_format
            )

