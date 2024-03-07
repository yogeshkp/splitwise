from django.shortcuts import render, HttpResponse

# Create your views here.


def homepage(self):
    return HttpResponse("this is the homepage")


def group_creation(request):
    if request.method == "POST":
        # group_name=mv&member=2&member0=yogi&member1=deep
        group_name = request.POST.get("group_name")
        member0 = request.POST.get("member0")
        member1 = request.POST.get("member1")
        print(group_name)
        return HttpResponse(f"{group_name}{member0}{member1}")

    else:
        print("wapas se form aa rhahai get request hai yeh")
        return render(request, "group.html")


# def group_get(request):
#     if request.POST:
#         return HttpResponse(request.POST)


def shares(request):
    return HttpResponse("this is ehere the shares are divided")


def debts(self):
    return HttpResponse("this is where you pay the debts")
