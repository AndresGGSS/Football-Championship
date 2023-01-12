import webbrowser
# FUNCIONES AUXILIARES
#ENTRADAS: un string y una lista
#SALIDAS: valor booleano
def validacion(codigo, equipos):
    x = 0
    if equipos:
        for equipo in equipos:
            if x == True:
                break
            for equipo1 in equipo:
                if codigo == equipo1:
                    x = True
                    break
                else:
                    x = False
    else:
        x = False
    return x
#ENTRADAS: un string y una lista 
#SALIDAS: alor booleano
def validar_codigos(codigo, equipos):
    a = True
    for equipo in equipos:
        if a == False:
            break
        for code in equipo:
            if a == False:
                break
            if code == codigo:
                x = equipo[1]
                a = False
    return x
#ENTRADAS: una tupla
#SALIDAS: una lista
def descomponer_tupla(equipos):
    equipos1 = []
    for equipo in equipos:
        equipos1 = equipos1 + [list(equipo)]
    return equipos1
#ENTRADAS: una lista
#SALIDAS: una tupla
def descomponer_lista(equipos):
    equipos1 = []
    for equipo in equipos:
        equipos1.append(tuple(equipo))
    equipos = equipos1
    return equipos
#ENTRADAS: una lista de listas
#SALIDAS: una tupla con tuplas
def convertir_a_tupla(equipos):
    lista_final = []
    calendario = []
    for equipo in equipos:
        numeros = len(equipo)
        for codigos in equipo:
            codigos = tuple(codigos)
            calendario.append(codigos)
            if len(calendario) == numeros:
                lista_final.append(calendario)
                calendario = []
    return lista_final 
#ENTRADAS: una lista 
#SALIDAS: una lista 
def agrupar_codigos(equipos):
    calendario_de_codigo = []
    for equipo in equipos:
        equipo = equipo[0]
        calendario_de_codigo.append(equipo)
    return calendario_de_codigo
#ENTRADAS: Dos listas 
#SALIDAS: una lista 
def union(lst1, lst2):
    final_list = lst1 + lst2
    return final_list
#ENTRADAS: dos strings 
#SALIDAS: valor booleano
def validacion_de_codigos(codigos,calendario_juegos):
    for codigo in calendario_juegos:
        for equipos in codigo:
            if codigos == equipos:
                return True
    return False
#ENTRADAS: dos listas
#SALIDAS: un indice
def validacion_de_indice(codigos,calendario_juegos):
    for codigo in calendario_juegos:
        for equipos in codigo:
            if codigos == equipos:
                return(calendario_juegos.index(codigo))
#ENTRADAS: dos listas
#SALIDAS: un indice          
def validacion_sub_indice(codigos,calendario_juegos):
    for codigo in calendario_juegos:
        for equipos in codigo:
            if codigos == equipos:
                return(codigo.index(codigos))
#ENTRADAS: una lista vacia
#SALIDAS: una lista de listas 
def crear_sub_listas(resultados,calendario_juegos):
    contador_principal = len(calendario_juegos)
    contador = 0
    for codigos in calendario_juegos:
        codigos = len(codigos)
        break
    while contador_principal > contador:
        resultados.append([])
        contador2 = 0
        while codigos > contador2:
            resultados[contador].append([])
            contador2 = contador2 + 1
        contador = contador + 1
    return resultados
#ENTRADAS: una tupla
#SALIDAS: una lista
def convertir_lista(equipos):
    resultado = []
    for equipo in equipos:
        resultados1 = []
        numero = len(equipo)
        for codigos in equipo:
            codigos = list(codigos)
            resultados1.append(codigos)
            if len(resultados1) == numero:
                resultado.append(resultados1)
    return resultado
#ENTRADAS: listas e indices
#SALIDAS: dos listas
def modificacion_resultados(resultados,goleadores,codigos,validacion_indice,validacion_subindice):
        equipo_casa = []
        equipo1 = []
        equipo_visitante = []
        equipo2 = []
        valor = 0
        valor1 = 90
        unir_jugadores = []
        goles = []
        contador = 0
        while True:
            try:
                print("-------------------------------------")
                goles_casa = int(input("Goles del equipo casa "))
                if goles_casa >= 1:
                    break
                elif goles_casa == 0:
                    equipo1.insert(0,0)
                    equipo1.insert(1,0)
                    equipo1.insert(2,0)
                    equipo_casa.append(equipo1)
                    break
            except:
                print("-------------------------------------")
                print("ERROR: LOS GOLES DEBEN SER UN ENTERO")
                print("-------------------------------------")
                input("PRESIONE < ENTER > PARA CONTINUAR ")
        while contador < goles_casa:
            equipo1 = []
            if goles_casa >= 2:
                goleador = input("Jugadores que anotaron ")
                if len(goleador) >= 2 and len(goleador) <= 40 and goleador.isspace() == False:
                    while True:
                        try:
                            minuto = int(input("Minuto "))
                            if isinstance(minuto,int) and abs(minuto) >= 0 and abs(minuto) <= 120:
                                if minuto < 0:
                                    if minuto < -1 and minuto > -30:
                                        equipo1.append(goleador)
                                        equipo1.append(valor1)
                                        equipo1.append(minuto)
                                        equipo_casa.append(equipo1)
                                        contador = contador + 1
                                        break
                                    elif abs(minuto) > 90:
                                        minuto = minuto + 90
                                        equipo1.append(goleador)
                                        equipo1.append(valor1)
                                        equipo1.append(minuto)
                                        equipo_casa.append(equipo1)
                                        contador = contador + 1
                                        break
                                    else:
                                        print("-------------------------------------")
                                        print("ERROR: EL TIEMPO EXTRA VA DE 91 A 120")
                                        print("-------------------------------------")
                                        input("PRESIONE < ENTER > PARA CONTINUAR ")
                                else:
                                    equipo1.append(goleador)
                                    equipo1.append(minuto)
                                    equipo1.append(valor)
                                    equipo_casa.append(equipo1)
                                    contador = contador + 1
                                    break
                            else:
                                print("-------------------------------------")
                                print("ERROR: EL NUMERO TIENE QUE SER MAYOR QUE 1 Y MENOR QUE 120")
                                print("-------------------------------------")
                                input("PRESIONE < ENTER > PARA CONTINUAR ")
                        except:
                            print("-------------------------------------")
                            print("ERROR: TIENE QUE SER UN NUMERO ENTERO")
                            print("-------------------------------------")
                            input("PRESIONE < ENTER > PARA CONTINUAR ")
                else:
                    print("-------------------------------------")
                    print("ERROR: LOS NOMBRES TIENEN QUE TENER ENTRE 2 Y 40 CARÁCTERES")
                    print("-------------------------------------")
                    input("PRESIONE < ENTER > PARA CONTINUAR ")
            elif goles_casa == 1:
                goleador = input("Jugador que anotó ")
                if len(goleador) >= 2 and len(goleador) <= 40 and goleador.isspace() == False:
                    while True:
                        try:
                            minuto = int(input("Minuto "))
                            if isinstance(minuto,int) and abs(minuto) >= 0 and abs(minuto) <= 120:
                                if minuto < 0:
                                    if minuto < -1 and minuto > -30:
                                        equipo1.append(goleador)
                                        equipo1.append(valor1)
                                        equipo1.append(minuto)
                                        equipo_casa.append(equipo1)
                                        contador = contador + 1
                                        break
                                    elif abs(minuto) > 90:
                                        minuto = minuto + 90
                                        equipo1.append(goleador)
                                        equipo1.append(valor1)
                                        equipo1.append(minuto)
                                        equipo_casa.append(equipo1)
                                        contador = contador + 1
                                        break
                                    else:
                                        print("-------------------------------------")
                                        print("ERROR: EL TIEMPO EXTRA VA DE 91 A 120")
                                        print("-------------------------------------")
                                        input("PRESIONE < ENTER > PARA CONTINUAR ")
                                else:
                                    equipo1.append(goleador)
                                    equipo1.append(minuto)
                                    equipo1.append(valor)
                                    equipo_casa.append(equipo1)
                                    contador = contador + 1
                                    break
                            else:
                                print("-------------------------------------")
                                print("ERROR: EL NUMERO TIENE QUE SER MAYOR QUE 1 Y MENOR QUE 120")
                                print("-------------------------------------")
                                input("PRESIONE < ENTER > PARA CONTINUAR ")
                        except:
                            print("-------------------------------------")
                            print("ERROR: TIENE QUE SER UN NUMERO ENTERO")
                            print("-------------------------------------")
                            input("PRESIONE < ENTER > PARA CONTINUAR ")
                else:
                    print("-------------------------------------")
                    print("ERROR: LOS NOMBRES TIENEN QUE TENER ENTRE 2 Y 40 CARÁCTERES")
                    print("-------------------------------------")
                    input("PRESIONE < ENTER > PARA CONTINUAR ")
        while True:
            try:
                print("-------------------------------------")
                goles_visitante = int(input("Goles del equipo Visitante "))
                if goles_visitante >= 1:
                    break
                elif goles_visitante == 0:
                    equipo2.insert(0,0)
                    equipo2.insert(1,0)
                    equipo2.insert(2,0)
                    equipo_visitante.append(equipo2)
                    break
            except:
                print("-------------------------------------")
                print("ERROR: LOS GOLES DEBEN SER UN ENTERO")
                print("-------------------------------------")
                input("PRESIONE < ENTER > PARA CONTINUAR ")
        contador = 0
        while contador < goles_visitante:
            equipo2 = []
            if goles_visitante >= 2:
                goleador = input("Jugadores que anotaron ")
                if len(goleador) >= 2 and len(goleador) <= 40 and goleador.isspace() == False:
                    while True:
                        try:
                            minuto = int(input("Minuto "))
                            if isinstance(minuto,int) and abs(minuto) >= 0 and abs(minuto) <= 120:
                                if minuto < 0:
                                    if minuto < -1 and minuto > -30:
                                        equipo2.append(goleador)
                                        equipo2.append(valor1)
                                        equipo2.append(minuto)
                                        equipo_visitante.append(equipo2)
                                        contador = contador + 1
                                        break
                                    elif abs(minuto) > 90:
                                        minuto = minuto + 90
                                        equipo2.append(goleador)
                                        equipo2.append(valor1)
                                        equipo2.append(minuto)
                                        equipo_visitante.append(equipo2)
                                        contador = contador + 1
                                        break
                                    else:
                                        print("-------------------------------------")
                                        print("ERROR: EL TIEMPO EXTRA VA DE 91 A 120")
                                        print("-------------------------------------")
                                        input("PRESIONE < ENTER > PARA CONTINUAR ")
                                else:
                                    equipo2.append(goleador)
                                    equipo2.append(minuto)
                                    equipo2.append(valor)
                                    equipo_visitante.append(equipo2)
                                    contador = contador + 1
                                    break
                            else:
                                print("-------------------------------------")
                                print("ERROR: EL NUMERO TIENE QUE SER MAYOR QUE 1 Y MENOR QUE 120")
                                print("-------------------------------------")
                                input("PRESIONE < ENTER > PARA CONTINUAR ")
                        except:
                            print("-------------------------------------")
                            print("ERROR: TIENE QUE SER UN NUMERO ENTERO")
                            print("-------------------------------------")
                            input("PRESIONE < ENTER > PARA CONTINUAR ")
                else:
                    print("-------------------------------------")
                    print("ERROR: LOS NOMBRES TIENEN QUE TENER ENTRE 2 Y 40 CARÁCTERES")
                    print("-------------------------------------")
                    input("PRESIONE < ENTER > PARA CONTINUAR ")
            elif goles_visitante == 1:
                goleador = input("Jugador que anotó ")
                if len(goleador) >= 2 and len(goleador) <= 40 and goleador.isspace() == False:
                    while True:
                        try:
                            minuto = int(input("Minuto "))
                            if isinstance(minuto,int) and abs(minuto) >= 0 and abs(minuto) <= 120:
                                if minuto < 0:
                                    if minuto < -1 and minuto > -30:
                                        equipo2.append(goleador)
                                        equipo2.append(valor1)
                                        equipo2.append(minuto)
                                        equipo_visitante.append(equipo2)
                                        contador = contador + 1
                                        break
                                    elif abs(minuto) > 90:
                                        minuto = minuto + 90
                                        equipo2.append(goleador)
                                        equipo2.append(valor1)
                                        equipo2.append(minuto)
                                        equipo_visitante.append(equipo2)
                                        contador = contador + 1
                                        break
                                    else:
                                        print("-------------------------------------")
                                        print("ERROR: EL TIEMPO EXTRA VA DE 91 A 120")
                                        print("-------------------------------------")
                                        input("PRESIONE < ENTER > PARA CONTINUAR ")
                                else:
                                    equipo2.append(goleador)
                                    equipo2.append(minuto)
                                    equipo2.append(valor)
                                    equipo_visitante.append(equipo2)
                                    contador = contador + 1
                                    break
                            else:
                                print("-------------------------------------")
                                print("ERROR: EL NUMERO TIENE QUE SER MAYOR QUE 1 Y MENOR QUE 120")
                                print("-------------------------------------")
                                input("PRESIONE < ENTER > PARA CONTINUAR ")
                        except:
                            print("-------------------------------------")
                            print("ERROR: TIENE QUE SER UN NUMERO ENTERO")
                            print("-------------------------------------")
                            input("PRESIONE < ENTER > PARA CONTINUAR ")
                else:
                    print("-------------------------------------")
                    print("ERROR: LOS NOMBRES TIENEN QUE TENER ENTRE 2 Y 40 CARÁCTERES")
                    print("-------------------------------------")
                    input("PRESIONE < ENTER > PARA CONTINUAR ")
        while True:
            print("--------------------------------------------------------------------")
            print("                     TORNEOS DE BOLA")
            print("               REGISTRAR RESULTADOS: AGREGAR")
            print("                                         Nombre goleador     Minuto")
            print("Código del equipo casa:    ",     codigos[0])
            print("Código del equipo visita:  ",     codigos[1])
            print("Goles del equipo casa:  ", goles_casa)
            print("--------------------------------------------------------------------")
            if equipo1[0] == 0 and equipo1[1] == 0 and equipo1[2] == 0:
                pass
            else:
                for equipo in equipo_casa:
                    if equipo[2] < 0:
                        print("                                            ", equipo[0],"            ",equipo[1], "+" ,abs(equipo[2]))
                    else:
                        print("                                            ", equipo[0],"            ",equipo[1])
            print("--------------------------------------------------------------------")
            print("Goles del equipo visitante:  ", goles_visitante)
            if equipo2[0] == 0 and equipo2[1] == 0 and equipo2[2] == 0:
                pass
            else:
                for equipo11 in equipo_visitante:
                    if equipo11[2] < 0:
                        print("                                            ", equipo11[0],"          ",equipo11[1], "+" ,abs(equipo11[2]))
                    else:
                        print("                                            ", equipo11[0],"            ",equipo11[1])
            opcion = input("OPCIÓN <C> CANCELAR <A> ACEPTAR ")
            if opcion == "A":
                equipo_casa = descomponer_lista(equipo_casa)
                equipo_casa = tuple(equipo_casa)
                equipo_visitante = descomponer_lista(equipo_visitante)
                equipo_visitante = tuple(equipo_visitante)
                unir_jugadores.append(equipo_casa)
                unir_jugadores.append(equipo_visitante)
                unir_jugadores = tuple(unir_jugadores)
                goles.append(goles_casa)
                goles.append(goles_visitante)
                goles = tuple(goles)
                resultados[validacion_indice].pop(validacion_subindice)
                resultados[validacion_indice].insert(validacion_subindice,goles)
                goleadores[validacion_indice].pop(validacion_subindice)
                goleadores[validacion_indice].insert(validacion_subindice,unir_jugadores)
                break
            elif opcion == "C":
                print("-------------------------------------")
                print("ESTA SEGURO QUE QUIERE REALIZAR ESTA ACCIÓN?")
                opcion = input("OPCIÓN <C> CANCELAR <A> ACEPTAR ")
                if opcion == "A":
                    break
                elif opcion == "C":
                    pass
                else:
                    print("-------------------------------------")
                    print("ERROR: OPCION INVALIDA")
                    input("PRESIONE < ENTER > PARA CONTINUAR ")
            else:
                print("-------------------------------------")
                print("ERROR: OPCION INVALIDA")
                input("PRESIONE < ENTER > PARA CONTINUAR ")
        resultados = convertir_a_tupla(resultados)
        resultados = descomponer_lista(resultados)
        goleadores = convertir_a_tupla(goleadores)
        goleadores = descomponer_lista(goleadores)
        return(goleadores,resultados)
