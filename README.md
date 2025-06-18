# Heart Failure Prediction Web App

## Descrição do Projeto

Este projeto é uma aplicação web para predição de doenças cardíacas, utilizando técnicas de aprendizado de máquina. O objetivo é permitir que os usuários enviem dados clínicos e recebam de volta a predição correspondente.

### Atenção

Este projeto é apenas um modelo desenvolvido para estudos e não deve ser usado para diagnósticos médicos reais.
Sempre consulte um profissional de saúde qualificado para questões médicas.

### Pré-requisitos

- [Python](https://www.python.org/downloads/) (versão 3.8 ou superior)
- Virtualenv (opcional, mas recomendado)

## Execução do Projeto

1. Clone o repositório.

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie o backend da API:

```bash
cd server
flask run --host 0.0.0.0 --port 5000
```

5. Com o backend em execução, navegue até o diretório `web` e abra diretamente o arquivo `index.html` no seu navegador:

```bash
cd web
open index.html # macOS
start index.html # Windows
xdg-open index.html # Linux
```
