from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_data(data_dir=DATA_DIR):
    """
    Carrega a base de salários dos profissionais de dados.
    """
    data_dir = Path(data_dir)

    df = pd.read_csv(data_dir / "salario_profissionais_dados.csv")

    return df


def validate_data(df):
    """
    Executa validações básicas de qualidade dos dados.
    """
    missing_values = df.isnull().sum().sum()

    if missing_values > 0:
        raise ValueError(f"Foram encontrados {missing_values} valores ausentes.")

    expected_columns = [
        "work_year",
        "country",
        "region",
        "experience_level",
        "job_title",
        "salary_in_usd",
        "employee_residence",
        "company_location",
        "company_size",
        "years_of_experience",
    ]

    missing_columns = [
        coluna for coluna in expected_columns if coluna not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Colunas ausentes: {missing_columns}")

    return True


def prepare_data(data_dir=DATA_DIR):
    """
    Executa o pipeline básico de preparação dos dados.
    """
    df = load_data(data_dir)

    validate_data(df)

    return df


if __name__ == "__main__":
    df = prepare_data()

    print("Base carregada:", df.shape)

    print("Valores ausentes:", df.isnull().sum().sum())

    print("Registros duplicados:", df.duplicated().sum())

    print("Pipeline executado com sucesso.")
