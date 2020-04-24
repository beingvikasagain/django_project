from django.shortcuts import render
from basicformtwo_app.models import AccessRecord,Topic,Webpage
from basicformtwo_app import forms

# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':webpage_list}
    return render(request,'basicformtwo_app/index.html',context=date_dict)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("validation successful!")
            print("name : "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request, 'basicformtwo_app/form.html',{'insert_form':form})
