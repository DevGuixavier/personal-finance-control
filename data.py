import pandas as pd
import os
import shutil
from datetime import datetime

DATA_FILE = "gastos.csv"
BACKUP_DIR = "backups"


def add_expense(date, description, amount, nome):
    # Carrega os dados existentes
    df = load_data()
    # Converte a data para o formato dd/mm/yyyy
    date_str = pd.to_datetime(date).strftime("%d/%m/%Y")
    # Cria um novo registro de despesa
    new_entry = {
        "data": date_str,
        "descrição": description,
        "valor": amount,
        "nome": nome,
    }
    # Remove valores nulos ou vazios do registro
    new_entry_clean = {k: v for k, v in new_entry.items() if pd.notna(v) and v != ""}
    # Adiciona o novo registro ao DataFrame existente
    df = pd.concat([df, pd.DataFrame([new_entry_clean])], ignore_index=True)
    # Converte a coluna 'data' para datetime, descartando valores inválidos
    df["data"] = pd.to_datetime(df["data"], dayfirst=True, errors="coerce")
    # Remove linhas com datas inválidas
    df = df.dropna(subset=["data"])
    df["data"] = df["data"].dt.strftime("%d/%m/%Y")
    # Salva o DataFrame atualizado no arquivo CSV
    df.to_csv(DATA_FILE, index=False)


def load_data():
    # Verifica se o arquivo CSV existe
    if os.path.exists(DATA_FILE):
        # Carrega os dados do CSV
        df = pd.read_csv(DATA_FILE)
        # Converte a coluna 'data' para datetime
        df["data"] = pd.to_datetime(df["data"], dayfirst=True, errors="coerce")
        return df
    else:

        return pd.DataFrame(columns=["data", "descrição", "valor", "nome"])


def create_backup():

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_file = os.path.join(BACKUP_DIR, f"gastos_backup_{timestamp}.csv")

    shutil.copy2(DATA_FILE, backup_file)
