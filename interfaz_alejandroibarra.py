from tkinter import * #importar interfaz tkinter
import time #importar tiempo de computadora
import threading #importar threading para hilos
from threading import Thread #importar Thread para hilos
import random #importar randomizador
import os #importar sistema operativo
import subprocess #importar subprocess para obtener y reproducir audio

flag_thread=True #variable global para inicio de hilos

#funcion para cargar imagenes
def loadpicture(name):
    route = os.path.join('Photos', name)
    photo = PhotoImage(file=route)
    return photo

main_window = Tk() #ventana principal
main_window.title('Interfaz') #titulo de ventana
main_window.minsize(700,700) #tamaño minimo de ventana

#carga de imagenes
fibonacciicon = loadpicture('fibonaccicon.gif')
profileicon = loadpicture('profileicon.gif')
primeicon = loadpicture ('primeicon.gif')
animationicon = loadpicture ('animationicon.gif')
exiticon = loadpicture('exiticon.gif')

backicon = loadpicture('backicon.gif')

profilepic = loadpicture('profilepic.gif')
mapa = loadpicture('mapa.gif')
racket = loadpicture('tennisracket.gif')
playicon = loadpicture('playicon.gif')

stopicon = loadpicture('stopicon.gif')
zero = loadpicture('zero.gif')
one = loadpicture('one.gif')

#funcion para salir del programa
def salir():
    main_window.destroy()

#ventana de perfil del programador
def profilewindow():
    main_window.withdraw() 
    profilewindow = Toplevel()
    profilewindow.title('Interfaz')
    profilewindow.minsize(700,700)

    #canvas de perfil del programador
    canvas1= Canvas(profilewindow, width = 700, height = 700, bg = 'white')
    canvas1.place(x=0,y=0)

    #funcion para reproducir audio, la descripcion del deporte preferido del programador
    def playsound():
        subprocess.call(["afplay", os.path.join('Photos', 'tennis.wav')])

    #funcion para volver atras
    def backprofile():
        profilewindow.destroy()
        main_window.deiconify()

    #nombre del programador
    labelnombre = Label(canvas1, text = 'Nombre: Alejandro Ibarra', font = 'Helvetica 16')
    labelnombre.place(x=25, y=100)

    #carnet del programador
    labelcarnet = Label(canvas1, text = 'Carnet: 2018089951', font = 'Helvetica 16')
    labelcarnet.place(x=25, y=150)

    #genero del programador
    labelgenero = Label(canvas1, text = 'Genero: Masculino', font = 'Helvetica 16')
    labelgenero.place(x=25, y=200)

    #edad del programador
    labeledad = Label(canvas1, text = 'Edad: 17', font = 'Helvetica 16')
    labeledad.place(x=25, y=250)

    #direccion del programador
    labeldireccion = Label(canvas1, text = 'Dirección: 50 metros oeste del Instituto\nTecnológico de Costa Rica', font = 'Helvetica 16', justify = LEFT)
    labeldireccion.place(x=25, y=300)

    #deporte preferido del programador
    labeldeporte = Label(canvas1, text ='Deporte preferido: Tenis', font = 'Helvetica 16')
    labeldeporte.place(x=25, y=450)

    #descripcion de deporte preferido del programador
    sportdescription = Label(canvas1, text = 'El tenis es un deporte que se practica con raquetas y una pelota.\nEl objetivo es impactar la pelota para que pase por encima de\nuna red y que el rival no consiga devolver.', font = 'Helvetica 16',  justify = LEFT)
    sportdescription.place(x=250,y=500)

    #label para indicar que al presionar el boton se reproduce la descripcion
    playinstruction = Label(canvas1, text = 'Reproducir descripción', font = 'Helvetica 16')
    playinstruction.place(x=400, y=600)

    #imagen del programador
    profilepiclabel = Label(canvas1, image = profilepic)
    profilepiclabel.place(x=450, y=25)

    #toma satelital de google maps de donde vive el programador
    fotomapa = Label(canvas1, image = mapa)
    fotomapa.place(x=300,y=225)

    #foto alusiva al deporte preferido del programador
    fototenis = Label(canvas1, image = racket)
    fototenis.place(x=75, y=500)

    #boton para reproducir la descripcion del deporte preferido del programador
    playbutton = Button(canvas1, image = playicon, command = playsound)
    playbutton.place(x=330, y=580)

    #boton para volver atras
    backbutton = Button(profilewindow, image = backicon, command = backprofile) #boton de atras
    backbutton.place (x=20, y=20)

