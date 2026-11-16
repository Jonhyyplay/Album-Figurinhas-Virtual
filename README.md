# Álbum de Figurinhas Virtual

> Uma aplicação web interativa simulando um álbum de figurinhas "flip book", orquestrando um frontend nativo de alta performance com uma API RESTful assíncrona em Python.

![Python](https://img.shields.io/badge/Backend-Python_&_FastAPI-blue)
![Frontend](https://img.shields.io/badge/Frontend-Vanilla_JS_&_CSS3-yellow)
![API](https://img.shields.io/badge/Integração-RESTful_API-green)

---

## 📋 Sobre o Projeto

Este projeto foi desenvolvido para demonstrar a construção de uma **arquitetura Full-Stack leve e desacoplada**, sem a necessidade de *frameworks* de interface pesados (como React ou Vue).

O objetivo principal é recriar a experiência tátil e imersiva de um álbum físico, com animações 3D de páginas e síntese de áudio em tempo real, alimentada por uma infraestrutura de API RESTful projetada para alta disponibilidade e baixa latência no envio de dados e assets multimídia.

---

## 🧠 Arquitetura e Engenharia do Sistema

O sistema adota uma separação clara de responsabilidades orientada a consumo de serviços REST:

### Backend (Python & FastAPI)

* **API RESTful Assíncrona:** Rotas estruturadas para servir metadados dos colecionáveis com baixo overhead.
* **Asset Streaming:** Utilização de `FileResponse` otimizado para entrega dinâmica de imagens dos cards.
* **Segurança e Integração:** Configuração granular de políticas de **CORS Middleware** permitindo requisições cross-origin controladas.
* **Autodocumentação:** Suporte nativo ao padrão OpenAPI com interface interativa (Swagger UI) disponível *out-of-the-box*.

### Frontend (Vanilla JS Architecture)

* **DOM Manipulation Engine:** Gerenciamento nativo de estado e renderização do DOM sem abstrações pesadas de Virtual DOM, garantindo taxa de quadros (FPS) constante.
* **Web Audio API:** Síntese sonora programática (White Noise + Filtros Biquad) para gerar o efeito tátil de folhear papel em tempo real, sem dependência de arquivos de áudio externos.
* **Physics & Rendering:** Integração com a biblioteca `St.PageFlip` para cálculo de física 3D de dobra e caimento das páginas.
* **Asynchronous Data Fetching:** Camada de serviço em JS ES6+ utilizando Fetch API para sincronização com o backend.

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologia / Ferramenta | Aplicação Prática |
| :--- | :--- | :--- |
| **Backend** | Python 3.10+ | Linguagem base de alta produtividade |
| | FastAPI | Framework web moderno, assíncrono e de alto desempenho |
| | Uvicorn | Servidor ASGI para execução concorrente |
| **Frontend** | JavaScript (ES6+) | Lógica de aplicação nativa e manipulação do DOM |
| | Web Audio API | Engenharia de som via código [síntese auditiva] |
| | CSS3 / HTML5 | Layout responsivo e aceleração de hardware 3D |
| **Bibliotecas** | St.PageFlip | Renderização da física de páginas |

---

## 🚀 Guia de Instalação e Execução

### 1. Configuração do Servidor Backend (API)

Requer Python 3.10 ou superior. Pode executar os comandos abaixo para inicializar o ambiente virtual e o servidor ASGI:

```powershell
# Acesse o diretório do backend
cd Backend

# Crie e ative o ambiente virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instale as dependências da aplicação
python -m pip install fastapi uvicorn

# Inicie o servidor em modo de desenvolvimento
python -m uvicorn main:app --reload
```

### 1.1 Demonstração
https://github.com/user-attachments/assets/4d25fca7-a1e5-40df-a601-2a040b4b13f4

### 2. Configuração da Interface Frontend
Com a API rodando no terminal principal:

1. Navegue até o diretório `Frontend`.
2. Execute o arquivo `index.html` através de um servidor HTTP local (recomendado: extensão **Live Server** do VS Code ou `python -m http.server` no diretório).
3. O cliente iniciará a comunicação assíncrona com `http://localhost:8000` (`API_BASE_URL`), mapeando e preenchendo os slots das figurinhas dinamicamente.
> 💡 Com o servidor ativo em `http://localhost:8000`, a especificação interativa das rotas pode ser inspecionada diretamente em `http://localhost:8000/docs`.
