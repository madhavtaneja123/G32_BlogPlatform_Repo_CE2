from django.urls import path
from . import views
from .views import feedback_view, feedback_thanks
from .views import logout_view

urlpatterns=[
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('display/',views.blog_display,name='blog_display'),
    path('create/',views.blog_create, name='blog_create'),
    path('blog/<int:blog_id>/',views.blog_detail,name='blog_detail'),
    path('categories/',views.search_by_category,name='categories'),
    path('blog/<int:blog_id>/delete/',views.delete_blog,name='delete_blog'),
    path('blog/<int:blog_id>/like/',views.like_blog,name='like_blog'),
    path('edit/<int:blog_id>/',views.blog_edit,name='blog_edit'),
    path('add_bookmark/<int:blog_id>/', views.add_bookmark, name='add_bookmark'),
    path('remove-bookmark/<int:blog_id>/', views.remove_bookmark, name='remove_bookmark'),
    path('bookmarks/', views.bookmark_list, name='bookmark_list'),
    path('about/',views.about_view,name='about'),
    path('privacy/',views.privacy_view,name='privacy_policy'),
    path('',views.index_view,name='index'),
    path('feedback/',feedback_view, name='feedback'),
    path('feedback/thanks/',feedback_thanks,name='feedback_thanks'),
    path('contact/',views.contact_view,name='contact'),
    path('messages/',views.display_messages,name='all_messages'),
    path('thank_you/',views.thank_you,name='thank_you'),
    path('logout/', logout_view, name='logout'),
    path('search/category/', views.search_by_category, name='search_by_category'),
    path('search/tag/', views.search_by_tag, name='search_by_tag'),
]