#ventana de verificacion de numero primo
def primewindow():
    main_window.withdraw() 
    primewindow = Toplevel()
    primewindow.title('Interfaz')
    primewindow.minsize(700,700)

    #canvas de verificacion de numero primo
    canvas2 = Canvas(primewindow, width = 700, height = 700, bg = 'white')
    canvas2.place(x=0,y=0)

    #titulo de ventana
    primetitle = Label(canvas2, text='Verificación de números primos', font ='Helvetica 32')
    primetitle.place(x=125,y=150)

    #instruccion de ventana
    primeinstruction = Label(canvas2, text='Inserte número aquí', font = 'Helvetica 32')
    primeinstruction.place(x=200, y=250)

    #funcion para limitar input en entry a numeros de 0 a 9
    def testvalue(instring,i,activetype):
        ind=int(i)
        if activetype == '1': 
            if not instring[ind].isdigit():
                return False
        return True

    #entry de numero primo
    primeentry = Entry(canvas2, width = 30, validate='key') #entry de numero a verfificar
    primeentry['validatecommand'] = (primeentry.register(testvalue),'%P','%i','%d') #validacion de input a numero de 0 a 9
    primeentry.place(x=220,y=330) #posicion de entry

    #muestra de resultado de verificacion de numero primo
    def showprime():
        num = int(primeentry.get())
        result = str(prime(num)) 
        printresult = Label(primewindow, text = result, font = 'Helvetica 32', bg = 'white', width = 20)
        printresult.place(x=160,y=500)
        primeentry.delete(0, END)
        
    #funcion para verificacion de numero primo
    #E: numero
    #S: si el numero es primo o no
    #R: numero entero positivo
    def prime(num):
            return prime_aux(num, num-1)

    def prime_aux(num, divi):
        if num == 1:
            return 'El número es neutro'
        elif num == 2 or num == 3 or num == 5 or num == 7:
            return 'El número es primo'
        elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
            return 'El número no es primo'
        elif divi == 1:
            return 'El número es primo'
        else:
            if num%divi == 0:
                return 'El número no es primo'
            else:
                return prime_aux(num, divi-1)

    #funcion para volver atras
    def backprime():
        primewindow.destroy()
        main_window.deiconify()

    #boton para iniciar la verificacion de numero primo
    prime_calcbutton = Button(canvas2, text = 'Verificar', font = 'Helvetica 26', command = showprime) #boton para calcular (verificar)
    prime_calcbutton.place(x=280, y=400)

    #boton para ir atras
    backbutton = Button(primewindow, image = backicon, command = backprime)
    backbutton.place (x=20, y=20)

#ventana de calculo numero fibonacci
def fibwindow():
    main_window.withdraw()
    fibwindow = Toplevel()
    fibwindow.title('Interfaz')
    fibwindow.minsize(700,700)

    #canvas de calculo numero fibonacci
    canvas3 = Canvas(fibwindow, width = 700, height = 700, bg = 'white')
    canvas3.place(x=0,y=0)

    #titulo de ventana
    fibtitle = Label(canvas3, text='Cálculo de numero de Fibonacci', font ='Helvetica 32')
    fibtitle.place(x=120,y=150)

    #titulo de ventana
    fibinstruction = Label(canvas3, text='Inserte número aquí', font = 'Helvetica 32')
    fibinstruction.place(x=200, y=250)

    #funcion para limitar el input a numeros de 0 a 9
    def testvalue(instring,i,activetype):
        ind=int(i)
        if activetype == '1': 
            if not instring[ind].isdigit():
                return False
        return True

    #entry de calculo de numero de fibonacci
    fibentry = Entry(canvas3, width = 30, validate='key') #entry de numero a verfificar
    fibentry['validatecommand'] = (fibentry.register(testvalue),'%P','%i','%d') #validacion de input a numero de 0 a 9
    fibentry.place(x=220,y=330) #posicion de entry

    #muestra de resultado de calculo de numero de fibonacci, llamadas realizadas y tiempo de ejecucion
    def showfib(): 
        start = time.time() #inicio de timer para ver tiempo de ejecucion
        num = int(fibentry.get())
        result = 'Resultado, total llamadas: '+str(fib(num)) #muestra de resultado y cantidad de llamadas recursivas realizadas
        printresult = Label(fibwindow, text = result, font = 'Helvetica 28', bg = 'white', width = 50)
        printresult.place(x=-50,y=500)
        fibentry.delete(0, END)
        end = time.time() #final de timer para ver tiempo de ejecucion
        #muestra de tiempo de ejecucion de funcion
        printtime = Label(fibwindow, text = 'Tiempo transcurrido: '+str(end-start), font = 'Helvetica 28', width = 50)
        printtime.place(x=-40, y=600)

    #funcion de calculo de numero de fibonacci
    #E: numero
    #S: numero de fibonacci para numero entrada
    #R: numero entero positivo
    def fib(num):
        global callcount #variable para contar llamadas recursivas realizadas
        callcount = 0
        def fib_aux_in(num):
            global callcount
            if num <= 1:
                callcount = callcount + 1
                return num
            else:
                return fib_aux_in(num-1) + fib_aux_in(num - 2)
        return fib_aux_in(num), callcount

    #boton para calcular numero de fibonacci
    fib_calcbutton = Button(canvas3, text = 'Verificar', font = 'Helvetica 26', command = showfib)
    fib_calcbutton.place(x=280, y=400)

    #funcion para volver atras
    def backfib():
        fibwindow.destroy()
        main_window.deiconify()

    #boton para volver atras
    backbutton = Button(fibwindow, image = backicon, command = backfib)
    backbutton.place (x=20, y=20)

