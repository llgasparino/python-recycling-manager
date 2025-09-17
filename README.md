[![Docker Image Version (latest by date)](https://img.shields.io/docker/v/llgasparino/recycling-manager?sort=date)](https://hub.docker.com/r/llgasparino/recycling-manager)
[![Docker Pulls](https://img.shields.io/docker/pulls/llgasparino/recycling-manager)](https://hub.docker.com/r/llgasparino/recycling-manager)
[![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/llgasparino/recycling-manager?sort=date)](https://hub.docker.com/r/llgasparino/recycling-manager)

# python-recycling-manager

Site para agendamento e consulta de pontos de reciclagem tech em Curitiba, com layout moderno, modo claro/escuro, integração com Discord e CI/CD automatizado.

Veja o site rodando localmente ou via Docker, e confira o layout:

🔗 [Acesse o site local](http://localhost:5000)

## Funcionalidades

- Landing page estilizada para reciclagem tech
- Modo claro/escuro com botão no topo
- Consulta de ponto de reciclagem com mapa embed
- Seção "O Que Reciclamos?" com ícones
- Footer com link especial no ano
- Página de erro personalizada
- Testes automáticos (pytest)
- Pipeline CI/CD com notificações no Discord

## Execução local

Clone o projeto e instale as dependências:

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows Git Bash
pip install -r requirements.txt
flask --app recycling_manager run --debug
```

Ou rode direto:

```bash
python app.py
```

## Docker

Build da imagem:

```bash
docker build -t recycling-manager:latest .
```

Rodar container:

```bash
docker run --rm -p 5000:5000 recycling-manager:latest
```

Acesse: [http://localhost:5000](http://localhost:5000)

### Modo desenvolvimento (hot-reload)

Para desenvolvimento, monte o volume do código local:

```bash
docker run --rm -it -p 5000:5000 -v $(pwd)/recycling_manager:/app/recycling_manager -e FLASK_ENV=development recycling-manager:latest
```

## Pipeline (CI/CD)

O workflow executa lint, testes automáticos e build/push da imagem Docker a cada push ou PR. Notificações são enviadas para o Discord do projeto.

## Próximos passos sugeridos

- Melhorar cobertura de testes
- Adicionar autenticação de usuário
- Permitir cadastro de novos pontos de reciclagem
- Dashboard para microempreendedores

---

---

Autor: Luiz Gasparino
