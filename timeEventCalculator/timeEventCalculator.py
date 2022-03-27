#Calculates the time in which an event will finalize after giving the initial time and the duration of the event in minutes

#inputing the integers
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))


#calculando hora final
horasSumar = round(dura / 60)#cantidad de horas que dura el evento
hourEnd = str((hour + horasSumar)% 24)#calcula la hora final en formato 24 horas

#calculando minutos
minsEnd = str ((dura + mins) % 60)

print("Event will end at " + hourEnd +":" + minsEnd )