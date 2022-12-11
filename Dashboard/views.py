from django.shortcuts import redirect
from Divine.models import Activity, Gallery, Ebook, Comment, HomeData
from django.views.generic import UpdateView, CreateView, DeleteView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse

# Create your views here.


class AdminHomeData(TemplateView):
    model = HomeData
    template_name =  "Dashboard/homedata.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homedata'] = HomeData.objects.first()
        return context
   
    
    

class CreateActivity(LoginRequiredMixin, CreateView):
    model = Activity
    template_name = 'Dashboard/create_activity.html'
    fields = ['title', 'description', 'image', 'date_of_event']

    def get_success_url(self):
        return reverse('admin_activity_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        messages.success(self.request, 'Successfully created a new activity/event !')
        return redirect(self.get_success_url())



class UpdateActivity(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Activity
    template_name = 'Dashboard/create_activity.html'
    fields = ['title', 'description', 'image', 'date_of_event']

    def form_valid(self, form):
        form.instance.user == self.request.user
        return super().form_valid(form)

    def test_func(self):
        activity = self.get_object()
        if self.request.user == activity.user:
            return True
        return False
    
    def get_success_url(self):
        return reverse('activity_detail', kwargs={'pk' : self.object.pk})




class DeleteActivity(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Activity
    success_message = "Activity was deleted successfully !"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteActivity, self).delete(request, *args, **kwargs)
    
    def test_func(self):
        activity = self.get_object()
        if self.request.user == activity.member:
            return True
        return False

    def get_success_url(self):
        return reverse('admin_activity_list')

