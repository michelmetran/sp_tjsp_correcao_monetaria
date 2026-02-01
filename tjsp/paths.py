"""
Pastas do Projeto
"""

from pathlib import Path

module_path = Path(__file__).absolute().parent

data_path = module_path / 'data'
data_path.mkdir(exist_ok=True)

if __name__ == '__main__':
    print(module_path)
