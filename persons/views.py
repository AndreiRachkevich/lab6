from django.shortcuts import get_object_or_404, render, redirect

from .models import Person, Address

# главная страница со списком людей
def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    # создание HTML-страницы по шаблону index.html
    # с заданными параметрами latest_persons и message
    return render(
        request,
        "index.html",
        {
            "latest_persons":
                Person.objects.order_by('-pub_date')[:5],
            "message": message
        }
    )


# страница адресов со списком адресов и  телефонов номеров
def detail(request, person_id,):
    error_message = None
    if "error_message" in request.GET:
        error_message = request.GET["error_message"]
    return render(
        request,
        "address.html",
        {
            "person": get_object_or_404(Person, pk=person_id),
            "error_message": error_message
        }
    )

# def answer(request, riddle_id):
#     riddle = get_object_or_404(Riddle, pk=riddle_id)
#     try:
#         option = riddle.option_set.get(pk=request.POST['option'])
#     except (KeyError, Option.DoesNotExist):
#         return redirect(
#             '/riddles/' + str(riddle_id) +
#             '?error_message=Option does not exist',
#         )
#     else:
#         if option.correct:
#             return redirect(
#                 "/riddles/?message=Nice! Choose another one!")
#         else:
#             return redirect(
#                 '/riddles/'+str(riddle_id)+
#                 '?error_message=Wrong Answer!',
#             )


