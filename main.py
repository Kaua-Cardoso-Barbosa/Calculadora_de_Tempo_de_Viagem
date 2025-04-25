from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/viagem', methods=['POST'])
def viagem():
    try:
        distancia = float(request.form['distancia'])
        velocidade = float(request.form['velocidade'])
        total = round((distancia/velocidade),2)
        tempo_s = int(total * 3600)
        horas = int(tempo_s / 3600)
        tempo_s = int(tempo_s % 3600)
        minutos = int(tempo_s / 60)
        return render_template('index.html',horas=horas , minutos=minutos)
    except Exception as e:
        total = f'Ocorreu um erro inesperado {e}'
        return render_template('index.html',horas=horas, minutos=minutos)

if __name__=='__main__' :
    app.run(debug=True)
