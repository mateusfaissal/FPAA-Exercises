# MaxMin Select Algorithm - Divisão e Conquista

Este projeto implementa o **algoritmo de seleção simultânea do maior e menor elementos** (MaxMin Select) utilizando a abordagem de **divisão e conquista**.

## 📋 Descrição do Projeto

O **algoritmo MaxMin Select** encontra simultaneamente o maior e menor elemento de uma sequência de números de forma eficiente, reduzindo significativamente o número de comparações necessárias em comparação com uma abordagem ingênua.

Este algoritmo é um exemplo clássico da técnica de **divisão e conquista**, onde o problema é dividido recursivamente em subproblemas menores, resolvidos independentemente, e os resultados são combinados para obter a solução final.

### Características Principais

- **Complexidade de Tempo:** O(n)
- **Número de Comparações:** Aproximadamente `3n/2 - 2` comparações
- **Técnica:** Divisão e Conquista (Divide and Conquer)
- **Eficiência:** Reduz significativamente o número de comparações em relação ao método ingênuo

## 🔍 Lógica do Algoritmo Implementado (Linha a Linha)

### Função Principal `maxmin_select_dc(arr, inicio=0, fim=None)`

#### Análise Detalhada do Código:

```python
def maxmin_select_dc(arr, inicio=0, fim=None):
    if arr is None or len(arr) == 0:
        raise ValueError("Array não pode estar vazio")
    
    if fim is None:
        fim = len(arr) - 1
```

**Linhas 1-6:** Definição da função e validação inicial
- Define a função recursiva com parâmetros opcionais para início e fim
- Valida se o array não é None ou vazio
- Inicializa o índice final se não fornecido

```python
    if inicio == fim:
        return arr[inicio], arr[inicio]
```

**Linhas 8-9:** **Caso base 1** - Um único elemento
- Se há apenas um elemento, ele é simultaneamente o menor e o maior
- **Comparações realizadas:** 0 (sem comparação necessária)
- Retorna uma tupla com o mesmo elemento

```python
    if fim - inicio == 1:
        if arr[inicio] <= arr[fim]:
            return arr[inicio], arr[fim]
        else:
            return arr[fim], arr[inicio]
```

**Linhas 11-15:** **Caso base 2** - Dois elementos
- Se há dois elementos, compara-os diretamente
- **Comparações realizadas:** 1 (uma comparação entre os dois elementos)
- Retorna o par ordenado (menor, maior)

```python
    meio = (inicio + fim) // 2
```

**Linha 17:** **Fase de Divisão**
- Calcula o ponto médio do array para dividir o problema
- **Operações:** 1 divisão inteira (O(1))

```python
    min_esq, max_esq = maxmin_select_dc(arr, inicio, meio)
    min_dir, max_dir = maxmin_select_dc(arr, meio + 1, fim)
```

**Linhas 19-20:** **Fase de Conquista**
- Resolve recursivamente os subproblemas da metade esquerda e direita
- Cada chamada retorna o par (menor, maior) de sua respectiva metade
- **Comparações realizadas:** T(n/2) + T(n/2) = 2T(n/2)

```python
    min_global = min(min_esq, min_dir)
    max_global = max(max_esq, max_dir)
    
    return min_global, max_global
```

**Linhas 22-25:** **Fase de Combinação**
- Compara os menores valores das duas metades para encontrar o mínimo global
- Compara os maiores valores das duas metades para encontrar o máximo global
- **Comparações realizadas:** 2 (uma para min, uma para max)
- Retorna o resultado final

### Estratégia do Algoritmo

1. **Divisão:** O problema de tamanho n é dividido em dois subproblemas de tamanho n/2
2. **Conquista:** Cada subproblema é resolvido recursivamente
3. **Combinação:** Os resultados são combinados com apenas 2 comparações adicionais

## 🚀 Como Executar o Projeto

### Pré-requisitos

- **Python 3.6 ou superior**
- Sistema operacional: Windows, macOS ou Linux

### Passo 1: Navegar para o Diretório

```bash
cd MaxMin-Select-Algorithm
```

### Passo 2: Executar o Programa

```bash
python3 main.py
```

### Passo 3: Interagir com o Programa

O programa oferece as seguintes funcionalidades automaticamente:

1. **Testes Automáticos de Casos Especiais**: Executa casos de teste predefinidos
2. **Exemplo Demonstrativo**: Mostra o algoritmo funcionando com um array exemplo
3. **Benchmarks Comparativos**: Compara diferentes implementações (ingênua, otimizada, divisão e conquista)
4. **Modo Interativo**: Permite testar com números próprios

#### Exemplo de Uso Manual

```python
from main import maxmin_select_dc

# Exemplo básico
arr = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
min_val, max_val = maxmin_select_dc(arr)
print(f"Menor: {min_val}, Maior: {max_val}")
# Saída: Menor: 5, Maior: 90
```

### Entrada Personalizada

