#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def maxmin_select_dc(arr, inicio=0, fim=None):
    if arr is None or len(arr) == 0:
        raise ValueError("Array não pode estar vazio")
    
    if fim is None:
        fim = len(arr) - 1
    
    # Caso base: apenas um elemento
    if inicio == fim:
        return arr[inicio], arr[inicio]
    
    # Caso base: dois elementos
    if fim - inicio == 1:
        if arr[inicio] <= arr[fim]:
            return arr[inicio], arr[fim]
        else:
            return arr[fim], arr[inicio]
    
    # Divisão: encontra o ponto médio
    meio = (inicio + fim) // 2
    
    # Conquista: resolve recursivamente as duas metades
    min_esq, max_esq = maxmin_select_dc(arr, inicio, meio)
    min_dir, max_dir = maxmin_select_dc(arr, meio + 1, fim)
    
    # Combinação: compara os resultados das duas metades
    min_global = min(min_esq, min_dir)
    max_global = max(max_esq, max_dir)
    
    return min_global, max_global


def maxmin_select_naive(arr):
    if not arr:
        raise ValueError("Array não pode estar vazio")
    
    min_val = min(arr)
    max_val = max(arr)
    
    return min_val, max_val


def maxmin_select_optimized(arr):
    if not arr:
        raise ValueError("Array não pode estar vazio")
    
    n = len(arr)
    
    # Inicialização baseada no tamanho do array
    if n == 1:
        return arr[0], arr[0]
    
    # Se o array tem número par de elementos
    if n % 2 == 0:
        if arr[0] <= arr[1]:
            min_val, max_val = arr[0], arr[1]
        else:
            min_val, max_val = arr[1], arr[0]
        inicio = 2
    else:
        # Se o array tem número ímpar de elementos
        min_val = max_val = arr[0]
        inicio = 1
    
    # Processa os elementos restantes em pares
    for i in range(inicio, n, 2):
        if i + 1 < n:
            # Compara o par atual
            if arr[i] <= arr[i + 1]:
                menor_par, maior_par = arr[i], arr[i + 1]
            else:
                menor_par, maior_par = arr[i + 1], arr[i]
            
            # Atualiza min e max globais
            if menor_par < min_val:
                min_val = menor_par
            if maior_par > max_val:
                max_val = maior_par
        else:
            # Elemento restante (caso ímpar)
            if arr[i] < min_val:
                min_val = arr[i]
            if arr[i] > max_val:
                max_val = arr[i]
    
    return min_val, max_val


def contar_comparacoes_dc(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return int(3 * n / 2 - 2)


def benchmark_algorithms(arr):
    import time
    
    print(f"\nBenchmark para array de tamanho {len(arr)}")
    print("=" * 50)
    
    # Algoritmo de Divisão e Conquista
    start_time = time.time()
    min_dc, max_dc = maxmin_select_dc(arr.copy())
    time_dc = time.time() - start_time
    
    # Algoritmo Ingênuo
    start_time = time.time()
    min_naive, max_naive = maxmin_select_naive(arr.copy())
    time_naive = time.time() - start_time
    
    # Algoritmo Otimizado
    start_time = time.time()
    min_opt, max_opt = maxmin_select_optimized(arr.copy())
    time_opt = time.time() - start_time
    
    print(f"Divisão e Conquista: Min={min_dc}, Max={max_dc}, Tempo={time_dc:.6f}s")
    print(f"Algoritmo Ingênuo:   Min={min_naive}, Max={max_naive}, Tempo={time_naive:.6f}s")
    print(f"Algoritmo Otimizado: Min={min_opt}, Max={max_opt}, Tempo={time_opt:.6f}s")
    print(f"Comparações teóricas (D&C): {contar_comparacoes_dc(len(arr))}")
    
    # Verificação de correção
    assert min_dc == min_naive == min_opt, "Resultados mínimos inconsistentes!"
    assert max_dc == max_naive == max_opt, "Resultados máximos inconsistentes!"
    print("✓ Todos os algoritmos produziram resultados consistentes")


def test_casos_especiais():
    print("\nTestes de Casos Especiais")
    print("=" * 30)
    
    # Teste com um elemento
    arr1 = [42]
    min_val, max_val = maxmin_select_dc(arr1)
    print(f"Array [42]: Min={min_val}, Max={max_val}")
    assert min_val == max_val == 42
    
    # Teste com dois elementos
    arr2 = [10, 5]
    min_val, max_val = maxmin_select_dc(arr2)
    print(f"Array [10, 5]: Min={min_val}, Max={max_val}")
    assert min_val == 5 and max_val == 10
    
    # Teste com elementos iguais
    arr3 = [7, 7, 7, 7]
    min_val, max_val = maxmin_select_dc(arr3)
    print(f"Array [7, 7, 7, 7]: Min={min_val}, Max={max_val}")
    assert min_val == max_val == 7
    
    # Teste com array ordenado
    arr4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    min_val, max_val = maxmin_select_dc(arr4)
    print(f"Array ordenado [1..10]: Min={min_val}, Max={max_val}")
    assert min_val == 1 and max_val == 10
    
    # Teste com array em ordem decrescente
    arr5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    min_val, max_val = maxmin_select_dc(arr5)
    print(f"Array decrescente [10..1]: Min={min_val}, Max={max_val}")
    assert min_val == 1 and max_val == 10
    
    print("✓ Todos os casos especiais passaram nos testes!")


def main():
    print("Algoritmo MaxMin Select - Divisão e Conquista")
    print("=" * 50)
    
    # Executa testes de casos especiais
    test_casos_especiais()
    
    # Exemplo básico
    exemplo = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    print(f"\nExemplo com array: {exemplo}")
    min_val, max_val = maxmin_select_dc(exemplo)
    print(f"Resultado: Menor = {min_val}, Maior = {max_val}")
    
    # Benchmark com diferentes tamanhos
    import random
    
    for size in [100, 1000, 10000]:
        test_array = [random.randint(1, 1000) for _ in range(size)]
        benchmark_algorithms(test_array)
    
    # Demonstração interativa
    print("\n" + "=" * 50)
    print("Teste Interativo")
    print("Digite uma sequência de números separados por espaço:")
    print("(ou pressione Enter para usar o exemplo padrão)")
    
    try:
        entrada = input("Números: ").strip()
        if entrada:
            numeros = list(map(int, entrada.split()))
        else:
            numeros = exemplo
        
        if numeros:
            min_resultado, max_resultado = maxmin_select_dc(numeros)
            print(f"\nArray analisado: {numeros}")
            print(f"Menor elemento: {min_resultado}")
            print(f"Maior elemento: {max_resultado}")
            print(f"Número teórico de comparações: {contar_comparacoes_dc(len(numeros))}")
        else:
            print("Nenhum número foi inserido.")
            
    except ValueError as e:
        print(f"Erro na entrada: {e}")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()