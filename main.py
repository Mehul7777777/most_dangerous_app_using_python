from tkinter import *

window = Tk()
window.minsize(width=800, height=600)
window.config(bg="#fb9300")

count = 5
rounds = 0
spaces = 0


def FirstPage():
    def SecondPage():
        label_1.destroy()
        label_2.destroy()
        button_1.destroy()

        text_area = Text(window, width=60, height=20,  bg="#f5e6ca")
        text_area.place(x=155, y=140)
        button_2 = Button(window, text="Start Again", width=20, height=2, bg="#00ead3", command=SecondPage)
        button_2.place(x=320, y=480)

        def timer():
            global count
            global spaces
            canvas.itemconfig(timer_text, text=f"{count} seconds")
            count -= 1
            if count == 0:
                count = 5
                if spaces == 0:
                    text_area.delete("1.0", END)
                    count = 5
                text_area.after(1000, timer)
                spaces = 0
            else:
                text_area.after(1000, timer)

        button_3 = Button(window, text="Start", width=20, height=2, bg="#00ead3", command=timer)
        button_3.place(x=320, y=90)

        canvas = Canvas(width=700, height=50, bg="#fb9300", highlightthickness=0)
        timer_text = canvas.create_text(350, 30, text="00:00", font=("Didot", 25, "bold"))
        canvas.place(x=50, y=20)

    def activity(event=None):
        global spaces
        spaces += 1

    label_1 = Label(window, text="The Most Dangerous Writing App", font=("Helvetica", 25), bg="#fb9300")
    label_1.place(x=160, y=100)
    label_2 = Label(window, text="Don’t stop writing, or all progress will be lost.", font=("Helvetica", 15),
                  bg="#fb9300")
    label_2.place(x=200, y=150)
    button_1 = Button(window, text="Start Writing", width=20, height=2, bg="#00ead3", command=SecondPage)
    button_1.place(x=320, y=250)
    window.bind("<space>", activity)


FirstPage()

window.mainloop()