#ENTRADAS: listas e indice
#SALIDAS: una lista
def eliminar_resultado(resultados,goleadores,validacion_indice,validacion_subindice):
        while True:
            opcion = input("OPCIÓN <C> CANCELAR <A> ACEPTAR ")
            if opcion == "A":
                resultados[validacion_indice].pop(validacion_subindice)
                resultados[validacion_indice].insert(validacion_subindice,[])
                goleadores[validacion_indice].pop(validacion_subindice)
                goleadores[validacion_indice].insert(validacion_subindice,[])
                break
            elif opcion == "C":
                print("-------------------------------------")
                print("ESTA SEGURO QUE QUIERE REALIZAR ESTA ACCIÓN?")
                opcion = input("OPCIÓN <C> CANCELAR <A> ACEPTAR ")
                if opcion == "A":
                    break
                elif opcion == "C":
                    pass
                else:
                    print("-------------------------------------")
                    print("ERROR: OPCION INVALIDA")
                    input("PRESIONE < ENTER > PARA CONTINUAR ")
            else:
                print("-------------------------------------")
                print("ERROR: OPCION INVALIDA")
                input("PRESIONE < ENTER > PARA CONTINUAR ")
        resultados = convertir_a_tupla(resultados)
        resultados = descomponer_lista(resultados)
        goleadores = convertir_a_tupla(goleadores)
        goleadores = descomponer_lista(goleadores)
        return(goleadores,resultados)
#ENTRADAS: dos listas
#SALIDAS: un indice
def clasificador(lista_resultados,cantidad):
    contador = 0
    clasificados = []
    resultados_lista = []
    while lista_resultados != []:
        if len(clasificados) != cantidad:
            resultados_lista.append(max(lista_resultados))
            clasificados.append(max(lista_resultados))
            numero = lista_resultados.index(max(lista_resultados))
            lista_resultados.pop(numero)
            contador = contador + 1
        else:
            validador = max(lista_resultados)
            if clasificados[contador-1][2] == validador[2]:
                clasificados.append(validador)
                resultados_lista.append(validador)
                numero = lista_resultados.index(max(lista_resultados))
                lista_resultados.pop(numero)
                contador = contador + 1
            else:
                resultados_lista.append(validador)
                numero = lista_resultados.index(max(lista_resultados))
                lista_resultados.pop(numero)
    lista_resultados = resultados_lista
    return lista_resultados,clasificados
#ENTRADAS: una lista y un numero entero
#SALIDAS: dos listas
def cambiar_nombres(lista_resultados,equipos):
  for equipo in equipos:
    for code in equipo:
      if len(code) > 3:
            break
      for resultados in lista_resultados:
        try:
          indice_eliminar = resultados.index(code)
          if resultados.index(code):
            pass
          else:
            resultados.insert(0,equipo[1])
          break
        except:
          pass
  return lista_resultados
#ENTRADAS: dos listas
#SALIDAS: una lista
def validacion1(resultados):
    resultados = convertir_lista(resultados)
    for resultado in resultados:
        for result in resultado:
            if result != []:
                return True
    return False
#FUNCION #8 PRINCIPAL
def acerca_de():
    # Despliega la informacion del Software
    while True:
        print("          ACERCA DE          ")
        print("-----------------------------")
        print("|     TORNEO DE EQUIPOS     |")
        print("|        VERSIÓN 1.0        |")
        print("|   ANDRES GONZALEZ SIRIAS  |")
        print("|           2022            |")
        print("-----------------------------")
        opcion = input("OPCION <C> CANCELAR <A> ACEPTAR ")
        if opcion == "A":
            pass
        elif opcion == "C":
            break
        else:
            print("ERROR OPCION INVALIDAD")
            input("DAR < ENTER > PARA CONTINUAR")
