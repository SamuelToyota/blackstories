from django.db import migrations


STORIES = [
    {
        "title": "Maré Tardia",
        "description": (
            "Ao fim de uma festa, Gustavo foi retirado inconsciente da piscina "
            "de um hotel. Recuperou-se, conversou, trocou de roupa e recusou a "
            "ambulância. Três horas depois, foi encontrado morto em um quarto "
            "seco, trancado por dentro. O laudo registrou afogamento."
        ),
        "answer": (
            "Gustavo não estava tão recuperado quanto parecia. Durante os minutos "
            "em que ficou submerso, aspirou uma quantidade significativa de água. "
            "A tosse diminuiu e ele voltou a falar, mas a agressão aos alvéolos "
            "continuou evoluindo.\n\n"
            "A água e a inflamação prejudicaram o surfactante pulmonar e a troca de "
            "oxigênio. Horas depois, já sozinho, Gustavo desenvolveu edema pulmonar "
            "e uma hipóxia cada vez mais grave. Perdeu a consciência e morreu antes "
            "de conseguir pedir ajuda.\n\n"
            "O quarto seco e a porta trancada desviavam a investigação: a morte foi "
            "a consequência tardia do episódio na piscina, não de algo ocorrido no "
            "quarto."
        ),
        "image": "stories/case_015_mare_tardia_cover.webp",
        "resolution_image": "stories/case_015_mare_tardia_solution.webp",
    },
    {
        "title": "O Vazio Perfeito",
        "description": (
            "Dois técnicos foram encontrados mortos dentro de um tanque industrial. "
            "A escotilha estava aberta, o tanque estava vazio, seco e recém-lavado. "
            "Não havia veneno, fumaça, queimaduras ou ferimentos. O segundo homem "
            "entrou depois de ver o primeiro cair."
        ),
        "answer": (
            "Antes da manutenção, uma tubulação de solda havia despejado argônio no "
            "tanque para impedir que o metal oxidasse. O gás é incolor, inodoro e "
            "não irrita as vias respiratórias, por isso nenhum dos homens percebeu "
            "o perigo.\n\n"
            "Mais denso que o ar, o argônio permaneceu acumulado no fundo mesmo com "
            "a escotilha aberta. Ele não envenenou os técnicos: apenas deslocou o "
            "oxigênio. O primeiro perdeu a consciência em poucos instantes. O segundo "
            "entrou por impulso para socorrê-lo, respirou a mesma atmosfera e caiu "
            "antes de conseguir subir."
        ),
        "image": "stories/case_016_vazio_perfeito_cover.webp",
        "resolution_image": "stories/case_016_vazio_perfeito_solution.webp",
    },
    {
        "title": "Sem Tocar o Chão",
        "description": (
            "Um trabalhador escorregou da fachada de um prédio. O cinto de segurança "
            "deteve a queda, ele não bateu em nada e continuou conversando durante o "
            "resgate. Vinte e cinco minutos depois, foi içado até o terraço. Assim que "
            "chegou, desmaiou e morreu."
        ),
        "answer": (
            "A queda não o matou; a espera imóvel no cinto, sim. Suspenso na vertical, "
            "Gustavo teve as pernas comprimidas pelas tiras e quase não conseguia "
            "movê-las. O sangue começou a se acumular nos membros inferiores, reduzindo "
            "progressivamente o retorno ao coração e a irrigação do cérebro.\n\n"
            "Ele ainda conseguia falar, mas já sofria intolerância à suspensão. A demora "
            "no resgate permitiu que a circulação entrasse em colapso. Quando alcançou "
            "o terraço, perdeu a consciência e sofreu uma parada cardíaca. O equipamento "
            "funcionou perfeitamente; faltou um resgate rápido para quem permanecia "
            "pendurado."
        ),
        "image": "stories/case_017_sem_tocar_o_chao_cover.webp",
        "resolution_image": "stories/case_017_sem_tocar_o_chao_solution.webp",
    },
    {
        "title": "O Primeiro Banquete",
        "description": (
            "Depois de semanas desaparecido, um homem foi resgatado muito magro, mas "
            "consciente e com sinais vitais estáveis. Naquela noite, a família preparou "
            "um enorme jantar de boas-vindas. A comida estava perfeita e todos comeram. "
            "Somente ele morreu."
        ),
        "answer": (
            "Durante a fome prolongada, o organismo do homem passou a consumir as "
            "próprias reservas e ficou profundamente carente de fosfato, potássio, "
            "magnésio e vitaminas. Ainda assim, os exames iniciais não tornavam o "
            "perigo evidente para a família.\n\n"
            "O banquete, rico em carboidratos, provocou uma descarga intensa de "
            "insulina. Os poucos eletrólitos restantes migraram rapidamente do sangue "
            "para dentro das células. Essa síndrome de realimentação desencadeou "
            "arritmia e falência cardíaca. Ele precisava ter recebido pequenas porções, "
            "suplementação e monitoramento — não uma refeição abundante."
        ),
        "image": "stories/case_018_primeiro_banquete_cover.webp",
        "resolution_image": "stories/case_018_primeiro_banquete_solution.webp",
    },
    {
        "title": "A Distância Imóvel",
        "description": (
            "Um mecânico foi encontrado morto no chão da oficina, a vários metros de "
            "um caminhão parado. O veículo não se moveu, nenhuma ferramenta elétrica "
            "estava ligada e ninguém havia entrado no galpão. A autópsia revelou um "
            "único impacto fatal."
        ),
        "answer": (
            "O caminhão usava uma roda antiga de aro multipartido. Depois de uma "
            "manutenção, o anel metálico que travava o conjunto não ficou perfeitamente "
            "assentado no sulco. O pneu, porém, continuou cheio e parecia normal.\n\n"
            "Quando o mecânico se aproximou para inspecioná-lo, a pressão interna "
            "expulsou o anel de retenção. A peça circular atravessou a oficina como um "
            "projétil, atingiu o homem e caiu longe do corpo. O caminhão jamais precisou "
            "se mover: a energia estava armazenada no ar comprimido do próprio pneu."
        ),
        "image": "stories/case_019_distancia_imovel_cover.webp",
        "resolution_image": "stories/case_019_distancia_imovel_solution.webp",
    },
    {
        "title": "A Outra Metade",
        "description": (
            "Um técnico viu a cabine do elevador subir e, certo de que ela se afastava, "
            "entrou no poço para fazer um reparo. Segundos depois, foi esmagado por algo "
            "que vinha de cima. A cabine continuou subindo, não mudou de direção e "
            "nenhuma peça se soltou."
        ),
        "answer": (
            "A cabine era apenas metade do sistema. Em um elevador de tração, cabos "
            "ligam a cabine a um grande contrapeso: quando um lado sobe, o outro desce.\n\n"
            "O técnico acompanhou visualmente a cabine, mas entrou no espaço ocupado "
            "pela trajetória do contrapeso. Enquanto a cabine se afastava para cima, "
            "a massa de aço descia silenciosamente pelo outro lado do poço e o prensou "
            "contra o fundo. Nada caiu nem apresentou defeito; o elevador executou "
            "exatamente o movimento para o qual fora construído."
        ),
        "image": "stories/case_020_outra_metade_cover.webp",
        "resolution_image": "stories/case_020_outra_metade_solution.webp",
    },
    {
        "title": "Cinzas sem Testemunha",
        "description": (
            "Um apartamento vazio pegou fogo no meio de uma tarde clara. A perícia "
            "descartou curto-circuito, vazamento de gás, velas, cigarros, raios e "
            "invasão. As janelas estavam fechadas e ninguém havia entrado desde a manhã."
        ),
        "answer": (
            "Uma garrafa transparente, ainda parcialmente cheia de água, havia sido "
            "deixada no parapeito. No horário certo da tarde, sua superfície curva "
            "refratou a luz do sol e funcionou como uma lente.\n\n"
            "O ponto de luz concentrada permaneceu sobre uma dobra escura da cortina. "
            "O tecido começou a carbonizar lentamente, produziu brasa e por fim pegou "
            "fogo. Não havia chama inicial nem defeito na casa: um objeto cotidiano "
            "concentrou energia solar no mesmo ponto durante tempo suficiente para "
            "iniciar o incêndio."
        ),
        "image": "stories/case_021_cinzas_sem_testemunha_cover.webp",
        "resolution_image": "stories/case_021_cinzas_sem_testemunha_solution.webp",
    },
    {
        "title": "A Companhia Ausente",
        "description": (
            "Lívia entrou sozinha em um elevador e apertou o botão. Antes de chegar ao "
            "andar seguinte, algo que permanecera no corredor morreu. A porta não o "
            "atingiu, nenhuma pessoa o tocou e Lívia só percebeu quando já era tarde."
        ),
        "answer": (
            "Lívia não chegara sozinha ao prédio: trazia um cão pequeno preso a uma "
            "guia longa. Ela entrou na cabine distraída, mas o animal hesitou e ficou "
            "no corredor. As portas se fecharam sobre a guia fina sem acionar o sensor.\n\n"
            "Quando o elevador começou a subir, a guia ficou presa entre o piso e a "
            "cabine. A extremidade ligada ao cão foi puxada violentamente para cima e "
            "o enforcou antes que Lívia conseguisse parar o equipamento. A cabine "
            "parecia vazia porque a única companhia dela nunca chegou a entrar."
        ),
        "image": "stories/case_022_companhia_ausente_cover.webp",
        "resolution_image": "stories/case_022_companhia_ausente_solution.webp",
    },
    {
        "title": "A Queda Horizontal",
        "description": (
            "Durante a transferência de um paciente para uma sala de exames, um "
            "cilindro de oxigênio fechado atravessou o ambiente e o matou. Ninguém "
            "arremessou o cilindro, ele não explodiu e o chão estava perfeitamente "
            "nivelado."
        ),
        "answer": (
            "A sala abrigava um aparelho de ressonância magnética. Mesmo quando não "
            "está produzindo imagens, o ímã principal do equipamento permanece ativo. "
            "O cilindro levado para perto dele não era compatível com aquele ambiente.\n\n"
            "Assim que cruzou a área de maior campo, o corpo ferromagnético do cilindro "
            "foi acelerado em direção ao túnel do aparelho. Ele se transformou em um "
            "projétil pesado e atingiu o paciente. A válvula nunca precisou ser aberta: "
            "o perigo estava no metal atraído pelo ímã, não no oxigênio."
        ),
        "image": "stories/case_023_queda_horizontal_cover.webp",
        "resolution_image": "stories/case_023_queda_horizontal_solution.webp",
    },
    {
        "title": "O Mar Amarelo",
        "description": (
            "Um trabalhador caminhava sobre uma superfície firme e perfeitamente "
            "nivelada dentro de um armazém. De repente, começou a afundar. Em poucos "
            "segundos, desapareceu por completo. Não houve desabamento, lama nem "
            "abertura no piso."
        ),
        "answer": (
            "A superfície era formada por toneladas de grãos dentro de um silo. A "
            "umidade havia criado uma crosta aparentemente sólida, enquanto a descarga "
            "por um transportador helicoidal abria uma cavidade logo abaixo.\n\n"
            "Quando o trabalhador pisou sobre a parte oca, a ponte de grãos rompeu. "
            "Ao mesmo tempo, o equipamento em funcionamento puxava o material para a "
            "saída inferior. O grão em movimento comportou-se como areia movediça: em "
            "segundos prendeu suas pernas, cobriu seu tórax e o sufocou antes que os "
            "colegas pudessem alcançá-lo."
        ),
        "image": "stories/case_024_mar_amarelo_cover.webp",
        "resolution_image": "stories/case_024_mar_amarelo_solution.webp",
    },
    {
        "title": "A Pausa na Soleira",
        "description": (
            "Um bombeiro sabia que havia uma pessoa atrás de uma porta fechada, mas "
            "proibiu a equipe de abri-la. Depois de observar a porta por alguns "
            "segundos, ordenou que todos recuassem. Logo depois, o cômodo explodiu. "
            "A decisão dele salvou a equipe."
        ),
        "answer": (
            "O incêndio dentro do apartamento consumira quase todo o oxigênio. Sem ar "
            "suficiente, as chamas diminuíram, mas móveis e revestimentos continuaram "
            "liberando gases quentes e combustíveis. A pressão fazia a fumaça pulsar "
            "pelas frestas, dando a impressão de que a porta respirava.\n\n"
            "O bombeiro reconheceu os sinais de um backdraft. Se abrisse a porta, o ar "
            "fresco se misturaria aos gases superaquecidos e produziria uma combustão "
            "explosiva no corredor. A pessoa lá dentro já havia sucumbido à fumaça; "
            "uma entrada imediata apenas acrescentaria toda a equipe às vítimas."
        ),
        "image": "stories/case_025_pausa_na_soleira_cover.webp",
        "resolution_image": "stories/case_025_pausa_na_soleira_solution.webp",
    },
    {
        "title": "A Noite em Marcha",
        "description": (
            "Uma família foi encontrada morta em casa. Na garagem anexa, o carro "
            "estava desligado e frio, com o tanque quase cheio. A chave continuava "
            "dentro da casa. Não havia vazamento de gás, sinais de incêndio ou invasão."
        ),
        "answer": (
            "O carro possuía um sistema de partida remota instalado pelo antigo dono. "
            "Durante a noite, o controle ficou pressionado sob a mão de uma pessoa que "
            "dormia e ativou, sem que ela percebesse, o modo programado para partidas "
            "periódicas em noites frias.\n\n"
            "Com a porta da garagem fechada, cada ciclo acumulou monóxido de carbono. "
            "O gás passou para os quartos por frestas e dutos, intoxicando a família "
            "durante o sono. O último ciclo terminou horas antes da descoberta; por "
            "isso o motor já estava frio, o carro parecia nunca ter ligado e a chave "
            "não estava na ignição."
        ),
        "image": "stories/case_026_noite_em_marcha_cover.webp",
        "resolution_image": "stories/case_026_noite_em_marcha_solution.webp",
    },
    {
        "title": "Depois do Silêncio",
        "description": (
            "Antes de entrar em uma prensa industrial, um técnico desligou a máquina, "
            "travou o comando e esperou até que todo ruído cessasse. Ninguém religou o "
            "equipamento. Mesmo assim, a prensa se moveu e o matou."
        ),
        "answer": (
            "O técnico isolou a alimentação elétrica, mas não eliminou todas as formas "
            "de energia. O cilindro hidráulico continuava pressurizado por um acumulador, "
            "e a enorme placa elevada também armazenava energia potencial pela própria "
            "gravidade.\n\n"
            "Sem um bloco mecânico rígido entre as partes da prensa, uma pequena fuga "
            "na válvula permitiu que a pressão se redistribuísse. A placa desceu de "
            "repente enquanto ele estava na zona de esmagamento. O silêncio provava "
            "apenas que o motor havia parado; não que a energia armazenada tivesse sido "
            "liberada ou contida."
        ),
        "image": "stories/case_027_depois_do_silencio_cover.webp",
        "resolution_image": "stories/case_027_depois_do_silencio_solution.webp",
    },
    {
        "title": "A Altura Perdida",
        "description": (
            "Um mecânico entrou sob um ônibus estacionado em piso plano. O motor estava "
            "desligado, as rodas estavam calçadas e o veículo não se deslocou um "
            "centímetro. Minutos depois, o ônibus o esmagou. Nenhuma peça caiu."
        ),
        "answer": (
            "A carroceria daquele ônibus era sustentada por bolsas de ar da suspensão "
            "pneumática. Com o motor desligado, o compressor deixou de repor a pressão. "
            "Uma mangueira danificada perdeu ar lentamente até que as bolsas murcharam.\n\n"
            "As rodas permaneceram imóveis e apoiadas no mesmo lugar, mas o chassi "
            "inteiro baixou vários centímetros. Como o mecânico confiou na altura da "
            "suspensão e não instalou cavaletes rígidos, ficou preso entre o piso e o "
            "ônibus. Nada precisou cair: foi a distância entre o veículo e o chão que "
            "desapareceu."
        ),
        "image": "stories/case_028_altura_perdida_cover.webp",
        "resolution_image": "stories/case_028_altura_perdida_solution.webp",
    },
]


def add_stories(apps, schema_editor):
    Story = apps.get_model("stories", "Story")

    for story in STORIES:
        Story.objects.update_or_create(
            title=story["title"],
            defaults=story,
        )


def remove_stories(apps, schema_editor):
    Story = apps.get_model("stories", "Story")
    Story.objects.filter(title__in=[story["title"] for story in STORIES]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("stories", "0005_polish_story_answers"),
    ]

    operations = [
        migrations.RunPython(add_stories, remove_stories),
    ]
