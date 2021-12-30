# **Padroes-de-projeto**
Demonstração do funcionamento dos padrões de projeto 'Template Method' e 'Command' que foram escolhidos para o meu grupo na cadeira de análise e projeto de software. 
## *Authors*

- [@guivilarim](https://www.github.com/guivilarim) - Guilherme Cavalcanti Vilarim
- [@lucaslmrs](https://github.com/lucaslmrs) - Lucas Matheus Rodrigues dos Santos
- [@vini-silva](https://github.com/vini-silva) - Vinicius Ferreira Silva

# **Padrões de Projeto: Template Method e Command**

## ***Template Method:***

O Template Method é um padrão de projeto comportamental que tem por definição implementar o esqueleto de um algoritmo na superclasse mas deixa as subclasses sobrescreverem etapas específicas do algoritmo sem modificar sua estrutura orginal. Isso é feito com o intuito de proteger a superclasse, fornecendo métodos abstratos a fim das subclasses utilizarem.

Para esse padrão de projeto comportamental, optamos por criar um esqueleto de 'Carro' em que a partir dessa superclasse, as subclasses seriam variações desses veículos

Na superclasse de 'Carro', colocamos os seguintes métodos abstratos de:
- add_porta: Método abstrato com o intuito de adicionar o número de portas ao carro, em que será atribuida ao atributo 'qtd_portas'. E definir seu tipo de porta: se será 'regular', 'automática' ou 'blindada' que será atribuida ao atributo 'porta'.
- add_pneu: Método abstrato com o intuito de definir seu tipo de pneu: se será 'Misto - À prova de balas', 'Onroad' ou 'Offroad' que será atribuida ao atributo 'pneus'.
- add_parabrisa: Método abstrato com o intuito de definir seu tipo de para-brisa: se será 'Vidro Temperado' ou 'Vidro laminado' que será atribuida ao atributo 'parabrisa'.
- add_motor: Método abstrato com o intuito de definir seu tipo de motor: se será 'V6', 'V8' ou 'Elétrico' que será atribuida ao atributo 'motor'.
- add_tipo_combustivel: Método abstrato com o intuito de definir seu tipo de combustível: se será 'gasolina' ou 'Gás' que será atribuida ao atributo 'tipo_combustivel'.
- abastecer: Método abstrato com o intuito de abastercer o atributo 'nivel_combustivel'.
- add_cambio: Método abstrato com o intuito de definir seu tipo de câmbio: se será 'Manual' ou 'Automático' que será atribuida ao atributo 'cambio'.
- andar: Método abstrato com o intuito de realizar os movimentos ao objeto carro.

## ***Command:***

O Command Method é um padrão de projeto que tem como objetivo abstrair toda a execução de um comando no código. Não apenas isso, como também é possível armazenar um histórico, enfileirar comandos e até cancelar operações.

A ideia por trás do Command é criar uma classe 'Invoker' que é responsável por armazenar todos os comandos que serão executados. Além disso, há também há a criação de uma interface 'Command' que possui o método 'execute' e pode possuir muitos outros tipos de chamadas, como 'undo', 'armazenar', 'recuperar', etc. Dessa forma, é possível criar várias classes que serão responsáveis por um determinado tipo de comando. Em resumo, são criados comandos para realizar algum tipo de ação e, a partir desses comandos, dizemos se queremos um 'execute' ou algum outro método implementado.

Com isso, optamos por criar um assistente virtual chamada de 'Vanellope' a fim de automatizar os aparelhos da casa. Com base nisso, montamos nossas classes separadas por pacotes. Cada pacote é responsável por conter os códigos relacionados às ações de um determinado aparelho e os arquivos dentro de cada pacote são divididos em dois tipos, o tipo command e o arquivo que carrega a classe referente ao objeto.

Para as classes principais, referente aos objetos, temos métodos que são opostos entre si, e que serão chamados pelas funções 'execute' e 'undo', que são os métodos mais usados por esse padrão de projeto os quais foram escolhidos para esse projeto. 

Como exemplo, podemos citar a classe 'Luz', cujas responsabilidades são ligar, desligar, aumentar e diminuir a intensidade do seu brilho. E, a partir dessas responsabilidades, foram criadas novas classes "Commands", e.g. a classe 'LuzPowerCommand' que controla as ações de ligar e desligar o dispositivo com seus métodos 'execute' e 'undo'. Após ter instanciado a classe LuzPowerCommand e adicionado à classe 'CasaInteligenteInvoker', nossa classe invoker, pelo método 'addCommands', podemos executar esse comando na forma "vanellope.executar_comando('luz quarto power')". Além disso, temos a possibilidade de desfazer esse comando usando "vanellope.undo_comando('luz quarto power')".

## *Informações adicionais:*
Para executar o código, basta seguir o passo a passo:

- No console do seu computador, executar os comandos abaixo:

        git clone https://github.com/Poli-Shopping/Padroes-de-projeto.git

        cd Padroes-de-projeto

        pip install -r requirements.txt

        python main.py
