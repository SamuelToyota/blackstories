from django.db import migrations


STORY_ANSWERS = {
    2: (
        "Renata comprou de um vendedor clandestino um frasco de Durmir®, um "
        "produto experimental que continha uma bactéria geneticamente modificada. "
        "Ela induzia uma hibernação tão profunda que nenhum estímulo comum seria "
        "capaz de despertá-la.\n\n"
        "O organismo havia sido desenvolvido para ambientes com umidade controlada. "
        "Renata, porém, dormia com um umidificador ligado. A umidade ativou uma "
        "segunda fase da bactéria, que passou a se reproduzir e transformou o muco "
        "dos pulmões em um líquido espesso.\n\n"
        "Inconsciente e incapaz de acordar, ela teve os alvéolos preenchidos pelo "
        "líquido. Renata se afogou por dentro enquanto experimentava o sono mais "
        "profundo de sua vida."
    ),
    3: (
        "Durante uma tempestade, o pescador bateu a cabeça em uma viga. O trauma "
        "danificou a região do cérebro responsável pela sensação de sede e também "
        "o deixou confuso.\n\n"
        "Ele continuou comendo, usando o rádio e tentando manter o barco em ordem, "
        "mas nunca sentia necessidade de beber. Sem perceber a gravidade do que "
        "acontecia, foi enfraquecendo até morrer desidratado, cercado por água potável."
    ),
    4: (
        "O estádio possuía um antigo sistema elétrico de aquecimento sob o gramado. "
        "Depois da irrigação, uma emenda com isolamento danificado energizou a área "
        "molhada próxima ao gol.\n\n"
        "As travas de borracha das chuteiras isolavam os jogadores enquanto estavam "
        "de pé. Ao defender o pênalti, porém, o goleiro mergulhou e apoiou as mãos e "
        "os antebraços molhados exatamente sobre o trecho energizado. A corrente "
        "atravessou seu tórax e provocou uma arritmia fatal poucos segundos depois."
    ),
    5: (
        "O homem era um arqueólogo que explorava um templo construído sobre uma "
        "região vulcânica. Fissuras subterrâneas liberavam dióxido de carbono, um gás "
        "invisível e mais pesado que o ar, que se acumulava junto ao chão.\n\n"
        "Ao pisar em uma placa, ele abriu uma antiga passagem para o gás. Quando se "
        "agachou para observar os desenhos, colocou o rosto dentro da camada de CO₂, "
        "perdeu a consciência e morreu asfixiado. Horas depois, o gás já havia se "
        "dissipado pelas frestas da câmara."
    ),
    6: (
        "João caiu de um cruzeiro e passou dias à deriva, sem comida ou água doce. "
        "Quando alcançou a ilha, acreditou que finalmente estava salvo.\n\n"
        "Ele era cirurgião e reconheceu no ar o cheiro produzido pelo eletrocautério "
        "ao queimar gordura humana. A fumaça vinha do interior da ilha: canibais "
        "preparavam uma refeição. João entendeu que acabara de chegar ao cardápio."
    ),
    7: (
        "O sineiro era cego. Naquela noite, ladrões roubaram o pesado sino de bronze "
        "e, ao serem surpreendidos pelo padre, deixaram-no desacordado e amarrado no "
        "alto da torre com a própria corda do sino.\n\n"
        "Sem saber do roubo, o sineiro subiu para anunciar a missa. A corda parecia "
        "leve porque já não sustentava o sino. Seu puxão desfez o nó improvisado, e "
        "o padre caiu na praça. A multidão, vendo o corpo cair no exato momento em "
        "que o sineiro puxava a corda, culpou-o pelo crime e o matou antes que pudesse "
        "se explicar."
    ),
    8: (
        "Kevin era o apelido dado a um organismo microscópico encontrado no espaço "
        "e levado para estudo em uma estação orbital. Em contato com os nutrientes "
        "do laboratório, ele cresceu com velocidade extraordinária e desenvolveu "
        "força, inteligência e comportamento predatório.\n\n"
        "Quando escapou do recipiente, a tripulação tentou eliminá-lo com um gás "
        "corrosivo. O organismo não respirava oxigênio; o produto apenas enfraqueceu "
        "as travas da câmara e facilitou sua fuga. Kevin matou a tripulação e se "
        "escondeu em uma cápsula automática enviada de volta à Terra."
    ),
    9: (
        "As duas trilhas não foram feitas ao mesmo tempo. O caçador entrou na floresta "
        "pela primeira e, ao tentar voltar durante uma nevasca, caminhou ao lado das "
        "próprias marcas para usá-las como referência.\n\n"
        "O vento apagou os detalhes que indicavam o sentido dos passos, fazendo parecer "
        "que duas pessoas haviam caminhado juntas. Ferido e desorientado, ele tomou a "
        "direção errada, afastou-se ainda mais do abrigo e morreu congelado no ponto em "
        "que as duas trilhas terminavam."
    ),
    10: (
        "O homem era um prisioneiro político que fugia de uma ditadura. Se fosse "
        "capturado, seria torturado para revelar os nomes de familiares e das pessoas "
        "que organizaram sua fuga. Ele havia decidido que não permitiria isso.\n\n"
        "Ao ver pela janela que o avião finalmente deixara o território do regime, "
        "sorriu: sua rota de fuga havia funcionado e os cúmplices já não poderiam ser "
        "interceptados no aeroporto. Então usou uma pequena lâmina escondida para "
        "tirar a própria vida e levar consigo todos os nomes que conhecia."
    ),
    11: (
        "O taxista estava profundamente deprimido e havia decidido que o comportamento "
        "do próximo passageiro determinaria se ele continuaria vivendo.\n\n"
        "O passageiro era mudo e acabara de ganhar uma grande quantia em uma loteria. "
        "Feliz, escreveu um bilhete oferecendo parte do prêmio ao motorista. O taxista, "
        "porém, era analfabeto. Em seu estado de paranoia, interpretou os números e as "
        "palavras como uma ameaça de assalto. Convencido de que aquele era o sinal que "
        "esperava, acelerou em direção ao penhasco antes que o passageiro pudesse explicar."
    ),
    12: (
        "O homem era um equilibrista conhecido por atravessar grandes alturas sem rede "
        "de proteção. Sua segurança dependia de sapatilhas especiais, com grande aderência.\n\n"
        "A esposa, que planejava ficar com o dinheiro do seguro de vida, comprou um par "
        "idêntico e aplicou óleo de silicone nas solas. Minutos antes do espetáculo, deu "
        "as sapatilhas de presente. Ao pisar na corda, ele escorregou e sofreu uma queda "
        "fatal. A perícia encontrou o lubrificante e ligou a esposa ao crime."
    ),
    13: (
        "O homem era um oceanógrafo que viajara à cidade para mergulhar. No aquário do "
        "hotel, percebeu peixes tentando se enterrar e outros nadando de forma errática.\n\n"
        "Animais marinhos são sensíveis a vibrações e mudanças de pressão. Para ele, o "
        "comportamento indicava que um grande maremoto se aproximava. Como o hotel ficava "
        "na praia, pegou as malas e partiu imediatamente para o interior. Pouco depois, "
        "um tsunami atingiu a costa."
    ),
    14: (
        "O homem era um egiptólogo que havia encontrado uma tumba intacta. Dentro de uma "
        "taça de alabastro havia um pó escuro: esporos de um fungo extinto, preservados por "
        "milênios no ambiente hermético.\n\n"
        "A análise mostrou que uma única inalação seria suficiente para colonizar os pulmões. "
        "O fungo permaneceria latente por semanas antes de se tornar letal e contagioso. Como "
        "passara a noite respirando dentro da câmara, ele percebeu que já era o vetor. Mandou "
        "selar a tumba e isolou-se para nunca transmitir a ameaça a outra pessoa."
    ),
}


def polish_story_answers(apps, schema_editor):
    Story = apps.get_model("stories", "Story")

    for story_id, answer in STORY_ANSWERS.items():
        Story.objects.filter(id=story_id).update(answer=answer)


class Migration(migrations.Migration):
    dependencies = [
        ("stories", "0004_polish_story_copy"),
    ]

    operations = [
        migrations.RunPython(polish_story_answers, migrations.RunPython.noop),
    ]
