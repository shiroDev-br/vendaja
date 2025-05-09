Scaffold do Projeto & Controle de Versão

Crie o repositório Git e defina a estrutura de pastas (app/, tests/, infra/, docs/).

Configure seu ambiente Python (venv/pyenv) e o requirements.txt.

Implemente um endpoint “Hello World” em FastAPI só para validar que o app sobe localmente.

Primeiros Endpoints Core

Modele suas entidades básicas (Store, Product, Sale, Receipt) em SQLAlchemy (ou outro ORM).

Crie o endpoint POST /sales/ com validações mínimas e persista no banco em memória (SQLite).

Escreva um teste “smoke” que confirma que /sales/ devolve 200 no fluxo feliz.

Banco de Dados & Migrações

Troque o SQLite em memória por PostgreSQL local (via Docker).

Adicione Alembic (ou similar) e escreva suas primeiras migrações para criar tabelas.

Ajuste a fixture de testes para apontar para esse Postgres de desenvolvimento.

Docker Compose para Dev Local

Crie Dockerfile para a API e docker-compose.yml incluindo Postgres, Redis e RabbitMQ.

Valide que, ao rodar docker-compose up --build, tudo sobe (web + banco + cache + fila).

Celery & Tarefas Assíncronas

Configure Celery apontando para RabbitMQ/Redis.

Implemente a task de “emitir recibo” (simulada) e teste localmente com celery -A app.celery_app worker.

Garanta que, ao chamar /sales/, a task é enfileirada.

Cache & Rate-Limit

Integre Redis para cachear o endpoint de dashboard (ou qualquer operação pesada).

Adicione rate-limit básico no /sales/ (ex.: 100 req/min/loja).

Testes Automatizados

Amplie sua cobertura: crie testes para fluxos “invalid payload”, “erro na task” e “reenvio de recibo”.

Mock das integrações (API fiscal, WhatsApp) usando monkeypatch no pytest.

Integre pytest-cov para medir cobertura.

CI/CD Básico

Configure um pipeline (GitHub Actions/GitLab CI) que rode: lint (black/flake8), testes (pytest), build Docker.

No merge em main, publique a imagem em um registry.

Deploy Inicial (Dev/Staging) em Kubernetes

Crie manifests mínimos (Deployment, Service) para API e worker; use ConfigMaps/Secrets para credenciais.

Configure um Ingress (ou LoadBalancer) para expor a API.

Aplique kubectl apply -f infra/k8s/ em um cluster de teste.

Monitoramento & Observabilidade

Instale o Prometheus + Grafana no cluster de staging para coletar métricas de latência e uso de CPU.

Configure Sentry (ou ferramenta similar) para capturar erros em produção.

Teste health-checks e auto-heal (kube liveness/readiness probes).