#ventana de animacion
def animationwindow():
    main_window.withdraw()
    animationwindow = Toplevel()
    animationwindow.title('Interfaz')
    animationwindow.minsize(700,700)

    #canvas de animacion
    canvas4 = Canvas(animationwindow, width = 700, height = 700, bg = 'black')
    canvas4.place(x=0,y=0)

    #funcion para randomizar imagenes de la animacion
    def binario():
        lista_numero = [zero, one]
        return lista_numero[random.randrange(0,2)]

    #hilo 1
    def thread1():
        #coordenadas en inicio de hilo
        x_thread1=0
        y_thread1=0
        #referencia a la bandera de inicio o detencion de hilo
        while flag_thread:
            try:
                #colocar imagenes en cada iteracion
                thread1= Label(canvas4, image = binario(), bg = 'black')
                thread1.place(x=x_thread1,y=y_thread1)
                if(y_thread1==700):
                    x_thread1=0
                    y_thread1=0
                else:
                    y_thread1+=50
                time.sleep(0.6)
            except Exception as errtxt:
                print ('Error en hilo 1')

    #hilo 2
    def thread2():
        #coordenadas en inicio de hilo
        x_thread2=50
        y_thread2=0
        #referencia a la bandera de inicio o detencion de hilo
        while flag_thread:
            try:
                #colocar imagenes en cada iteracion
                thread2= Label(canvas4, image = binario(), bg = 'black')
                thread2.place(x=x_thread2,y=y_thread2)
                if(y_thread2==700):
                    x_thread2=50
                    y_thread2=0
                else:
                    y_thread2+=50
                time.sleep(0.8)
            except Exception as errtxt:
                print ('Error en hilo 2')

    #hilo 3
    def thread3():
        #coordenadas en inicio de hilo
        x_thread3=100
        y_thread3=0
        #referencia a la bandera de inicio o detencion de hilo
        while flag_thread:
            try:
                #colocar imagenes en cada iteracion
                thread3= Label(canvas4, image = binario(), bg = 'black')
                thread3.place(x=x_thread3,y=y_thread3)
                if(y_thread3==700):
                    x_thread3=100
                    y_thread3=0
                else:
                    y_thread3+=50
                time.sleep(0.6)
            except Exception as errtxt:
                print ('Error en hilo 3')

    #hilo 4
    def thread4():
        #coordenadas en inicio de hilo
        x_thread4=150
        y_thread4=0
        #referencia a la bandera de inicio o detencion de hilo
        while flag_thread:
            try:
                #colocar imagenes en cada iteracion
                thread4= Label(canvas4, image = binario(), bg = 'black')
                thread4.place(x=x_thread4,y=y_thread4)
                if(y_thread4==700):
                    x_thread4=150
                    y_thread4=0
                else:
                    y_thread4+=50
                time.sleep(0.7)
            except Exception as errtxt:
                print ('Error en hilo 4')

    #hilo 5
    def thread5():
        #coordenadas en inicio de hilo
        x_thread5=200
        y_thread5=0
        #referencia a la bandera de inicio o detencion de hilo
        while flag_thread:
            try:
                #colocar imagenes en cada iteracion
                thread5= Label(canvas4, image = binario(), bg = 'black')
                thread5.place(x=x_thread5,y=y_thread5)
                if(y_thread5==700):
                    x_thread5=200
                    y_thread5=0
                else:
                    y_thread5+=50
                time.sleep(0.9)
            except Exception as errtxt:
                print ('Error en hilo 5')

    #hilo 6
    def thread6():
        #coordenadas en inicio de hilo
        x_thread6=250
        y_thread6=0
        #referencia a la bandera de inicio o detencion de hilo
        while flag_thread:
            try:
                #colocar imagenes en cada iteracion
                thread6= Label(canvas4, image = binario(), bg = 'black')
                thread6.place(x=x_thread6,y=y_thread6)
                if(y_thread6==700):
                    x_thread6=250
                    y_thread6=0
                else:
                    y_thread6+=50
                time.sleep(0.7)
            except Exception as errtxt:
                print ('Error en hilo 6')

    #hilo 7
    def thread7():
        #coordenadas en inicio de hilo
        x_thread7=300
        y_thread7=0
        #referencia a la bandera de inicio o detencion de hilo
        while flag_thread:
            try:
                #colocar imagenes en cada iteracion
                thread7= Label(canvas4, image = binario(), bg = 'black')
                thread7.place(x=x_thread7,y=y_thread7)
                if(y_thread7==700):
                    x_thread7=300
                    y_thread7=0
                else:
                    y_thread7+=50
                time.sleep(0.8)
            except Exception as errtxt:
                print ('Error en hilo 7')

    #hilo 8
    def thread8():
        #coordenadas en inicio de hilo
        x_thread8=350
        y_thread8=0
        #referencia a la bandera de inicio o detencion de hilo
        while flag_thread:
            try:
                #colocar imagenes en cada iteracion
                thread8= Label(canvas4, image = binario(), bg = 'black')
                thread8.place(x=x_thread8,y=y_thread8)
                if(y_thread8==700):
                    x_thread8=350
                    y_thread8=0
                else:
                    y_thread8+=50
                time.sleep(0.6)
            except Exception as errtxt:
                print ('Error en hilo 8')

    #hilo 9
    def thread9():
        #coordenadas en inicio de hilo
        x_thread9=400
        y_thread9=0
        #referencia a la bandera de inicio o detencion de hilo
        while flag_thread:
            try:
                #colocar imagenes en cada iteracion
                thread9= Label(canvas4, image = binario(), bg = 'black')
                thread9.place(x=x_thread9,y=y_thread9)
                if(y_thread9==700):
                    x_thread9=400
                    y_thread9=0
                else:
                    y_thread9+=50
                time.sleep(0.7)
            except Exception as errtxt:
                print ('Error en hilo 9')

    #hilo 10
    def thread10():
        #coordenadas en inicio de hilo
        x_thread10=450
        y_thread10=0
        #referencia a la bandera de inicio o detencion de hilo
        while flag_thread:
            try:
                #colocar imagenes en cada iteracion
                thread10= Label(canvas4, image = binario(), bg = 'black')
                thread10.place(x=x_thread10,y=y_thread10)
                if(y_thread10==700):
                    x_thread10=450
                    y_thread10=0
                else:
                    y_thread10+=50
                time.sleep(0.9)
            except Exception as errtxt:
                print ('Error en hilo 10')

    #hilo 11
    def thread11():
        #coordenadas en inicio de hilo
        x_thread11=500
        y_thread11=0
        #referencia a la bandera de inicio o detencion de hilo
        while flag_thread:
            try:
                #colocar imagenes en cada iteracion
                thread11= Label(canvas4, image = binario(), bg = 'black')
                thread11.place(x=x_thread11,y=y_thread11)
                if(y_thread11==700):
                    x_thread11=500
                    y_thread11=0
                else:
                    y_thread11+=50
                time.sleep(0.7)
            except Exception as errtxt:
                print ('Error en hilo 11')

    #hilo 12
    def thread12():
        #coordenadas en inicio de hilo
        x_thread12=550
        y_thread12=0
        #referencia a la bandera de inicio o detencion de hilo
        while flag_thread:
            try:
                #colocar imagenes en cada iteracion
                thread12= Label(canvas4, image = binario(), bg = 'black')
                thread12.place(x=x_thread12,y=y_thread12)
                if(y_thread12==700):
                    x_thread12=550
                    y_thread12=0
                else:
                    y_thread12+=50
                time.sleep(0.6)
            except Exception as errtxt:
                print ('Error en hilo 12')

    #hilo 13
    def thread13():
        #coordenadas en inicio de hilo
        x_thread13=600
        y_thread13=0
        #referencia a la bandera de inicio o detencion de hilo
        while flag_thread:
            try:
                #colocar imagenes en cada iteracion
                thread13= Label(canvas4, image = binario(), bg = 'black')
                thread13.place(x=x_thread13,y=y_thread13)
                if(y_thread13==700):
                    x_thread13=600
                    y_thread13=0
                else:
                    y_thread13+=50
                time.sleep(0.7)
            except Exception as errtxt:
                print ('Error en hilo 13')

    #hilo 14
    def thread14():
        #coordenadas en inicio de hilo
        x_thread14=650
        y_thread14=0
        #referencia a la bandera de inicio o detencion de hilo
        while flag_thread:
            try:
                #colocar imagenes en cada iteracion
                thread14= Label(canvas4, image = binario(), bg = 'black')
                thread14.place(x=x_thread14,y=y_thread14)
                if(y_thread14==700):
                    x_thread14=650
                    y_thread14=0
                else:
                    y_thread14+=50
                time.sleep(0.8)
            except Exception as errtxt:
                print ('Error en hilo 14')

    #funcion para iniciar hilos
    def start_thread():
        global flag_thread #referencia a variable de inicio y detencion de hilos
        flag_thread=True #inicio de hilo
        #creacion de hilos
        a = Thread(target=thread1, args=())
        b = Thread(target=thread2, args=())
        c = Thread(target=thread3, args=())
        d = Thread(target=thread4, args=())
        e = Thread(target=thread5, args=())
        f = Thread(target=thread6, args=())
        g =Thread(target=thread7, args=())
        h = Thread(target=thread8, args=())
        i = Thread(target=thread9, args=())
        j = Thread(target=thread10, args=())
        k = Thread(target=thread11, args=())
        l = Thread(target=thread12, args=())
        m = Thread(target=thread13, args=())
        n = Thread(target=thread14, args=())
        #inicio de hilos
        a.start()
        b.start()
        c.start()
        d.start()
        e.start()
        f.start()
        g.start()
        h.start()
        i.start()
        j.start()
        k.start()
        l.start()
        m.start()
        n.start()
        
    #funcion para detener los hilos
    def kill_thread():
        global flag_thread #referencia a variable de inicio y detencion de hilos
        flag_thread=False #detencion de hilo

    #boton para detener hilos
    botonDetenerHilos = Button(animationwindow, image=stopicon,command=kill_thread)
    botonDetenerHilos.place(x=225,y=20)

    botonIniciarHilo = Button(animationwindow, image=playicon,command=start_thread)
    botonIniciarHilo.place(x=150,y=20)

    #funcion para volver atras
    def backanimation():
        kill_thread()
        animationwindow.destroy()
        main_window.deiconify()
        
    #boton para ir atras
    backbutton = Button(animationwindow, image = backicon, command = backanimation)
    backbutton.place (x=20, y=20) 
    