#FUNCIÓN #7 PRINCIPAL
# Entradas: nada
# Salidas: nada
# Funcion: muetras el manual del programa
def ayuda():
    # Llama a un URL para desplegar el manual de usuario
    while True:
        path = 'https://www.canva.com/design/DAFOTZHjbnI/uFWb0z95J7SFVAaFkGEQVQ/view?utm_content=DAFOTZHjbnI&utm_campaign=designshare&utm_medium=link&utm_source=publishpresent'
        webbrowser.open_new(path)
        print("DESEA VOLVER A CONSULTAR EL MANUAL")
        opcion = input("OPCIÓN <C> CANCELAR <A> ACEPTAR ")
        if opcion == "A":
            pass
        elif opcion == "C":
            break
        else:
            print("ERROR:OPCION INVALIDA")
            input("PRESIONE < ENTER > PARA CONTINUAR ")
#FUNCIÓN #6 PRINCIPAL
# Entradas: nada
# Salidas: nada
# Funcion: muestra la informacion del programa 
def tabla_goleadores(equipos,calendario_juegos,resultados,goleadores,nombre):
    # Valida que se hayan registrado los goleadores
    if validacion1(goleadores):
        copia_equipos = equipos
        equipos = agrupar_codigos(equipos)
        calendario_juegos = convertir_lista(calendario_juegos)
        resultados = convertir_lista(resultados)
        goleadores = convertir_lista(goleadores)
        agregar = []
        lista_goleadores = []
        validador = len(calendario_juegos)
        contador = 0
        # Itera sobre los equipos para buscar un equipo
        for equipo in equipos:
            if validador == contador:
                if len(agregar) == 1:
                    agregar = []
                    pass
                else:
                    lista_goleadores.append(agregar)
                    agregar = []
            agregar.append(equipo)
            contador = 0
            # Itera sobre el calendario para buscar si el equipo esta en calendario
            for juegos in calendario_juegos:
                contador = contador + 1
                indice = calendario_juegos.index(juegos)
                for juego in juegos:
                    try:
                        sub_indice = juegos.index(juego)
                        subb_indice = juego.index(equipo)
                        try:
                            # Itera sobre la lista de goleadores para ver si en ese equpo hay goleadores
                            if goleadores[indice][sub_indice][subb_indice]:
                                jugadores = goleadores[indice][sub_indice][subb_indice]
                                for jugador in jugadores:
                                    agregar.append(jugador[0])
                        except:
                            pass
                    except:
                        pass
        if len(agregar) == 1:
            agregar = []
            pass
        else:
            lista_goleadores.append(agregar)
        lista = []
        lista_resultados = []
        #Agrega el nombre del equipo con los jugadores correspondientes
        for goleadores in  lista_goleadores:
            codigo = goleadores[0]
            goleadores.pop(0)
            # Reordena la informacion y cuenta cuantas veces esta el jugador en la lista 
            for goleador in goleadores:
                contador = goleadores.count(goleador)
                lista.append(contador)
                lista.append(goleador)
                lista.append(codigo)
                if lista_resultados.count(lista) == 1:
                    lista = []
                else:
                    lista_resultados.append(lista)
                    lista = []
        for equipos in copia_equipos:
            for resultados in lista_resultados:
                if equipos[0] == resultados[2]:
                    resultados.append(equipos[1])
        lista_goleadores = []
        # Itera para imprimir los goleadores con mas goles
        while lista_resultados != []:
            validador = max(lista_resultados)
            lista_goleadores.append(validador)
            lista_resultados.remove(validador)
        #Imprime los goleadores
        print(nombre)
        print("Tabla de goleadores")
        print("------------------------------------------------")
        print("Jugador                 Equipo             Goles")
        for goleadores in lista_goleadores:
            print("{:<21}".format(goleadores[1]),"{:<21}".format(goleadores[3]),"{:>1}".format(goleadores[0]))
        input("DAR < ENTER > PARA CONTINUAR")
    else:
        print("-------------------------------------")
        print("ERROR: DEBE REGISTAR ALGUN DATO PRIMERO")
        print("-------------------------------------")
        input("DAR < ENTER > PARA CONTINUAR")
#FUNCIÓN #5 PRINCIPAL
# Entradas: listas,string
# Salidas: nada
#Funcion: imprime las posciones de los goleadores
def tabla_posiciones(nombre,clasificados,puntos_ganado,puntos_empate,equipos,calendario_juegos,resultados):
    if validacion1(resultados):
        # Prepara los datos para ser ejecutados en formato de lista
        copia_equipos = equipos
        equipos = agrupar_codigos(equipos)
        resultados = convertir_lista(resultados)
        calendario_juegos = convertir_lista(calendario_juegos)
        lista_resultados = []
        agregar = []
        validador = len(calendario_juegos)
        contador = 0
        JJ = 0
        JG = 0
        JE = 0
        JP = 0
        GF = 0
        GC = 0
        GD = 0
        PUNTOS = 0
        # Itero sobre los equipos para buscar el equipo 
        for equipo in equipos:
            if validador == contador:
                if PUNTOS == 0 and GD == 0 and GF == 0 and JJ == 0 and JG == 0 and JE == 0 and JP == 0 and GC == 0:
                    pass
                else:
                    agregar.append(PUNTOS)
                    agregar.append(GD)
                    agregar.append(GF)
                    agregar.append(JJ)
                    agregar.append(JG)
                    agregar.append(JE)
                    agregar.append(JP)
                    agregar.append(GC)
                    lista_resultados.append(agregar)
                agregar = []
                JJ = 0
                JG = 0
                JE = 0
                JP = 0
                GF = 0
                GC = 0
                GD = 0
                PUNTOS = 0
            agregar.append(equipo)
            contador = 0
            # Itero para buscar en que posiciones esta ese equipo en las fechas
            for juegos in calendario_juegos:
                contador = contador + 1
                indice = calendario_juegos.index(juegos)
                for juego in juegos:
                    try:
                        subindice = juegos.index(juego)
                        subbindice = juego.index(equipo)
                        if subbindice == 1:
                            indice_contrario = 0
                        else:
                            indice_contrario = 1
                        try:
                            # Itero para buscar si hay resultados de ese equipo
                            if resultados[indice][subindice][subbindice]:
                                numero1 = resultados[indice][subindice][subbindice]
                                numero2 = resultados[indice][subindice][indice_contrario]
                                JJ = JJ + 1
                                GF = GF + numero1
                                GC = GC + numero2
                                GD = GF - GC
                                if numero1 > numero2:
                                    JG = JG + 1
                                    PUNTOS = PUNTOS + puntos_ganado
                                elif numero1 < numero2:
                                    JP = JP + 1
                                elif numero1 == numero2:
                                    PUNTOS = PUNTOS + puntos_empate
                        except:
                            pass
                    except:
                        pass
        # valida que si no se han registrado datos no agregue el equipo a la lista
        if PUNTOS == 0 and GD == 0 and GF == 0 and JJ == 0 and JG == 0 and JE == 0 and JP == 0 and GC == 0:
            pass
        else:
            agregar = []
            agregar.append(equipo)
            agregar.append(PUNTOS)
            agregar.append(GD)
            agregar.append(GF)
            agregar.append(JJ)
            agregar.append(JG)
            agregar.append(JE)
            agregar.append(JP)
            agregar.append(GC)
            lista_resultados.append(agregar)
        for resultados in lista_resultados:
            resultados.insert(4,resultados[0])
            resultados.pop(0)
        # Llamo a la funcion para que me retorne dos listas de los equipos y sus posiciones y los clasificados
        clasificar = clasificador(lista_resultados,clasificados)
        lista_resultados = clasificar[0]
        clasificados = clasificar[1]
        for resultados in lista_resultados:
            resultados.insert(0,resultados[3])
            resultados.pop(4)
        # Agrega los nombres en las listas
        lista_resultados = cambiar_nombres(lista_resultados,copia_equipos)
        cantidad = len(clasificados)
        # Imprime los equipos de acuerdo a su posición
        print(nombre)
        print("Tabla de posiciones")
        print("      Equipos clasificados:",cantidad)
        print("-------------------------------------------------------------------------------------")
        print("Equipo                 JJ      JG      JE      JP      GF      GC      GD      PUNTOS")
        print("-------------------------------------------------------------------------------------")
        for resultados in lista_resultados:
            print("{:<21}".format(resultados[0]),"{:>2}".format(resultados[5]),"{:>7}".format(resultados[6]),"{:>7}".format(resultados[7]),"{:>7}".format(resultados[8]),"{:>7}".format(resultados[4]),"{:>8}".format(resultados[9]),"{:>7}".format(resultados[3]),"{:>9}".format(resultados[2]))
            print("-------------------------------------------------------------------------------------")
        input("PRESIONE < ENTER > PARA CONTINUAR ")
        # Itero para ordenar los datos de clasificados
        for clasificado in clasificados:
            numero = clasificado[0]
            clasificado.append(numero)
            clasificado.pop(0)
        for clasificado in clasificados:
            numero = clasificado[0]
            clasificado.append(numero)
            clasificado.pop(0)
        if len(clasificados) > 1:
            lista = []
            contador = 1
            print("Equipos clasificados a la fecha:")
            print("--------------------------------")
        # Itero para hacer el calculo de buscar cuales equipos clasificados estan empatados
            for equipo in range(len(clasificados)-1):
                mensaje = ""
                lista = clasificados[equipo + 1][:3]
                if clasificados[equipo][:3] == lista:
                    mensaje = "EMPATE"
                    print(contador,"-","{:<20}".format(clasificados[equipo][8]),"{:>10}".format(mensaje))
                    contador += 1
                else:
                    print(contador,"-",clasificados[equipo][8])
                    contador += 1
            if clasificados[-2][:3] == clasificados[-1][:3]:
                print(contador,"-","{:<20}".format(clasificados[-1][8]),"{:>10}".format(mensaje))
            else:
                print(contador,"-",clasificados[-1][8])
        else:
            print("Equipo clasificado a la fecha:")
            print("1-",clasificados[0][8])
            input("DAR < ENTER > PARA CONTINUAR")
        print("----------------------------")
        input("DAR < ENTER > PARA CONTINUAR")
    else:
        print("-------------------------------------")
        print("ERROR: DEBE REGISTAR ALGUN DATO PRIMERO")
        print("-------------------------------------")
        input("DAR < ENTER > PARA CONTINUAR")
