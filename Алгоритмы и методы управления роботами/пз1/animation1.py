import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

t = np.linspace(0, 20, 100)

# Позиционные массивы
x = np.cos( t)
y = np.sin(t)
z = np.linspace(0, 100, 100)

# Задаем набор данных для анимации
dataSet = np.array([x, y, z])  # Комбинируем наши позиционные координаты
numDataPoints = len(t)

def animate_func(num):
   ax.clear()  # Очищаем фигуру для обновления линии, точки,
   ax.plot3D(dataSet[0, :num+1], dataSet[1, :num+1],
             dataSet[2, :num+1], c='blue')    # Обновляем локацию точки
   ax.scatter(dataSet[0, num], dataSet[1, num], dataSet[2, num],
              c='blue', marker='o')    # Добавляем постоянную начальную точку
   ax.plot3D(dataSet[0, 0], dataSet[1, 0], dataSet[2, 0],
              c='black', marker='o')    # Задаем пределы для осей
   ax.set_xlim3d([-1, 1])
   ax.set_ylim3d([-1, 1])
   ax.set_zlim3d([0, 100])

   # Добавляем метки
   ax.set_title('Trajectory \nTime = ' + str(np.round(t[num], decimals=2)) + ' sec')
   ax.set_xlabel('x')
   ax.set_ylabel('y')
   ax.set_zlabel('z')

fig = plt.figure()
ax = plt.axes(projection='3d')
line_ani = animation.FuncAnimation(fig, animate_func, interval=100,
                                  frames=numDataPoints)
plt.show()

f = r"1.gif"
writergif = animation.PillowWriter(fps=numDataPoints/6)
line_ani.save(f, writer=writergif)

'''

'''