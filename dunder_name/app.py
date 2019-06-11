def print_hello():
    print("Hello from app.")

print(__name__)

if __name__ == '__main__':      # zapobiega automatycznemu wykonywaniu w innych plikach, ktore importuja app.py
    print_hello()
