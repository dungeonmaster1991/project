from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Досвидание")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Закрыть окно", command=self.quit)
        quitButton.place(x=10, y=50)

        startButton = Button(self, text="Запустить бота", command=self.quit)
        startButton.place(x=10, y=80)

def main():
    root = Tk()
    root.geometry("350x250+100+100")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
