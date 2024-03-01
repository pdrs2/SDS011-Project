import serial
import csv
import datetime 
import time


serial_port = '/dev/ttyACM0'
baud_rate = 9600

# Configurar o arquivo CSV
csv_file_path = 'dados.csv'

# Abrir a porta serial
ser = serial.Serial(serial_port, baud_rate)


def read_data():
    dados_do_sensor = ser.readline().decode('utf-8').strip()

    return dados_do_sensor.split(",")



nome_arquivo = "dados_do_sensor.csv"

# Abrir o arquivo para escrita
with open(nome_arquivo, "w") as arquivo:
    # Escrever o cabeçalho do arquivo (opcional, se for um novo arquivo)
    arquivo.write("Timestamp,P2.5,P10\n")

    # Loop para leitura contínua dos dados do sensor
    while True:
        # Obter o timestamp atual
        timestamp_atual = datetime.datetime.now().timestamp()
        data_hora_legivel = datetime.datetime.fromtimestamp(timestamp_atual).strftime('%Y-%m-%d %H:%M:%S')

        # Ler os dados do sensor
        data = read_data()

        # Extrair os valores separados dos dados do sensor
        dado1, dado2 = data

        # Escrever o timestamp e os dados do sensor no arquivo
        arquivo.write(f"{data_hora_legivel},{dado1},{dado2}\n")
        arquivo.flush()  

        # Imprimir os dados (opcional)
        print(f"Timestamp: {data_hora_legivel}, P2.5: {dado1}, P10: {dado2}")
        time.sleep(1)

