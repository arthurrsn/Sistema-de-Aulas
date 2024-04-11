# Perguntar ao usuário o horário de início das aulas e o horário de término das mesmas
horario_inicio_aulas = input("Qual é o horário de início das aulas? (hh:mm) ")
horario_termino_aulas = input("Qual é o horário de término das aulas? (hh:mm) ")

# Converter os horários para minutos desde a meia-noite
inicio_aulas_horas, inicio_aulas_minutos = map(int, horario_inicio_aulas.split(':'))
termino_aulas_horas, termino_aulas_minutos = map(int, horario_termino_aulas.split(':'))

inicio_aulas_total_minutos = inicio_aulas_horas * 60 + inicio_aulas_minutos
termino_aulas_total_minutos = termino_aulas_horas * 60 + termino_aulas_minutos

# Calcular a duração do período de aulas em minutos
duracao_aulas_minutos = termino_aulas_total_minutos - inicio_aulas_total_minutos

# Perguntar ao usuário quantas aulas os alunos têm por dia e a duração de cada aula
quantidade_aulas = int(input("Quantas aulas os alunos têm por dia? "))
duracao_aula_minutos = int(input("Qual é a duração de cada aula em minutos? "))

# Calcular o total de minutos de aulas por dia
total_minutos_aulas = quantidade_aulas * duracao_aula_minutos

# Calcular o tempo de intervalo entre as aulas
tempo_intervalo_minutos = duracao_aulas_minutos - total_minutos_aulas

# Mostrar os resultados
print("\nHorário de início das aulas:", horario_inicio_aulas)
print("Horário de término das aulas:", horario_termino_aulas)
print("Duração do período de aulas:", duracao_aulas_minutos, "minutos")
print("Total de minutos de aulas por dia:", total_minutos_aulas, "minutos")
print("Soma do tempo de intervalo entre as aulas:", tempo_intervalo_minutos, "minutos")

# Salvar os resultados em variáveis
horario_inicio_aulas = (horario_inicio_aulas)
horario_termino_aulas = (horario_termino_aulas)
duracao_periodo_aulas = duracao_aulas_minutos
quantidade_aulas_por_dia = quantidade_aulas
duracao_aula = duracao_aula_minutos
total_minutos_aulas_por_dia = total_minutos_aulas
soma_tempo_intervalo_entre_aulas = tempo_intervalo_minutos
