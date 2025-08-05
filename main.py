from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    time.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        time.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        time.config(text="Break", fg=PINK)
    else:
        count_down(work_seconds)
        time.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer

    min_time = math.floor(count/60)
    sec_time = int(count % 60)
    if sec_time < 10:
        sec_time = f"0{sec_time}"
    canvas.itemconfig(timer_text, text=f"{min_time}:{sec_time}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "*"
            check_mark.config(text=f"{marks} Marks")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

start = Button(text="Start", width=5, command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", width=5, command=reset_timer)
reset.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_image)
timer_text = canvas.create_text(102, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

time = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
time.grid(column=1, row=0)
window.mainloop()