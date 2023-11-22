from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class QuizApp(App):
    def build(self):
        self.score = 0
        self.question_index = 0

        self.questions = [
             {"question": "Quem descobriu o Brasil?",
             "options": ["Cristovão da Gama", "Pedro Álvares Cabral", "Dom Pedro", "Floriano Peixoto"],
             "correct_option": "Pedro Álvares Cabral"},

             {"question": "Encontre as vogais?",
             "options": ["p,q,r,s,t", "a,b,c,d,e", "a,e,i,o,u", "l,m,n,o,p"],
             "correct_option": "a,e,i,o,u"},

              {"question": "Encontre um planeta do nosso sistema solar?",
             "options": ["Sol", "Lua", "Marte", "Orion"],
             "correct_option": "Marte"},

              {"question": "Qual desses não é uma fruta?",
             "options": ["Mamão", "Caju", "Tomate", "Amendoim"],
             "correct_option": "Amendoim"},  
              
              {"question": "Qual é a vogal que faz o som em 'elefante'?",
            "options": ["a", "e", "i", "o"],
            "correct_option": "e"},


            {"question": "Na palavra 'abelha', qual é a segunda vogal?",
            "options": ["a", "e", "i", "o"],
    "correct_option": "e"},

    {"question": "Complete a palavra: c__sa",
    "options": ["a", "e", "i", "o"],
    "correct_option": "a"},

    {"question": "Quantas vogais têm a palavra 'família'?",
    "options": ["3", "4", "5", "6"],
    "correct_option": "4"},

    {"question": "Na palavra 'avião', quais são as duas vogais?",
    "options": ["a, e", "a, i", "a, o", "e, i"],
    "correct_option": "a, o"},

    {"question": "Complete a sequência de vogais: __, __, i, __, u",
    "options": ["a, e, o", "e, i, o", "o, u, a", "i, o, u"],
    "correct_option": "a, e, o"},

    {"question": "Qual é a vogal que vem antes de 'a' na palavra 'coração'?",
    "options": ["e", "i", "o", "u"],
    "correct_option": "o"},

    {"question": "Complete a palavra: l__ão",
    "options": ["a", "e", "i", "o"],
    "correct_option": "e"},

    {"question": "Quantas vogais têm a palavra 'papagaio'?",
    "options": ["3", "4", "5", "6"],
    "correct_option": "5"},

    {"question": "Na palavra 'bola', quais são as duas vogais?",
    "options": ["o, u", "a, e", "o, a", "o, i"],
    "correct_option": "o, a"},

    {"question": "Complete a palavra: __rvilha",
    "options": ["a", "e", "i", "o"],
    "correct_option": "e"},

    {"question": "Quantas vogais têm a palavra 'escola'?",
    "options": ["3", "4", "5", "6"],
    "correct_option": "3"},

    {"question": "Qual é a vogal que vem antes de 'e' na palavra 'nuvem'?",
    "options": ["a", "e", "i", "o"],
    "correct_option": "u"},

    {"question": "Complete a palavra: p__lhaço",
    "options": ["a", "e", "i", "o"],
    "correct_option": "a"},

    {"question": "Na palavra 'amigo', qual é a terceira vogal?",
    "options": ["a", "e", "i", "o"],
    "correct_option": "o"},

    {"question": "Quantas vogais têm a palavra 'floresta'?",
    "options": ["3", "4", "5", "6"],
    "correct_option": "3"},

    {"question": "Na palavra 'gelado', quais são as três vogais?",
    "options": ["e, i, a", "e, o, u", "a, e, o", "i, o, u"],
    "correct_option": "e, a, o"},

    {"question": "Complete a palavra: __lefante",
    "options": ["a", "e", "i", "o"],
    "correct_option": "e"},

    {"question": "Quantas vogais têm a palavra 'barco'?",
    "options": ["2", "3", "4", "5"],
    "correct_option": "2"},

    {"question": "Na palavra 'chuva', quais são as duas vogais?",
    "options": ["a, e", "o, u", "a, o", "i, u"],
    "correct_option": "u, a"},
      # Adicione mais perguntas conforme necessário
        ]

        self.layout = BoxLayout(orientation='vertical')
        self.question_label = Label(text="")
        self.layout.add_widget(self.question_label)

        self.option_buttons = []  # Lista para armazenar os botões de opção dinamicamente

        self.update_question()  # Adicionado para exibir a primeira pergunta
        return self.layout

    def check_answer(self, instance):
        current_question = self.questions[self.question_index]

        if instance.text == current_question["correct_option"]:
            self.score += 10
            
            self.show_popup("Parabéns! Resposta correta - {} - \n Pontuação: {}".format(current_question["correct_option"], self.score))
            
        else:
            
            self.show_popup("Você errou. Resposta correta - {} - \n Pontuação: {}".format(current_question["correct_option"], self.score))

        self.question_index += 1

        if self.question_index < len(self.questions):
            self.update_question()
        else:
            self.show_popup("Quiz concluído. Pontuação final: {}".format(self.score))

    def update_question(self):
        current_question = self.questions[self.question_index]
        self.question_label.text = current_question["question"]

        # Limpa os botões de opção anteriores
        for button in self.option_buttons:
            self.layout.remove_widget(button)

        self.option_buttons = []  # Limpa a lista de botões

        # Adiciona novos botões de opção
        for option in current_question["options"]:
            btn = Button(text=option, on_press=self.check_answer)
            self.layout.add_widget(btn)
            self.option_buttons.append(btn)

    def show_popup(self, text):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=text))
        popup = Popup(title='Resultado', content=content, size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    QuizApp().run()
