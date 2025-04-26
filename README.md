# Controle Financeiro Pessoal

Este projeto é um aplicativo simples de controle financeiro pessoal desenvolvido com Streamlit. Permite que o usuário registre suas despesas, visualize análises mensais e distribuições por categoria, além de gerar backups dos dados.

## Funcionalidades

- Adicionar despesas com informações de data, descrição, valor e nome da pessoa que realizou o gasto.
- Visualizar dashboard interativo com:
  - Gráfico de barras dos gastos mensais.
  - Gráfico de barras horizontal da distribuição por categoria.
  - Indicadores de total gasto e média mensal.
- Filtrar despesas por pessoa e intervalo de datas.
- Criar backup dos dados manualmente.

## Tecnologias Utilizadas

- Python 3.7+
- Streamlit
- Pandas
- Plotly Express

## Como usar

1. Clone o repositório:
   ```
   git clone https://github.com/DevGuixavier/personal-finance-control.git
   ```
2. Navegue até o diretório do projeto:
   ```
   cd personal-finance-control
   ```
3. (Opcional) Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
4. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
5. Execute o aplicativo:
   ```
   streamlit run app.py
   ```
6. Use a interface para adicionar despesas e visualizar o dashboard.

## Estrutura do Projeto

- `app.py`: Arquivo principal com a interface Streamlit.
- `data.py`: Manipulação de dados, armazenamento e backup.
- `analysis.py`: Funções para análise e visualização dos dados.
- `gastos.csv`: Arquivo CSV onde os dados são armazenados.
- `backups/`: Pasta onde os backups são salvos.

## Observações

- O arquivo `gastos.csv` e a pasta `backups/` estão no `.gitignore` para evitar versionamento de dados sensíveis.
- O projeto é modular e pode ser facilmente expandido com novas funcionalidades.
- Certifique-se de criar backups regularmente para evitar perda de dados.

## Contato

Para dúvidas ou sugestões, entre em contato.

---
Projeto criado para controle financeiro pessoal simples e funcional.
