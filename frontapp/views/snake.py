from django.shortcuts import render


def snake(request):
    return render(request, 'snake.html', {'user': request.user.username})