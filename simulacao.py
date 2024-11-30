from geradores import Gerador_Aleatorio, Gerador_TEC, Gerador_TS

class Cliente:
    def __init__(self, gerador_Aleatorio, gerador_TEC, gerador_TS):
        check = gerador_Aleatorio.random()
        if   (check < 0.6):
            self.tipo = 1
        elif (check < 0.9):
            self.tipo = 2
        else:
            self.tipo = 3
        self.TEC = round(gerador_TEC.random(),2)
        self.TS  = round(gerador_TS.random(self.tipo),2)

    # Utilizado para debug
    def __str__(self):
        return f'(Tipo:{self.tipo},TEC:{self.TEC},TS:{self.TS})'

class Simulacao:
    def __init__(self, seed, n_aten = 1):
        self.GA   = Gerador_Aleatorio(seed)
        self.GTEC = Gerador_TEC(self.GA)
        self.GTS  = Gerador_TS(self.GA)
        self.n_aten = n_aten
      
    def run(self, T_chegada_max = 3600):
        # Inicializa o cabeçalho e a tabela  da simulação
        cabecalho = ['Cliente','Tipo','TEC','TS','Chegada-Relogio','Inicio-Servico',
                     'Fim-Servico','Tempo-Fila','Tempo-Sistema','Tempo-Ocioso']
        cabecalho += [f'Atendente{i+1}' for i in range(0,self.n_aten)]
        tabela_simul = [cabecalho]
        # Inicializa o contador e o primeiro cliente
        i, cl = 1, Cliente(self.GA, self.GTEC, self.GTS)
        atual = [i , cl.tipo, cl.TEC, cl.TS, cl.TEC, cl.TEC, cl.TEC + cl.TS, 0, cl.TS, cl.TEC]
        atendentes = [atual[6]] + [0 for i in range(0,self.n_aten-1)]
        
        while (atual[4] <= T_chegada_max):
            atual += atendentes
            tabela_simul.append(atual)
            anterior = atual
            i, cl = i+1, Cliente(self.GA, self.GTEC, self.GTS)
            # Vai ser atendido pelo atendente que ficar disponível mais rápido
            i_atendente = atendentes.index(min(atendentes))
            t_cheg = round(anterior[4] + cl.TEC, 2)
            t_ini  = round(max(atendentes[i_atendente],t_cheg), 2)
            t_fim  = round(t_ini + cl.TS, 2)
            t_fila = round(t_ini - t_cheg, 2)
            t_sis  = round(t_fila + cl.TS, 2)
            t_oci  = round(t_ini - atendentes[i_atendente], 2)
            # Esse atendente só vai ficar disponível após o término do atendimento
            atendentes[i_atendente] = t_fim
            atual = [i, cl.tipo, cl.TEC, cl.TS, t_cheg, t_ini, t_fim, t_fila, t_sis, t_oci]
        return tabela_simul