#FUNCIÓN #4 DE FUNCIÓN #4
# Entradas: listas,string y numeros enteros
# Salidas: nada
#Funcion: imprime las posiciones de los equipos
def eliminar_resultados(calendario_juegos,resultados,goleadores):
    if calendario_juegos:
        # Valida que calendario tenga datos
        if resultados:
            # Valida que los resultados tenga datos
            while True:
                calendario_juegos = convertir_lista(calendario_juegos)
                resultados = convertir_lista(resultados)
                goleadores = convertir_lista(goleadores)
                print("                                     ")
                print("                                     ")
                print("-------------------------------------")
                print("          TORNEOS DE BOLA")
                print("    REGISTRAR RESULTADOS: ELIMINAR")
                codigos = [input("Código del equipo casa: "), input("Código del equipo visita: ")]
                if codigos[0] == "C" or codigos[1] == "C":
                    break
                else:
                    # Valida los datos ingresados en el calendario de juegos
                    if validacion_de_codigos(codigos,calendario_juegos):
                        # Valida posiciones
                        validacion_indice = validacion_de_indice(codigos,calendario_juegos)
                        validacion_subindice = validacion_sub_indice(codigos,calendario_juegos)
                        if resultados[validacion_indice][validacion_subindice]:
                            resultado = resultados[validacion_indice][validacion_subindice]
                            goleadore = goleadores[validacion_indice][validacion_subindice]
                            print("                                     ")
                            print("                                     ")
                            print("-------------------------------------")
                            print("          TORNEOS DE BOLA")
                            print("    REGISTRAR RESULTADOS: ELIMINAR DATOS")
                            print("-------------------------------------")
                            print("Juegos       Goles")
                            print(codigos[0],"          ",resultado[0])
                            print(codigos[1],"          ",resultado[1])
                            print("-------------------------------------")
                            print("Jugadores que anotaron:")
                            print("Gol del Jugador      Equipo      Minuto      Repocisión")
                            for jugadores in goleadore[0]:
                                if jugadores[2] < 0:
                                    print("{:<10}".format(jugadores[0]),"          ",codigos[0],"        ",jugadores[1],"          ",jugadores[2])
                                else:
                                    print("{:<10}".format(jugadores[0]),"          ",codigos[0],"        ",jugadores[1])
                            for jugadadores1 in goleadore[1]:
                                if jugadadores1[2] < 0:
                                    print("{:<10}".format(jugadadores1[0]),"          ",codigos[1],"        ",jugadadores1[1],"          ",jugadadores1[2])
                                else:
                                    print("{:<10}".format(jugadadores1[0]),"          ",codigos[1],"        ",jugadadores1[1])
                            # Funcion que elimina los datos de la lista 
                            x = eliminar_resultado(resultados,goleadores,validacion_indice,validacion_subindice)
                            goleadores = x[0]
                            resultados = x[1]
                        else:
                            print("-------------------------------------")
                            print("ESTE RESULTADO NO ESTA REGISTRADO, NO SE PUEDE ELIMINAR")
                            print("-------------------------------------")
                            input("PRESIONE < ENTER > PARA CONTINUAR ")
                    else:
                        print("-------------------------------------")
                        print("ERROR: ESTE JUEGO NO ESTA")
                        print("-------------------------------------")
                        input("PRESIONE < ENTER > PARA CONTINUAR ")
        else:           
            print("-------------------------------------")
            print("ERROR: NO HAY RESULTADOS REGISTRADOS")
            print("-------------------------------------")
            input("PRESIONE < ENTER > PARA CONTINUAR ")
    else:        
        print("-------------------------------------")
        print("ERROR: DEBE CREAR EL CALENDARIO DE JUEGOS PRIMERO")
        print("-------------------------------------")
        input("PRESIONE < ENTER > PARA CONTINUAR ")
    resultados = convertir_a_tupla(resultados)
    resultados = descomponer_lista(resultados)
    goleadores = convertir_a_tupla(goleadores)
    goleadores = descomponer_lista(goleadores)
    return(goleadores,resultados)
#FUNCIÓN #3 DE FUNCIÓN #4
# Entradas: listas
# Salidas: una lista
#Funcion: elimina los resultados registrados
def modificar_resultados(calendario_juegos,resultados,goleadores):
    if calendario_juegos:
        # Valida que calendario 
        if resultados:
            # Valida que hayan datos en resultados
            while True:
                calendario_juegos = convertir_lista(calendario_juegos)
                resultados = convertir_lista(resultados)
                goleadores = convertir_lista(goleadores)
                print("                                     ")
                print("                                     ")
                print("-------------------------------------")
                print("          TORNEOS DE BOLA")
                print("    REGISTRAR RESULTADOS: MODIFICAR")
                codigos = [input("Código del equipo casa: "), input("Código del equipo visita: ")]
                if codigos[0] == "C" or codigos[1] == "C":
                    break
                else:
                    # Valida que esten los datos ingresados en el calendario de quipos
                    if validacion_de_codigos(codigos,calendario_juegos):
                        # Valida las posiciones
                        validacion_indice = validacion_de_indice(codigos,calendario_juegos)
                        validacion_subindice = validacion_sub_indice(codigos,calendario_juegos)
                        if resultados[validacion_indice][validacion_subindice]:
                            resultado = resultados[validacion_indice][validacion_subindice]
                            goleadore = goleadores[validacion_indice][validacion_subindice]
                            print("                                     ")
                            print("                                     ")
                            print("-------------------------------------")
                            print("          TORNEOS DE BOLA")
                            print("    REGISTRAR RESULTADOS: DATOS ACTUALES")
                            print("-------------------------------------")
                            print("Juegos       Goles")
                            print(codigos[0],"          ",resultado[0])
                            print(codigos[1],"          ",resultado[1])
                            print("-------------------------------------")
                            print("Jugadores que anotaron:")
                            print("Gol del Jugador      Equipo      Minuto      Repocisión")
                            for jugadores in goleadore[0]:
                                if jugadores[2] < 0:
                                    print("{:<10}".format(jugadores[0]),"          ",codigos[0],"        ",jugadores[1],"          ",jugadores[2])
                                else:
                                    print("{:<10}".format(jugadores[0]),"          ",codigos[0],"        ",jugadores[1])
                            for jugadadores1 in goleadore[1]:
                                if jugadadores1[2] < 0:
                                    print("{:<10}".format(jugadadores1[0]),"          ",codigos[1],"        ",jugadadores1[1],"          ",jugadadores1[2])
                                else:
                                    print("{:<10}".format(jugadadores1[0]),"          ",codigos[1],"        ",jugadadores1[1])
                            input("\nPRESIONE < A > PARA CONTINUAR ")
                            # Empieza a desplegar los formularios para modificar los resultados
                            x = modificacion_resultados(resultados,goleadores,codigos,validacion_indice,validacion_subindice)
                            goleadores = x[0]
                            resultados = x[1]
                        else:
                            print("-------------------------------------")
                            print("ESTE RESULTADO NO ESTA REGISTRADO, NO SE PUEDE MODIFICAR")
                            print("-------------------------------------")
                            input("PRESIONE < ENTER > PARA CONTINUAR ")
                    else:
                        print("-------------------------------------")
                        print("ERROR: ESTE JUEGO NO ESTA")
                        print("-------------------------------------")
                        input("PRESIONE < ENTER > PARA CONTINUAR ")
        else:           
            print("-------------------------------------")
            print("ERROR: NO HAY RESULTADOS REGISTRADOS")
            print("-------------------------------------")
            input("PRESIONE < ENTER > PARA CONTINUAR ")
    else:        
        print("-------------------------------------")
        print("ERROR: DEBE CREAR EL CALENDARIO DE JUEGOS PRIMERO")
        print("-------------------------------------")
        input("PRESIONE < ENTER > PARA CONTINUAR ")
    resultados = convertir_a_tupla(resultados)
    resultados = descomponer_lista(resultados)
    goleadores = convertir_a_tupla(goleadores)
    goleadores = descomponer_lista(goleadores)
    return(goleadores,resultados)
#FUNCIÓN #2 DE FUNCIÓN #4
# Entradas: listas
# Salidas: una lista
#Funcion: modifica los resultados de los euipos registrados
def consultar_resultados(calendario_juegos,resultados,goleadores):
    calendario_juegos = convertir_lista(calendario_juegos)
    resultados = convertir_lista(resultados)
    goleadores = convertir_lista(goleadores)
    if calendario_juegos:
        # Valida que el calendario se haya creado
        if resultados:
            # Valida que hayan registrado resultados
            while True:
                print("-------------------------------------")
                print("          TORNEOS DE BOLA")
                print("    REGISTRAR RESULTADOS: CONSULTAR")
                codigos = [input("Código del equipo casa: "), input("Código del equipo visita: ")]
                if codigos[0] == "C" or codigos[1] == "C":
                    break
                else:
                    #Valida que los datos ingresados esten en la lista
                    if validacion_de_codigos(codigos,calendario_juegos):
                        # Valida los indices de los datos ingresados en el calendario
                        validacion_indice = validacion_de_indice(codigos,calendario_juegos)
                        validacion_subindice = validacion_sub_indice(codigos,calendario_juegos)
                        if resultados[validacion_indice][validacion_subindice]:
                            indice = resultados[validacion_indice][validacion_subindice]
                            subindice = goleadores[validacion_indice][validacion_subindice]
                            print("-------------------------------------")
                            print("          TORNEOS DE BOLA")
                            print("    REGISTRAR RESULTADOS: CONSULTAR")
                            print("-------------------------------------")
                            print("Juegos       Goles")
                            print(codigos[0],"          ",indice[0])
                            print(codigos[1],"          ",indice[1])
                            print("-------------------------------------")
                            print("Jugadores que anotaron:")
                            print("Gol del Jugador      Equipo      Minuto      Repocisión")
                            for jugadores in subindice[0]:
                                if jugadores[2] < 0:
                                    print("{:<10}".format(jugadores[0]),"          ",codigos[0],"        ",jugadores[1],"          ",jugadores[2])
                                else:
                                    print("{:<10}".format(jugadores[0]),"          ",codigos[0],"        ",jugadores[1])
                            for jugadadores1 in subindice[1]:
                                if jugadadores1[2] < 0:
                                    print("{:<10}".format(jugadadores1[0]),"          ",codigos[1],"        ",jugadadores1[1],"          ",jugadadores1[2])
                                else:
                                    print("{:<10}".format(jugadadores1[0]),"          ",codigos[1],"        ",jugadadores1[1])
                            input("PRESIONE < A > PARA CONTINUAR ")
                        else:
                            print("-------------------------------------")
                            print("ESTE RESULTADO NO ESTA REGISTRADO, NO SE PUEDE CONSULTAR")
                            print("-------------------------------------")
                            input("PRESIONE < ENTER > PARA CONTINUAR ")
                    else:
                        print("-------------------------------------")
                        print("ERROR: ESTE JUEGO NO ESTA")
                        print("-------------------------------------")
                        input("PRESIONE < ENTER > PARA CONTINUAR ")
        else:
            print("-------------------------------------")
            print("ERROR: NO HAY RESULTADOS REGISTRADOS")
            print("-------------------------------------")
            input("PRESIONE < ENTER > PARA CONTINUAR ")
    else:
        print("-------------------------------------")
        print("ERROR: DEBE CREAR EL CALENDARIO DE JUEGOS PRIMERO")
        print("-------------------------------------")
        input("PRESIONE < ENTER > PARA CONTINUAR ")
