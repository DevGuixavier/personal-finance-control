import streamlit as st
from data import add_expense, load_data, create_backup
from analysis import (
    plot_monthly_expenses,
    plot_category_distribution_horizontal,
    show_kpis,
)
import pandas as pd


# Função principal do aplicativo Streamlit
def main():

    st.title("Painel de Controle Financeiro")

    # Menu lateral com opções
    menu = ["Adicionar Despesa", "Dashboard"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Adicionar Despesa":

        st.header("Adicionar nova despesa")
        with st.form(key="expense_form"):

            nome = st.text_input("Nome")

            date = st.date_input("Data")

            description = st.text_input("Descrição")

            amount = st.number_input("Valor gasto", min_value=0.0, format="%.2f")

            submit = st.form_submit_button("Adicionar")

            if submit:
                # Validações dos campos
                if amount == 0:
                    st.error(
                        "O valor gasto não pode ser zero. Por favor, insira um valor válido."
                    )
                elif not nome.strip():
                    st.error("Por favor, insira o nome da pessoa que fez o gasto.")
                else:
                    # Adiciona despesa usando a função do data.py
                    add_expense(date, description, amount, nome.strip())
                    st.success("Despesa adicionada com sucesso!")

    elif choice == "Dashboard":

        data = load_data()
        if data.empty:
            st.info("Nenhuma despesa registrada ainda.")
        else:
            # Escolha do tipo de dashboard
            dashboard_type = st.sidebar.radio(
                "Tipo de Dashboard", ("Gasto Total", "Gasto Pessoal")
            )
            if dashboard_type == "Gasto Pessoal":
                # Lista de pessoas para filtro
                pessoas = data["nome"].unique()
                pessoa_selecionada = st.sidebar.selectbox("Selecione a pessoa", pessoas)
                filtered_data = data[data["nome"] == pessoa_selecionada]
            else:
                filtered_data = data

            # Filtros interativos de data
            min_date = filtered_data["data"].min()
            max_date = filtered_data["data"].max()
            date_range = st.sidebar.date_input(
                "Selecione o intervalo de datas", [min_date, max_date]
            )

            if len(date_range) == 2:
                start_date, end_date = date_range
                # Filtra o DataFrame para incluir apenas despesas dentro do intervalo das datas selecionadas
                mask = (filtered_data["data"] >= pd.to_datetime(start_date)) & (
                    filtered_data["data"] <= pd.to_datetime(end_date)
                )
                filtered_data = filtered_data.loc[mask]

            # Exibe KPIs e gráficos usando as funções do analysis.py
            show_kpis(filtered_data)
            plot_monthly_expenses(filtered_data)
            plot_category_distribution_horizontal(filtered_data)

    if st.button("Finalizar Sessão e Criar Backup"):
        create_backup()
        st.success("Backup criado com sucesso!")


if __name__ == "__main__":
    main()
