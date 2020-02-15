from django.shortcuts import render
from .models import testtable

# Create your views here.


def index(request):
    records = testtable.objects.all()
    print(repr(records))
    if request.method == 'POST':
        recordid = request.POST.get('id')
        if not recordid.isnumeric(): 
            return render(request, 'psql01\index.html', {'records': records,'error_message': "id must be a number!",})
        recordname = request.POST.get('name')
        recordpath = request.POST.get('path')
        record = testtable(name=recordname, id=recordid, path=recordpath)
        record.save()
        # return HttpResponseRedirect(reverse('psql01:index', args=(records,)))
    return render(request, 'psql01\index.html', {'records': records})

