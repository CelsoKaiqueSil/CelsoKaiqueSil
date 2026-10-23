# Celso Kaique

### Análise de Dados · Business Intelligence · Automação

Transformo registros operacionais em indicadores, dashboards e rotinas automatizadas.
Neste portfólio, você pode explorar o código, abrir uma demonstração e conferir os relatórios gerados.

[LinkedIn](https://www.linkedin.com/in/celso-kaique/) ·
[Experimentar a dashboard](https://celsokaiquesil.github.io/coreops-noc-dashboard/)

## Projetos

| Projeto | O que ele entrega | Explore o resultado |
| :--- | :--- | :--- |
| [CoreOps NOC Dashboard](https://github.com/CelsoKaiqueSil/coreops-noc-dashboard) | Disponibilidade, incidentes e priorização operacional, com conciliação e qualidade dos dados. | [Dashboard ao vivo](https://celsokaiquesil.github.io/coreops-noc-dashboard/) · [Excel](https://github.com/CelsoKaiqueSil/coreops-noc-dashboard/raw/refs/heads/main/docs/examples/coreops_weekly_demo.xlsx) |
| [Service Desk Analytics](https://github.com/CelsoKaiqueSil/service-desk-analytics) | SLA, backlog e tempos de atendimento, com visão executiva e detalhe por chamado. | [Excel com indicadores](https://github.com/CelsoKaiqueSil/service-desk-analytics/raw/refs/heads/main/docs/examples/service_desk.xlsx) |
| [Zabbix Reporting Pipeline](https://github.com/CelsoKaiqueSil/zabbix-reporting-pipeline) | Métricas de CPU, memória e tráfego consolidadas em relatórios rastreáveis. | [Relatório Excel](https://github.com/CelsoKaiqueSil/zabbix-reporting-pipeline/raw/refs/heads/main/docs/examples/zabbix_report.xlsx) |
| [FortiView Excel Automation](https://github.com/CelsoKaiqueSil/fortiview-excel-automation) | Atualização recorrente de planilhas, sem duplicidades, com backup e histórico de alterações. | [Planilha de exemplo](https://github.com/CelsoKaiqueSil/fortiview-excel-automation/raw/refs/heads/main/docs/examples/traffic_weekly.xlsx) |

<sub>Todos os resultados públicos usam dados sintéticos. As regras, os exemplos e os limites estão documentados em cada projeto.</sub>

## Por dentro das entregas

<details>
<summary><strong>CoreOps | De eventos técnicos a uma visão de operação</strong></summary>

[![CoreOps NOC Dashboard](assets/projects/coreops.png)](https://github.com/CelsoKaiqueSil/coreops-noc-dashboard)

- **Problema:** eventos repetidos, inventário inconsistente e dificuldade de priorizar incidentes.
- **Entrega:** ETL com normalização, deduplicação e matching, conectado a dashboard, Excel e análise exploratória.
- **Tecnologias:** Python, Pandas, SQL, PostgreSQL e JavaScript.

[Ver código](https://github.com/CelsoKaiqueSil/coreops-noc-dashboard) ·
[Abrir dashboard](https://celsokaiquesil.github.io/coreops-noc-dashboard/) ·
[Conferir estudo e evidências](https://github.com/CelsoKaiqueSil/coreops-noc-dashboard/blob/main/docs/IMPACT_EVIDENCE.md)

</details>

<details>
<summary><strong>Service Desk | Indicadores para acompanhar o atendimento</strong></summary>

[![Service Desk Analytics](assets/projects/service-desk.png)](https://github.com/CelsoKaiqueSil/service-desk-analytics)

- **Problema:** avaliar prazos e backlog sem contar chamados repetidos ou tratar dados ausentes como SLA cumprido.
- **Entrega:** relatório executivo, detalhamento dos chamados e métricas de média, mediana e P90.
- **Tecnologias:** Python, Pandas, Excel, Power BI e DAX.

[Ver código e metodologia](https://github.com/CelsoKaiqueSil/service-desk-analytics) ·
[Explorar modelo Power BI](https://github.com/CelsoKaiqueSil/service-desk-analytics/tree/main/powerbi)

O modelo Power BI aguarda homologação no Desktop. As prévias publicadas são geradas em Python, não capturas do Power BI.

</details>

<details>
<summary><strong>Zabbix | Métricas de monitoramento em relatórios auditáveis</strong></summary>

[![Zabbix Reporting Pipeline](assets/projects/zabbix.png)](https://github.com/CelsoKaiqueSil/zabbix-reporting-pipeline)

- **Problema:** consolidar séries sem esconder picos, misturar unidades ou perder registros rejeitados.
- **Entrega:** classificação de CPU, memória e tráfego, agregações por série e evidências de picos e descartes.
- **Tecnologias:** Python, Pandas e Excel; proteção de integração com API somente leitura.

[Ver código e regras](https://github.com/CelsoKaiqueSil/zabbix-reporting-pipeline)

A demonstração funciona offline a partir de CSV sintético; não exige acesso a um Zabbix real.

</details>

<details>
<summary><strong>FortiView | Uma rotina de planilhas confiável e reproduzível</strong></summary>

[![FortiView Excel Automation](assets/projects/fortiview.png)](https://github.com/CelsoKaiqueSil/fortiview-excel-automation)

- **Problema:** reimportar dados, duplicar linhas ou perder o arquivo anterior durante uma atualização.
- **Entrega:** normalização, atualização idempotente, backup, trava de execução e auditoria de alterações.
- **Tecnologias:** Python, openpyxl, Excel e PowerShell.

[Ver código e agendamento](https://github.com/CelsoKaiqueSil/fortiview-excel-automation)

O exemplo público não acessa um firewall real nem envia arquivos para SharePoint.

</details>

## Competências aplicadas

**Análise e preparação:** Python, Pandas, SQL, qualidade dos dados e análise exploratória.

**Indicadores e visualização:** Power BI, DAX, Excel, SLA, backlog e disponibilidade.

**Automação e validação:** ETL, APIs, Git, testes e GitHub Actions.

Meu processo parte do problema de negócio, explicita as regras de cálculo e termina com resultados reproduzíveis.
O [estudo da Central de Relatórios](https://github.com/CelsoKaiqueSil/coreops-noc-dashboard/blob/main/docs/REPORT_CENTER_CASE_STUDY.md)
também documenta decisões de produto e organização das fontes.

## Sobre mim

Estudante de Data Science na FIAP, com experiência em operações NOC e foco em Dados, BI e Automação.
Os projetos demonstram competências de análise e desenvolvimento, sem publicar informações de clientes ou credenciais.

[Vamos conversar no LinkedIn](https://www.linkedin.com/in/celso-kaique/).

<details>
<summary>Apresentação visual do perfil</summary>

![Celso Kaique | Dados, BI e Automação](assets/header-v2.png)

</details>
