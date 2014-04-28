#/////////////// LIBRARIES ///////////////////# {
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.app import runTouchApp
from kivy.lang import Builder
from kivy.uix.button import Button

 
__author__ = 'Mark Anthony Remetir Pequeras'
__devteam__ = 'CoreSEC Softwares'

#/////////////// LIBRARIES ///////////////////# }






#/////////// C.C++.CPython ///////////////////# {

#/////////// C.C++.CPython ///////////////////# }



#///////////////// KV Lang ///////////////////# {

Builder.load_string("""
# KV Language Start {


# KV Language End }
""")

#///////////////// KV Lang ///////////////////# }






#///////////////// Python ///////////////////# {
from kivy.parser import parse_color
class B(Button):
    def __init__(self, **kwargs):
        super(B, self).__init__(**kwargs)
        self.size_hint=None,None
        self.size=123,50
        self.text="123"
        self.background_normal="#ffffff"
        self.color=parse_color("#000000")
        self.opacity=.9
    def on_press(self):
        print "Finished"


class AnchorOne(AnchorLayout):
    def __init__(self,**kwargs):
        super(AnchorOne,self).__init__(**kwargs)
        self.anchor_x="right"
        self.anchor_y="top"
        self.add_widget(B())









# Main Function
class main(FloatLayout):
    def __init__(self,**kwargs):
        super(main,self).__init__(**kwargs)
        self.add_widget(AnchorOne())

#///////////////// Python ///////////////////# }



if __name__ == "__main__":
    runTouchApp(main())












