"""
Atualiza dados
"""

from datetime import datetime

from paths import data_path

import tjsp


# Only to change
date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
with open(data_path / 'date.txt', 'w') as f:
    f.write(f'Data: {date_time}')

# Create Dataframe
tj = tjsp.TJSP()

# Salva
tj.save_pdf(filepath=data_path / 'tabela_debitos_judiciais.pdf')
tj.save_csv(filepath=data_path / 'tabela_debitos_judiciais.csv')
