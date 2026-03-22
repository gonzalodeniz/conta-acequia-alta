from wsgiref.simple_server import make_server

from conta_acequia_alta.web import create_app


def main() -> None:
    app = create_app()
    with make_server("127.0.0.1", 8000, app) as httpd:
        print("Aplicacion disponible en http://127.0.0.1:8000")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
