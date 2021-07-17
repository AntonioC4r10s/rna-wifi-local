from sklearn.neural_network import MLPClassifier
import streamlit as st
import pandas as pd

enderecodata = '/home/antonio/PycharmProjects/rna-wifi-local/src/wifi_localization1.csv'
datas = pd.read_csv(enderecodata)

entradas = pd.read_csv(enderecodata, usecols=['wifi-1', 'wifi-2', 'wifi-3', 'wifi-4', 'wifi-5',
                                              'wifi-6', 'wifi-7'])
entradas = entradas.values.tolist()
saidas = pd.read_csv(enderecodata, usecols=['sala'])
saidas = saidas.values.tolist()
print(saidas)

redeNeural = MLPClassifier(verbose=False,
                           max_iter=100,
                           tol=0.001,
                           activation='logistic',
                           learning_rate_init=0.1,
                          solver='sgd')  # cria a RNA

st.title("Encontrando localização através do wifi")

st.sidebar.header("Menu")
sb = st.sidebar.selectbox(label='Esscolha uma opção', options=['Informações', 'Teste'])

if sb == 'Informações':

    st.subheader("RNA com sklearn")
    st.markdown("Neste projeto tem como objetivo treinar uma RNA com medições da distancia e qualidade do sinal "
                "de wifi entre algumas salas. Ao longo da execução, será passado o modelo com 2000 testes "
                "feitos, e feito uma predicção. Ao fim, o modelo será capaz de deduzir em qual sala "
                "o receptor com as coordenadas passadas pode estar.")

    st.dataframe(datas)

if sb == 'Teste':

    wifi1 = st.number_input("Wifi-1", min_value=-89, max_value=-56, value=-60)
    wifi2 = st.number_input("Wifi-2", min_value=-89, max_value=-56, value=-60)
    wifi3 = st.number_input("Wifi-3", min_value=-89, max_value=-56, value=-60)
    wifi4 = st.number_input("Wifi-4", min_value=-89, max_value=-56, value=-60)
    wifi5 = st.number_input("Wifi-5", min_value=-89, max_value=-56, value=-60)
    wifi6 = st.number_input("Wifi-6", min_value=-89, max_value=-56, value=-60)
    wifi7 = st.number_input("Wifi-7", min_value=-89, max_value=-56, value=-60)

    redeNeural.fit(entradas, saidas)
    if st.button(label="Calcular teste"):
        resultado = redeNeural.predict([[wifi1, wifi2, wifi3, wifi4, wifi5, wifi6, wifi7]])
        st.text("O receptor pode estar na sala " + str(resultado[0]) + "!")