#FUNCIÓN #1 DE FUNCIÓN #4
# Entradas: listas
# Salidas: nada
#Funcion: consulta los resultados de los equipos
def agregar_resultados(calendario_juegos,resultados,goleadores):
    equipo_casa = []
    equipo1 = []
    equipo_visitante = []
    equipo2 = []
    valor = 0
    valor1 = 90
    unir_jugadores = []
    goles = []
    if calendario_juegos:
        # Valida que se haya creado el calendario
        contador = 0
        while True:
            print("-------------------------------------")
            print("          TORNEOS DE BOLA")
            print("    REGISTRAR RESULTADOS: AGREGAR")
            codigos = [input("Código del equipo casa: "), input("Código del equipo visita: ")]
            codigos = tuple(codigos)
            if codigos[0] == "C":
                return(goleadores,resultados)
            # Valida que esten los codigos en el calendario
            if validacion_de_codigos(codigos,calendario_juegos):
                # Valida los indices de los equipos en el calendario
                validacion_indice = validacion_de_indice(codigos,calendario_juegos)
                validacion_subindice = validacion_sub_indice(codigos,calendario_juegos)
                if resultados:
                    resultados = convertir_lista(resultados)
                    try:
                        if resultados[validacion_indice][validacion_subindice]:
                            print("-------------------------------------")
                            print("ERROR: YA LOS RESULTADOS FUERON REGISTRADOS")
                            print("-------------------------------------")
                            input("PRESIONE < ENTER > PARA CONTINUAR ")
                        else:
                            break
                    except:
                        break
                else:
                    resultados = crear_sub_listas(resultados,calendario_juegos)
                    break        
            else:
                print("-------------------------------------")
                print("ERROR: ESTE JUEGO NO ESTÁ EN EL CALENDARIO, NO SE PUEDE REGISTRAR RESULTADO")
                print("-------------------------------------")
                input("PRESIONE < ENTER > PARA CONTINUAR ")
        # Empieza a preguntar sobre los datos de los resultados a registrar 
        while True:
            try:
                print("-------------------------------------")
                goles_casa = int(input("Goles del equipo casa "))
                if goles_casa >= 1:
                    break
                elif goles_casa == 0:
                    equipo1.insert(0,0)
                    equipo1.insert(1,0)
                    equipo1.insert(2,0)
                    equipo_casa.append(equipo1)
                    break
            except:
                print("-------------------------------------")
                print("ERROR: LOS GOLES DEBEN SER UN ENTERO")
                print("-------------------------------------")
                input("PRESIONE < ENTER > PARA CONTINUAR ")
        # Pregunta por los jugadores del equipo visitante
        while contador < goles_casa:
            equipo1 = []
            if goles_casa >= 2:
                goleador = input("Jugadores que anotaron ")
                if len(goleador) >= 2 and len(goleador) <= 40 and goleador.isspace() == False:
                    while True:
                        try:
                            minuto = int(input("Minuto "))
                            if isinstance(minuto,int) and abs(minuto) >= 0 and abs(minuto) <= 120:
                                contador = contador + 1
                                equipo1.insert(0,goleador)
                                if minuto > 0:
                                    equipo1.insert(1,minuto)
                                    equipo1.insert(2,valor)
                                    equipo_casa.append(equipo1)
                                    break
                                else:
                                    equipo1.insert(1,valor1)
                                    equipo1.insert(2,minuto)
                                    equipo_casa.append(equipo1)
                                    break
                            else:
                                print("-------------------------------------")
                                print("ERROR: EL NUMERO TIENE QUE SER MAYOR QUE -120 Y MENOR QUE 120")
                                print("-------------------------------------")
                                input("PRESIONE < ENTER > PARA CONTINUAR ")
                        except:
                            print("-------------------------------------")
                            print("ERROR: TIENE QUE SER UN NUMERO ENTERO")
                            print("-------------------------------------")
                            input("PRESIONE < ENTER > PARA CONTINUAR ")
                else:
                    print("-------------------------------------")
                    print("ERROR: LOS NOMBRES TIENEN QUE TENER ENTRE 2 Y 40 CARÁCTERES")
                    print("-------------------------------------")
                    input("PRESIONE < ENTER > PARA CONTINUAR ")
            elif goles_casa == 1:
                goleador = input("Jugador que anotó ")
                if len(goleador) >= 2 and len(goleador) <= 40 and goleador.isspace() == False:
                    while True:
                        try:
                            minuto = int(input("Minuto "))
                            if isinstance(minuto,int) and abs(minuto) >= 0 and abs(minuto) <= 120:
                                contador = contador + 1
                                equipo1.insert(0,goleador)
                                if minuto > 0:
                                    equipo1.insert(1,minuto)
                                    equipo1.insert(2,valor)
                                    equipo_casa.append(equipo1)
                                    break
                                else:
                                    equipo1.insert(1,valor1)
                                    equipo1.insert(2,minuto)
                                    equipo_casa.append(equipo1)
                                    break
                            else:
                                print("-------------------------------------")
                                print("ERROR: EL NUMERO TIENE QUE SER MAYOR QUE -120 Y MENOR QUE 120")
                                print("-------------------------------------")
                                input("PRESIONE < ENTER > PARA CONTINUAR ")
                        except:
                            print("-------------------------------------")
                            print("ERROR: TIENE QUE SER UN NUMERO ENTERO")
                            print("-------------------------------------")
                            input("PRESIONE < ENTER > PARA CONTINUAR ")
                else:
                    print("-------------------------------------")
                    print("ERROR: LOS NOMBRES TIENEN QUE TENER ENTRE 2 Y 40 CARÁCTERES")
                    print("-------------------------------------")
                    input("PRESIONE < ENTER > PARA CONTINUAR ")
        # Goles del equipo visitante
        while True:
            try:
                print("-------------------------------------")
                goles_visitante = int(input("Goles del equipo Visitante "))
                if goles_visitante >= 1:
                    break
                elif goles_visitante == 0:
                    equipo2.insert(0,0)
                    equipo2.insert(1,0)
                    equipo2.insert(2,0)
                    equipo_visitante.append(equipo2)
                    break
            except:
                print("-------------------------------------")
                print("ERROR: LOS GOLES DEBEN SER UN ENTERO")
                print("-------------------------------------")
                input("PRESIONE < ENTER > PARA CONTINUAR ")
        contador = 0
        #Jugadores que anotaron del equipo visitante
        while contador < goles_visitante:
            equipo2 = []
            if goles_visitante >= 2:
                goleador = input("Jugadores que anotaron ")
                if len(goleador) >= 2 and len(goleador) <= 40 and goleador.isspace() == False:
                    while True:
                        try:
                            minuto = int(input("Minuto "))
                            if isinstance(minuto,int) and abs(minuto) >= 0 and abs(minuto) <= 120:
                                contador = contador + 1
                                equipo2.insert(0,goleador)
                                if minuto > 0:
                                    equipo2.insert(1,minuto)
                                    equipo2.insert(2,valor)
                                    equipo_visitante.append(equipo2)
                                    break
                                else:
                                    equipo2.insert(1,valor1)
                                    equipo2.insert(2,minuto)
                                    equipo_visitante.append(equipo2)
                                    break
                            else:
                                print("-------------------------------------")
                                print("ERROR: EL NUMERO TIENE QUE SER MAYOR QUE -120 Y MENOR QUE 120")
                                print("-------------------------------------")
                                input("PRESIONE < ENTER > PARA CONTINUAR ")
                        except:
                            print("-------------------------------------")
                            print("ERROR: TIENE QUE SER UN NUMERO ENTERO")
                            print("-------------------------------------")
                            input("PRESIONE < ENTER > PARA CONTINUAR ")
                else:
                    print("-------------------------------------")
                    print("ERROR: LOS NOMBRES TIENEN QUE TENER ENTRE 2 Y 40 CARÁCTERES")
                    print("-------------------------------------")
                    input("PRESIONE < ENTER > PARA CONTINUAR ")
            # Goleadores del equipo visitante
            elif goles_visitante == 1:
                goleador = input("Jugador que anotó ")
                if len(goleador) >= 2 and len(goleador) <= 40 and goleador.isspace() == False:
                    while True:
                        try:
                            minuto = int(input("Minuto "))
                            if isinstance(minuto,int) and abs(minuto) >= 0 and abs(minuto) <= 120:
                                contador = contador + 1
                                equipo2.insert(0,goleador)
                                if minuto > 0:
                                    equipo2.insert(1,minuto)
                                    equipo2.insert(2,valor)
                                    equipo_visitante.append(equipo2)
                                    break
                                else:
                                    equipo2.insert(1,valor1)
                                    equipo2.insert(2,minuto)
                                    equipo_visitante.append(equipo2)
                                    break
                            else:
                                print("-------------------------------------")
                                print("ERROR: EL NUMERO TIENE QUE SER MAYOR QUE -120 Y MENOR QUE 120")
                                print("-------------------------------------")
                                input("PRESIONE < ENTER > PARA CONTINUAR ")
                        except:
                            print("-------------------------------------")
                            print("ERROR: TIENE QUE SER UN NUMERO ENTERO")
                            print("-------------------------------------")
                            input("PRESIONE < ENTER > PARA CONTINUAR ")
                else:
                    print("-------------------------------------")
                    print("ERROR: LOS NOMBRES TIENEN QUE TENER ENTRE 2 Y 40 CARÁCTERES")
                    print("-------------------------------------")
                    input("PRESIONE < ENTER > PARA CONTINUAR ")
        # Si los datos cumplen los parametros despliega los datos a agregar
        while True:
            print("--------------------------------------------------------------------")
            print("                     TORNEOS DE BOLA")
            print("               REGISTRAR RESULTADOS: AGREGAR")
            print("                                         Nombre goleador     Minuto")
            print("Código del equipo casa:    ",     codigos[0])
            print("Código del equipo visita:  ",     codigos[1])
            print("Goles del equipo casa:  ", goles_casa)
            print("--------------------------------------------------------------------")
            if equipo1[0] == 0 and equipo1[1] == 0 and equipo1[2] == 0:
                pass
            else:
                for equipo in equipo_casa:
                    if equipo[2] < 0:
                        print("{:>50}".format(equipo[0]),"{:>14}".format(equipo[1]),"+","{:>3}".format(abs(equipo[2])))
                    else:
                        print("{:>50}".format(equipo[0]),"{:>14}".format(equipo[1]))
            print("--------------------------------------------------------------------")
            print("Goles del equipo visitante:  ", goles_visitante)
            if equipo2[0] == 0 and equipo2[1] == 0 and equipo2[2] == 0:
                pass
            else:
                for equipo11 in equipo_visitante:
                    if equipo11[2] < 0:
                        print("{:>50}".format(equipo11[0]),"{:>14}".format(equipo11[1]),"+","{:>3}".format(abs(equipo11[2])))
                    else:
                        print("{:>50}".format(equipo11[0]),"{:>14}".format(equipo11[1]))
            opcion = input("OPCIÓN <C> CANCELAR <A> ACEPTAR ")
            if opcion == "A":
                equipo_casa = descomponer_lista(equipo_casa)
                equipo_casa = tuple(equipo_casa)
                equipo_visitante = descomponer_lista(equipo_visitante)
                equipo_visitante = tuple(equipo_visitante)
                unir_jugadores.append(equipo_casa)
                unir_jugadores.append(equipo_visitante)
                unir_jugadores = tuple(unir_jugadores)
                goles.append(goles_casa)
                goles.append(goles_visitante)
                goles = tuple(goles)
                resultados[validacion_indice].pop(validacion_subindice)
                resultados[validacion_indice].insert(validacion_subindice,goles)
                if goleadores:
                    goleadores = convertir_lista(goleadores)
                    goleadores[validacion_indice].pop(validacion_subindice)
                    goleadores[validacion_indice].insert(validacion_subindice,unir_jugadores)
                    break
                else:
                    goleadores = crear_sub_listas(goleadores,calendario_juegos)
                    goleadores[validacion_indice].pop(validacion_subindice)
                    goleadores[validacion_indice].insert(validacion_subindice,unir_jugadores)
                    break
            elif opcion == "C":
                print("-------------------------------------")
                print("ESTA SEGURO QUE QUIERE REALIZAR ESTA ACCIÓN?")
                opcion = input("OPCIÓN <C> CANCELAR <A> ACEPTAR ")
                if opcion == "A":
                    break
                elif opcion == "C":
                    pass
                else:
                    print("-------------------------------------")
                    print("ERROR: OPCION INVALIDA")
                    input("PRESIONE < ENTER > PARA CONTINUAR ")
            else:
                print("-------------------------------------")
                print("ERROR: OPCION INVALIDA")
                input("PRESIONE < ENTER > PARA CONTINUAR ")
    else:
        print("-------------------------------------")
        print("ERROR: DEBE CREAR EL CALENDARIO DE JUEGOS PRIMERO")
        print("-------------------------------------")
        input("PRESIONE < ENTER > PARA CONTINUAR ")
    resultados = convertir_a_tupla(resultados)
    resultados = descomponer_lista(resultados)
    goleadores = convertir_a_tupla(goleadores)
    goleadores = descomponer_lista(goleadores)
    return(goleadores,resultados)
