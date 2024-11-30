import csv
import statistics as st
from simulacao import Simulacao

def extrair_estatisticas(tabela_simul):
    # Média das estatísticas pedidas (ignorando a linha 0 - cabeçalho)
    t_espera_fila        = [linha[7] for linha in tabela_simul[1:]]
    t_servico            = [linha[3] for linha in tabela_simul[1:]]
    t_sistema            = [linha[8] for linha in tabela_simul[1:]]
    t_ocioso_funcionario = [linha[9] for linha in tabela_simul[1:]]
    estatisticas = [round(st.mean(t_espera_fila),        2),
                    round(st.mean(t_servico),            2),
                    round(st.mean(t_sistema),            2),
                    round(st.mean(t_ocioso_funcionario), 2)]
    return estatisticas

def tabela_simul_para_csv(tabela_simul, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(tabela_simul)

def estatisticas_para_csv(estatisticas, nome_arquivo):
    with open(nome_arquivo, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(estatisticas)

def main(seeds, T_chegada_max):
    # Escrita do cabeçalho do arquivo de estatísticas
    cabecalho = ['T médio espera na fila', 'T médio serviço',
                 'T médio sistema', 'T médio ocioso funcionário']
    estatisticas_para_csv(cabecalho, 'resultados.csv')
    # Execução das simulações e escrita dos resultados
    for seed in seeds:
        simulacao = Simulacao(seed,1)
        tabela_simul = simulacao.run(T_chegada_max)
        estatisticas = extrair_estatisticas(tabela_simul)
        tabela_simul_para_csv(tabela_simul, f'tabelas/simul_{seed}.csv')
        estatisticas_para_csv(estatisticas, 'resultados.csv')
    
if __name__=="__main__":
    main([i for i in range(10, 1010)], 3600)