Durante a execução, você pode inserir seus próprios números:
```
Digite uma sequência de números separados por espaço:
15 3 89 42 7 156 23 91 4 67
```

## 🔧 Funcionalidades

### 1. Algoritmo Principal
- `maxmin_select_dc(arr)`: Implementação usando divisão e conquista

### 2. Algoritmos de Comparação
- `maxmin_select_naive(arr)`: Implementação ingênua (2n comparações)
- `maxmin_select_optimized(arr)`: Implementação otimizada em uma passada

### 3. Análise e Testes
- Testes automáticos com casos especiais
- Benchmark comparativo entre diferentes implementações
- Cálculo teórico do número de comparações
- Teste interativo para entrada personalizada

## 📊 Relatório Técnico - Análise de Complexidade Assintótica

### 1. Análise da Complexidade Assintótica pelo Método de Contagem de Operações

#### 1.1 Contagem Detalhada de Comparações por Etapa

**Casos Base:**
- **n = 1:** 0 comparações (elemento único é min e max)
- **n = 2:** 1 comparação (compara os dois elementos)

**Caso Recursivo (n > 2):**

**Etapa 1 - Divisão:**
- Cálculo do ponto médio: 0 comparações
- Divisão em subproblemas: 0 comparações
- **Total da Divisão:** 0 comparações

**Etapa 2 - Conquista (Chamadas Recursivas):**
- Subproblema esquerdo: T(⌊n/2⌋) comparações
- Subproblema direito: T(⌈n/2⌉) comparações
- Para simplificar, consideramos T(n/2) + T(n/2) = 2T(n/2)
- **Total da Conquista:** 2T(n/2) comparações

**Etapa 3 - Combinação:**
- Comparação entre os mínimos das duas metades: 1 comparação
- Comparação entre os máximos das duas metades: 1 comparação
- **Total da Combinação:** 2 comparações

#### 1.2 Cálculo Total de Comparações

**Equação de Recorrência:**
```
T(n) = 2T(n/2) + 2    para n > 2
T(2) = 1
T(1) = 0
```

**Resolução por Substituição:**

Para n = 2^k, expandindo a recorrência:

```
T(2^k) = 2T(2^(k-1)) + 2
       = 2[2T(2^(k-2)) + 2] + 2
       = 4T(2^(k-2)) + 4 + 2
       = 4T(2^(k-2)) + 2(2 + 1)
       
Continuando:
T(2^k) = 8T(2^(k-3)) + 2(4 + 2 + 1)
       = ...
       = 2^i T(2^(k-i)) + 2(2^(i-1) + 2^(i-2) + ... + 2 + 1)
```

**Quando i = k-1 (chegamos ao caso base T(2) = 1):**

```
T(2^k) = 2^(k-1) × T(2) + 2(2^(k-2) + 2^(k-3) + ... + 1)
       = 2^(k-1) × 1 + 2 × (2^(k-1) - 1)
       = 2^(k-1) + 2^k - 2
       = 2^(k-1) + 2^k - 2
       = 2^k(1/2 + 1) - 2
       = 3×2^(k-1) - 2
```

**Como n = 2^k, então k = log₂n:**
```
T(n) = 3n/2 - 2
```

#### 1.3 Demonstração da Complexidade O(n)

**Para n elementos, o número total de comparações é:**
- **Fórmula exata:** T(n) = 3n/2 - 2
- **Análise assintótica:** 
  - Termo dominante: 3n/2
  - Termos de menor ordem: -2
  - **Complexidade:** O(n)

**Prova que T(n) ∈ O(n):**
- Precisamos mostrar que ∃c > 0 e n₀ tal que T(n) ≤ c×n para n ≥ n₀
- T(n) = 3n/2 - 2 ≤ 3n/2 ≤ 2n para n ≥ 4
- Portanto, c = 2 e n₀ = 4 satisfazem a condição
- **Conclusão:** T(n) ∈ O(n)

### 2. Análise da Complexidade Assintótica pela Aplicação do Teorema Mestre

#### 2.1 Recorrência do MaxMin Select

**Recorrência estabelecida:**
```
T(n) = 2T(n/2) + O(1)
```

Mais especificamente, com base na nossa análise:
```
T(n) = 2T(n/2) + 2
```

#### 2.2 Identificação dos Parâmetros

**Forma padrão do Teorema Mestre:**
```
T(n) = a·T(n/b) + f(n)
```

**Comparando com nossa recorrência T(n) = 2T(n/2) + 2:**

**1. Identifique os valores de a, b e f(n):**
- **a = 2** (número de subproblemas recursivos)
- **b = 2** (fator de redução do tamanho do problema)
- **f(n) = 2 = O(1)** (custo do trabalho fora das chamadas recursivas)

**2. Calcule log_b a para determinar o valor de p:**
```
log_b a = log₂ 2 = 1
```
Portanto, **p = 1**

#### 2.3 Determinação do Caso do Teorema Mestre

