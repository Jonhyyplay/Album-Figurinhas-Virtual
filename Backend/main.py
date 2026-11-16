from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi import HTTPException  # Avisa quando uma imagem não existir
from fastapi.responses import FileResponse # Envia o arquivo da imagem direto ao navegador
from fastapi.middleware.cors import CORSMiddleware  # Libera o acesso do Frontend
import os
import glob  # Busca arquivos no computador usando padrões de texto

# Inicializa a aplicação FastAPI
app = FastAPI()

PASTA_BASE = os.path.dirname(os.path.abspath(__file__)) # Aqui descobre onde a main.py está agora
PASTA_IMAGENS = os.path.join(PASTA_BASE, "Images") # Aponta para a pasta Imagens (as figurinhas) dentro da pasta Backend

#app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs") # Monta a pasta de imagens para ser acessada via URL

app.add_middleware( # Configuração do CORS para permitir que o frontend acesse a API
    CORSMiddleware,
    allow_origins=["*"],  # Permite que qualquer origem acesse a API
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Listar as figurinhas
Figurinhas = [
        
        {"id": 1, 
         "nome": "Alan Turing", 
         "categoria": "IA",
         "imagem_url": "/figurinhas/1/imagem"
        },

        {"id": 2, 
         "nome": "John McCarthy", 
         "categoria": "IA",
         "imagem_url": "/figurinhas/2/imagem"
        },

        {"id": 3, 
         "nome": "Sam", 
         "categoria": "IA",
         "imagem_url": "/figurinhas/3/imagem"
        },

        {"id": 4, 
         "nome": "Geoffrey", 
         "categoria": "IA",
         "imagem_url": "/figurinhas/4/imagem"
        },

        {"id": 5, 
         "nome": "Yann", 
         "categoria": "IA",
         "imagem_url": "/figurinhas/5/imagem"
        },

        {"id": 6, 
         "nome": "Guido", 
         "categoria": "Python",
         "imagem_url": "/figurinhas/6/imagem"
        },

        {"id": 7, 
         "nome": "Tim", 
         "categoria": "Python",
         "imagem_url": "/figurinhas/7/imagem"
        },

        {"id": 8, 
         "nome": "Ray", 
         "categoria": "Python",
         "imagem_url": "/figurinhas/8/imagem"
        },

        {"id": 9, 
         "nome": "Travis", 
         "categoria": "Python",
         "imagem_url": "/figurinhas/9/imagem"
        },

        {"id": 10, 
         "nome": "Wes", 
         "categoria": "Python",
         "imagem_url": "/figurinhas/10/imagem"
        },

        {"id": 11, 
         "nome": "Edgar", 
         "categoria": "Banco de Dados",
         "imagem_url": "/figurinhas/11/imagem"
        },

        {"id": 12, 
         "nome": "Larry", 
         "categoria": "Banco de Dados",
         "imagem_url": "/figurinhas/12/imagem"
        },

        {"id": 13, 
         "nome": "Michael", 
         "categoria": "Banco de Dados",
         "imagem_url": "/figurinhas/13/imagem"
        },

        {"id": 14, 
         "nome": "Salvatore", 
         "categoria": "Banco de Dados",
         "imagem_url": "/figurinhas/14/imagem"
        },

        {"id": 15, 
         "nome": "Eliot", 
         "categoria": "Banco de Dados",
         "imagem_url": "/figurinhas/15/imagem"
        },

        {"id": 16, 
         "nome": "Linus", 
         "categoria": "Sistemas Operacionais",
         "imagem_url": "/figurinhas/16/imagem"
        },

        {"id": 17, 
         "nome": "Dennis", 
         "categoria": "Sistemas Operacionais",
         "imagem_url": "/figurinhas/17/imagem"
        },

        {"id": 18, 
         "nome": "Richard", 
         "categoria": "Sistemas Operacionais",
         "imagem_url": "/figurinhas/18/imagem"
        },

        {"id": 19, 
         "nome": "Bill", 
         "categoria": "Sistemas Operacionais",
         "imagem_url": "/figurinhas/19/imagem"
        },

        {"id": 20, 
         "nome": "Steve", 
         "categoria": "Sistemas Operacionais",
         "imagem_url": "/figurinhas/20/imagem"
        },

        {"id": 21, 
         "nome": "Paulo", 
         "categoria": "Celebridade Tech",
         "imagem_url": "/figurinhas/21/imagem"
        },

        {"id": 22, 
         "nome": "Guilherme", 
         "categoria": "Brasil",
         "imagem_url": "/figurinhas/22/imagem"
        },

        {"id": 23, 
         "nome": "Gus", 
         "categoria": "Brasil",
         "imagem_url": "/figurinhas/23/imagem"
        },

        {"id": 24, 
         "nome": "Mauricio", 
         "categoria": "Brasil",
         "imagem_url": "/figurinhas/24/imagem"
        },

        {"id": 25, 
         "nome": "Andre", 
         "categoria": "Brasil",
         "imagem_url": "/figurinhas/25/imagem"
        },

        {"id": 26, 
         "nome": "Guilherme", 
         "categoria": "Brasil",
         "imagem_url": "/figurinhas/26/imagem"
        },

        {"id": 27, 
         "nome": "Gi", 
         "categoria": "Brasil",
         "imagem_url": "/figurinhas/27/imagem"
        },

        {"id": 28, 
         "nome": "Vinicius", 
         "categoria": "Brasil",
         "imagem_url": "/figurinhas/28/imagem"
        },

        {"id": 29, 
         "nome": "Rafa", 
         "categoria": "Brasil",
         "imagem_url": "/figurinhas/29/imagem"
        },

        {"id": 30,
         "nome": "Jonhyyplay", 
         "categoria": "Brasil",
         "imagem_url": "/figurinhas/30/imagem"
        }
    ]

@app.get("/figurinhas")
def listar_figurinhas():
    return Figurinhas

# Definir endpoint para listar as figurinhas
@app.get("/figurinhas/{id}/imagem")
def imagem_imagem(id: int):
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")  # Cria o padrão de busca para a imagem
    arquivos = glob.glob(padrao)

    if not arquivos:
        raise HTTPException(status_code=404, detail="Figurinha não encontrada")  # Retorna erro 404 se a imagem não for encontrada

    return FileResponse(arquivos[0])  # Envia a primeira imagem encontrada