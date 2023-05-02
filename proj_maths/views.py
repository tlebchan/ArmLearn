from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from . import progress_work


def index(request):
    return render(request, "index.html")


def terms_list(request):
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})


def add_term(request):
    return render(request, "term_add.html")


def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_word = request.POST.get("new_word", "")
        new_translation = request.POST.get("new_translation", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_translation) == 0:
            context["success"] = False
            context["comment"] = "Перевод должен быть не пустым"
        elif len(new_word) == 0:
            context["success"] = False
            context["comment"] = "Армянское слово должно быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваше слово принято"
            terms_work.write_term(new_word, new_translation)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)


def show_stats(request):
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)


def add_progress(request):
    return render(request, "progress_add.html")

def send_progress(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_date = request.POST.get("new_date", "")
        new_n = request.POST.get("new_n", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_n) == 0:
            context["success"] = False
            context["comment"] = "Количество слов должно быть не пустым"
        elif len(new_date) == 0:
            context["success"] = False
            context["comment"] = "Дата должна быть не пустой"
        else:
            context["success"] = True
            context["comment"] = "Ваше слово принято"
            progress_work.write_progress(new_date, new_n)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "progress_request.html", context)
    else:
        add_progress(request)