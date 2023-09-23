from django.shortcuts import render, redirect
from .models import Student, Nationality
from django.views.generic import ListView, CreateView, DetailView, View
from .forms import SearchForm, StudentForm, NationalityForm
from django.urls import reverse_lazy

class Home(ListView):
    model = Student
    template_name = 'home.html'
    context_object_name = 'students'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm()
        return context
    
    def post(self, request, *args, **kwargs):       
        form = SearchForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            nationality = form.cleaned_data['nationality']
            queryset = Student.objects.all()
            if keyword:
                queryset = Student.objects.filter(name__icontains=keyword)
                queryset = Student.objects.filter(lastname__icontains=keyword)
            if nationality:
                queryset = Student.objects.filter(nationality=nationality)
            
            self.object_list =queryset.all()
            
            context = self.get_context_data()
            return self.render_to_response(context)
        return render(request, self.template_name,
                    {
                        'search_form': form,
                        'students': self.object_list
                    }
            )

class CreateStudent(CreateView):
    form_class = StudentForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')    

class CreateNationality(View):
    form_class = NationalityForm()
    template_name = 'createnationality.html'
    success_url = reverse_lazy('home')
        
    def post(self, request):     
        if request.method == 'POST':
            form = NationalityForm(request.POST)
            if form.is_valid():
                nationality = form.cleaned_data['nationality']
                Nationality.objects.create(nationality=nationality)                
            return redirect('home')
        return render(request, 'createnationality.html')
    
    def get(self, request):
        return render(request, self.template_name, {'form':self.form_class})
        

