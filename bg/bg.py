from flask import Flask, render_template, request, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    if "image" not in request.files:
        return "No file uploaded"

    file = request.files["image"]
    input_data = file.read()
    
    output_data = remove(input_data)
    
    return send_file(
        io.BytesIO(output_data),
        mimetype="image/png",
        as_attachment=True,
        download_name="output.png"
    )

if __name__ == "__main__":
    app.run(debug=True)

