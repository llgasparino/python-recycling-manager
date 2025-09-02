# python-recycling-manager

Projeto acadêmico: aplicação Flask simples para agendar entrega de descarte eletrônico para um micro-empreendedor.

## Execução local

Clonar e instalar dependências:

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows Git Bash
pip install -r requirements.txt
flask --app recycling_manager run --debug
```

Ou com `python` direto:

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

Acessar: http://localhost:5000

### Modo desenvolvimento (com hot-reload opcional)

Para desenvolvimento você pode montar o volume do código local:

```bash
docker run --rm -it -p 5000:5000 -v $(pwd)/recycling_manager:/app/recycling_manager -e FLASK_ENV=development recycling-manager:latest
```

## Pipeline (CI)

O workflow atual executa lint (flake8) a cada push/PR em `main`.

## Próximos passos sugeridos

- Adicionar testes (pytest)
- Publicar imagem no Docker Hub via GitHub Actions
- Adicionar variáveis de ambiente para configuração

---

Autor: Luiz
