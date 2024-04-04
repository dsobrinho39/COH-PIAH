# Detector de COH-PIAH

Este repositório contém o projeto didático "Detector de COH-PIAH", desenvolvido como parte de um curso de programação. O objetivo é identificar textos que possam estar infectados com a fictícia doença COH-PIAH, uma condição que leva os indivíduos a produzirem textos extremamente similares entre si.

## Introdução

A COH-PIAH é uma doença linguística rara e contagiosa, na qual os infectados começam a escrever de maneira muito semelhante. A detecção precoce é crucial para o tratamento eficaz. Este projeto utiliza uma abordagem baseada em características linguísticas para identificar possíveis casos da doença.

## Funcionalidades

O programa analisa uma série de textos e compara suas características linguísticas com a assinatura padrão de um texto infectado por COH-PIAH. As características analisadas incluem:

- Tamanho médio de palavra
- Relação Type-Token
- Razão Hapax Legomana
- Tamanho médio de sentença
- Complexidade de sentença
- Tamanho médio de frase

## Como Utilizar

1. **Clone o repositório** para o seu ambiente local.
2. Execute o **script principal** (`detector_coh_piah.py`).
3. Forneça a **assinatura típica** de um aluno infectado e os textos a serem analisados conforme solicitado pelo programa.
4. O programa indicará qual dos textos fornecidos tem maior probabilidade de estar infectado.

## Tecnologias Utilizadas

- **Python 3**
- Bibliotecas: `re` (para manipulação de expressões regulares)

## Contribuições

Contribuições são sempre bem-vindas. Para contribuir:

1. Faça um **fork do repositório**.
2. Crie um **branch para suas modificações**.
3. Submeta um **pull request**.

## Licença

Este projeto é licenciado sob a Licença GNU - veja o arquivo `LICENSE.md` para detalhes.