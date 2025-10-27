import sys, os
sys.stdout.flush()

from rembg import remove
from PIL import Image
import time
import io

try:
    path = input("Digite o caminho da imagem: ")
    input_image = Image.open(path)
except FileNotFoundError:
    print("Erro: Imagem de entrada não encontrada. Verifique o nome do arquivo.")
    sys.exit(1)
except Exception as e:
    print("Erro ao abrir imagem:", e)
    raise

print("Imagem carregada. Iniciando remoção do fundo (pode demorar na primeira execução)...")
t0 = time.time()
try:
    output = remove(input_image)
except Exception as e:
    print("Erro durante remove():", e)
    raise
t1 = time.time()
print(f"remove() finalizado em {t1 - t0:.1f}s")

# rembg pode retornar bytes ou PIL.Image
if isinstance(output, (bytes, bytearray)):
    output_image = Image.open(io.BytesIO(output)).convert("RGBA")
else:
    output_image = output.convert("RGBA")

# Salva imagem
save_path = path.replace('.jpeg', '-sem-fundo.png')
output_image.save(save_path)
print(f"Imagem salva como '{save_path}'")