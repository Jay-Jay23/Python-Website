from website._init_ import create_app


app = create_app()

if __name__ == '_main_':
    app.run(host="0.0.0.0", port=8000, debug=True)
