from django.urls import path
from Divine.views import (
    HomeView, 
    ActivityDetail, 
    comment, 
    CommentUpdate, 
    EbookList, 
    MembersList, 
    MembersDetail,
    GrowthMaterialsList,
    GalleryList,
    search_members,
    search_ebook,
    search_gallery,
    search_growth_materials
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('activity/details/<int:pk>/', ActivityDetail.as_view(), name='activity_detail'),
    path('comment/<int:id>/', comment, name='comment'),
    path('comment/update/<int:pk>/', CommentUpdate.as_view(), name='update_comment'),
    path('ebooks/', EbookList.as_view(), name='ebook_list'),
    path('our/members/', MembersList.as_view(), name='members_list'),
    path('member/details/<int:pk>/', MembersDetail.as_view(), name='members_detail'),
    path('essential/materials/for/growth/', GrowthMaterialsList.as_view(), name='growth_materials_list'),
    path('our/gallery/', GalleryList.as_view(), name='gallery_list'),
    path('search_for_members/', search_members, name='search_members'),
    path('search_for_books/', search_ebook, name='search_ebooks'),
    path('search_our_gallery/', search_gallery, name='search_gallery'),
    path('search_for_materials/', search_growth_materials, name='search_growth_materials'),
]
