from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET

from .forms import StoryForm
from .models import Story


@staff_member_required(login_url="admin:login")
def story_create(request):
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES)

        if form.is_valid():
            story = form.save()
            return redirect("stories:detail", story_id=story.id)
    else:
        form = StoryForm()

    return render(
        request,
        "story_form.html",
        {
            "form": form,
            "render_free_mode": settings.RENDER_FREE_MODE,
        },
    )


def story_index(request):
    stories = Story.objects.only(
        "id",
        "title",
        "description",
        "image",
        "created_at",
    ).order_by("-created_at")

    return render(
        request,
        "story_index.html",
        {"stories": stories},
    )


def story_detail(request, story_id):
    story = get_object_or_404(
        Story.objects.only(
            "id",
            "title",
            "description",
            "image",
            "answer",
            "resolution_image",
        ),
        id=story_id,
    )

    return render(
        request,
        "story_detail.html",
        {"story": story},
    )


@require_GET
def reveal_answer(request, story_id):
    story = get_object_or_404(
        Story.objects.only("id", "answer"),
        id=story_id,
    )

    return JsonResponse({
        "answer": story.answer,
        "story_id": story.id,
    })


def master_view(request, story_id):
    story = get_object_or_404(
        Story.objects.only(
            "id",
            "title",
            "description",
            "image",
            "answer",
            "resolution_image",
        ),
        id=story_id,
    )

    return render(
        request,
        "master.html",
        {"story": story},
    )


@require_GET
def health_check(request):
    return JsonResponse({"status": "ok"})
