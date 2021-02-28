from django.shortcuts import render
from django.contrib import messages

# Create your views here.


count=0
def physics(request):

    return render(request,'physics.html')



def thank(request):
    global count
    ans = ['E=mc2', 'brick', 'top', 'LPG', 'CNG', 'Neutron','methane','coal','solar panels','solar']

    if request.method == "POST":
        q1 = request.POST['qno1']
        q2 = request.POST['qno2']
        q3 = request.POST['qno3']
        q4 = request.POST['qno4']
        q5 = request.POST['qno5']
        q6 = request.POST['qno6']
        q7 = request.POST['qno7']
        q8 = request.POST['qno8']
        q9 = request.POST['qno9']
        q10 = request.POST['qno10']

        if q1 == ans[0]:
            count = count + 1
        if q2 == ans[1]:
            count += 1
        if q3 == ans[2]:
            count += 1
        if q4 == ans[3]:
            count += 1
        if q5 == ans[4]:
            count += 1
        if q6 == ans[5]:
            count += 1
        if q7 == ans[6]:
            count += 1
        if q8 == ans[7]:
            count += 1
        if q9 == ans[8]:
            count += 1
        if q10 == ans[9]:
            count += 1

    print(count)

    messages.info(request, count)
    count=0



    return render(request,'thank.html')