
from django.urls import path

from . import views


app_name = "stories"

urlpatterns = [
    path(
        "health/",
        views.health_check,
        name="health",
    ),

    path(
        "",
        views.story_index,
        name="index",
    ),

    path(
        "nova-historia/",
        views.story_create,
        name="create",
    ),

    path(
        "historia/<int:story_id>/",
        views.story_detail,
        name="detail",
    ),

    path(
        "api/reveal/<int:story_id>/",
        views.reveal_answer,
        name="reveal",
    ),

    path(
        "historia/<int:story_id>/mestre/",
        views.master_view,
        name="master",
    ),
]

