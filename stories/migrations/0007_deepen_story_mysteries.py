from django.db import migrations


STORY_REVISIONS = {
    "Sono Perfeito": {
        "description": (
            "Depois de quatro anos sem dormir uma noite inteira, Renata anunciou que finalmente "
            "encontrara a solução. Trancou um quarto seco, deitou-se sozinha e não voltou a "
            "acordar. Nada fora derramado e ninguém entrou, mas seus pulmões estavam cheios de "
            "líquido."
        ),
        "answer": (
            "A solução de Renata era o Durmir®, comprado de um fornecedor clandestino. O frasco "
            "não trazia um sedativo comum, mas um microrganismo experimental criado para reduzir "
            "o metabolismo e induzir um estado semelhante à hibernação. A primeira dose funcionou: "
            "ela perdeu a capacidade de reagir até mesmo a estímulos extremos.\n\n"
            "O detalhe que ninguém associou ao produto era o umidificador ligado ao lado da cama. "
            "Em ar muito úmido, o microrganismo iniciava uma segunda fase de reprodução e alterava "
            "as secreções das vias respiratórias. O muco tornou-se abundante e espesso, invadindo "
            "progressivamente os alvéolos.\n\n"
            "A mesma hibernação que prometia o sono perfeito impediu Renata de tossir, despertar "
            "ou pedir ajuda. O líquido não veio do quarto: formou-se dentro dos pulmões até bloquear "
            "a troca de oxigênio. Por isso a porta permanecia trancada, a cama estava seca e o laudo "
            "parecia descrever um afogamento impossível."
        ),
    },
    "O Náufrago": {
        "description": (
            "Um barco em perfeito estado foi encontrado à deriva, longe da costa. O único ocupante "
            "morrera de desidratação, embora houvesse água potável aberta, ao alcance de sua mão, "
            "e sinais de que ele continuara trabalhando por vários dias."
        ),
        "answer": (
            "Durante uma tempestade, o pescador bateu a cabeça em uma viga. O impacto não o deixou "
            "paralisado nem inconsciente por muito tempo; danificou de modo seletivo regiões do "
            "hipotálamo e vias ligadas à percepção da sede. Ele desenvolveu adipsia: seu organismo "
            "perdia água, mas o cérebro não transformava essa necessidade em vontade de beber.\n\n"
            "A lesão também prejudicou sua capacidade de avaliar o próprio estado. Por isso ele ainda "
            "consertou cabos, separou comida e tentou usar o rádio. Essas ações davam a impressão de "
            "lucidez completa, enquanto a concentração de sódio no sangue aumentava, a fraqueza "
            "piorava e o raciocínio se tornava cada vez menos confiável.\n\n"
            "As garrafas abertas não eram prova de que bebera: ele as movimentara ao organizar o "
            "convés. Cercado pelo que poderia salvá-lo, nunca sentiu a urgência que o faria levar a "
            "água à boca. Quando a confusão se tornou evidente, já não tinha forças para corrigir o "
            "erro que seu próprio cérebro escondia."
        ),
    },
    "Pênalti Fatal": {
        "description": (
            "Aos 47 minutos, o goleiro defendeu o pênalti decisivo. Levantou-se, ergueu os braços e "
            "caiu morto diante de vinte jogadores ilesos. Não havia tempestade, ninguém o tocou e "
            "todo o time atravessara o mesmo gramado molhado. Ainda assim, a causa foi elétrica."
        ),
        "answer": (
            "Sob o gramado existia um antigo sistema elétrico de aquecimento. Uma emenda danificada "
            "ficava exatamente atrás da pequena área e a irrigação criara, naquele ponto, uma faixa "
            "de terra encharcada e energizada. A falha não fazia o estádio inteiro conduzir corrente; "
            "produzia uma perigosa diferença de potencial em poucos metros.\n\n"
            "Enquanto corriam, os jogadores tocavam o solo principalmente com as travas de borracha "
            "das chuteiras. O goleiro foi o único a mergulhar no trecho defeituoso e apoiar, ao mesmo "
            "tempo, as duas mãos e os antebraços molhados em pontos de potencial diferente. Seu corpo "
            "fechou um caminho de baixa resistência através do tórax.\n\n"
            "A descarga desorganizou o ritmo do coração, mas ele ainda conseguiu se levantar por alguns "
            "segundos. Ao erguer os braços para comemorar, já estava entrando em fibrilação ventricular. "
            "A defesa apenas determinou onde e como ele tocaria o gramado; o golpe fatal estava invisível "
            "sob a água."
        ),
    },
    "A Curiosidade Mata": {
        "description": (
            "Um homem se abaixou para observar marcas no chão e perdeu a consciência. Quem o encontrou "
            "permaneceu de pé no mesmo lugar e nada sentiu. Horas depois, o ar parecia normal; mesmo "
            "assim, o homem morrera asfixiado."
        ),
        "answer": (
            "O homem era um arqueólogo dentro de uma câmara construída sobre terreno vulcânico. Fissuras "
            "no subsolo liberavam dióxido de carbono. Como o gás é invisível, não tem cheiro e é mais "
            "denso que o ar, ele formou uma camada concentrada apenas nos centímetros mais baixos do piso.\n\n"
            "Ao deslocar uma placa para enxergar as marcas, o arqueólogo abriu uma passagem adicional "
            "para o gás. Enquanto estava em pé, sua cabeça permanecia acima da camada perigosa. Ao se "
            "agachar, colocou nariz e boca justamente dentro dela. Respirou um ambiente quase sem oxigênio, "
            "ficou confuso e desmaiou antes de perceber que precisava se levantar.\n\n"
            "O socorrista respirou o ar da parte alta da câmara e não foi afetado. Até a perícia chegar, "
            "a abertura da porta e as correntes de ar haviam dispersado o acúmulo, tornando as medições "
            "normais. A ameaça existia apenas na altura exata à qual a curiosidade levou a vítima."
        ),
    },
    "João, o Azarado": {
        "description": (
            "Depois de sobreviver dias à deriva, João alcançou uma ilha habitada. Antes de avistar "
            "qualquer pessoa, sentiu um cheiro que conhecia apenas por causa de sua profissão. Naquele "
            "instante, entendeu que chegar à terra havia diminuído suas chances de viver."
        ),
        "answer": (
            "João era cirurgião. Durante procedimentos, usava eletrocautério para cortar tecido e conter "
            "sangramentos. A fumaça produzida quando a lâmina quente atingia gordura humana tinha um odor "
            "muito particular, impossível de confundir para alguém que passara anos em um centro cirúrgico.\n\n"
            "Ao pisar na ilha, ele sentiu esse mesmo cheiro vindo de fogueiras no interior. Não havia "
            "hospital, energia elétrica ou equipe de resgate; os habitantes estavam assando carne humana. "
            "Restos na praia e o silêncio repentino da mata confirmaram que sua chegada fora percebida.\n\n"
            "Para qualquer outro náufrago, o odor poderia parecer apenas comida queimando. O conhecimento "
            "profissional de João transformou o cheiro em uma sentença: ele escapara do mar sem água, "
            "armas ou forças e acabara de desembarcar no território de um grupo canibal."
        ),
    },
    "Silêncio de Chumbo": {
        "description": (
            "A corda do sino pareceu leve demais. O sineiro puxou-a, nenhum som ecoou e, um segundo depois, "
            "os gritos da praça fizeram-no entender que seria morto por algo que não fizera."
        ),
        "answer": (
            "O sineiro era cego e conhecia a torre pela posição dos degraus, das cordas e pelo peso do sino. "
            "Naquela madrugada, ladrões retiraram o bronze. O padre os surpreendeu; foi amarrado e deixado "
            "desacordado no alto da torre com a própria corda que antes acionava o sino.\n\n"
            "Quando o sineiro chegou para anunciar a missa, não poderia ver que o mecanismo fora desmontado. "
            "A corda parecia estranhamente leve porque já não sustentava o badalo. Seu puxão desfez o nó "
            "improvisado dos ladrões e o corpo do padre caiu diante das pessoas reunidas na praça.\n\n"
            "Para a multidão, causa e efeito pareciam evidentes: o homem puxara a corda e, no mesmo instante, "
            "o padre despencara. O sino ausente também eliminara o som que poderia denunciar o roubo. Sem "
            "conseguir explicar rapidamente o que não enxergara, o sineiro foi tomado pelo assassino e "
            "linchado antes que a torre fosse examinada."
        ),
    },
    "Raiva Imparável": {
        "description": (
            "Kevin nasceu pequeno demais para ser visto sem ajuda, cresceu em uma sala selada e nunca foi "
            "tratado como gente. Quando tentaram matá-lo com o que deveria fazê-lo respirar, abriram o caminho "
            "para que ele matasse todos ao redor."
        ),
        "answer": (
            "Kevin era o apelido dado a um organismo microscópico recolhido de uma amostra espacial. Em uma "
            "estação orbital, pesquisadores o mantinham dentro de uma câmara com nutrientes e atmosfera "
            "controlada. Sem predadores e cercado por alimento, ele aumentou de massa com velocidade anormal.\n\n"
            "A equipe presumiu que o organismo dependia de oxigênio. Quando Kevin rompeu o primeiro recipiente, "
            "eles inundaram a sala com um composto corrosivo destinado a destruir seu sistema respiratório. "
            "Kevin, porém, metabolizava outro gás. O produto não o sufocou: corroeu vedações, sensores e a trava "
            "da porta que ainda o separava da tripulação.\n\n"
            "O plano de contenção transformou uma fuga parcial em acesso ao restante da estação. Já grande, "
            "rápido e capaz de aprender com as tentativas humanas, Kevin eliminou a tripulação e se ocultou em "
            "uma cápsula automática de retorno. Aquilo que deveria obrigá-lo a respirar foi exatamente o que "
            "abriu sua prisão."
        ),
    },
    "Passos Paralelos": {
        "description": (
            "Duas fileiras de pegadas iguais atravessavam a neve lado a lado, como se duas pessoas tivessem "
            "caminhado juntas. Elas começavam separadas, terminavam no mesmo ponto e ali havia apenas um corpo."
        ),
        "answer": (
            "As trilhas pertenciam ao mesmo caçador, mas foram feitas em momentos opostos. Ele entrou na floresta "
            "pela primeira fileira. Quando a nevasca encobriu referências e o obrigou a voltar, encontrou suas "
            "marcas e decidiu caminhar ao lado delas para não apagar o único guia que acreditava possuir.\n\n"
            "O vento arredondou as bordas das pegadas e cobriu a ponta mais profunda deixada pelos dedos do pé. "
            "Sem esses detalhes, tornou-se impossível perceber que uma fileira seguia para dentro e a outra, "
            "teoricamente, para fora. Uma lesão e a baixa visibilidade também fizeram o caçador contornar uma "
            "clareira e reencontrar o próprio rastro pelo lado errado.\n\n"
            "Convencido de que voltava ao abrigo, ele passou a acompanhar as marcas na direção em que originalmente "
            "entrara. Assim, as duas trilhas acabaram avançando juntas para mais longe da saída. O corpo no ponto "
            "final era o de uma única pessoa que, duas vezes, percorreu quase o mesmo caminho."
        ),
    },
    "Último Voo": {
        "description": (
            "Um homem escolheu o assento da janela e passou toda a decolagem olhando para trás. Quando uma linha "
            "específica desapareceu sob as nuvens, ele sorriu, pegou uma pequena lâmina e cortou a própria garganta."
        ),
        "answer": (
            "O homem era um dissidente usado como peça central de uma fuga política. Enquanto a polícia seguia "
            "seus movimentos no aeroporto, outras pessoas da resistência atravessavam áreas restritas disfarçadas "
            "de funcionários. Ele sabia que o governo do destino negociara sua entrega e que, vivo no pouso, seria "
            "interrogado até revelar toda a rede.\n\n"
            "Sua função, portanto, não era sobreviver, mas manter a operação parecendo uma fuga real até que o avião "
            "deixasse o território. Pelo assento da janela, ele podia reconhecer a fronteira costeira. Se morresse "
            "antes, o voo retornaria, o aeroporto seria fechado e os cúmplices ainda em deslocamento seriam capturados.\n\n"
            "Quando a costa ficou para trás, as equipes em solo já tinham cruzado os últimos controles e a aeronave "
            "não poderia voltar a tempo de detê-las. O sorriso era a confirmação de que o plano funcionara. Ele então "
            "levou consigo os nomes e rotas que a tortura procuraria obter."
        ),
    },
    "Suicídio Duplo": {
        "description": (
            "Um passageiro entrou em um táxi, entregou ao motorista um bilhete e sorriu. O motorista leu apenas uma "
            "parte do que estava diante dele, trancou as portas e acelerou para um penhasco. Nenhum dos dois se conhecia."
        ),
        "answer": (
            "O taxista estava em uma crise profunda e criara uma regra irracional para não decidir sozinho: o comportamento "
            "do passageiro seguinte seria o sinal para continuar vivendo ou morrer. Ele não sabia ler, mas escondia o fato "
            "há anos e reconhecia apenas números, placas e algumas palavras memorizadas.\n\n"
            "O passageiro era mudo e acabara de conferir um bilhete de loteria premiado. Escreveu que queria ir ao mirante, "
            "onde a família o esperava, e ofereceu dividir parte do prêmio com o motorista pela ajuda. No papel estavam o "
            "valor milionário, a palavra 'bilhete' e o endereço junto ao penhasco.\n\n"
            "Incapaz de compreender a frase e já dominado pela paranoia, o motorista interpretou a grande quantia e o destino "
            "isolado como uma ameaça de assalto. O sorriso nervoso do passageiro pareceu confirmar sua leitura. Convencido de "
            "que recebera o sinal que esperava, trancou o carro e acelerou antes que o homem pudesse escrever uma explicação."
        ),
    },
    "Passos de Veludo": {
        "description": (
            "Pouco antes de repetir um número que executara centenas de vezes, um artista recebeu da esposa um objeto idêntico "
            "ao que sempre usava. Ele deu poucos passos, nada se rompeu e morreu. A perícia prendeu a esposa por causa do presente."
        ),
        "answer": (
            "O artista era um equilibrista. Para o público, suas sapatilhas pareciam um detalhe de figurino; para ele, eram parte "
            "do sistema de segurança. A borracha macia e limpa criava o atrito necessário para corrigir pequenas oscilações sobre "
            "o cabo, especialmente nos primeiros passos.\n\n"
            "A esposa comprou um par visualmente igual e aplicou uma camada quase invisível de óleo de silicone nas solas. Entregou-o "
            "como presente imediatamente antes da apresentação, quando ele não teria tempo de testar a aderência. Cabo, estrutura, "
            "vento e técnica estavam normais; por isso nenhuma falha aparecia no restante do equipamento.\n\n"
            "Ao transferir o peso para o primeiro pé, a sola deslizou antes que ele pudesse abaixar o centro de gravidade. A queda foi "
            "fatal. O óleo resistiu nas ranhuras e também estava no frasco encontrado entre os pertences da esposa. O presente não "
            "quebrou: funcionou exatamente como ela havia preparado."
        ),
    },
    "O Aquário": {
        "description": (
            "Um hóspede chegou a um hotel à beira-mar, olhou por menos de um minuto para o aquário perfeitamente conservado do saguão "
            "e abandonou a cidade sem fazer o check-in. Horas depois, o hotel foi destruído."
        ),
        "answer": (
            "O homem era oceanógrafo e mergulhador. No aquário, viu espécies de fundo tentando se enterrar ao mesmo tempo em que peixes "
            "de mar aberto nadavam contra o vidro. A água apresentava ondulações regulares apesar de bombas, iluminação e temperatura "
            "estarem normais.\n\n"
            "Ele associou o comportamento a vibrações de baixa frequência transmitidas pelo solo e a pequenas mudanças de pressão. As "
            "ondas sísmicas mais rápidas de um terremoto submarino podiam alcançar a costa antes da grande massa de água deslocada. Os "
            "animais estavam reagindo a sinais que quase ninguém no saguão conseguia perceber.\n\n"
            "O hotel ficava em uma faixa baixa, de frente para a praia, e a estrada para o interior ainda estava livre. Ele não tentou "
            "convencer desconhecidos com uma hipótese que consumiria minutos preciosos: pegou as malas e subiu para terreno alto. O que "
            "destruiu o prédio depois foi o tsunami associado ao abalo."
        ),
    },
    "Arrependido para Sempre": {
        "description": (
            "Ao abrir uma antiga taça, um pesquisador encontrou algo que não valia nada e não podia feri-lo naquele instante. Depois de "
            "examinar uma amostra, mandou selar a descoberta e decidiu nunca mais se aproximar de outra pessoa."
        ),
        "answer": (
            "O pesquisador era egiptólogo e a taça estava em uma câmara funerária que permanecera hermética por milênios. O pó escuro no "
            "interior não era veneno nem tesouro: continha esporos preservados de uma linhagem de fungo desconhecida. Ao retirar a tampa, "
            "ele levantou uma nuvem fina e a respirou sem perceber.\n\n"
            "No laboratório móvel, a amostra germinou à temperatura corporal. Os testes indicaram que o fungo colonizava os pulmões, "
            "ficava assintomático por semanas e depois liberava novos esporos na respiração. Quando os primeiros sinais surgissem, ele já "
            "teria contaminado todos com quem convivesse.\n\n"
            "A taça não o matou no momento da abertura; deu-lhe tempo suficiente para entender o que aconteceria. Como já passara horas "
            "sem proteção dentro da tumba, considerou-se infectado. Selou o sítio, comunicou o risco à distância e escolheu isolamento "
            "permanente para que seu próprio corpo não transformasse a descoberta em uma epidemia."
        ),
    },
    "Maré Tardia": {
        "description": (
            "Gustavo entrou andando em um quarto seco, conversou normalmente no corredor e trancou a porta por dentro. Três horas depois, "
            "estava morto. Não havia água suficiente em nenhum lugar do quarto, mas o laudo descreveu uma morte por afogamento."
        ),
        "answer": (
            "O evento fatal começara antes de Gustavo entrar no quarto. Durante uma festa no hotel, ele ficara submerso na piscina e fora "
            "retirado inconsciente. Depois de tossir e recuperar a fala, recusou atendimento porque parecia ter voltado ao normal. Trocar "
            "a roupa e caminhar sozinho mascararam a gravidade do que havia aspirado.\n\n"
            "A água e os contaminantes irritaram os alvéolos e prejudicaram o surfactante que os mantém abertos. Nas horas seguintes, a "
            "inflamação aumentou a passagem de líquido para o tecido pulmonar. A troca de oxigênio piorou de forma silenciosa enquanto "
            "Gustavo descansava, já longe da piscina.\n\n"
            "Quando a falta de oxigênio provocou confusão e perda de consciência, ele estava sozinho e a porta trancada impediu ajuda "
            "rápida. Assim, o quarto não precisava conter água nem um agressor. A cena final era seca porque a causa fora transportada nos "
            "próprios pulmões desde o episódio anterior."
        ),
    },
    "O Vazio Perfeito": {
        "description": (
            "Dois técnicos foram encontrados no fundo de um reservatório aberto, vazio e seco. O segundo descera para salvar o primeiro, "
            "mas caiu antes de alcançá-lo. Não havia fumaça, cheiro, veneno detectável ou qualquer ferimento nos corpos."
        ),
        "answer": (
            "Horas antes, uma linha usada em soldagem despejara argônio no reservatório para impedir a oxidação do metal. O serviço fora "
            "encerrado, o líquido drenado e a escotilha aberta; por isso o espaço parecia seguro. O argônio, porém, é incolor, inodoro e "
            "não causa a ardência que faria alguém recuar.\n\n"
            "Mais denso que o ar, ele permaneceu acumulado no fundo, como um lago invisível. Não era um veneno a ser encontrado no sangue. "
            "Simplesmente ocupava o volume onde deveria haver oxigênio. O primeiro técnico respirou algumas vezes, ficou confuso e perdeu "
            "a consciência sem conseguir subir.\n\n"
            "Visto de cima, aquilo pareceu um desmaio comum. O segundo técnico entrou por impulso, sem linha de resgate ou medidor, e abaixou "
            "a cabeça justamente na camada pobre em oxigênio. A escotilha aberta ventilava apenas a parte alta; o vazio do tanque estava, "
            "na verdade, preenchido pelo que ninguém podia perceber."
        ),
    },
    "Sem Tocar o Chão": {
        "description": (
            "O equipamento impediu que um trabalhador atingisse o chão. Ele não bateu em nada, permaneceu consciente e conversou durante "
            "todo o resgate. Quando finalmente foi colocado em segurança, desmaiou e morreu."
        ),
        "answer": (
            "O cinto interrompeu a queda, mas deixou o trabalhador suspenso na vertical por quase meia hora. As tiras pressionavam a virilha "
            "e ele mal conseguia mover as pernas. Sem a contração dos músculos da panturrilha, grande parte do sangue ficou represada nos "
            "membros inferiores.\n\n"
            "A redução progressiva do retorno venoso obrigou o coração a trabalhar com menos volume. Ainda havia sangue suficiente para ele "
            "falar e responder, o que fez a equipe subestimar a urgência, mas a irrigação do cérebro e dos órgãos já estava no limite. A "
            "posição aparentemente segura era a própria ameaça.\n\n"
            "No fim do resgate, a mudança brusca de posição somou-se ao colapso circulatório e à resposta do organismo ao período de suspensão. "
            "Ele perdeu a consciência e entrou em parada cardíaca. Nada precisava se romper: o sistema salvou-o do impacto inicial, mas não "
            "eliminou o risco de permanecer imóvel e pendurado por tanto tempo."
        ),
    },
    "O Primeiro Banquete": {
        "description": (
            "Quando Mauro voltou para casa, a família decidiu compensar, em poucas horas, tudo o que lhe faltara durante semanas. Ninguém "
            "errou uma dose, ninguém o feriu e tudo o que lhe ofereceram estava perfeito. Antes do amanhecer, o gesto de carinho o matou."
        ),
        "answer": (
            "Mauro havia sido resgatado após semanas com alimentação quase inexistente. Para sobreviver, seu corpo reduzira a produção de "
            "insulina, consumira gordura e proteína e esgotara reservas intracelulares de fosfato, potássio, magnésio e tiamina. Ele estava "
            "consciente e podia parecer estável, mas esse equilíbrio dependia justamente da escassez.\n\n"
            "A família preparou um grande jantar rico em carboidratos e insistiu para que ele repetisse. A entrada repentina de glicose provocou "
            "uma descarga de insulina. Para metabolizá-la, as células puxaram do sangue os poucos eletrólitos restantes; água e sódio também "
            "foram retidos. Em poucas horas, a composição do sangue mudou de forma perigosa.\n\n"
            "A queda de fosfato comprometeu a energia das células cardíacas e respiratórias, enquanto potássio e magnésio baixos favoreceram "
            "uma arritmia fatal. Não havia veneno, alergia nem comida estragada: qualquer pessoa saudável poderia comer o mesmo. Mauro precisava "
            "de porções pequenas, reposição de vitaminas e eletrólitos e monitoramento — não de recuperar semanas de fome em uma noite."
        ),
    },
    "A Distância Imóvel": {
        "description": (
            "Um mecânico foi encontrado morto no centro de uma oficina trancada. Sofrera um único impacto, mas o objeto que o atingira não "
            "estava perto do corpo. Nenhuma máquina funcionava e o único veículo no galpão não saíra do lugar."
        ),
        "answer": (
            "O caminhão tinha uma roda antiga de aro multipartido. Nesse sistema, um anel metálico encaixado em um sulco retém o conjunto "
            "quando o pneu é inflado. Depois de uma manutenção, o mecânico deixou o anel aparentemente colocado, mas uma pequena parte não "
            "assentou por completo.\n\n"
            "O pneu recebeu pressão e permaneceu estável por alguns minutos. Essa calma ocultava enorme energia no ar comprimido. Quando o "
            "mecânico se aproximou para uma inspeção final, o anel escapou do sulco e foi lançado de lado como um projétil de aço. A peça o "
            "atingiu uma única vez e continuou atravessando o galpão.\n\n"
            "Ela caiu atrás de materiais empilhados, longe do corpo, e não pareceu imediatamente parte da roda. Por isso não havia arma ao "
            "lado da vítima nem marca de deslocamento do caminhão. A força não veio de um motor ou de outra pessoa; estava armazenada havia "
            "minutos dentro de algo que parecia completamente imóvel."
        ),
    },
    "A Outra Metade": {
        "description": (
            "Um técnico esperou a única parte visível de uma máquina subir, confirmou que ela continuava se afastando e entrou no espaço "
            "abaixo. Segundos depois, foi esmagado por algo que descia. Nada caiu, nada mudou de direção e a máquina funcionou normalmente."
        ),
        "answer": (
            "A máquina era um elevador de tração. A cabine que o técnico observava representava apenas metade do sistema. Do outro lado dos "
            "cabos havia um contrapeso pesado, guiado por trilhos próprios: quando a cabine sobe, o contrapeso necessariamente desce.\n\n"
            "O técnico verificou a posição da cabine, mas entrou no fundo do poço pela lateral ocupada pela trajetória do contrapeso. Como a "
            "massa se movia dentro de guias escuras e quase sem ruído, ela não aparecia no campo de visão que ele usara para decidir que o "
            "espaço estava livre.\n\n"
            "A cabine continuou subindo exatamente como ele previra. Esse movimento, longe de afastar todo o perigo, trazia a outra metade do "
            "sistema em sua direção. O técnico foi prensado entre o contrapeso e a estrutura inferior. Nenhuma peça se soltou e nenhum comando "
            "falhou: o acidente ocorreu porque ele interpretou um movimento correto como prova de segurança."
        ),
    },
    "Cinzas sem Testemunha": {
        "description": (
            "Um apartamento vazio pegou fogo em plena tarde. A energia estava desligada, não havia gás, chama, cigarro ou sinal de entrada. "
            "As janelas continuavam fechadas e tudo que poderia iniciar o incêndio parecia frio."
        ),
        "answer": (
            "Uma garrafa transparente parcialmente cheia de água ficara no parapeito. O recipiente curvo combinava duas superfícies capazes "
            "de refratar a luz. Durante a maior parte do dia, isso não produzia nada além de reflexos; em um intervalo específico, o sol "
            "atravessava a janela no ângulo exato para formar um foco intenso.\n\n"
            "Esse pequeno ponto de luz permanecia sobre uma dobra escura da cortina. O tecido absorveu calor por vários minutos, começou a "
            "carbonizar e criou uma brasa escondida entre as camadas. Só depois a brasa encontrou oxigênio suficiente para formar chama e "
            "alcançar o restante do cômodo.\n\n"
            "Quando os bombeiros chegaram, a fumaça havia escurecido a garrafa e o incêndio deslocara o tecido, desfazendo o alinhamento que "
            "explicaria a origem. Não existia uma fonte quente permanente para a perícia encontrar. Um objeto frio e inofensivo apenas "
            "concentrou, por tempo suficiente, a energia que vinha de fora do apartamento."
        ),
    },
    "A Companhia Ausente": {
        "description": (
            "Lívia entrou sozinha em um elevador. Antes que a cabine chegasse ao andar seguinte, seu companheiro — que permanecera no corredor "
            "e não fora atingido pela porta — morreu. Nenhuma pessoa o tocou e Lívia só percebeu quando já era tarde."
        ),
        "answer": (
            "O companheiro de Lívia era um cão pequeno preso a uma guia longa. Ela entrou na cabine olhando para o painel, mas o animal hesitou "
            "e permaneceu no corredor. A guia era fina demais para ser percebida corretamente pelo sensor, e as portas se fecharam entre a "
            "mulher e o cão.\n\n"
            "Quando a cabine começou a subir, a fita deslizou até ficar presa na fresta entre porta, piso e elevador. A extremidade dentro da "
            "cabine subiu com Lívia; a outra, ligada à coleira, foi tensionada contra o animal. A porta em si nunca o atingiu, e não havia uma "
            "pessoa do lado de fora puxando a guia.\n\n"
            "O movimento vertical multiplicou a força rápido demais para que Lívia alcançasse o botão de emergência. Como o cão nunca entrara, "
            "as câmeras internas mostravam a cabine ocupada apenas por ela. A companhia ausente estava conectada ao elevador por algo estreito "
            "o bastante para quase desaparecer na cena."
        ),
    },
    "A Queda Horizontal": {
        "description": (
            "Dentro de uma sala nivelada, um cilindro fechado atravessou o ar e matou um homem. Ninguém o empurrou, ele não explodiu e o "
            "equipamento mais poderoso do ambiente parecia não estar funcionando."
        ),
        "answer": (
            "A sala era de ressonância magnética. O aparelho não precisava estar produzindo imagens para representar perigo: seu ímã "
            "supercondutor permanecia energizado continuamente. O silêncio e a ausência de luzes de exame faziam visitantes acreditarem "
            "que a máquina estava desligada.\n\n"
            "Durante a transferência de um paciente, alguém levou para além da linha de segurança um cilindro de oxigênio feito de material "
            "ferromagnético. Quanto mais perto do túnel, maior a força exercida pelo campo. Em poucos instantes, o cilindro deixou o carrinho "
            "e acelerou horizontalmente em direção ao centro do ímã.\n\n"
            "O recipiente não vazou e sua válvula permaneceu fechada; o oxigênio não teve participação na morte. Foi a massa metálica que "
            "se transformou em projétil e atingiu o paciente. O chão nivelado e a ausência de empurrão eram irrelevantes porque a força que "
            "o moveu não dependia da gravidade nem de contato humano."
        ),
    },
    "O Mar Amarelo": {
        "description": (
            "Um trabalhador caminhava sobre uma superfície firme e nivelada quando começou a afundar. Em segundos, desapareceu por completo. "
            "Não havia lama, água, abertura no piso ou desabamento ao redor."
        ),
        "answer": (
            "A superfície não era um piso, mas a parte superior de toneladas de grãos dentro de um silo. Umidade e pressão haviam formado uma "
            "crosta rígida, uma ponte que parecia sustentar o peso de uma pessoa. Abaixo dela, porém, o sistema de descarga retirava material "
            "e deixava uma cavidade invisível.\n\n"
            "Quando o trabalhador alcançou a região oca, a crosta rompeu. Ele caiu no vazio e imediatamente foi cercado por grãos que se "
            "comportavam como um fluido. Ao mesmo tempo, o transportador no fundo continuava puxando o conteúdo para a saída, criando uma "
            "corrente descendente.\n\n"
            "Tentar mover as pernas aumentava a pressão do material ao redor, e a força necessária para retirar um membro enterrado superava "
            "o que ele podia produzir. Em poucos segundos, o grão atingiu o tórax, impediu sua expansão e cobriu as vias respiratórias. O mar "
            "amarelo parecia sólido apenas porque sua superfície escondia o movimento que acontecia por baixo."
        ),
    },
    "A Pausa na Soleira": {
        "description": (
            "Um bombeiro chegou a uma porta sabendo que ainda havia alguém do outro lado. Em vez de abri-la, proibiu a entrada e mandou a "
            "equipe recuar. Segundos depois, o cômodo explodiu — e sua recusa foi considerada a decisão correta."
        ),
        "answer": (
            "O incêndio dentro do apartamento já consumira quase todo o oxigênio. Sem ar suficiente, as chamas diminuíram, mas móveis e "
            "revestimentos continuavam submetidos a calor extremo e liberavam gases combustíveis. O ambiente parecia menos ativo justamente "
            "quando acumulava a mistura mais perigosa.\n\n"
            "Pelas frestas, o bombeiro viu fumaça escura sendo sugada para dentro e expelida em pulsos. A maçaneta estava quente e a porta "
            "parecia respirar. Eram sinais de um backdraft: abrir de imediato forneceria uma grande quantidade de oxigênio aos gases "
            "superaquecidos e colocaria a frente de combustão no corredor.\n\n"
            "Ele ordenou ventilação e afastamento antes de qualquer entrada. A explosão ocorreu quando uma falha estrutural permitiu a entrada "
            "de ar por outro ponto, confirmando o diagnóstico. A vítima interna já sucumbira à fumaça; abrir a porta alguns segundos antes "
            "não a salvaria e posicionaria toda a equipe no caminho da combustão."
        ),
    },
    "A Noite em Marcha": {
        "description": (
            "Uma família foi encontrada morta durante o sono. O carro na garagem estava desligado, frio, com o tanque quase cheio e a chave "
            "na cozinha. Não havia vazamento na casa; ainda assim, aquele carro matara todos sem sair do lugar."
        ),
        "answer": (
            "O veículo tinha um sistema de partida remota instalado pelo antigo dono. O controle não precisava da chave na ignição e estava "
            "configurado para repetir ciclos curtos em noites frias. Durante o sono, ficou pressionado entre o colchão e a mão de uma das "
            "vítimas, ativando o programa sem produzir um som perceptível nos quartos.\n\n"
            "Com a porta da garagem fechada, cada ciclo acumulou monóxido de carbono. O gás não tem cor nem cheiro e atravessou frestas e um "
            "duto de retorno de ar ligado à casa. As vítimas ficaram progressivamente sonolentas e incapazes de notar dor de cabeça ou "
            "confusão antes de perderem a consciência.\n\n"
            "O último ciclo terminou horas antes da descoberta. O motor esfriou, parte dos gases se dispersou e o tanque continuou quase "
            "cheio porque poucos minutos de funcionamento bastaram para contaminar um espaço fechado. A chave na cozinha parecia provar que "
            "o carro não ligara, mas o verdadeiro comando jamais precisou dela."
        ),
    },
    "Depois do Silêncio": {
        "description": (
            "Um técnico desligou uma prensa, bloqueou o comando e esperou até o último ruído desaparecer. Ninguém tocou no painel. Dentro "
            "da máquina silenciosa, ele foi morto por um movimento que não precisava de eletricidade."
        ),
        "answer": (
            "O bloqueio interrompeu a alimentação elétrica e impediu que outra pessoa ligasse o motor. Isso eliminou apenas uma das fontes "
            "de energia. O circuito hidráulico continuava pressurizado por um acumulador, e a enorme placa mantida no alto armazenava energia "
            "potencial devido ao próprio peso.\n\n"
            "O técnico não sangrou a pressão residual nem instalou um calço mecânico rígido entre as partes móveis. Enquanto trabalhava na "
            "zona de esmagamento, uma pequena fuga interna na válvula permitiu que o fluido mudasse de lado. A gravidade começou a baixar a "
            "placa e a pressão restante acelerou o movimento.\n\n"
            "Nenhum motor precisou girar, portanto não houve aviso sonoro. O cadeado no comando continuou intacto e ninguém violou o "
            "procedimento elétrico. A falha foi tratar ausência de ruído como ausência de energia: a máquina estava desligada, mas ainda não "
            "estava descarregada nem fisicamente impedida de se mover."
        ),
    },
    "A Altura Perdida": {
        "description": (
            "Um mecânico entrou sob um ônibus parado em piso plano. O motor estava desligado, as rodas calçadas e o veículo não avançou nem "
            "um centímetro. Minutos depois, ele foi esmagado, embora nenhuma peça tivesse caído."
        ),
        "answer": (
            "A carroceria do ônibus era sustentada por bolsas de ar da suspensão pneumática. Com o motor funcionando, um compressor mantinha "
            "a pressão e a altura do chassi. Depois que o veículo foi desligado, uma mangueira danificada começou a perder ar lentamente, sem "
            "ruído suficiente para chamar atenção na oficina.\n\n"
            "As rodas permaneceram apoiadas exatamente no mesmo ponto e os calços cumpriram sua função. O que mudou foi a distância entre os "
            "eixos e a carroceria: à medida que as bolsas esvaziavam, todo o chassi descia alguns centímetros. O mecânico estava justamente "
            "no espaço que essa descida eliminava.\n\n"
            "Como confiou na suspensão e não colocou cavaletes rígidos sob a estrutura, não havia nada que limitasse o rebaixamento. O ônibus "
            "não precisou se deslocar, tombar ou perder uma peça. Seu peso já estava sobre o mecânico em potencial; bastou desaparecer o "
            "colchão de ar que o mantinha afastado do chão."
        ),
    },
}


def deepen_story_mysteries(apps, schema_editor):
    Story = apps.get_model("stories", "Story")

    for title, revision in STORY_REVISIONS.items():
        Story.objects.filter(title=title).update(**revision)


class Migration(migrations.Migration):
    dependencies = [
        ("stories", "0006_add_realistic_story_collection"),
    ]

    operations = [
        migrations.RunPython(deepen_story_mysteries, migrations.RunPython.noop),
    ]
