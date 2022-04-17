from django.shortcuts import render, redirect
from .models import List
# Create your views here.

def index(request):
	task = List.objects.all()
	if request.method == 'POST':
		new_list = List(title=request.POST['title'])
		new_list.save()
		return redirect('/')

	context = {'tasks':task}
	return render(request, 'index.html', context)

def delete(request, pk):
	task = List.objects.get(id=pk)
	task.delete()
	return redirect('/')