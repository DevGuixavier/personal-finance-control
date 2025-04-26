import pandas as pd
import streamlit as st
import plotly.express as px

def generate_monthly_summary(df):
    df["mês"] = df["data"].dt.to_period("M")
    summary = df.groupby("mês")["valor"].sum().reset_index()
    summary["mês"] = summary["mês"].dt.strftime("%m-%Y")
    return summary

def generate_category_summary(df):
    summary = df.groupby("descrição")["valor"].sum().reset_index()
    return summary

def plot_monthly_expenses(df):
    summary = generate_monthly_summary(df)
    fig = px.bar(summary, x="mês", y="valor", labels={"mês": "Mês", "valor": "Total de Gastos"},
                 title="Gastos Mensais")
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

def plot_category_distribution_horizontal(df):
    summary = generate_category_summary(df)
    fig = px.bar(summary, y="descrição", x="valor", orientation='h',
                 labels={"descrição": "Categoria", "valor": "Total de Gastos"},
                 title="Distribuição por Categoria")
    st.plotly_chart(fig, use_container_width=True)

def show_kpis(df):
    total_spent = df["valor"].sum()
    months = df["data"].dt.to_period("M").nunique()
    avg_per_month = total_spent / months if months > 0 else 0

    col1, col2 = st.columns(2)
    col1.metric("Total Gasto", f"R$ {total_spent:,.2f}")
    col2.metric("Média Mensal", f"R$ {avg_per_month:,.2f}")