#FUNCIÓN #4 PRINCIPAL
# Entradas: listas
# Salidas: una lista
#Funcion: registra los resultados de los equipos
def registrar_resultados(calendario_juegos,resultados,goleadores):
    opcion = 1
    # Menu principal 
    while opcion >= 0:
        print("\n\n\nTORNEOS DE BOLA")
        print("REGISTRAR LOS RESULTADOS")
        print("1. AGREGAR RESULTADOS ")
        print("2. CONSULTAR RESULTADOS")
        print("3. MODIFICAR RESULTADOS")
        print("4. ELIMINAR RESULTADOS")
        print("0. SALIR")
        try:
            opcion = int(input("OPCIÓN "))
            if opcion == 1:
                # Agrega resultados
                x = agregar_resultados(calendario_juegos,resultados,goleadores)
                goleadores = x[0]
                resultados = x[1]
            elif opcion == 2:
                # consulta los resultados
                consultar_resultados(calendario_juegos,resultados,goleadores)
            elif opcion == 3:
                # modifica los resultados
                x = modificar_resultados(calendario_juegos,resultados,goleadores)
                goleadores = x[0]
                resultados = x[1]
            elif opcion == 4:
                # elimina los resultados
                x = eliminar_resultados(calendario_juegos,resultados,goleadores)
                goleadores = x[0]
                resultados = x[1]
            elif opcion == 0:
                break
            else:
                print("-------------------------------------")
                print("OPCIÓN INVALIDA")
                print("-------------------------------------")
                input("PRESIONE < ENTER > PARA CONTINUAR ")
        except:
            print("-------------------------------------")
            print("ERROR: LA OPCIÓN TIENE QUE SER UN NUMERO ENTERO")
            print("-------------------------------------")
            input("PRESIONE < ENTER > PARA CONTINUAR ")
    return(goleadores,resultados)
# FUNCIÓN #3 PRINCIPAL
# Entradas: listas
# Salidas: una lista
#Funcion: muestra las opciones de registrar resultados
def consultar_calendario(nombre, equipos, cantidad, calendario_juegos):
    if calendario_juegos:
        # Si el calendario esta creado solo lo consulta
        equipos_copia = equipos
        jugadas = []
        contador = 0
        print(nombre)
        print("-------")
        for equipo in calendario_juegos:
            contador = contador + 1
            print("Fecha", contador)
            a = True
            for club in equipo:
                for code in club:
                    a = True
                    for clube in equipos_copia:
                        if a == False:
                            break
                        for codigo in clube:
                            if code == codigo:
                                jugadas.append(clube[1])
                                if len(jugadas) == 2:
                                    print(jugadas[0], "-", jugadas[1])
                                    jugadas.clear()
            print("----------------------------")
            input("DAR < ENTER > PARA CONTINUAR")
            print("----------------------------")
    else:
        # si no tiene valores en la lista, crea las combinaciones y las consulta
        equipos_copia = equipos
        if cantidad >= 2:
            # validad que se hayan registrado todos los equipos
            if len(equipos) == cantidad:
                equipos = descomponer_tupla(equipos)
                clubes = agrupar_codigos(equipos)
                # crea las posibles combinaciones de los juegos y las fechas
                index_clubes = 0
                cantidad_de_equipos = len(clubes)
                impar = True if cantidad_de_equipos % 2 != 0 else False
                if impar:
                    cantidad_de_equipos += 1
                total_partidos = cantidad_de_equipos // 2  # total de partidos de una jornada
                indice_inverso = cantidad_de_equipos - 2
                for i in range(1, cantidad_de_equipos):
                    equipos = []
                    for indice_partido_inicial in range(0, total_partidos):
                        if index_clubes > cantidad_de_equipos - 2:
                            index_clubes = 0
                        if indice_inverso < 0:
                            indice_inverso = cantidad_de_equipos - 2
                        # seria el partido inicial de cada fecha
                        if indice_partido_inicial == 0:  
                            if impar:
                                equipos.append(clubes[index_clubes])
                            else:
                                if (i + 1) % 2 == 0:
                                    partido = [clubes[index_clubes],clubes[cantidad_de_equipos-1]]
                                else:
                                    partido = [clubes[cantidad_de_equipos-1], clubes[index_clubes]]
                                equipos.append(partido)
                        else:
                            partido = [clubes[index_clubes],clubes[indice_inverso]]
                            equipos.append(partido)
                            indice_inverso -= 1
                        index_clubes += 1
                    calendario_juegos.append(equipos)
                # Itera la lista creada, pero crea las combinaciones al reves de las que ya hay 
                equipos1 = []
                equipos2 = []
                for equipo in calendario_juegos:
                    for club in equipo:
                        club = list(reversed(club))
                        equipos1.append(club)
                        if len(equipos1) == len(equipos_copia) // 2:
                            equipos2.append(equipos1)
                            equipos1 = []
                # une las dos combinaciones
                calendario_juegos = union(calendario_juegos, equipos2)
                jugadas = []
                contador = 0
                # consulta el calendario ya creado
                print(nombre)
                print("----------")
                for equipo in calendario_juegos:
                    contador = contador + 1
                    print("Fecha", contador)
                    a = True
                    for club in equipo:
                        for code in club:
                            a = True
                            for clube in equipos_copia:
                                if a == False:
                                    break
                                for codigo in clube:
                                    if code == codigo:
                                        jugadas.append(clube[1])
                                        if len(jugadas) == 2:
                                            print(jugadas[0], "-", jugadas[1])
                                            jugadas.clear()
                    print("----------------------------")
                    input("DAR < ENTER > PARA CONTINUAR")
                    print("----------------------------")
            else:
                print("-------------------------------------")
                print(
                    "ERROR: PARA CONTINUAR DEBE REGISTRAR LA CONFIGURACIÓN DE LOS EQUIPOS")
                print("-------------------------------------")
        else:
            print("-------------------------------------")
            print("ERROR: PARA CONTINUAR DEBE REGISTRAR LA CONFIGURACIÓN DEL TORNEO")
            print("-------------------------------------")
            input("DAR < ENTER > PARA CONTINUAR")
    calendario_juegos = convertir_a_tupla(calendario_juegos)
    calendario_juegos = descomponer_lista(calendario_juegos)
    return calendario_juegos
