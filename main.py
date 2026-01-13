from fastapi import FastAPI
from datetime import datetime, date
import ephem

app = FastAPI()

@app.get("/nielstest/agora")
def get_data_hora():
    now = datetime.now()
    return {"data_hora": now.strftime("%Y-%m-%d %H:%M:%S")}

@app.get("/nielstest/faltamxdias")
def dias_faltando(data: str):
    try:
        target_date = datetime.strptime(data, "%Y-%m-%d").date()
        today = date.today()
        diff = (target_date - today).days
        return {"dias_faltando": diff}
    except ValueError:
        return {"error": "Data inválida. Use formato YYYY-MM-DD"}

@app.get("/nielstest/proximaluacheia")
def proxima_lua_cheia():
    today = datetime.now()
    next_full = ephem.next_full_moon(today)

    return {"proxima_lua_cheia": next_full.datetime().strftime("%Y-%m-%d %H:%M:%S")}

@app.get("/health")
def health():
    return {"status": "ok"}


class Pessoa(BaseModel):
    nome: str
    idade: int

@app.post("/pessoa")
def criar_pessoa(pessoa: Pessoa):
    return {
        "mensagem": "Pessoa recebida com sucesso",
        "dados": pessoa
    }
