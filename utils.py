import random
from machine import Pin
from time import sleep


def randint(min=0, max=100):
    """Gera um número inteiro aleatório entre min e max (inclusivo)"""
    return min + random.getrandbits(30) % (max - min + 1)


def button_clicked(pin):
    """Detecta um clique com debounce em um pino configurado como pull-up
    Retorna True se o botão foi pressionado e solto (um clique completo)"""
    if not pin.value():  # Botão pressionado (ativo baixo)
        sleep(0.05)  # Debounce
        if not pin.value():  # Ainda pressionado após debounce
            while not pin.value():  # Espera soltar
                sleep(0.01)
            return True
    return False


buzzer = Pin(16, Pin.OUT)


def buzz(freq=400, time=0.05):
    """Faz som de buzz. Quando maior a frequência, mais agudo o som"""
    for i in range(time * freq):
        buzzer.value(0)
        sleep(1 / (2 * freq))
        buzzer.value(1)
        sleep(1 / (2 * freq))
        sleep(1 / (2 * freq))
