"""Application entry point."""

from personality_bfi import create_app


app = create_app()

if __name__ == "__main__":
    app.run()
