from django.urls import path

from habit.views import HabitUpdateAPIView, HabitDestroyAPIView, HabitCreateAPIView, \
    HabitRetriveAPIView, HabitListView, HabitPublicView

urlpatterns = [
    path('habit/', HabitListView.as_view(), name='habit_list'),
    path('habit/<int:pk>/',HabitRetriveAPIView.as_view(), name='habit_view'),
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/public/', HabitPublicView.as_view(), name='habit_public'),


]