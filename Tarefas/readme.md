# Gerenciador de tarefas

Projeto Flask com ambiente e dependências gerenciados pelo `uv`.

## Preparar o projeto

Abra o terminal na pasta que contém `pyproject.toml` e execute:

```powershell
uv sync
```

Configure o arquivo `.env` com os dados do seu MySQL. Use `.env.example` como modelo.

## Executar

```powershell
uv run python -m tarefas.app
```

O servidor ficará disponível em `http://127.0.0.1:5000`.

Para testar se está online, acesse `http://127.0.0.1:5000/test`.

O banco e a tabela são inicializados quando o arquivo `app.py` é executado diretamente.
O MySQL precisa estar instalado e em execução.
