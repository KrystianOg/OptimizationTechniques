#Klasa przedstawiajaca sygnal AMI
class Sygnal:
    def __init__(self,signal):      #konstruktor klasy Sygnal
        self.signal = list(signal)  #postac zero-jedynkowa
        self.voltage = ['Z']*len(signal) #na poczatku sygnal jest wypelniony zerami - reprezentacja napieciowa
        counter = 0
        lastvoltage = 'Z'       #zmienna opisujaca ostatnia zmiane napiecia 
        for i in self.signal:
            if i == 1 and counter == 0: #poczatek sygnalu
                self.voltage[counter] = 'H'
                lastvoltage = 'H'
            elif i == 1 and lastvoltage == 'H':
                self.voltage[counter] = 'L'
                lastvoltage = 'L'
            elif i == 1 and lastvoltage =='L':
                self.voltage[counter] = 'H'
                lastvoltage = 'H'
            counter +=1
    