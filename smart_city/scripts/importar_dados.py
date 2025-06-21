import os
import django
import pandas as pd

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_city.settings')
django.setup()

from sensores.models import Sensor, Ambiente, Historico

def importar_arquivo(smart_city, tipo_sensor):
    df = pd.read_excel(smart_city, engine='openpyxl')

    for index, row in df.iterrows():
        sensor_id = row['sensor']
        ambiente_id = row['ambiente']
        valor = row['valor']
        timestamp = row['timestamp']

        sensor, _ = Sensor.objects.get_or_create(
            sensor=sensor_id,
            defaults={
                'mac_address': '00:00:00:00',
                'unidade_med': tipo_sensor,
                'latitude': 0.0,
                'longitude': 0.0,
                'status': True,
            }
        )

        ambiente, _ = Ambiente.objects.get_or_create(
            sig=ambiente_id,
            defaults={
                'descricao': f'Ambiente {ambiente_id}',
                'ni': 'NI',
                'responsavel': 'Responsável Padrão'
            }
        )

        Historico.objects.create(
            sensor=sensor,
            ambiente=ambiente,
            valor=valor,
            timestamp=timestamp
        )

    print(f"Importação de '{nome_arquivo}' concluída.")

if __name__ == '__main__':
    arquivos = [
        ('temperatura.xlsx', '°C'),
        ('umidade.xlsx', '%'),
        ('luminosidade.xlsx', 'lux'),
        ('contador.xlsx', 'num'),
    ]

    for nome_arquivo, tipo_sensor in arquivos:
        caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)
        importar_arquivo(caminho, tipo_sensor)
