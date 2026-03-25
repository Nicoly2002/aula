Aula 25/03

Nicoly Cristina 2519155
 5 Semestre de ADS Manha

1. Qual é o objetivo do algoritmo?
Demonstrar o aprendizado de máquina (Machine Learning).
 
2. O que representam as variáveis X e y?
X: o que queremos saber. 
y: o que queremos prever. 
 
3. Para que serve train_test_split()?
Dividir conjuntos de dados em partes distintas: uma para treinamento e outra para teste de modelos de aprendizado.

4. O que faz o método .fit()?
O método pega os dados de treino e ajusta a matemática interna do algoritmo para encontrar os padrões ocultos.

5. O que faz o método .predict()?
Ele recebe dados inéditos (teste) e gera as respostas baseadas nas regras ou vizinhanças que aprendeu durante o .fit().

6. O que é acurácia?
A Acurácia é a taxa de acerto. 

7. Para que serve accuracy_score()?
A função accuracy_score() ela alinha as respostas reais (y_teste) com as respostas do modelo (pred) e calcula a porcentagem de acertos.


8. O que é a matriz de confusão?
Verificador dos erros. Enquanto a acurácia diz o quanto acertamos, a matriz mostra como erramos.

9. Qual a diferença entre Árvore de Decisão e KNN?
Árvore de Decisão: Cria uma sequência lógica de perguntas sobre as características dos dados.
KNN: Olha para os dados mais próximos no gráfico e adota a classe da maioria.

10. Por que usar dois modelos no algoritmo?
Para comparar o desempenho lado a lado, identificar pontos fortes e descobrir qual arquitetura e mais eficiente.

11. Um modelo com alta acurácia pode ser ruim? Por quê?
Porque a acurácia mede apenas a porcentagem total de acertos, o que pode esconder as falhas, especialmente quando os dados não estão equilibrados.
