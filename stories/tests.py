from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Story


class StoryViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.story = Story.objects.create(
            title="O caso de teste",
            description="Um enigma sem resposta aparente.",
            image="stories/teste.png",
            answer="A verdade estava escondida desde o início.",
        )

    def test_library_lists_story_without_answer(self):
        response = self.client.get(reverse("stories:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.story.title)
        self.assertNotContains(response, self.story.answer)
        self.assertNotContains(response, "Adicionar história")

    def test_detail_is_focused_on_the_riddle(self):
        response = self.client.get(
            reverse("stories:detail", args=[self.story.id]),
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.story.description)
        self.assertNotContains(response, self.story.answer)
        self.assertNotContains(response, "Perguntas")
        self.assertNotContains(response, "Anotações do mestre")

    def test_reveal_returns_only_requested_story_answer(self):
        response = self.client.get(
            reverse("stories:reveal", args=[self.story.id]),
        )

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {"answer": self.story.answer, "story_id": self.story.id},
        )

    def test_master_guide_contains_complete_solution(self):
        response = self.client.get(
            reverse("stories:master", args=[self.story.id]),
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.story.answer)

    def test_story_creation_requires_staff_login(self):
        response = self.client.get(reverse("stories:create"))

        self.assertRedirects(
            response,
            f"{reverse('admin:login')}?next={reverse('stories:create')}",
        )

    def test_staff_can_open_story_creation(self):
        user = get_user_model().objects.create_user(
            username="mestre",
            password="senha-de-teste",
            is_staff=True,
        )
        self.client.force_login(user)

        response = self.client.get(reverse("stories:create"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Adicionar história")

    def test_health_check(self):
        response = self.client.get(reverse("stories:health"))

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "ok"})

    def test_curated_cases_include_cover_and_solution_images(self):
        curated = Story.objects.filter(
            title__in=[
                "Maré Tardia",
                "O Vazio Perfeito",
                "Sem Tocar o Chão",
                "O Primeiro Banquete",
                "A Distância Imóvel",
                "A Outra Metade",
                "Cinzas sem Testemunha",
                "A Companhia Ausente",
                "A Queda Horizontal",
                "O Mar Amarelo",
                "A Pausa na Soleira",
                "A Noite em Marcha",
                "Depois do Silêncio",
                "A Altura Perdida",
            ],
        )

        self.assertEqual(curated.count(), 14)
        self.assertFalse(curated.filter(image="").exists())
        self.assertFalse(curated.filter(resolution_image="").exists())
