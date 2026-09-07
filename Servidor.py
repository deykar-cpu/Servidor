from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/estado/<imei>')
def estado(imei):
    print("Dispositivo:", imei)
    return jsonify({
        "estado": "pagado",
        "mensaje": "Todo al dia"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
