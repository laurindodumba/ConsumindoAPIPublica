from flask import Flask, render_template, request
import urllib.request, json

app = Flask(__name__)

frutas = []
registros = []
filmes = []
#Página principal
@app.route('/teste', methods=["GET", "POST"])
def principal():
   
    if request.method == "POST": #Metódo para coletar a listas das frutas que vão ser inseridas na lista.
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("index.html", frutas=frutas)


#Página secundária
@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})
    return render_template("sobre.html", registros=registros)


#Rota para interar com a API
@app.route('/filmes/<propriedade>')
def filmes(propriedade):
    if propriedade == 'populares':
          url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=4a54c25daca978288cd35a9a78ab6519"
    elif propriedade == 'Kids':
          url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=4a54c25daca978288cd35a9a78ab6519"
    elif propriedade == '2010':
          url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=4a54c25daca978288cd35a9a78ab6519"
    elif propriedade == 'Drama':
         url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=4a54c25daca978288cd35a9a78ab6519"
    elif propriedade == 'tom_cruise':
         url = "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=4a54c25daca978288cd35a9a78ab6519"
  
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    jsondata = json.loads(dados)
    return render_template("filmes.html", filmes=jsondata['results'])


if __name__ == "__main__":
    app.run(debug=True)