import subprocess
import platform

from tkinter import *


def retrieve_input():
    input = self.myText_Box.get("1.0",END)


def dosAttack():
  value = int(inputType.get())
  str_value = str(value)
  # for windows
  subprocess.Popen(['start', 'cmd', '/k', 'python dos_temp.py', str_value], shell=True)


  str_value = "your_value"
  if platform.system() == "Windows":
      command = ['cmd', '/k', 'python', 'dos_temp.py', str_value]
  elif platform.system() == "Linux":
      command = ['gnome-terminal', '--', 'python', 'dos_temp.py', str_value]
  else:
      raise NotImplementedError("Unsupported operating system")

  subprocess.Popen(command)




if __name__ == "__main__":
    #gui
    mainWin = Tk()

    mainWin.iconbitmap("icon.ico")

    mainWin.geometry("400x450")
    mainWin.title("dos")

    
    space_label = Label(mainWin, text = "\n")
    space_label2 = Label(mainWin, text = "\n")
    

    inputType = StringVar() #�옄猷뚰삎 吏��젙
      
    

    
    btnDos = Button (mainWin, command = dosAttack, text ="Attack")
    
    
    label1 = Label(mainWin, text = "Please input the ip address for attac\n")
    trans_textbox = Text(mainWin, width=15, height=1)
    

    label1.pack()
    trans_textbox.pack()
    btnDos.pack()
    
    
    
 
    mainWin.mainloop()

