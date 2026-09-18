# Black Stories

Aplicação Django para partidas presenciais de enigmas sombrios. O mestre escolhe um caso, lê o enunciado em voz alta e conduz os jogadores até a solução respondendo apenas **sim**, **não**, **irrelevante** ou pedindo que reformulem a pergunta.

## Recursos

- Biblioteca com busca, sorteio e visualização em grade ou lista.
- Tela de investigação com cronômetro, notas locais e revelação da solução.
- Guia completo do mestre com imagens e respostas rápidas.
- Cadastro de novos casos restrito a usuários da equipe.
- Layout responsivo e acessível para celular, tablet e computador.
- Configurações prontas para Render, incluindo health check e arquivos estáticos.

## Executar localmente

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

Abra `http://127.0.0.1:8000/`.

## Qualidade

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
.\.venv\Scripts\python.exe manage.py collectstatic --no-input
```

## Publicação

O arquivo `render.yaml` configura o plano gratuito. Ele inicia com 13 casos a partir de `stories/seed.sqlite3`, que não contém usuários, senhas ou sessões.

Para criar um administrador no primeiro início, configure no Render:

- `DJANGO_SUPERUSER_USERNAME`
- `DJANGO_SUPERUSER_PASSWORD`
- `DJANGO_SUPERUSER_EMAIL` (opcional)

Não coloque essas credenciais no repositório.

O sistema de arquivos do plano gratuito é temporário. Novos casos e uploads podem desaparecer após reinícios. Para armazenamento permanente, use `render.persistent.yaml` ou migre os dados para PostgreSQL e as imagens para um serviço de arquivos.
