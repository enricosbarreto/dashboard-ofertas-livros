"""Leitura dos arquivos CSV do projeto.
"""

from pathlib import Path
import csv

PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

def processar_dados():
    livros = []
    
    with open(CAMINHO_LIVROS, mode='r', encoding='utf-8') as ficheiro:
        leitor = csv.DictReader(ficheiro)
        for linha in leitor:
            livros.append(linha)
    
    soma_precos = 0.0
    total_livros = len(livros)
    livros_5_estrelas = 0
    livro_mais_caro = None
    maior_preco = -1.0
    
    for livro in livros:
        preco_str = str(livro.get('preco', '0')).replace('£', '').replace('R$', '').strip()
        
        try:
            preco = float(preco_str)
        except ValueError:
            preco = 0.0
            
        soma_precos += preco
        
        if preco > maior_preco:
            maior_preco = preco
            livro_mais_caro = livro
        
        nota = str(livro.get('nota', '')).strip().lower()
        if nota in ['five', '5']:
            livros_5_estrelas += 1

    preco_medio = soma_precos / total_livros if total_livros > 0 else 0

    return livros, preco_medio, livros_5_estrelas, livro_mais_caro

if __name__ == "__main__":
    livros, preco_medio, contagem_5_estrelas, mais_caro = processar_dados()
    print(f"Total de livros: {len(livros)}")
    print(f"Preço médio: £ {preco_medio:.2f}")
    print(f"Livros com 5 estrelas: {contagem_5_estrelas}")
    if mais_caro:
        print(f"Mais caro: {mais_caro['titulo']} - £ {mais_caro['preco']}")