**Os três casos do Teorema Mestre:**

- **Caso 1:** f(n) = O(n^c) onde c < log_b a
- **Caso 2:** f(n) = Θ(n^c log^k n) onde c = log_b a
- **Caso 3:** f(n) = Ω(n^c) onde c > log_b a

**Análise do nosso problema:**
- f(n) = O(1) = O(n⁰)
- log_b a = 1
- Comparando: 0 < 1

**3. Determine em qual dos três casos esta recorrência se enquadra:**

Como f(n) = O(n⁰) e 0 < log_b a = 1, nossa recorrência se enquadra no **Caso 1** do Teorema Mestre.

#### 2.4 Solução Assintótica

**4. Encontre a solução assintótica T(n):**

**Aplicação do Caso 1 do Teorema Mestre:**
```
Se f(n) = O(n^c) onde c < log_b a, então:
T(n) = Θ(n^(log_b a))
```

**Substituindo nossos valores:**
```
T(n) = Θ(n^(log₂ 2))
T(n) = Θ(n¹)
T(n) = Θ(n)
```

#### 2.5 Verificação da Solução

**Confirmação por ambos os métodos:**
- **Método de Contagem:** T(n) = 3n/2 - 2 = O(n)
- **Teorema Mestre:** T(n) = Θ(n)

**Consistência:** ✓ Ambos os métodos confirmam que a complexidade é linear

**Interpretação:** O algoritmo MaxMin Select utilizando divisão e conquista tem complexidade temporal linear, o que é ótimo para este problema, pois é necessário examinar cada elemento pelo menos uma vez para determinar o mínimo e máximo.

### 3. Comparação com Outros Métodos

| Método | Comparações | Complexidade Assintótica |
|--------|-------------|-------------------------|
| Ingênuo (2 passadas) | 2n - 2 | O(n) |
| Otimizado (1 passada) | ~3n/2 | O(n) |
| **Divisão e Conquista** | **3n/2 - 2** | **O(n)** |
| Limite Teórico Inferior | n + ⌈log₂ n⌉ - 2 | Ω(n) |

**Conclusão:** O algoritmo de divisão e conquista atinge quase o limite teórico mínimo de comparações, sendo extremamente eficiente para o problema MaxMin Select.

## 🧪 Casos de Teste

O programa inclui testes automáticos para:

- Array com um elemento
- Array com dois elementos  
- Array com elementos iguais
- Array ordenado crescente
- Array ordenado decrescente
- Arrays aleatórios de diferentes tamanhos

## 📈 Exemplo de Execução

```python
# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
min_val, max_val = maxmin_select_dc(arr)
print(f"Menor: {min_val}, Maior: {max_val}")
# Saída: Menor: 5, Maior: 90
```

## 🎯 Como Funciona

1. **Caso Base:** Se o array tem 1 ou 2 elementos, resolve diretamente
2. **Divisão:** Divide o array no ponto médio
3. **Conquista:** Aplica recursivamente o algoritmo nas duas metades
4. **Combinação:** Compara os resultados das duas metades para encontrar o min/max global

## 📋 Estrutura do Código

```
MaxMin-Select-Algorithm/
├── main.py          # Implementação completa do algoritmo
└── README.md        # Documentação do projeto
```

## 🔍 Vantagens da Abordagem

- **Eficiência:** Reduz o número de comparações
- **Elegância:** Solução recursiva clara e bem estruturada  
- **Escalabilidade:** Mantém boa performance para arrays grandes
- **Otimalidade:** Número próximo ao mínimo teórico de comparações

## 📚 Conceitos Aplicados

- **Divisão e Conquista (Divide and Conquer)**
- **Análise de Complexidade Assintótica**
- **Teorema Mestre**
- **Recorrências Matemáticas**
- **Otimização de Algoritmos**
- **Análise Comparativa de Performance**

## 🔍 Exemplo de Execução Detalhada

```python
# Exemplo: [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]

# Divisão 1: [64, 34, 25, 12, 22] e [11, 90, 5, 77, 30]
# Divisão 2: [64, 34] [25, 12, 22] | [11, 90] [5, 77, 30]
# ... continuando recursivamente até casos base

# Resultado: Menor = 5, Maior = 90
# Comparações realizadas: 3×10/2 - 2 = 13 comparações
```

## 📈 Performance e Resultados

O algoritmo demonstra sua eficiência através dos benchmarks automáticos incluídos no programa, mostrando que a abordagem de divisão e conquista mantém performance linear constante, independentemente do tamanho do array, com número de comparações próximo ao limite teórico mínimo.

## ✅ Conclusão

A implementação do algoritmo MaxMin Select através de divisão e conquista representa uma solução elegante e eficiente para o problema de seleção simultânea. Com complexidade O(n) e número de comparações otimizado (3n/2 - 2), o algoritmo demonstra as vantagens da técnica de divisão e conquista, combinando clareza conceitual com eficiência computacional.