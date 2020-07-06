from django.shortcuts import render
from .form import numForm

def index(request):
  if request.method == 'POST':
    form = numForm(request.POST)
    if form.is_valid():
      a=int(form.cleaned_data['num1'])
      b=int(form.cleaned_data['num2'])
      ans=str(a)+" + "+str(b)+" = "+str(a+b)
  else:
    form=numForm()
    ans=""
  return render(request,'mycalc/index.html',{'form':form, 'ans' : ans})
