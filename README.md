# API Simples com FastAPI

Esta é uma API simples criada com FastAPI que fornece informações sobre data e hora, além de calcular dias restantes até uma data específica.

## Pré-requisitos

- Python 3.10 ou superior
- Ambiente virtual configurado (venv)

## Como executar

1. Certifique-se de que o Python está instalado.
2. Ative o ambiente virtual: `.\venv\Scripts\Activate.ps1` (no Windows)
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute o servidor: `uvicorn main:app --reload --host 127.0.0.1 --port 8000`
5. Acesse a documentação interativa em `http://127.0.0.1:8000/docs`

## Endpoints

### 1. Obter Data e Hora Atual
- **Endpoint**: `GET /nielstest/agora`
- **Descrição**: Retorna a data e hora atual no formato JSON.
- **Exemplo de resposta**:
  ```json
  {
    "data_hora": "2026-01-13 14:30:00"
  }
  ```

### 2. Calcular Dias Restantes
- **Endpoint**: `GET /nielstest/faltamxdias`
- **Parâmetros**:
  - `data` (obrigatório): Data no formato `YYYY-MM-DD`
- **Descrição**: Calcula quantos dias faltam da data atual até a data fornecida. Retorna um número positivo se a data for no futuro, negativo se no passado.
- **Exemplos**:
  - Para uma data futura: `http://127.0.0.1:8000/nielstest/faltamxdias?data=2026-12-25`
    ```json
    {
      "dias_faltando": 346
    }
    ```
  - Para uma data passada: `http://127.0.0.1:8000/nielstest/faltamxdias?data=2025-01-01`
    ```json
    {
      "dias_faltando": -347
    }
    ```
  - Para data inválida: `http://127.0.0.1:8000/nielstest/faltamxdias?data=invalid`
    ```json
    {
      "error": "Data inválida. Use formato YYYY-MM-DD"
    }
    ```

### 3. Próxima Lua Cheia
- **Endpoint**: `GET /nielstest/proximaluacheia`
- **Descrição**: Retorna a data e hora da próxima lua cheia.
- **Exemplo de resposta**:
  ```json
  {
    "proxima_lua_cheia": "2026-02-01 22:09:10"
  }
  ```