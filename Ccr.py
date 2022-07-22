from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.core.window import Window
from kivymd.theming import ThemeManager



class Container(GridLayout):

    calculate = ''
    calculate2 = ''
    oper = ''
    ext = False

    def update_label(self):
        self.label.text = ''
        self.calculate = ''
        self.calculate2 = ''
        self.oper = ''
        self.ext = False
        self.label.font_size = '50sp'

    def downdate_label(self):
        self.label.text = ''


    def add_number(self, num):


        if len(self.oper) < 1 and self.ext == False:
            self.calculate += str(num)
            self.label.text += str(num)
        elif len(self.oper) == 1:
            self.calculate2 += str(num)
            self.label.text += str(num)


    def add_operation(self, op):

        self.downdate_label()
        self.oper += str(op)
        if len(self.oper) > 1:
            self.label.text = 'Введите только одно действие'
            self.label.font_size = '30sp'






    def add_dot(self, dott):

        p1 = str(self.calculate.find("."))
        p2 = str(self.calculate2.find("."))
        if len(self.oper) < 1 and p1 == '-1' and len(self.calculate) > 0:
            self.calculate += str(dott)
            self.label.text += str(dott)
        elif len(self.oper) == 1 and p2 == '-1' and len(self.calculate2) > 0:
            self.calculate2 += str(dott)
            self.label.text += str(dott)

    def add_nule(self, nul):

        n1 = str(self.calculate.find("0"))
        n2 = str(self.calculate2.find("0"))


        if len(self.oper) == 1:
            if len(self.calculate2) >= 2:
                self.calculate2 += str(nul)
                self.label.text += str(nul)

            elif n2 == '-1':
                if len(self.calculate2) <= 1:
                    self.calculate2 += str(nul)
                    self.label.text += str(nul)


        elif len(self.calculate) >= 2:
            self.calculate += str(nul)
            self.label.text += str(nul)

        elif n1 == '-1':
            if len(self.calculate) <= 1:
                self.calculate += str(nul)
                self.label.text += str(nul)



    def result(self):
        try:
            if self.oper == '/' and float(self.calculate2) == 0.0:
                self.label.text = 'Error'
            else:
                res = float(eval(self.calculate + self.oper + self.calculate2))
                self.label.text = str(res)
                self.calculate = str(res)
                self.oper = ''
                self.calculate2 = ''
                self.ext = True
        except:
            self.label.text = 'Error'


Window.size = (360, 640)

class CountApp(App):
    theme_cls = ThemeManager()
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Container()

if __name__ == "__main__":
    CountApp().run()
