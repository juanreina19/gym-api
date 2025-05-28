from django.shortcuts import render

# Create your views here.
def plans(request):
    """
    Render the plans page.
    """
    return render(request, 'plans/plans.html')