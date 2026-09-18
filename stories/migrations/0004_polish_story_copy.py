from django.db import migrations


STORY_COPY = {
    2: {
        "title": "Sono Perfeito",
        "description": (
            "Renata sofria de insônia havia quatro anos. Desesperada, comprou "
            "pela internet um remédio que prometia o sono perfeito. Tomou o "
            "conteúdo do frasco e foi dormir. Na manhã seguinte, foi encontrada "
            "morta. A autópsia apontou afogamento."
        ),
    },
    3: {
        "title": "O Náufrago",
        "description": (
            "Um barco pesqueiro foi encontrado à deriva, a 300 quilômetros da "
            "costa. No convés havia um homem morto, água potável e comida para "
            "semanas. O motor, o rádio e o tanque estavam em perfeito estado. "
            "Mesmo assim, ele morreu de desidratação."
        ),
    },
    4: {
        "title": "Pênalti Fatal",
        "description": (
            "Final do campeonato. Empate em 1 a 1. Aos 47 minutos do segundo "
            "tempo, o time da casa ganha um pênalti. O goleiro defende, levanta "
            "os braços para comemorar e cai morto. Não havia ferimentos nem "
            "doenças: ele morreu por choque elétrico."
        ),
    },
    5: {
        "title": "A Curiosidade Mata",
        "description": (
            "Um homem se agacha para examinar algo no chão. Segundos depois, "
            "cai morto. A autópsia não encontra ferimentos, veneno ou sinais de "
            "ataque cardíaco. A causa da morte foi asfixia."
        ),
    },
    6: {
        "title": "João, o Azarado",
        "description": (
            "Depois de dias perdido no mar, João finalmente alcança uma ilha. "
            "Ele respira fundo, reconhece um cheiro familiar e entende que seu "
            "fim está muito próximo."
        ),
    },
    7: {
        "title": "Silêncio de Chumbo",
        "description": (
            "A corda do sino nunca pareceu tão leve. O sineiro a puxou com "
            "força, mas nenhum som ecoou. Um segundo depois, os gritos da vila "
            "anunciaram que aquele gesto decretaria sua morte."
        ),
    },
    8: {
        "title": "Raiva Imparável",
        "description": (
            "Kevin nasceu minúsculo e indefeso. Em pouco tempo, cresceu, "
            "escapou de sua prisão e matou todos ao redor."
        ),
    },
    9: {
        "title": "Passos Paralelos",
        "description": (
            "Na neve, duas trilhas de pegadas idênticas seguiam lado a lado "
            "pela floresta. No fim do caminho, porém, havia apenas um corpo "
            "congelado."
        ),
    },
    10: {
        "title": "Último Voo",
        "description": (
            "Um homem embarca em um avião comercial e escolhe o assento da "
            "janela. Assim que a aeronave decola, ele olha para fora, sorri e "
            "corta a própria garganta."
        ),
    },
    11: {
        "title": "Suicídio Duplo",
        "description": (
            "Um homem entra em um táxi e entrega um bilhete ao motorista. "
            "Segundos depois, o motorista acelera em direção a um penhasco, "
            "matando os dois."
        ),
    },
    12: {
        "title": "Passos de Veludo",
        "description": (
            "Um homem ganha da esposa um par de sapatos novos. Ele os calça, "
            "dá alguns passos e morre. A esposa é presa logo depois."
        ),
    },
    13: {
        "title": "O Aquário",
        "description": (
            "Um homem entra em um hotel luxuoso e observa o aquário do saguão "
            "por alguns segundos. Em seguida, dá meia-volta, pega as malas e "
            "abandona a cidade sem falar com ninguém."
        ),
    },
    14: {
        "title": "Arrependido para Sempre",
        "description": (
            "Ao encontrar uma antiga taça, um homem decide examinar seu "
            "conteúdo. Logo percebe que cometeu um erro terrível e decide "
            "nunca mais encontrar outra pessoa."
        ),
    },
}


def polish_story_copy(apps, schema_editor):
    Story = apps.get_model("stories", "Story")

    for story_id, fields in STORY_COPY.items():
        Story.objects.filter(id=story_id).update(**fields)


class Migration(migrations.Migration):
    dependencies = [
        ("stories", "0003_remove_story_resolution"),
    ]

    operations = [
        migrations.RunPython(polish_story_copy, migrations.RunPython.noop),
    ]
