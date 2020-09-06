import datetime


class Utils:

    @staticmethod
    def datetime_format(date):
        saida = date
        print(saida)
        if date == "1899-12-31 00:00:00" or date == "21/12/1961 00:00" or date == "04/01/1966 00:00":
            print(saida)
            return datetime.datetime.strptime("1970-01-01 00:00", '%Y-%m-%d %H:%M')

        if len(date) > 16:
            exp = date.split('.')
            saida = exp[0][:-3]
            saida_exp = saida.split('-')

            print(saida)

            if len(saida_exp) > 2:
                return datetime.datetime.strptime(saida, '%Y-%m-%d %H:%M')

        return datetime.datetime.strptime(saida, '%d/%m/%Y %H:%M').strftime("%Y-%m-%d %H:%M")

    @staticmethod
    def date_format(date):
        exp = date.split(' ')
        return datetime.datetime.strptime(exp[0], '%d/%m/%Y').strftime("%Y-%m-%d")
