from django.urls import path
from .apiviews import CreateVote, ChoiceList, PollViewSet, UserCreate, LoginView
from rest_framework.routers import DefaultRouter





router = DefaultRouter()
router.register('polls', PollViewSet)


urlpatterns = [
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),

]

urlpatterns += router.urls
