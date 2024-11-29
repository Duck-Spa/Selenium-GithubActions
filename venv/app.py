from flask import Flask, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        first_number = int(request.form.get("first_number"))
        second_number = int(request.form.get("second_number"))
        # Si els camps estan buits, torna un missatge per evitar errors
        if not first_number or not second_number:
            return "Els camps no poden estar buits!."
        return f"El resultat de {first_number} + {second_number} es {first_number + second_number}"
    
    # Aquesta resposta s'envia si la petició no és POST
    return '''
    <form method="post">
        Primer Numero: <input type="number" name="first_number"><br>
        Segon Numero: <input type="number" name="second_number"><br>
        <input type="submit" value="Enviar">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
    if __name__ == "__main__":
        app.run(debug=True)