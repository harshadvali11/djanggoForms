from django import forms
g=[['MALE','Male'],['FEMALE','Female']]
c=[['Django','DJANGO'],['python','PYTHON'],['sql','SQL']]
class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    #age=forms.IntegerField(max_value=80,min_value=18)
    #email=forms.EmailField(max_length=100)
    #url=forms.URLField()
    #date=forms.DateField()
    #date1=forms.DateTimeField()
    #time=forms.TimeField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())
    address=forms.CharField(max_length=200,widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    gender=forms.ChoiceField(choices=g)
    course=forms.MultipleChoiceField(choices=c)
    gender2=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course2=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple())


