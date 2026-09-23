# Publicar gratuitamente no Render

1. Envie este projeto para um repositório Git.
2. No Render, escolha **New > Blueprint**.
3. Conecte o repositório e selecione `render.yaml`.
4. Confirme a criação do serviço e aguarde o health check em `/health/`.

O Render gera a `SECRET_KEY` e configura HTTPS automaticamente. O primeiro início copia o banco limpo `stories/seed.sqlite3` e as imagens existentes para a área de dados da aplicação.

## Administração

O cadastro de histórias não fica disponível para visitantes. Para habilitá-lo ao administrador, adicione as variáveis secretas `DJANGO_SUPERUSER_USERNAME` e `DJANGO_SUPERUSER_PASSWORD` no painel do serviço e faça um novo deploy.

## Limite do plano gratuito

No modo gratuito, banco e uploads adicionados durante o uso não são permanentes. Depois de uma reinicialização ou nova publicação, o site volta aos 27 casos incluídos no projeto. Para persistir novos casos, use a configuração `render.persistent.yaml` ou serviços externos de banco e armazenamento.
