import turtle
import random
import time

retraso = 0.1

marcador = 0
mejor_marca = 0

#pantalla
screen = turtle.Screen()
#tamaño de la pantalla
screen.setup(700,700)
#titulo de la pestaña
screen.title("Tortuninja")

#color de fondo
screen.bgcolor("black")

#nombramos especificaciones del jugador
jugador = turtle.Turtle()
jugador.speed(700)
jugador.shape("square")
jugador.color("green", "green")
jugador.penup()
jugador.goto(0,0)
jugador.direction = "stop"

cuerpo = []

#marcador
texto = turtle.Turtle()
texto.speed(10)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 300)
texto.write("Marcador: 0 \t Marcador mas alto: 0", align = "center", font=("Arial", 24))

#nombramos la comida
comida = turtle.Turtle()
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)
comida.speed(0)


def arriba():
    jugador.direction ="up"
    
def abajo():
    jugador.direction ="down"

def derecha():
    jugador.direction ="right"

def izquierda():
    jugador.direction ="left"


def movimiento():
    #para arriba
    if (jugador.direction == 'up'):
        y = jugador.ycor()
        jugador.sety(y + 20)
    #para abajo
    if (jugador.direction == 'down'):
        y = jugador.ycor()
        jugador.sety(y - 20)
    #para la derecha
    if (jugador.direction == 'right'):
        x = jugador.xcor()
        jugador.setx(x + 20)
    #para la izquierda
    if (jugador.direction == 'left'):
        x = jugador.xcor()
        jugador.setx(x - 20) 

#funciones del teclado
screen.listen()
screen.onkeypress(arriba, "Up")
screen.onkeypress(abajo, "Down")
screen.onkeypress(derecha, "Right")
screen.onkeypress(izquierda, "Left")


while True:
    screen.update()
    
    
    if jugador.xcor() > 350 or jugador.xcor() < -350 or jugador.ycor() > 350 or jugador.ycor() < -350:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        jugador.home()
        jugador.direction = "stop"
        cuerpo.clear()
        
        marcador = 0
        
        texto.clear()
        texto.write("Marcador: 0 \t Marcador mas alto: 0", align = "center", font=("Arial", 24))
        
        
    #movimientos aleatorios de la comida
    if jugador.distance(comida) < 20:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        comida.goto(x,y)
        
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("green")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)
        
        #suma de puntos
        marcador += 10
        if marcador > mejor_marca :
            mejor_marca  = marcador      
            texto.clear()
            texto.write("Marcador: {}\t Mejor marcador:{}".format(marcador, mejor_marca ),align="center", font=("arial",24))
    
    total = len(cuerpo)
    for i in range(total -1,0,-1):
        x =  cuerpo [i-1].xcor()
        y =  cuerpo [i-1].ycor()
        cuerpo[i].goto(x,y)
    
    if total > 0:
        x = jugador.xcor()
        y = jugador.ycor()
        cuerpo[0].goto(x,y)
        
    movimiento()
    time.sleep(retraso)
    
    for i in cuerpo:
        if i.distance(jugador) <20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            jugador.home()
            jugador.clear()
            jugador.direction = "stop"

#mantiene la pantalla abierta
turtle.done()