from django.shortcuts import render
from GovtJobApp.models import RailwayJobsModel
# Create your views here.
def index(request):
    return render(request,'index.html')

# Railway Jobs View starts #


# Railway Jobs View Ends #
def railwayview(request):
    railway_data = RailwayJobsModel.objects.all()
    context={'railway_data':railway_data}
    return render(request, 'govtapp/railway-jobs.html', context=context)