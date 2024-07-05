from django.shortcuts import render, HttpResponse
def index (request):
    peoples = [
        {'name':'kashish','Domain':'python'},
         {'name':'arya','Domain':'cpp'},
         {'name':'tanu','Domain':'java'},
    ]
    for people in peoples:
        print(people)
    return render(request,"home/index.html",context = {'peoples':peoples,'texts': text})
def success_page(request):
    print("*"*10)
    return HttpResponse("<h1>this is a success page</h1>")
text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
"""