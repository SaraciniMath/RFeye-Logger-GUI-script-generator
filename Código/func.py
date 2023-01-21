def converte_tempo(tempo, unidade):
    if unidade == 'milissegundos':
        saida = tempo + ' ms'
        return saida
    elif unidade == 'segundos':
        saida = tempo + ' sec'
        return saida
    elif unidade == 'minutos':
        saida = tempo + ' mins'
        return saida
    elif unidade == 'horas':
        saida = tempo + ' hour'
        return saida

def converte_tempo_2(unidade):
    if unidade == 'milissegundos':
        saida = 'ms'
        return saida
    elif unidade == 'segundos':
        saida = 'sec'
        return saida
    elif unidade == 'minutos':
        saida = 'mins'
        return saida
    elif unidade == 'horas':
        saida = 'hour'
        return saida

def inserir(texto, df):
    if texto in df.id.values:
        print("Existe")
        print(df)
    else:
        # append row to the dataframe
        new_row = {'id': str(texto), 'tipo': 87, 'param': 92}
        # df.insert(2, str(self.lineEdit_5.text()), 87, 87)
        # df_new_row = pd.DataFrame({'id': [str(self.lineEdit_5.text())], 'tipo': [2], 'param': [3]})
        # df = pd.concat([df, df_new_row], ignore_index=True)

        df = df.append(new_row, ignore_index=True)
        print(df)
        print("Nao existe")
        return df