#titulo de icono de ficha del programador
titleprofile = Label(main_window, text = 'Ficha Programador', font = 'Helvetica 28')
titleprofile.place(x=80,y=300)

#titulo de icono de calculo de numero primo
titleprime = Label(main_window, text = 'Número Primo', font = 'Helvetica 28')
titleprime.place(x=415, y=300)

#titulo de icono de calculo de numero de fibonacci
titlefib = Label(main_window, text = 'Fibonacci', font = 'Helvetica 28')
titlefib.place(x=145,y=600)

#titulo de icono de animacion
titleanimation = Label(main_window, text = 'Animación', font = 'Helvetica 28')
titleanimation.place(x=440, y=600)

#boton para ir a la ventana de ficha del programador
buttonprofile = Button(main_window, image = profileicon, command = profilewindow)
buttonprofile.place (x=100, y=75)

#boton para ir a la ventana de calculo de numero primo
buttonprime = Button(main_window, image=primeicon, command = primewindow)
buttonprime.place (x=400, y=75)

#boton para ir a la ventana de calculo de numero fibonacci
buttonfib = Button(main_window, image = fibonacciicon, command = fibwindow)
buttonfib.place (x=100, y=375)

#boton para ir a ventana de animacion
buttonanimation = Button(main_window, image = animationicon, command = animationwindow)
buttonanimation.place (x=400, y=375)

#boton para salir del programa
buttonexit = Button(main_window, image = exiticon, command = salir)
buttonexit.place (x=20, y=20)
            
main_window.mainloop()
