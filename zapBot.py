from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Mensagem Automatica Para" #mensagem inicial
        self.pessoas = ["Contato 1", "Contato 2", "Contato 3"] #um array para colocar o nome dos contatos {Deverá conter o nome exato do contato que o seu whatsapp está cadastrado}
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):

        self.driver.get('https://web.whatsapp.com')

        time.sleep(30)
        
        for pessoa in self.pessoas:#este for fica responsavel por fazer isso com todos os contatos que foram cadastrados na variavel pessoas
            pessoa = self.driver.find_element_by_xpath(f"//span[@title='{pessoa}']")
            pessoa.click()#clica no contato indicado pelo nome

            time.sleep(2)

            chatBox = self.driver.find_element_by_class_name('_13mgZ')
            chatBox.click()#clica no campo onde a mensagem deve ser inserida

            time.sleep(2)

            mensagemp .= ' '+pessoa # está parte não está conseguindo enviar com o nome da pessoa, alterações são bem vindas.

            chatBox.send_keys(mensagemp)# digita a mensagem que deve ser enviada

            time.sleep(2)

            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            botao_enviar.click()#clica no botão de enviar a mensagem

            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()
