from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calcular_imc():
    resultado = None
    
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            altura_cm = float(request.form['altura'])
            altura_m = altura_cm / 100

            if peso > 0 and altura_m > 0:
                imc = peso / (altura_m ** 2)
                imc_redondeado = round(imc, 1)

                if imc_redondeado < 18.5:
                    clasificacion = "Bajo peso"
                elif 18.5 <= imc_redondeado < 25:
                    clasificacion = "Peso normal (Saludable)"
                elif 25 <= imc_redondeado < 30:
                    clasificacion = "Sobrepeso"
                else:
                    clasificacion = "Obesidad"

                resultado = f"Tu IMC es {imc_redondeado} ({clasificacion})."
            else:
                resultado = "Por favor, introduce valores mayores a cero."
                
        except ValueError:
            resultado = "Por favor, introduce valores numéricos válidos."

    return render_template('calculadora.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)