#noe her avr tatt fra github noe er fra chatgpt noe er fra egen hånd og noe er fra en nettside https://krython.com/tutorial/python/web-project-full-stack-application/?utm_source=chatgpt.com 
from flask import Flask, redirect, request, render_template
from datetime import datetime, timedelta
from flask import send_file
import mariadb
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def get_db():
    conn = mariadb.connect(
    host="127.0.0.1",
    port=3307,
    user="flaskuser",
    password="flaskpass",
    database="prosjekter"
    )
    return conn

def cleanup_expired_files():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT filename, filepath, uploaded_at FROM files")
    files = cur.fetchall()

    for file in files:
        filename, filepath, uploaded_at = file

        if datetime.now() - uploaded_at > timedelta(days=7):
            if os.path.exists(filepath):
                os.remove(filepath)

            cur.execute("DELETE FROM files WHERE filename=?", (filename,))

    conn.commit()
    conn.close()

# bassissen fikk jeg fra github men jeg endra på det med både min egen hånd og chatgpt 
@app.route("/")
def forside():
    cleanup_expired_files()  
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT filename FROM files")
    filer = cur.fetchall()

    conn.close()

    return render_template("forside.html", filer=filer)

# jeg bygde opp bassisen selv men etter det ikke ville fungererte spurtet jeg chatgpt og den jalp meg 
@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        conn = get_db()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO files (filename, filepath, uploaded_at) VALUES (?, ?, ?)",
            (file.filename, filepath, datetime.now())
)

        conn.commit()
        conn.close()

    return redirect("/")
#samme som over
@app.route("/download/<filename>")
def download(filename):

    conn=get_db()
    cur=conn.cursor()

    cur.execute("SELECT filepath FROM files WHERE filename=?", (filename,))
    result = cur.fetchone()

    conn.close()

    if result: 
        filepath = result[0]
        return send_file(filepath, as_attachment=True)
    
    return "File not found", 
# her prøvde jeg å gjøre noe lingnene til den øvere men det fungerte ikke helt så jeg sjekka på flask dokumentasjonen og fant ut at jeg måtte bruke os biblioteket for å slette filen den delen fungerte men jeg fikk fortsatt error meldinger så jeg spurte chatgpt og den hjalp meg med å fikse det
@app.route("/delete/<filename>",methods=["POST"])
def delete(filename):

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT filepath FROM files WHERE filename=?", (filename,))
    result = cur.fetchone()

    if result: 
        filepath = result[0]
        
        if os.path.exists(filepath):
            os.remove(filepath)

        cur.execute("DELETE FROM files WHERE filename=?", (filename,))
        conn.commit()   
    
    conn.close()        

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)