from flask import Flask, render_template, request
app = Flask(__name__)


def texto_a_binario(texto):
    binario = ' '.join(format(ord(char), '08b') for char in texto)
    return binario


def binario_a_texto(binario):
    texto = ''.join(chr(int(binario[i:i+8], 2))
                    for i in range(0, len(binario), 8))
    return texto


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/texto_a_binario', methods=['POST'])
def convertir_texto_a_binario():
    texto = request.form['texto']
    resultado_texto = texto_a_binario(texto)
    return render_template('index.html', resultado_texto=resultado_texto)


@app.route('/binario_a_texto', methods=['POST'])
def convertir_binario_a_texto():
    binario = request.form['binario'].replace(
        " ", "")  # Eliminar espacios en blanco
    resultado_binario = binario_a_texto(binario)
    return render_template('index.html', resultado_binario=resultado_binario)


if __name__ == '__main__':
    app.run(debug=True)
