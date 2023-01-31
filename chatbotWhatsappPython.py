### INSTRUÇÕES BÁSICAS ###
# 1 PASSO: INSTALAR O PYTHON
# 2 PASSO: VERIFICAR A VERSÃO DO CHROME E BAIXAR O CHROMEDRIVER CORRESPONDENTE
# 3 PASSO: INSTALAR A BIBLIOTECA SELENIUM -> CTRL + R -> DIGITA: CMD E PRESSIONA ENTER - > pip install selenium
# 4 PASSO: INSETIR O CÓDIGO ABAIXO E SALVAR COMO chatbotWhatapp.py ATRAVÉS DE UM EDITOR DA SUA PREFERÊNCIA
# 5 PASSO: DEIXAR O CHROMEDRIVER NO MESMO DIRETÓRIO DO SCRIPT "chatbotWhatapp.py"
# 6 PASSO: EXECUTAR O SCRIPT


'''
Selenium é uma biblioteca de automação de navegador que permite controlar navegadores web
(como o Google Chrome, Firefox, etc.) através de um script. Ele é amplamente utilizado para
automatizar tarefas de teste, raspagem de dados e interação com páginas da web. Ele suporta 
múltiplas linguagens de programação, incluindo Python, Java, C# e Ruby. Além disso, ele se 
integra com ferramentas de teste de software, como o JUnit e TestNG, para permitir a automação 
de testes funcionais.
'''
from selenium import webdriver

'''
A linha de código "from selenium import webdriver" é usada para importar a classe WebDriver do 
módulo selenium. O WebDriver é a principal classe na biblioteca Selenium, que fornece uma interface
para controlar um navegador web. Com essa linha de código, você pode criar uma instância da classe
WebDriver para controlar o navegador especificado e realizar ações como navegar para uma página, 
preencher formulários, clicar em botões e coletar dados da página.
from selenium.webdriver.common.keys import Keys
'''

from selenium.webdriver.common.by import By

'''
A linha de código "from selenium.webdriver.common.by import By" importa a classe By do módulo common.by 
dentro do pacote webdriver do Selenium. A classe By é usada para especificar como um elemento da página 
web será localizado quando se usa o método "find_element" ou "find_elements" do WebDriver. Ele define 
diferentes formas de localizar um elemento, como por ID, nome, classe, xpath, entre outros, assim você
pode especificar como um elemento deve ser encontrado de acordo com sua estrutura HTML. Por exemplo,
você pode usar By.ID para localizar um elemento por seu atributo "id" ou By.XPATH para localizar um 
elemento usando uma expressão XPath.
'''



def enviararrayMensagensDiversas(text):
    navegador.find_element(By.XPATH, '/html//div[@id="main"]/footer[@class="_3E8Fg"]//div[@class="g0rxnol2"]//div[@role="textbox"]').click() # ativar campo para digitar mensagem
    navegador.find_element(By.XPATH, '/html//div[@id="main"]/footer[@class="_3E8Fg"]//div[@class="g0rxnol2"]//div[@role="textbox"]').send_keys(text)	   # ativação do campo para digitação da mensagem no whatsapp 
    navegador.find_element(By.XPATH,'//*[@id="main"]//button[@class="tvf2evcx oq44ahr5 lb5m6g5c svlsagor p2rjqpw5 epia9gcq"]').click() #enviar mensagem digitada


    arrayMensagensDiversas = navegador.find_elements(by='xpath', value='//*[@id="main"]//span[@class="_11JPr selectable-text copyable-text"]')  #textos digitados no whatsapp
    ultimaMensagem.append(arrayMensagensDiversas[-1].text)


navegador = webdriver.Chrome()

'''
A linha de código "navegador = webdriver.Chrome()" cria uma instância do navegador
Google Chrome usando a classe Chrome do pacote webdriver do Selenium. Essa linha de
código inicia o navegador Chrome e o torna pronto para ser controlado pelo script.
A partir desse ponto, você pode usar métodos dessa instância, como get() para navegar
para uma página específica, find_element() para localizar elementos da página, entre outros.
É importante notar que para usar essa linha de código é necessário ter o driver do Chrome 
instalado e configurado corretamente no seu sistema.
'''

navegador.get("https://web.whatsapp.com/")
navegador.maximize_window()

arrayMensagensDiversas =['NO_INICIAL']  #capturará todas as mensagens disponíveis      
historicoMensagens=['NO_INICIAL']       #armazenará todas as mensagens enviadas pelos usuários
ultimaMensagem=['NO_INICIAL']           #conterá sempre a última mensagem encaminhada pelo usuário


loop = True

enter=input("PRESSIONE ENTER PARA CONTINUAR APÓS SELECIONAR O GRUPO OU USUÁRIO DO WHATSAPP:")



while loop:

    try:
        arrayMensagensDiversas = navegador.find_elements(by='xpath', value='//*[@id="main"]//span[@class="_11JPr selectable-text copyable-text"]')  #todos os textos digitados no whatsapp
        ultimaMensagem.append(arrayMensagensDiversas[-1].text)      #adiciona a última mensagem digitada no array ultimaMensagem, extratindo de arrayMensagensDiversas[-1].text
        
        if not (ultimaMensagem[-1]== historicoMensagens[-1]): # se a última mensagem contida no whatsapp já estiver registrada no historico, ou seja, se a solicitação já estiver processada, não executará 
            historicoMensagens.append(ultimaMensagem[-1])  #caso seja uma nova solicitação, adicionará no historico para futura comparação
            if len(ultimaMensagem[-1])>6 and ("?" in ultimaMensagem[-1] or "!" in ultimaMensagem[-1]):  #inicio do processamento das mensagens e checagem de solicitações

                enviararrayMensagensDiversas("Vejo que você tem uma dúvida! Vou consultar no meu banco de dados a resposta para a sua solicitação!")
                
            if "BOM DIA" in ultimaMensagem[-1].upper():

                enviararrayMensagensDiversas("Também lhe desejo um excelente dia!")

            if "BOA NOITE" in ultimaMensagem[-1].upper():

                enviararrayMensagensDiversas("Também lhe desejo umA excelente noite!")



        else:
            #print("Não tem resposta, pois já foi respondido")
            continue

         
    except:
        {print("Exceção / Tratamento de erro")}






