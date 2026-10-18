from app import create_app

app = create_app()

print("Ruta de la aplicación:", app.root_path)
print("Carpetas de plantillas:", app.jinja_loader.searchpath)

if __name__ == "__main__":
    app.run(debug=True)