# FUNCIÓN #4 DE FUNCIÓN #2
# Entradas: string, listas y numeros enteros
# Salidas: una lista
#Funcion: crea las posibles combinaciones en las que van a jugar los equipos
def eliminar_equipos(cantidad, equipos, calendario_juegos):
    if cantidad >= 2:
        # Hace validacion de que el usuario haya ingresado la configuracion del torneo
        if len(calendario_juegos) == 0:
            if equipos:
                # Valida que se haya registrado al menos un equipo
                a = True
                while a == True:
                    codigo = input("\n\n\nCÓDIGO DEL EQUIPO ")
                    if equipos:
                        if validacion(codigo, equipos):
                            # Valida que se haya registrado al menos un equipo y que el dato que se consulta este en la lista
                            equipos = descomponer_tupla(equipos)
                            for equipo in equipos:
                                if codigo in equipo:
                                    while a == True:
                                        print(
                                            "-------------------------------------")
                                        print("TORNEOS DE BOLA")
                                        print(
                                            "REGISTRAR EQUIPOS: ELIMINAR EQUIPOS")
                                        print("Código del equipo: ", codigo)
                                        print("Nombre del equipo: ", equipo[1])
                                        print(
                                            "-------------------------------------")
                                        print("OPCIÓN <C> CANCELAR <A>ACEPTAR")
                                        print(
                                            "-------------------------------------")
                                        opcion = input("OPCIÓN ")
                                        if opcion == "A":
                                            numero = equipos.index(equipo)
                                            equipos.pop(numero)
                                            equipos
                                            break
                                        elif opcion == "C":
                                            print(
                                                "-------------------------------------")
                                            print(
                                                "¿ESTA SEGURO QUE QUIERE CANCELAR?")
                                            print(
                                                "OPCIÓN <C> CANCELAR <A>ACEPTAR")
                                            print(
                                                "-------------------------------------")
                                            opcion = input("OPCIÓN ")
                                            if opcion == "A":
                                                equipos
                                                break
                                            else:
                                                equipos
                                        else:
                                            print(
                                                "-------------------------------------")
                                            print("OPCIÓN INVALIDA")
                                            print(
                                                "-------------------------------------")
                        elif codigo == "C":
                            break
                        else:
                            print("-------------------------------------")
                            print("ESTE EQUIPO NO ESTA REGISTRADO, NO SE PUEDE ELIMINAR")
                            print("-------------------------------------")
                    else:
                        print("-------------------------------------")
                        print("ERROR NO HAY EQUIPOS REGISTRADOS")
                        print("-------------------------------------")
                        break
            else:
                print("-------------------------------------")
                print("ERROR: NO HAY EQUIPOS REGISTRADOS")
                print("-------------------------------------")
                equipos = []
                return equipos
        else:
            print("-------------------------------------")
            print("ERROR: EL CALENDARIO DE JUEGOS YA SE CREO")
            print("-------------------------------------")
    else:
        print("-------------------------------------")
        print("ERROR: DEBE REGISTRAR LA CANTIDAD DE EQUIPOS PARTICIPANTES")
        print("-------------------------------------")
    equipos = descomponer_lista(equipos)
    return (equipos)
# FUNCION #3 DE FUNCION #2
# Entradas: strings y listas 
# Salidas: una lista
#Funcion: elimina los datos de la lista de equipos
def modificar_equipos(equipos, cantidad):
    if cantidad >= 2:
        # Hace validacion de que el usuario haya ingresado la configuracion del torneo
        if equipos:
             # Valida que se haya registrado al menos un equipo
            a = True
            while a == True:
                b = True
                codigo = input("\n\n\nCODIGO DEL EQUIPO ")
                if validacion(codigo, equipos):
                     # Valida que se haya registrado al menos un equipo
                    equipos = descomponer_tupla(equipos)
                    for equipo in equipos:
                        if codigo in equipo:
                            while b == True:
                                print("-------------------------------------")
                                print("TORNEOS DE BOLA")
                                print("REGISTRAR EQUIPOS: MODIFICAR EQUIPOS")
                                print("Código del equipo: ", codigo)
                                print("Nombre actual del equipo: ", equipo[1])
                                print("-------------------------------------")
                                nombre = input("Nombre modificado del equipo ")
                                if len(nombre) >= 3 and len(nombre) <= 40 and nombre.isspace() == False:
                                    print("-------------------------------------")
                                    print("OPCIÓN <C> CANCELAR <A>ACEPTAR")
                                    opcion = input("OPCIÓN ")
                                    if opcion == "A":
                                        equipo.pop()
                                        equipo.insert(1, nombre)
                                        equipos
                                        b = False
                                        break
                                    elif opcion == "C":
                                        print(
                                            "-------------------------------------")
                                        print(
                                            "¿ESTA SEGURO QUE QUIERE CANCELAR?")
                                        print("OPCIÓN <C> CANCELAR <A>ACEPTAR")
                                        print(
                                            "-------------------------------------")
                                        opcion = input("OPCIÓN ")
                                        if opcion == "A":
                                            equipos
                                            break
                                        else:
                                            equipos
                                    else:
                                        print(
                                            "-------------------------------------")
                                        print("OPCIÓN INVALIDA")
                                        print(
                                            "-------------------------------------")
                                else:
                                    print("-------------------------------------")
                                    print(
                                        "ERROR: EL NOMBRE DEL TORNEO TIENE QUE TENER ENTRE 10 Y 40 CARACTERES")
                                    print("-------------------------------------")
                elif codigo == "C":
                    break
                else:
                    print("-------------------------------------")
                    print("ESTE EQUIPO NO ESTA REGISTRADO, NO SE PUEDE MODIFICAR")
                    print("-------------------------------------")
        else:
            print("-------------------------------------")
            print("ERROR: NO HAY EQUIPOS REGISTRADOS")
            print("-------------------------------------")
            equipos = []
            return equipos
    else:
        print("-------------------------------------")
        print("ERROR: DEBE REGISTRAR LA CANTIDAD DE EQUIPOS PARTICIPANTES")
        print("-------------------------------------")
    equipos = descomponer_lista(equipos)
    return (equipos)
# FUNCION #2 DE FUNCION #2
# Entradas: un numero entero y una lista de tuplas
# Salidas: una lista
# Funcion: modifica los valores que estan en la lista de equipos
def consultar_codigos(cantidad, equipos):
    if cantidad >= 2:
        # Hace validacion de que el usuario haya ingresado la configuracion del torneo
        if equipos:
            # Valida que se haya registrado al menos un equipo
            a = True
            while a == True:
                codigo = input("\n\n\nCODIGO DEL EQUIPO ")
                if validacion(codigo, equipos):
                    # Valida que se haya registrado el equipo en la lista
                    print("-------------------------------------")
                    print("TORNEOS DE BOLA")
                    print("REGISTRAR EQUIPOS: CONSULTAR EQUIPOS")
                    print("Código del equipo: ", codigo)
                    print("Nombre del equipo: ", validar_codigos(codigo, equipos))
                    print("-------------------------------------")
                    opcion = input("OPCION <A> ACEPTAR ")
                    if opcion == "A":
                        pass
                    else:
                        pass
                elif codigo == "C":
                    break
                else:
                    print("-------------------------------------")
                    print("ESTE EQUIPO NO ESTA REGISTRADO, NO SE PUEDE CONSULTAR")
                    print("-------------------------------------")
        else:
            print("-------------------------------------")
            print("ERROR: NO HAY EQUIPOS REGISTRADOS")
            print("-------------------------------------")
    else:
        print("-------------------------------------")
        print("ERROR: DEBE REGISTRAR LA CANTIDAD DE EQUIPOS PARTICIPANTES")
        print("-------------------------------------")
    return equipos
# FUNCION #1 DE FUNCION #2
# Entradas: un numero entero y una lista de tuplas
# Salidas: ninguna
# Funcion: consulta los valores en la lista de equipos
def agregar_equipos(equipos, codigos, cantidad):
    if cantidad >= 2:
        #En caso de ya hayan sido registrados todos los equipos esto detiene para que no se registren mas
        if len(equipos) == cantidad:
            print("-------------------------------------")
            print("ERROR YA FUERON AGREGADOS TODOS LOS EQUIPOS")
            print("-------------------------------------")
            input("PRESIONE < ENTER > PARA CONTINUAR ")
        else:
            #En caso de no haber registrado todos los equipos deja registrar en este flujo
            a = True
            while a == True:
                codigo = input("\n\n\nCODIGO DEL EQUIPO ")
                if codigo == "C":
                    break
                elif codigo.isupper() and len(codigo) == 3:
                    if validacion(codigo, equipos) == False:
                        a = False
                        while a == False:
                            nombre = input("NOMBRE DEL EQUIPO ")
                            if len(nombre) >= 3 and len(nombre) <= 40 and nombre.isspace() == False and nombre != codigo:
                                a = True
                            #Hace todas las validaciones de datos, tanto que el equipo no este registrado como validar las caracteristcias propias de los datos de los equipos
                                while a == True:
                                    print("-------------------------------------")
                                    print("TORNEOS DE BOLA")
                                    print("REGISTRAR EQUIPOS: AGREGAR EQUIPOS")
                                    print("Código del equipo: ", codigo)
                                    print("Nombre del equipo: ", nombre)
                                    print("-------------------------------------")
                                    #Interfaz de la aplicacion para registar equipos
                                    print("OPCION <C> CANCELAR <A> ACEPTAR")
                                    #Opcionales para que el usuario escoja si se registran los datos ingresados
                                    opcion = input("OPCIÓN ")
                                    if opcion == "A":
                                        codigos = codigos + (codigo, nombre)
                                        equipos.append(codigos)
                                        codigos = ()
                                        a = "h"
                                        break
                                    elif opcion == "C":
                                        print("-------------------------------------")
                                        print("¿ESTA SEGURO DE REALIZAR ESTA ACCIÓN?")
                                        print("-------------------------------------")
                                        print("OPCION <C> CANCELAR <A> ACEPTAR")
                                        opcion = input("OPCION ")
                                        if opcion == "A":
                                            a = "h"
                                            break
                                        elif opcion == "C":
                                            pass
                                    else:
                                        print("-------------------------------------")
                                        print("ERROR: OPCIÓN INVALIDA")
                                        print("-------------------------------------")
                                        input("PRESIONE < ENTER > PARA CONTINUAR ")
                            else:
                                print("-------------------------------------")
                                print("ERROR: NOMBRE DEBER SER IGUAL O MAYOR A TRES CARACTERES Y MENOR O IGUAL A 40 CARACTERES")
                                print("-------------------------------------")
                                input("PRESIONE < ENTER > PARA CONTINUAR ")
                    else:
                        print("-------------------------------------")
                        print("ESTE EQUIPO YA ESTÁ REGISTRADO, NO SE PUEDE AGREGAR")
                        print("-------------------------------------")
                        input("PRESIONE < ENTER > PARA CONTINUAR ")
                else:
                    print("-------------------------------------")
                    print("ERROR: CODIGO DEBER SER DE 3 DIGITOS EN MAYUSCULA")
                    print("-------------------------------------")
                    input("PRESIONE < ENTER > PARA CONTINUAR ")
    else:
        print("-------------------------------------")
        print("ERROR: DEBE REGISTRAR LA CANTIDAD DE EQUIPOS PARTICIPANTES")
        print("-------------------------------------")
        input("PRESIONE < ENTER > PARA CONTINUAR ")
    return equipos
