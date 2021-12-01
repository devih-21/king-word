from tkinter import *
from tkinter import messagebox
import time
import random

PROVINCES_WORD = ["AGINANG", "BIEACUL", "TNHAHHAO", "NBNIHHIN", "LAGNNOS",
                  "NOHIA", "NDIAMHN", "CABANC", "NHAMA", "NQAUNGHIN"]

PROVINCES_ANSWER = ["AN GIANG", "BAC LIEU", "THANH HOA", "NINH BINH", "LANG SON",
                    "HA NOI", "NAM DINH", "BAC CAN", "HA NAM", "QUANG NINH"]

var = 0
ran_num_array = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
ran_num_array.append(10)
ran_num = ran_num_array[var]
points = 0


def main():
    def back():
        global var, ran_num_array
        var = 0
        ran_num_array = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
        my_window.destroy()
        import index
        index.start_main_page()

    def change():
        global ran_num
        global var,  ran_num_array
        var += 1
        if var == 10 and points >= 30:
            var = 0
            ran_num_array = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
            my_window.destroy()
            messagebox.showinfo('You win!', "Bạn là nhất!!!")
            import index
            index.start_main_page()
        elif var == 10 and points < 30:
            var = 0
            ran_num_array = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
            my_window.destroy()
            messagebox.showinfo('You loss!', "Bạn như lốp xe vậy, hơi non!!!")
            import index
            index.start_main_page()
        ran_num = ran_num_array[var]
        word.configure(text=PROVINCES_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def cheak(event=None):
        global points, ran_num, var, ran_num_array
        user_word = get_input.get().upper().strip()
        if user_word == PROVINCES_ANSWER[ran_num]:
            points += 5
            score.configure(text="Point: " + str(points))
            messagebox.showinfo('Good', "Được của ló, tiếp thôi bro!")
            var += 1
            if var == 10 and points >= 30:
                var = 0
                ran_num_array = random.sample(
                    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
                my_window.destroy()
                messagebox.showinfo('You win!', "Bạn là nhất!!!")
                import index
                index.start_main_page()
            elif var == 10 and points < 30:
                var = 0
                ran_num_array = random.sample(
                    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
                my_window.destroy()
                messagebox.showinfo(
                    'You loss!', "Bạn như lốp xe vậy, hơi non!!!")
                import index
                index.start_main_page()
            ran_num = ran_num_array[var]
            word.configure(text=PROVINCES_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Error", "Xai dồi!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Điểm: " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=PROVINCES_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Kiếm 5 điểm rồi quay lại nha :v')

    my_window = Tk()
    my_window.geometry("450x600+500+150")
    my_window.resizable(0, 0)
    my_window.title("Vua Tiếng Việt")
    my_window.configure(background="#e6fff5")
    img1 = PhotoImage(file="back.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#e6fff5',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(
        text="Point: 0",
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium 14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=PROVINCES_WORD[ran_num],
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium 50 bold"
    )
    word.pack()

    get_input = Entry(
        font="Titillium 26",
        borderwidth=10,
        justify='center',
    )
    get_input.bind('<Return>', cheak)
    get_input.focus_set()
    get_input.pack()

    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 18),
        fg="#000000",
        bg="#99ffd6",
        command=cheak,
    )
    submit.pack(pady=(10, 20))

    change = Button(
        text="Chane Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 18),
        command=change,
    )
    change.pack()

    ans = Button(
        text="Answer",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 18),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#e6fff5",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()
