#Задание повышенной сложности 1
import matplotlib.pyplot as plt
import numpy as np

# Функция для рисования головы кота
def draw_head(ax):
    x = [-1, -1, 1, 1]
    y = [1, -1, -1, 1]
    ax.fill(x, y, 'k')

# Функция для рисования ушей кота
def draw_ears(ax):
    ear_left_x = [-1.5, -1.75, -1.5]
    ear_left_y = [1, 1.5, 1]
    ear_right_x = [1.5, 1.75, 1.5]
    ear_right_y = [1, 1.5, 1]
    ax.fill(ear_left_x, ear_left_y, 'k')
    ax.fill(ear_right_x, ear_right_y, 'k')

# Функция для рисования глаз кота
def draw_eyes(ax):
    eye_left_x = [-0.5, -0.5, -0.35, -0.35]
    eye_left_y = [0.5, 0.65, 0.65, 0.5]
    eye_right_x = [0.5, 0.5, 0.35, 0.35]
    eye_right_y = [0.5, 0.65, 0.65, 0.5]
    ax.fill(eye_left_x, eye_left_y, 'w')
    ax.fill(eye_right_x, eye_right_y, 'w')

# Функция для рисования носа кота
def draw_nose(ax):
    nose_x = [0, 0, 0.15, 0.15]
    nose_y = [0.45, 0.55, 0.55, 0.45]
    ax.fill(nose_x, nose_y, 'pink')

# Функция для рисования рта кота
def draw_mouth(ax):
    mouth_x = [0, 0.1, -0.1, -0.1]
    mouth_y = [0.1, 0.1, 0.1, 0.2]
    ax.plot(mouth_x, mouth_y, 'r')

# Функция для рисования туловища кота
def draw_body(ax):
    body_x = [-1, -1, 1, 1]
    body_y = [-1, -2, -2, -1]
    ax.fill(body_x, body_y, 'k')

# Функция для рисования лап кота
def draw_legs(ax):
    leg_left_x = [-0.5, -0.5, -0.75, -0.75]
    leg_left_y = [-1, -1.5, -1.5, -1]
    leg_right_x = [0.5, 0.5, 0.75, 0.75]
    leg_right_y = [-1, -1.5, -1.5, -1]
    ax.fill(leg_left_x, leg_left_y, 'k')
    ax.fill(leg_right_x, leg_right_y, 'k')

# Функция для рисования хвоста кота
def draw_tail(ax):
    tail_x = [1, 1.5, 1.5, 1]
    tail_y = [-2, -2.5, -3, -2.5]
    ax.fill(tail_x, tail_y, 'k')

# Основная функция для рисования кота
def draw_cat():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    draw_head(ax)
    draw_ears(ax)
    draw_eyes(ax)
    draw_nose(ax)
    draw_mouth(ax)
    draw_body(ax)
    draw_legs(ax)
    draw_tail(ax)

    plt.show()

# Вызываем основную функцию
draw_cat()

