from kivy.app import App
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import  Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.checkbox import  CheckBox
from kivy.uix.slider import  Slider
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import  Spinner
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout


Config.set('graphics', 'orientation', 'landscape')
class BMI_Calculator(App):
    def build(self):
        self.power_h=1
        self.power_w = 1
        self.layout= FloatLayout() 
        button = Button(text="Calculate",color=(0,0,0,1), background_normal="box.png",on_press=self.calculate_action,size_hint=  (.5,.08) ,pos_hint = {"x": .450, "y": .32})
        
        btn4=Button(text="BMI Calculator",size_hint=(1,.07),pos=(0,1370),background_color=(1,0,1,1))
        self.layout.add_widget(btn4)
       
        
        #knowledge box 
        btn_k=Label(text="Knowledge Box",size_hint=(.3,.06),pos=(130,300),color=(0,1,1,1),font_size=40)
        btn_k.underline=True
        self.layout.add_widget(btn_k)
        
        img2=Image(source = "bmi_box2.png",size_hint=(1,.217))
        self.layout.add_widget(img2)
        
       
        
        #self.btn5=None
        
        lbl = Image(source  = "gender.png",size_hint=(.268,.06),pos=(400,1250))  
        self.layout.add_widget (lbl)
        
        
        
        lbl_m=Image(source="label_m.png",size_hint=(.24,.05),pos=( 320,1180))
        self.layout.add_widget(lbl_m)
        lbl_f=Image(source="label_f.png",size_hint=(.24,.05),pos=( 500,1180))
        self.layout.add_widget(lbl_f)        

        
        self.check_f = CheckBox(active = False,group = 'gender',size_hint=(.20,.20),color=(1,1,0,1),pos=(558,1072)) 
        self.check_f.bind(active=self.on_checkbox_active)
        self.check_m = CheckBox(active= False,group = 'gender',size_hint=(.1,.1),pos=(414,1145))
        self.check_m.bind(active=self.on_checkbox_active) 
        self.layout.add_widget(self.check_m)
        self.layout.add_widget(self.check_f)
        
        
        
        lbl_heigh = Image(source="height_lbl.png",size_hint=(.210,.050),pos=(125,1080))
        self.layout.add_widget(lbl_heigh)
        self.input_heigh = TextInput(text="0",pos=(380,1030),size_hint=(.230,.030),halign="center")
        self.layout.add_widget(self.input_heigh)
        self.input_heigh.bind(text=self.on_click_inputbox)
        
        
        self.spinner_h = Spinner(
            text='select\nparameter',
            values=('meter', 'feet',"inch"),
            size_hint=(None, None),
            size=(130, 45),halign="center"
            ,pos=(550,1030)
        )
        self.layout.add_widget(self.spinner_h)
       
       
        lbl_weigh = Image(source='weight_lbl.png',size_hint=(.210,.050),pos=(460,1080))
        self.layout.add_widget(lbl_weigh)           
        self.input_weigh = TextInput(text="0",pos=(30,1030),size_hint=(.230,.030),halign="center")
        self.layout.add_widget(self.input_weigh)
        self.input_weigh.bind(text=self.on_click_inputbox)
        
        self.spinner_w = Spinner(
            text='select\nparameter',halign="center",
            values=('kilograms', 'grams'),
            size_hint=(None, None),
            size=(130, 45),
            pos=(200,1030)
        )
        self.layout.add_widget(self.spinner_w)
        
        self.spinner_h.set_disabled(True)
        self.spinner_w.set_disabled(True)        
        
        def on_spinner_w_select(spinner_w,value):
                #write code to chech valid integer
                             
             
                if self.check_integer() :
                    self.check_integer()
                else:
                    if value==self.spinner_w.values[0]:
                         self.power_w=(self.input_weigh.text)
                    elif value==self.spinner_w.values[1]:
                        self.power_w=(self.input_weigh.text)/1000
                                        
        
        def on_spinner_h_select(spinner_h,value):
               try:
               
                   if  self.check_integer():
                       self.check_integer()
                    
                   else:  
                        if value==self.spinner_h.values[0]:
                            self.power_h=self.input_heigh.text
                        elif value==self.spinner_h.values[1]:
                            self.power_h=float(self.input_heigh.text)*0.3048
                        elif value==self.spinner_h.values[2]:
                            self.power_h=float(self.input_heigh.text)*0.0254
               except:
                    pass
                    
         
        self.spinner_h.bind(text=on_spinner_h_select)      
        self.spinner_w.bind(text=on_spinner_w_select) 
        
        btn0=Button(background_color=(0,1,0,1),size_hint=(.09,.05),pos=(10,1380),background_normal='info.png')
        btn0.bind(on_press=lambda instance: self.show_message_box('About','''Developed by:-Dinkar Godiyal
        
    BMI :- Body Mass Index'''))
        self.layout.add_widget(btn0) 
        
        
        self.layout.add_widget(button)        
        return self.layout
   

    def show_message_box(self, title, message):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Image(source="about.png"))
        popup = Popup(title='About',content=content,size_hint=(.920,.8))
        popup.title_align="center"
       
        popup.open()
            
           
    def on_click_inputbox(self,instance,value) :
              
        if (self.input_heigh.text)=='0'and (self.is_float_convertable(str(self.input_heigh.text))==False)  :
            self.spinner_h.set_disabled(True)
        if (self.input_weigh.text)=='0' and (self.is_float_convertable(str(self.input_weigh.text))==False) :
            self.spinner_w.set_disabled(True)
        if (self.input_weigh.text) != '0' and (self.is_float_convertable(str(self.input_weigh.text))==True) :        
            self.spinner_w.set_disabled(False)
        if (self.input_heigh.text)!='0' and (self.is_float_convertable(str(self.input_heigh.text))==True):
            self.spinner_h.set_disabled(False)  
       
          
                                     
                            
    def check_integer(self):
         if (type(self.input_heigh)!=(float or int) and type(self.input_weigh)!=(float or int ) ):
             lbl=Button(text="please enter interger only",color=(1,0,0,1),size_hint=(.5,.03),background_color=(1,1,1,1),pos=(330,950))
             self.layout.add_widget(lbl)    
             return False
           
               
   
    def is_float_convertable(self,string):
        try:
            float(string)
            return True
        except ValueError:
            return False
   
   
    def on_checkbox_active(self,instance,value):
        self.img=Image()
        if self.check_f.active:
            self.layout.remove_widget(next(child for child in self.layout.children if isinstance(child, Image)))
            self.img=Image(source="female.png" ,pos=(80,1159),size_hint=(.25,.13))
            
        else:
            self.layout.remove_widget(next(child for child in self.layout.children if isinstance(child, Image)))
            self.img=Image(source='male.png',size_hint=(.25,.13),pos=(80,1159))
        self.layout.add_widget(self.img)
            
    def calculate_action(self, value):
        lbl_weigh = Image(source='weight_lbl.png', size_hint=(.210, .050), pos=(460, 1080))
        self.layout.add_widget(lbl_weigh)
        
        if not self.is_float(self.input_heigh.text) or not self.is_float(self.input_weigh.text):
            lbl_error = Button(text='enter integer only', color=(1, 0, 0, 1), size_hint=(.5, .03), background_color=(1, 1, 1, 1), pos=(330, 950))
            self.layout.add_widget(lbl_error)
        elif not self.check_f.active and not self.check_m.active:
            lbl_error = Button(text='Please select gender (male or female)', color=(1, 0, 0, 1), size_hint=(.5, .03), background_color=(1, 1, 1, 1), pos=(330, 950))
            self.layout.add_widget(lbl_error) 
        
        else:
            gender = "male"
            if self.check_f.active:
                gender = "female"
            if self.check_m.active:
                gender = "male"
            self.power_h = float(self.input_heigh.text)
            self.power_w = float(self.input_weigh.text)
            bmi = float((self.power_w / (self.power_h * self.power_h)))
            bmi = round(bmi, 2)
            lbl9 = Button(background_color=(0, 0, 1, 1), font_size=35, size_hint=(.42, .05))
            lbl9.disabled = True
            btn4 = Button()
            if gender == 'male':
                if float(bmi) < 18.5:
                    btn4 = Button(background_color=(1, 1, 1, 1), background_normal='underweight_male.png', size_hint=(.447, .420), pos=(0, 400))
                    lbl9 = Button(text="underweight male", font_size=35, size_hint=(.45, .05), pos=(350, 650))
                elif float(bmi) < 24.9 and float(bmi) > 18.5:
                    btn4 = Button(background_color=(1, 1, 1, 1), background_normal='healthy_male.png', size_hint=(.447, .420), pos=(0, 400))
                    lbl9 = Button(text='healthy male', font_size=35, size_hint=(.45, .05), pos=(350, 650))
                else:
                    btn4 = Button(background_color=(1, 1, 1, 1), background_normal='overweight_male.png', size_hint=(.447, .420), pos=(0, 400))
                    lbl9 = Button(text='overweight male', font_size=35, size_hint=(.45, .05), pos=(350, 650))
            else:
                if float(bmi) < 18.5:
                    btn4 = Button(background_color=(1, 1, 1, 1), background_normal='underweight_female.png', size_hint=(.447, .420), pos=(0, 400))
                    lbl9 = Button(text='underweight female', font_size=35, size_hint=(.45, .05), pos=(350, 650))
                elif float(bmi) > 18.5 and float(bmi) > 24.9:
                    btn4 = Button(background_color=(1, 1, 1, 1), background_normal='healthy_female.png', size_hint=(.447, .420), pos=(0, 400))
                    lbl9 = Button(text='healthy female', font_size=35, size_hint=(.45, .05), pos=(350, 650))
                else:
                    btn4 = Button(background_color=(1, 1, 1, 1), background_normal='overweight_female.png', size_hint=(.447, .420), pos=(0, 400))
                    lbl9 = Button(text='overweight female', font_size=35, size_hint=(.45, .05), pos=(350, 650))
            self.layout.add_widget(lbl9)
            lbl6 = Button(text=str(bmi), background_color=(1, 1, 1, 1), font_size=80, color=(1, 1, 0, 1), size_hint=(.3, .1), pos=(400, 750))
            self.layout.add_widget(btn4)
            self.layout.add_widget(lbl6)
    
    def is_float(self, text):
        try:
            float(text)
            return True
        except ValueError:
            return False
    
            
        

if __name__ == '__main__':
    BMI_Calculator().run( )     