import csv
import os
from db.create import Create
from dao.DadosDao import DadosDao
from Utils import Utils

create = Create()

dadosDao = DadosDao()

create.create_table()

index = 0

with open('boavista_covid_dados_abertos.csv', 'r') as arquivo:
    dados = csv.DictReader(arquivo, delimiter=";")
    for value in dados:
        index = index + 1
        data_publicacao = Utils.datetime_format(value['data_publicacao'])
        data_inicio_sintomas = Utils.date_format(value['data_inicio_sintomas'])
        data_obito = None
        data_entrada_uti = None
        data_internacao = None
        data_evolucao_caso = None
        data_saida_uti = None
        data_coleta = None

        if value['data_coleta'] != 'IGNORADO':
            data_coleta = Utils.date_format(value['data_coleta'])

        if value['data_obito'] != 'NULL':
            data_obito = Utils.date_format(value['data_obito'])

        if value['data_internacao'] != 'NULL':
            data_internacao = Utils.date_format(value['data_internacao'])

        if value['data_entrada_uti'] != 'NULL':
            data_entrada_uti = Utils.date_format(value['data_entrada_uti'])

        if value['data_evolucao_caso'] != 'NULL':
            data_evolucao_caso = Utils.date_format(value['data_evolucao_caso'])

        if value['data_saida_uti'] != 'NULL':
            data_saida_uti = Utils.date_format(value['data_saida_uti'])

        data_resultado = Utils.datetime_format(value['data_resultado'])
        val = (
            data_publicacao,
            value['recuperados'],
            data_inicio_sintomas,
            data_coleta,
            value['sintomas'],
            value['comorbidades'],
            value['gestante'],
            value['internacao'],
            value['internacao_uti'],
            value['sexo'],
            value['municipio'],
            value['obito'],
            data_obito,
            value['idade'],
            value['regional'],
            value['raca'],
            data_resultado,
            value['codigo_ibge_municipio'],
            value['latitude'],
            value['longitude'],
            value['estado'],
            value['criterio_confirmacao'],
            value['tipo_teste'],
            value['municipio_notificacao'],
            value['codigo_ibge_municipio_notificacao'],
            value['latitude_notificacao'],
            value['longitude_notificacao'],
            value['classificacao'],
            value['origem_esus'],
            value['origem_sivep'],
            value['origem_lacen'],
            value['origem_laboratorio_privado'],
            value['nom_laboratorio'],
            value['fez_teste_rapido'],
            value['fez_pcr'],
            data_internacao,
            data_entrada_uti,
            value['regional_saude'],
            data_evolucao_caso,
            data_saida_uti,
            value['bairro'],

        )

        dadosDao.insert(val)
        print(index)

print("Finall")
