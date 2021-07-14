from sklearn.neural_network import MLPClassifier
from data import my_data as md

entradas, saidas = md.dts()

redeNeural = MLPClassifier(verbose=False,
                           max_iter=100,
                           tol=0.001,
                           activation='logistic',
                           learning_rate_init=0.1,
                           solver='sgd')  # cria a RNA

redeNeural.fit(entradas, saidas)

print(redeNeural.predict([[-39, -54, -53, -45, -68, -78, -81]]))
