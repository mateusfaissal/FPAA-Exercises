import math
import time

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    power_of_10 = 10 ** m
    
    a = x // power_of_10
    b = x % power_of_10
    c = y // power_of_10
    d = y % power_of_10
    
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    
    result = ac * (10 ** (2 * m)) + ad_plus_bc * (10 ** m) + bd
    
    return result

def medir_tempo(func, x, y):
    inicio = time.time()
    resultado = func(x, y)
    fim = time.time()
    return resultado, fim - inicio

def testar_algoritmos():
    print("=" * 60)
    print("TESTE DO ALGORITMO DE KARATSUBA")
    print("=" * 60)
    
    casos_teste = [
        (123, 456),
        (1234, 5678),
        (12345, 67890),
        (123456789, 987654321),
        (123456789012345678998979797979, 987654321098765432197897897897897)
    ]
    
    for i, (x, y) in enumerate(casos_teste, 1):
        print(f"\nTeste {i}: {x} × {y}")
        print("-" * 40)
        
        resultado_karatsuba, tempo_karatsuba = medir_tempo(karatsuba, x, y)
        
        resultado_esperado = x * y
        
        if resultado_karatsuba == resultado_esperado:
            print(f"✓ Resultado: {resultado_karatsuba}")
        else:
            print(f"✗ ERRO: Resultado incorreto!")
            print(f"  Karatsuba: {resultado_karatsuba}")
            print(f"  Esperado: {resultado_esperado}")
        
        print(f"Tempo de execução: {tempo_karatsuba:.6f} segundos")

def exemplo_interativo():
    print("\n" + "=" * 60)
    print("MODO INTERATIVO")
    print("=" * 60)
    
    while True:
        try:
            print("\nDigite dois números para multiplicar (ou 'q' para sair):")
            entrada1 = input("Primeiro número: ").strip()
            
            if entrada1.lower() == 'q':
                break
                
            entrada2 = input("Segundo número: ").strip()
            
            if entrada2.lower() == 'q':
                break
            
            x = int(entrada1)
            y = int(entrada2)
            
            print(f"\nCalculando {x} × {y}...")
            
            resultado_karatsuba, tempo_karatsuba = medir_tempo(karatsuba, x, y)
            
            print(f"Resultado: {resultado_karatsuba}")
            print(f"Tempo de execução: {tempo_karatsuba:.6f} segundos")
                
        except ValueError:
            print("Por favor, digite números inteiros válidos.")
        except KeyboardInterrupt:
            print("\nSaindo...")
            break

def main():
    print("ALGORITMO DE KARATSUBA - MULTIPLICAÇÃO EFICIENTE")
    print("Implementação em Python")
    print("Complexidade: O(n^log₂3) ≈ O(n^1.585)")

    testar_algoritmos()
    
    print("\n" + "=" * 60)
    resposta = input("Deseja testar com seus próprios números? (s/n): ").strip().lower()
    
    if resposta in ['s', 'sim', 'y', 'yes']:
        exemplo_interativo()
    
    print("\nObrigado por usar o algoritmo de Karatsuba!")

if __name__ == "__main__":
    main()