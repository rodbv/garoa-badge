# Experimentos para o Garoa Badge

Coleção de experimentos e scripts para o [Garoa Badge](https://garoa.net.br/wiki/Badge#REV._0). 

Grande parte do código foi inspirada no repositório de [Juliana Karoline](https://github.com/julianaklulo/garoa-badge).

## Sobre o Garoa Badge

O Garoa Badge é um projeto desenvolvido no [Garoa Hacker Clube](https://garoa.net.br/). Para mais informações, visite a [página do projeto](https://garoa.net.br/wiki/Badge#REV._0).

## Experimentos

### 1. Animação DVD Screensaver

Implementação da animação do logo DVD, adaptada para dispositivos com MicroPython e display OLED SH1106. Inclui efeitos sonoros ao atingir as bordas da tela.


#### Requisitos de Hardware
- Placa ESP8266/ESP32
- Display OLED SH1106 (128x64)
- Buzzer (conectado ao GPIO16)
- Conexões:
  - SCL -> GPIO5
  - SDA -> GPIO4
  - RESET -> GPIO16
  - VCC -> 3.3V
  - GND -> GND

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/rodbv/garoa-badge.git
```

2. Instale as ferramentas necessárias:
   - Firmware MicroPython em sua placa
   - [Thonny IDE](https://thonny.org/) (recomendado para iniciantes)
   - Ou outras ferramentas como ampy, mpexplore

3. Para copiar os arquivos usando Thonny:
   - Instale e abra o Thonny
   - No menu View, ative "Files"
   - Em Tools > Options > Interpreter, selecione "MicroPython (ESP32)"
   - Selecione a porta serial correta
   - No painel de arquivos à direita, você verá os arquivos da placa
   - Arraste os arquivos do seu computador para a placa ou use o botão "Upload"
   
   Para um guia detalhado com screenshots, veja [Getting Started with Thonny MicroPython](https://randomnerdtutorials.com/getting-started-thonny-micropython-python-ide-esp32-esp8266/)

### Para o experimento DVD Screensaver:
- `main.py`
- `dvd.py`
- `sh1106.py`
- `utils.py`

## Uso

### DVD Screensaver
A animação iniciará automaticamente quando a placa for ligada, pois é acionada pelo `main.py`. O texto "((DVD))" quicará pela tela, com um bipe sempre que atingir uma borda.

Para personalizar o texto exibido, modifique o parâmetro em `run`:

```python
run("OLÁ!")  # Altere para o texto desejado
```

## Estrutura de Arquivos

### DVD Screensaver
- `main.py`: Ponto de entrada que executa a animação DVD
- `dvd.py`: Lógica principal da animação e controle do display/som
- `sh1106.py`: Driver do display OLED SH1106
- `utils.py`: Funções utilitárias (geração de números aleatórios)

## Licença

O driver SH1106 está sob Licença MIT. Veja o cabeçalho em `sh1106.py` para detalhes.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request.

## Agradecimentos

- Driver SH1106 baseado no trabalho de Radomir Dopieralski, Robert Hammelrath e Tim Weber
- [Garoa Hacker Clube](https://garoa.net.br/) pelo desenvolvimento do Garoa Badge
- Inspirado no clássico screensaver do DVD player