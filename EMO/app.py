from flask import Flask, render_template, request, send_from_directory
import pandas as pd
import os
from werkzeug.utils import secure_filename
from EMOwithSnow import generate_player_stat_plot

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

df = None  # 用來存 CSV 資料（全域）

@app.route("/", methods=["GET", "POST"])
def index():
    global df
    image_url = None
    error = None
    success = None
    player_name = ""

    # 上傳 CSV 處理
    if 'csv_file' in request.files:
        file = request.files['csv_file']
        if file.filename.endswith('.csv'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            file.save(filepath)
            try:
                df = pd.read_csv(filepath)
                success = "CSV 檔案上傳成功！現在可以查球員了"
            except Exception as e:
                error = f"CSV 解析錯誤：{str(e)}"
        else:
            error = "請上傳 .csv 檔案"

    # 查球員圖表處理
    if request.form.get("player_name") and df is not None:
        player_name = request.form.get("player_name")
        try:
            image_path = generate_player_stat_plot(player_name, df)
            image_url = "/" + image_path.replace("\\", "/")
        except Exception as e:
            error = str(e)

    return render_template("index.html", image_url=image_url, error=error, success=success, player_name=player_name)

@app.route("/static/playerstats/<filename>")
def player_image(filename):
    return send_from_directory("static/playerstats", filename)

if __name__ == "__main__":
    app.run(debug=True)
