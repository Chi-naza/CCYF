from django.shortcuts import render, redirect
from Divine.models import HomeData, Activity, CustomUser, Gallery, Ebook, Comment, GrowthMaterial
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q


#HOME view
class HomeView(ListView):
    model = Activity
    template_name =  "Divine/home.html"
    context_object_name = 'activities'
    queryset = Activity.objects.order_by('-date_created')
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homedata'] = HomeData.objects.first() 
        context['activityCount'] = Activity.objects.count()
        context['memberCount'] = CustomUser.objects.count()
        context['galleryCount'] = Gallery.objects.count()
        context['ebookCount'] = Ebook.objects.count()
        context['galleries'] = Gallery.objects.all()
        context['executives'] = CustomUser.objects.filter(exco=True)
        return context
    



# ACTIVITY detail
class ActivityDetail(DetailView):
    model = Activity
    template_name = 'Divine/activity_detail.html'
    context_object_name = 'activity'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = context['activity'].comment_set.order_by('-date_commented')
        context['commentCount'] = context['activity'].comment_set.count()
        context['homedata'] = HomeData.objects.first() 
        return context  


#COMMENT function
@login_required
def comment(request, id):
        if request.method == 'POST':
            current_user = request.user
            activity = Activity.objects.get(pk=id)
            user_comment = request.POST.get('comment')
            c = Comment(user=current_user, activity=activity, comment=user_comment)
            c.save()
            messages.success(request, f'Thank you, {current_user.username}, for your opinion and contribution !')
        return redirect(f'/activity/details/{id}/')
    



#COMMENT update
class CommentUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'Divine/update_comment.html'
    fields = ['comment']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homedata'] = HomeData.objects.first() 
        return context    

    def form_valid(self, form):
        form.instance.user == self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False
    
    def get_success_url(self):
        return reverse('activity_detail', kwargs={'pk' : self.object.activity.pk})
    
    
# EBOOK list
class EbookList(ListView):
    model = Ebook
    template_name = 'Divine/ebook.html'
    context_object_name = 'ebooks'
    queryset = Ebook.objects.order_by('-id')
    paginate_by = 12  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homedata'] = HomeData.objects.first() 
        return context   
    
    
# MEMBERS list
class MembersList(ListView):
    model = CustomUser
    template_name = 'Divine/members.html'
    context_object_name = 'members'
    queryset = CustomUser.objects.order_by('-id')
    paginate_by = 15  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homedata'] = HomeData.objects.first() 
        return context   
    


# Members Detail View
class MembersDetail(DetailView):
    model = CustomUser
    template_name = 'Divine/members_detail.html'
    context_object_name = 'member'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homedata'] = HomeData.objects.first() 
        return context  
    
    
    
# GROWTH MATERIALS list
class GrowthMaterialsList(ListView):
    model = GrowthMaterial
    template_name = 'Divine/growth_material.html'
    context_object_name = 'growth_materials'
    queryset = GrowthMaterial.objects.order_by('-id')
    paginate_by = 12  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homedata'] = HomeData.objects.first() 
        return context   
    
    
    
    
# GALLERY list
class GalleryList(ListView):
    model = Gallery
    template_name = 'Divine/gallery.html'
    context_object_name = 'gallery'
    queryset = Gallery.objects.order_by('-id')
    paginate_by = 16  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homedata'] = HomeData.objects.first() 
        return context   
    
    
    

# SEARCH for activities/events
def search_members(request):
    search_term = ''
    if request.GET.get('search'):
        search_term = request.GET.get('search')
    members = CustomUser.objects.filter(
        Q(username__icontains=search_term)|
        Q(dept__icontains=search_term)|
        Q(first_name__icontains=search_term)|
        Q(last_name__icontains=search_term)|
        Q(state__icontains=search_term)|
        Q(town__icontains=search_term)|
        Q(level__icontains=search_term)|
        Q(gender__icontains=search_term)
    )

    context = {
        'members' : members,
        'search_term' : search_term
    }
    return render(request, 'Divine/members.html', context)




# SEARCH for activities/events
def search_ebook(request):
    search_term = ''
    if request.GET.get('search'):
        search_term = request.GET.get('search')
    ebooks = Ebook.objects.filter(Q(name__icontains=search_term)|Q(author__icontains=search_term))

    context = {
        'ebooks' : ebooks,
        'search_term' : search_term
    }
    return render(request, 'Divine/ebook.html', context)



# SEARCH for photos in the Gallery
def search_gallery(request):
    search_term = ''
    if request.GET.get('search'):
        search_term = request.GET.get('search')
    gallery = Gallery.objects.filter(description__icontains=search_term)

    context = {
        'gallery' : gallery,
        'search_term' : search_term
    }
    return render(request, 'Divine/gallery.html', context)



# SEARCH for materials for Growth
def search_growth_materials(request):
    search_term = ''
    if request.GET.get('search'):
        search_term = request.GET.get('search')
    growth_materials = GrowthMaterial.objects.filter(title__icontains=search_term)

    context = {
        'growth_materials' : growth_materials,
        'search_term' : search_term
    }
    return render(request, 'Divine/growth_material.html', context)
    
