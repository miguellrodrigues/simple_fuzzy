from fuzzy_set import FuzzySet

# conjuntos = { baixa, media baixa, media alta }

baixa = FuzzySet(FuzzySet.TRIANGULAR, [])
media_baixa = FuzzySet(FuzzySet.TRIANGULAR, [])
media_alta = FuzzySet(FuzzySet.TRIANGULAR, [])

precipitacao_acumulada = [13.6, 115, 148, 31, 3, 320, 110, 180, 102, 123, 23]
salinidade_inicial = [14, 30, 24, 18, 18, 26, 20, 18, 25, 30, 23]
vazao_rio = [2016, 1163, 763, 1515, 2273, 687, 938, 800, 584, 469, 1454]
salinidade_observada = [6, 18, 18, 15, 8, 5, 13, 16, 25, 26, 17]

salinidade_final = []

# R 1 -Se chuva acumulada em Cananéia no intervalo de 1 a 3 dias for baixa E a salinidade inicial do
# período for média baixa E a salinidade inicial do periodo for média baixa E e a vazão do Rio Ribeira
# é alta E a salinidade final é baixa.
# R 11 -Se a chuva acululada em Cananéia no intervalo de 1 a 3 dias for média alta E a salinidade inicial
# do período for média baixa E a vazão do Rio Ribeira for baixa Então a salinidade final é média
# baixa.

