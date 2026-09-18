from django import forms

from .models import Story


class StoryForm(forms.ModelForm):
    max_image_size = 5 * 1024 * 1024

    class Meta:
        model = Story
        fields = (
            "title",
            "description",
            "image",
            "answer",
            "resolution_image",
        )
        labels = {
            "title": "Título do caso",
            "description": "Enigma para os jogadores",
            "image": "Imagem inicial",
            "answer": "Solução completa",
            "resolution_image": "Imagem da solução",
        }
        help_texts = {
            "image": "A imagem que aparece antes da resposta.",
            "resolution_image": "Opcional, mas deixa a revelação mais marcante.",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Ex.: O último bilhete",
                    "autocomplete": "off",
                },
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Escreva o mistério curto que será lido para a mesa.",
                },
            ),
            "answer": forms.Textarea(
                attrs={
                    "rows": 7,
                    "placeholder": "Explique a solução completa para o mestre conduzir a partida.",
                },
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "accept": "image/*",
                    "data-file-input": "image",
                },
            ),
            "resolution_image": forms.ClearableFileInput(
                attrs={
                    "accept": "image/*",
                    "data-file-input": "resolution",
                },
            ),
        }

    def clean_title(self):
        return self.cleaned_data["title"].strip()

    def clean_description(self):
        return self.cleaned_data["description"].strip()

    def clean_answer(self):
        return self.cleaned_data["answer"].strip()

    def _validate_image_size(self, field_name):
        image = self.cleaned_data.get(field_name)

        if image and image.size > self.max_image_size:
            raise forms.ValidationError("A imagem deve ter no máximo 5 MB.")

        return image

    def clean_image(self):
        return self._validate_image_size("image")

    def clean_resolution_image(self):
        return self._validate_image_size("resolution_image")