# FUNCION #2 PRINCIPAL
# Entradas:una lista, tupla y numero entero
# Salidas: una lista
# Funcion: Registra los equipos
def registrar_equipos(equipos, codigos, cantidad, calendario_juegos):
    # Menu principal de la funcion principal #2
    opcion = 1
    while opcion >= 0:
        # Imprime las opciones de la segunda opcion
        print("\n\n\nTORNEOS DE BOLA")
        print("REGISTRAR EQUIPOS")
        print("1. AGREGAR EQUIPOS")
        print("2. CONSULTAR EQUIPOS")
        print("3. MODIFICAR EQUIPOS")
        print("4. ELIMINAR EQUIPOS")
        print("0. SALIR")
        try:
            opcion = int(input("OPCIÓN "))
            if opcion == 1:
                #Esta funcion registra los nombres de los equipos a jugar 
                equipos = agregar_equipos(equipos, codigos, cantidad)
            elif opcion == 2:
                #Esta funcion consulta los datos registrados sobre los equipos
                equipos = consultar_codigos(cantidad, equipos)
            elif opcion == 3:
                #Esta funcion modifica el nombre de los equipos registrados 
                equipos = modificar_equipos(equipos, cantidad)
            elif opcion == 4:
                #Esta funcion elimina todos los datos registrados sobre los equipos
                equipos = eliminar_equipos(cantidad, equipos, calendario_juegos)
            elif opcion == 0:
                #Opcion para cerrar la pestana de la funcion #2 y volver a la funcion principal
                break
            else:
                print("-------------------------------------")
                print("OPCIÓN INVALIDA")
                print("-------------------------------------")
                input("PRESIONE < ENTER > PARA CONTINUAR ")
        except:
            print("-------------------------------------")
            print("ERROR: LA OPCIÓN TIENE QUE SER UN NUMERO ENTERO")
            print("-------------------------------------")
            input("PRESIONE < ENTER > PARA CONTINUAR ")
    return equipos
# FUNCIÓN #1 PRINCIPAL
# Entradas: strings, numeros enteros y listas 
# Salidas: una lista
#Funcion: presenta las opciones para configurar el troneo 
def configuracion_del_torneo(nombre, cantidad, clasificados, puntos_ganado, puntos_empate):
    a = False
    # Registrar el nombre del torneo
    while a == False:
        nombre1 = input("\n\n\nIngrese el nombre del torneo ")
        if len(nombre1) >= 10 and len(nombre1) <= 40 and nombre1.isspace() == False:
            a = True
        else:
            a = False
            print("-------------------------------------")
            print("ERROR: EL NOMBRE DEL TORNEO TIENE QUE TENER ENTRE 10 Y 40 CARACTERES")
            print("-------------------------------------")
    #Registra la cantidad de equipos a jugar
    while a == True:
        try:
            cantidad1 = int(
                input("Ingrese la cantidad de equipos participantes "))
            if cantidad1 >= 2 and cantidad1 % 2 == 0:
                a = False
            else:
                a = True
                print("-------------------------------------")
                print("ERROR: LA CANTIDAD DE EQUIPOS TIENE QUE SER ENTERO PAR >= 2")
                print("-------------------------------------")
        except:
            print("-------------------------------------")
            print("ERROR: LA CANTIDAD DE EQUIPOS TIENE QUE SER ENTERO")
            print("-------------------------------------")
    # Registra la cantidad de equipos que clasifican
    while a == False:
        try:
            clasificados1 = int(
                input("Ingrese la cantidad de equipos que clasifican "))
            if clasificados1 >= 1 and clasificados1 < cantidad1:
                a = True
            else:
                a = False
                print("-------------------------------------")
                print(
                    "ERROR: LOS CLASIFICADOS TIENEN QUE SER MENORES A LA CANTIDAD DE EQUIPOS PARTICIPANTES")
                print("-------------------------------------")
        except:
            print("-------------------------------------")
            print("ERROR: LA CANTIDAD DE EQUIPOS TIENE QUE SER ENTERO")
            print("-------------------------------------")
    #Registra la cantidad de puntos ganados por partido ganado
    while a == True:
        try:
            puntos_ganados1 = int(
                input("Ingrese la cantidad de puntos ganados por cada partido ganado "))
            if puntos_ganados1 >= 1:
                a = False
            else:
                a = True
                print("-------------------------------------")
                print("ERROR: LA CANTIDAD DE PUNTOS GANADOS TIENE QUE SER >= 1")
                print("-------------------------------------")
        except:
            print("-------------------------------------")
            print("ERROR: LA CANTIDAD DE EQUIPOS TIENE QUE SER ENTERO")
            print("-------------------------------------")
    #Registra la cantidad de puntos por partido empatado
    while a == False:
        try:
            puntos_empate1 = int(
                input("Ingrese la cantidad de puntos ganados por cada partido empatado "))
            if puntos_empate1 >= 0 and puntos_empate1 < puntos_ganados1:
                a = True
            else:
                a = False
                print("-------------------------------------")
                print(
                    "ERROR: LOS PUNTOS DE EMPATE TIENEN QUE SER MENORES A LA CANTIDAD De PUNTOS POR PARTIDO GANADO")
                print("-------------------------------------")
        except:
            print("-------------------------------------")
            print("ERROR: LA CANTIDAD DE EQUIPOS TIENE QUE SER ENTERO")
            print("-------------------------------------")
    # Presenta todos los parametros a registrar 
    while a == True:
        print("-------------------------------------")
        print("TORNEOS DE BOLA")
        print("CONFIGURACIÓN DEL TORNEO")
        print("Nombre del torneo: ", nombre1)
        print("Cantidad de equipos participantes: ", cantidad1)
        print("Cantidad de equipos que clasifican directamente: ", clasificados1)
        print("Puntos ganados por cada partido ganado: ", puntos_ganados1)
        print("Puntos ganados por cada partido empatado: ", puntos_empate1)
    #Opcionales, aca se puede decidir si se agrega o no la informacion registrada 
        print("-------------------------------------")
        opcion = input("OPCION <C> CANCELAR <A> ACEPTAR ")
        if opcion == "A":
            nombre = nombre1
            cantidad = cantidad1
            clasificados = clasificados1
            puntos_ganado = puntos_ganados1
            puntos_empate = puntos_empate1
            a = False
            return (nombre, cantidad, clasificados, puntos_ganado, puntos_empate)
        elif opcion == "C":
            print("-------------------------------------")
            print("¿ESTA SEGURO QUE QUIERE CANCELAR?")
            print("-------------------------------------")
            opcion = input("OPCION <C> CANCELAR <A> ACEPTAR")
            if opcion == "A":
                a = False
                return (nombre, cantidad, clasificados, puntos_ganado, puntos_empate)
            elif opcion == "C":
                a = True
            else:
                pass
        else:
            pass
# FUNCIÓN PRINCIPAL
# Entradas: ninguna
# Salidas: ninguna
#Funcion: presenta las opciones para hacer el torneo
def torneo_de_bola():
#Variables que seran pasadas a otras funciones para ser usadas
    opcion = 1
    nombre = ""
    cantidad = 0
    clasificados = 0
    puntos_ganado = 0
    puntos_empate = 0
    equipos = []
    codigos = ()
    calendario_juegos = []
    resultados = []
    goleadores = []
#Menu principal de la apalicacion principal
    while opcion >= 0:
        print("\n\n\nTORNEOS DE BOLA")
        print("1. Configuracion del Torneo")
        print("2. Registrar equipos")
        print("3. Crear y consultar el calendario de juegos")
        print("4. Registrar los resultados de cada fecha")
        print("5. Tabla de posiciones")
        print("6. Tabla de goleadores")
        print("7. Ayuda")
        print("8. Acerca de")
        print("0. Salir")
#Condicionales para entrar a otras aplicaciones de la aplicacion principal
        try:
            opcion = int(input("OPCIÓN "))
            if opcion == 1:
                #Opcion para registar los parametros de la funcion
                if equipos:
                    # Valida que la lista de equipos ya se haya llenado
                    print("-------------------------------------")
                    print("ERROR LOS EQUIPOS YA HAN SIDO REGISTRADOS")
                    print("-------------------------------------")
                    input("DAR < ENTER > PARA CONTINUAR")
                else:
                    x = configuracion_del_torneo(nombre, cantidad, clasificados, puntos_ganado, puntos_empate)
                    nombre = x[0]
                    cantidad = x[1]
                    clasificados = x[2]
                    puntos_ganado = x[3]
                    puntos_empate = x[4]
            elif opcion == 2:
                #Opcion para registar los equipos de los partidos a jugar
                equipos = registrar_equipos(equipos, codigos, cantidad, calendario_juegos)
            elif opcion == 3:
                #Opcion para crear los encuentros entre los equipos
                calendario_juegos = consultar_calendario(nombre, equipos, cantidad, calendario_juegos)
            elif opcion == 4:
                #Opcion para registrar los parametros de los juegos a jugar 
                a = registrar_resultados(calendario_juegos,resultados,goleadores)
                goleadores = a[0]
                resultados = a[1]
            elif opcion == 5:
                tabla_posiciones(nombre,clasificados,puntos_ganado,puntos_empate,equipos,calendario_juegos,resultados)
            elif opcion == 6:
                tabla_goleadores(equipos,calendario_juegos,resultados,goleadores,nombre)
            elif opcion == 7:
                ayuda()
            elif opcion == 8:
                acerca_de()
            elif opcion == 0:
                print("-------------------------------------")
                print("         CERRANDO APLICACIÓN        ")
                print("-------------------------------------")
                break
            else:
                print("OPCIÓN INVALIDA")
                input("DAR < ENTER > PARA CONTINUAR")
        except:
            print("-------------------------------------")
            print("ERROR: LA OPCIÓN TIENE QUE SER UN NUMERO ENTERO")
            print("-------------------------------------")
            input("DAR < ENTER > PARA CONTINUAR")
torneo_de_bola()