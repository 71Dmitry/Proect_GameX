import tkinter as tk
import time

window = tk.Tk()
window.geometry('600x600')
window.resizable(False, False)
window.title('хайп, а не крестики')

game_end = False
play_button = goaway_button = None


def start_game():
    draw_board()
    start_button.pack_forget()
    quit_button.pack_forget()
    title_label.pack_forget()


title_label = tk.Label(window, text="Крестики-Нолики", font=("SANS", 30))
title_label.pack(pady=65,)


start_button = tk.Button(window, text="Начать игру", command=start_game, width=30, height=3, font=("SANS", 16),
                         bg='green')
start_button.pack(pady=60)

quit_button = tk.Button(window, text="Выйти", command=window.quit, width=30, height=3, font=("SANS", 16), bg='red')
quit_button.pack(pady=60)

c = tk.Canvas(window, width=600, height=600, highlightthickness=0)
c.pack()

currect_player = 'X'
step = 1
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
docuvoditel = []


def quadro(n):
    global currect_player, step, play_button, goaway_button, game_end
    if not check_win() and board[n] not in ['X', 'O']:
        board[n] = currect_player
        if currect_player == 'X':
            currect_player = 'O'
        else:
            currect_player = 'X'
        step += 1
        update_board()

        pobeditelb = check_win()
        if pobeditelb:
            y1 = pobeditelb[0] // 3 * 200 + 100
            y2 = pobeditelb[2] // 3 * 200 + 100
            c.create_line(pobeditelb[0] % 3 * 200 + 100, y1, pobeditelb[2] % 3 * 200 + 100, y2, width=7)
            window.update()

            time.sleep(2)

            c.delete("all")
            c.create_text(300, 50, text="победили " + str(board[pobeditelb[0]]) + " !!!", anchor=tk.CENTER,
                          font=('SANS', 20))

            play_button = tk.Button(window, text="Начать заново", command=start_game, width=30, height=4,
                                    font=("SANS", 16), bg='yellow')
            play_button.place(x=100, y=200)

            goaway_button = tk.Button(window, text="Выйти", command=window.quit, width=30, height=4, font=("SANS", 16),
                                      bg='red')
            goaway_button.place(x=100, y=400)
            game_end = True

        window.update()


def draw_board():
    q_1 = c.create_rectangle(0, 0, 200, 200, fill='white', outline='')
    q_2 = c.create_rectangle(200, 0, 400, 200, fill='white', outline='')
    q_3 = c.create_rectangle(400, 0, 600, 200, fill='white', outline='')
    q_4 = c.create_rectangle(0, 200, 200, 400, fill='white', outline='')
    q_5 = c.create_rectangle(200, 200, 400, 400, fill='white', outline='')
    q_6 = c.create_rectangle(400, 200, 600, 400, fill='white', outline='')
    q_7 = c.create_rectangle(0, 400, 200, 600, fill='white', outline='')
    q_8 = c.create_rectangle(200, 400, 400, 600, fill='white', outline='')
    q_9 = c.create_rectangle(400, 400, 600, 600, fill='white', outline='')

    c.tag_bind(q_1, "<Button-1>", lambda event: quadro(0))  #создаём функцию без параметров  котороя вызовет функцию с параметрами
    c.tag_bind(q_2, "<Button-1>", lambda event: quadro(1))
    c.tag_bind(q_3, "<Button-1>", lambda event: quadro(2))
    c.tag_bind(q_4, "<Button-1>", lambda event: quadro(3))
    c.tag_bind(q_5, "<Button-1>", lambda event: quadro(4))
    c.tag_bind(q_6, "<Button-1>", lambda event: quadro(5))
    c.tag_bind(q_7, "<Button-1>", lambda event: quadro(6))
    c.tag_bind(q_8, "<Button-1>", lambda event: quadro(7))
    c.tag_bind(q_9, "<Button-1>", lambda event: quadro(8))

    c.create_line(200, 0, 200, 600, width=5)
    c.create_line(400, 0, 400, 600, width=5)
    c.create_line(0, 200, 600, 200, width=5)
    c.create_line(0, 400, 600, 400, width=5)
    window.update()


def update_board():
    global docuvoditel
    for i in docuvoditel:
        c.delete(i)
    docuvoditel = []
    for y in range(3):
        for x in range(3):
            if board[y * 3 + x] == 'X':
                el1 = c.create_line(x * 200 + 10, y * 200 + 10, (x + 1) * 200 - 10, (y + 1) * 200 - 10, width=5,
                                    fill='blue')
                el2 = c.create_line(x * 200 + 10, (y + 1) * 200 - 10, (x + 1) * 200 - 10, y * 200 + 10, width=5,
                                    fill='blue')
                docuvoditel.append(el1)
                docuvoditel.append(el2)
            elif board[y * 3 + x] == 'O':
                el1 = c.create_oval(x * 200 + 10, y * 200 + 10, (x + 1) * 200 - 10, (y + 1) * 200 - 10, width=5,
                                    fill='white', outline='red')
                docuvoditel.append(el1)
    window.update()


def check_win():
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )

    for pos in win_combination:
        if board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]:
            return pos

    return False


def start_game():
    global play_button, goaway_button, currect_player, step, board, docuvoditel
    currect_player = 'X'
    step = 1
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    docuvoditel = []
    c.delete("all")
    if game_end:
        play_button.destroy()
        goaway_button.destroy()
    draw_board()


start_game()

window.mainloop()