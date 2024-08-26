import streamlit as st
import pandas as pd

# Título do projeto
st.title("EduMetrics: Análise da Qualidade da Educação")

# Descrição do problema de negócio e dos objetivos do projeto
st.markdown("""
## Descrição do Projeto
A qualidade da educação é um dos pilares fundamentais para o desenvolvimento de uma sociedade. 
Este projeto tem como objetivo analisar diferentes aspectos que influenciam a qualidade da educação nas escolas públicas 
de vários estados brasileiros, com foco inicial nas escolas do estado de São Paulo e Paraná.

## Objetivos
- Analisar a infraestrutura das escolas e como ela impacta o desempenho dos alunos.
- Identificar padrões e tendências nos dados educacionais que possam ajudar na tomada de decisões.
- Sugerir melhorias com base nos dados analisados para potencializar a qualidade da educação.
""")

# Links úteis para as iniciativas e fontes de inspiração do projeto
st.markdown("""
## Links Úteis
- [QEdu - Plataforma de Dados Educacionais](https://analitico.qedu.org.br/)
- [INEP - Censo Escolar e SAEB](https://www.gov.br/inep/pt-br)
- [Artigo sobre Project Charter](https://artia.com/blog/project-charter/)
""")

# Carregar e exibir uma amostra dos dados de infraestrutura para as escolas do estado de São Paulo e Paraná
file_path = "data/01_raw/infraestrutura_SP_PR.csv"
data = pd.read_csv(file_path)

st.markdown("## Amostra dos Dados de Infraestrutura (SP e PR)")
st.dataframe(data.head(10))

# Rodar a aplicação
if __name__ == "__main__":
    st.run()
