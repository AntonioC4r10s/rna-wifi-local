import csv


archive = open('../src/wifi_localization.csv', 'r')  # Abrindo um arquivo
datas = csv.reader(archive, delimiter=',', )  # Abrindo o arquivo como csv


#   Função que retorna o vetor de entradas e o vetor de saidas
def dts():
    e = []
    s = []
    for row in datas:
        e_temp = []
        for column in range(0, 7):
            e_temp.append(int(row[column]))
        e.append(e_temp)
        s.append(int(row[7]))
    return e, s
