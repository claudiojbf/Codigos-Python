from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.data_formatada()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "marco",
            "abril", "maio", "junho", "julho",
            "agosto", "setembro", "outubro",
            "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        semanas = [
            "segunda", "terca",
            "quarta", "quinta", "sexta", 
            "sabado","domingo"
        ]

        semana_cadastro = self.momento_cadastro.weekday() 
        
        return semanas[semana_cadastro]

    def data_formatada(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro