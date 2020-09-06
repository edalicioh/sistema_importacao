from dao.Dao import Dao


class DadosDao(Dao):

    def insert(self, params):
        sql = """
            INSERT INTO dados ( 
                data_publicacao,
                recuperados,
                data_inicio_sintomas,
                data_coleta,
                sintomas,
                comorbidades,
                gestante,
                internacao,
                internacao_uti,
                sexo,
                municipio,
                obito,
                data_obito,
                idade,
                regional,
                raca,
                data_resultado,
                codigo_ibge_municipio,
                latitude,
                longitude,
                estado,
                criterio_confirmacao,
                tipo_teste,
                municipio_notificacao,
                codigo_ibge_municipio_notificacao,
                latitude_notificacao,
                longitude_notificacao,
                classificacao,
                origem_esus,
                origem_sivep,
                origem_lacen,
                origem_laboratorio_privado,
                nom_laboratorio,
                fez_teste_rapido,
                fez_pcr,
                data_internacao,
                data_entrada_uti,
                regional_saude,
                data_evolucao_caso,
                data_saida_uti,
                bairro
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
        """

        self.db.execute_query(sql, params)
        self.db.conn.commit()
