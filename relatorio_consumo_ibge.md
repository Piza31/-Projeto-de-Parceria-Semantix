
# 📊 Relatório de Análise de Dados – Consumo Alimentar no Brasil (IBGE – Simulação)

## 1. Introdução
Este projeto tem como objetivo analisar os **hábitos de consumo alimentar no Brasil**, utilizando dados inspirados na Pesquisa de Orçamentos Familiares (POF) do **IBGE**.  
A análise busca identificar padrões de consumo per capita em diferentes grupos de alimentos e propor insights que possam contribuir para **políticas públicas de nutrição** e **promoção da saúde alimentar**.

---

## 2. Coleta de Dados
**Fonte de Dados:** Pesquisa de Orçamentos Familiares (POF/IBGE) – valores simulados a partir de médias históricas.  
**Formato:** Arquivo CSV (`ibge_pof_consumo_br.csv`) com delimitador `;` e separador decimal `,`.  
**Descrição:**  
- **Grupo** → Categoria de alimento (ex.: frutas, carnes, cereais).  
- **Consumo_per_capita** → Quantidade média consumida per capita (kg ou litros por ano).  

### Exemplo de dados:
| Grupo               | Consumo_per_capita |
|----------------------|--------------------|
| Leite e derivados    | 60,2               |
| Frutas               | 45,3               |
| Verduras e legumes   | 38,7               |
| Cereais e massas     | 35,4               |
| Carnes               | 32,8               |

---

## 3. Modelagem e Análise Exploratória (EDA)
- Conversão dos valores numéricos (vírgula como separador decimal).  
- Normalização dos nomes dos grupos de alimentos.  
- **Consumo médio per capita:** ~30 kg/ano.  
- **Grupo mais consumido:** Leite e derivados (60,2).  
- **Grupo menos consumido:** Óleos e gorduras (8,7).  

---

## 4. Conclusões e Insights

**Principais Achados:**  
1. Há concentração de consumo em grupos específicos (laticínios e frutas).  
2. Grupos importantes para saúde, como verduras e legumes, ainda ficam abaixo do recomendado pela OMS.  
3. Grupos energéticos (cereais, massas, carnes) têm participação significativa.  

**Relevância:**  
- O consumo desequilibrado impacta diretamente na saúde pública.  
- A análise pode embasar campanhas de educação alimentar.  

**Recomendações:**  
- Campanhas educativas para aumentar consumo de frutas e verduras.  
- Subsídios para tornar alimentos saudáveis mais acessíveis.  
- Monitoramento contínuo dos dados para avaliar impacto das políticas.  

---

## 5. Próximos Passos
- Expandir a base de dados para incluir séries históricas.  
- Integrar dados de regiões para identificar desigualdades regionais.  
- Usar técnicas de machine learning para prever tendências de consumo.  

---

✍️ **Autor:** Gabriel (Projeto Acadêmico – Análise de Dados)  
📊 **Ferramentas:** Python, Pandas, Matplotlib, Google Sheets, Looker Studio  
