from machine import Pin, PWM
import network
import ubinascii
import machine
import time
import socket
from ssd1306 import SSD1306_I2C
# Configuración de los pines OLED
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)  # GP15 (SCL) y GP14 (SDA)
oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


# Define los pines para controlar los motores
input1_1 = Pin(16, Pin.OUT)
input1_2 = Pin(17, Pin.OUT)

input2_1 = Pin(18, Pin.OUT)
input2_2 = Pin(19, Pin.OUT)

# Define los pines PWM para controlar la velocidad de los motores
pwm_pin1 = Pin(20)  # Pin 18 para control de velocidad del motor 1
pwm1 = PWM(pwm_pin1)
pwm1.freq(1000)  # Frecuencia del PWM (Hz)

pwm_pin2 = Pin(21)  # Pin 19 para control de velocidad del motor 2
pwm2 = PWM(pwm_pin2)
pwm2.freq(1000)  # Frecuencia del PWM (Hz)

def control_motor(input1, input2, pwm, speed, direction):
    pwm.duty_u16(int(65535 * speed/100))  # Establece el ciclo de trabajo del PWM
    if direction == 1:
        input1.on()
        input2.off()
    elif direction == -1:
        input1.off()
        input2.on()
    else:
        input1.off()
        input2.off()
        
def forward(speed1, speed2):
    control_motor(input1_1, input1_2, pwm1, speed1, 1)  # Motor 1 hacia adelante con velocidad speed1
    control_motor(input2_1, input2_2, pwm2, speed2, 1)  # Motor 2 hacia adelante con velocidad speed2

def backward(speed1, speed2):
    control_motor(input1_1, input1_2, pwm1, speed1, -1)  # Motor 1 hacia atras con velocidad speed1
    control_motor(input2_1, input2_2, pwm2, speed2, -1)  # Motor 2 hacia atras con velocidad speed2
    
def left_har(speed1, speed2):
    control_motor(input1_1, input1_2, pwm1, speed1, 1)  # Motor 1 hacia adelante con velocidad speed1
    control_motor(input2_1, input2_2, pwm2, speed2, 0)  # Motor 2 hacia adelante con velocidad speed2

def rigth_har(speed1, speed2):
    control_motor(input1_1, input1_2, pwm1, speed1, 0)  # Motor 1 hacia adelante con velocidad speed1
    control_motor(input2_1, input2_2, pwm2, speed2, 1)  # Motor 2 hacia adelante con velocidad speed2

def lef(speed1, speed2):
    control_motor(input1_1, input1_2, pwm1, speed1, 1)  # Motor 1 hacia adelante con velocidad speed1
    control_motor(input2_1, input2_2, pwm2, speed2, 1)  # Motor 2 hacia adelante con velocidad speed2

def rigt(speed1, speed2):
    control_motor(input1_1, input1_2, pwm1, speed1, 1)  # Motor 1 hacia adelante con velocidad speed1
    control_motor(input2_1, input2_2, pwm2, speed2, 1)  # Motor 2 hacia adelante con velocidad speed2
        
    
def stop():
    control_motor(input1_1, input1_2, pwm1, 0, 0)
    control_motor(input2_1, input2_2, pwm2, 0, 0)

# Set country to avoid possible errors
#rp2.country('DE')

# Configurar la Raspberry Pi Pico W como un punto de acceso WiFi
ap = network.WLAN(network.AP_IF)  # Crea un objeto de punto de acceso
ap.config(essid='MiPuntoDeAcceso', password='MiContraseña')  # Configura SSID y contraseña
ap.active(True)  # Activa el punto de acceso
print('Dirección IP del punto de acceso:', ap.ifconfig()[0])  # Obtiene la dirección IP del punto de acceso

# HTTP server con socket
addr = socket.getaddrinfo(ap.ifconfig()[0], 80)[0][-1]  # Utiliza la IP del punto de acceso
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)
print('Listening on', addr)

# Función para cargar la página HTML
def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()
    return html

# Función para manejar las peticiones HTTP
def handle_http_request(client_socket, request):
    request = str(request)
    motor_forward = request.find('?motor=forward')
    motor_backward = request.find('?motor=backward')
    motor_stop = request.find('?motor=stop')
    left_hard = request.find('?left=hard')
    rigth_hard = request.find('?rigth=hard')
    left = request.find('?left=left')
    rigth = request.find('?rigth=rigth')
    quite = request.find('quite=quite')

    if motor_forward > -1:
        print('Forward')
        forward(40, 40)  # Ejemplo de velocidad diferente para cada motor
            
    if motor_backward > -1:
        print('Backward')
        forward(40, 40)  # Ejemplo de velocidad diferente para cada motor
            
    if motor_stop > -1:
        print('Stop')
        stop()
        
    if left_hard >-1:
        left_har(40,0)
        print('Left hard')
        
    if rigth_hard >-1:
        rigth_har(0,40)
        print('rigth hard')
            
    if left >-1:
        lef(70,55)
        print('Left')
        
    if rigth>-1:
        rigt( 55,70)
        print('rigth')

    if quite > -1:
        print('QUIT')
        client_socket.close()
        s.close()
        ap.active(False)
        print('Bye')
        return True

    response = get_html('web_server_cube.html')
    client_socket.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    client_socket.send(response)
    client_socket.close()
    return False

# Manejar las conexiones entrantes
while True:
    try:
        client_socket, addr = s.accept()
        print('Client connected from', addr)
        request = client_socket.recv(1024)
        if handle_http_request(client_socket, request):
            break
    except OSError as e:
        client_socket.close()
        print('Connection closed')
