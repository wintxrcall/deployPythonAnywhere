from django.shortcuts import render
from payroll_proj.forms import PayrollForm
from django.template import loader
from django.http import HttpResponse
# Create your views here.


def run_payroll(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            context['pay_total'] = context['pay_rate'] * context['hours_worked']
            return render(request, 'result.html', context)
        else:
            return HttpResponse("Invalid Form")
    else:
        template = loader.get_template('input.html')
        return HttpResponse(template.render())
