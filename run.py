import subprocess, sys


def run():

    options = ["runserver", "migrate", "build migration" , "build static", "build app", "shell", "create app", "run with gunicorn"]
 

    answer = input(f"Reply (with {', '.join(options)}): ")

     
    if answer.__contains__("runserver"):
        subprocess.run([sys.executable, 'manage.py', 'runserver', 'localhost:3000'])

    elif answer.__contains__("migrate"):
        subprocess.run([sys.executable, 'manage.py', 'migrate'])

    elif answer.__contains__("build migration"):
        subprocess.run([sys.executable, 'manage.py', 'makemigrations'])

    elif answer.__contains__("build_static"):
        subprocess.run([sys.executable, 'manage.py', 'collectstatic'])  

    elif answer.__contains__("build app"):
        app_name = input("Enter the name of the app: ")
        subprocess.run([sys.executable, 'manage.py', 'startapp', app_name])   

    elif answer.__contains__("shell"):
        subprocess.run([sys.executable, 'manage.py', 'shell'])

    elif answer.__contains__("run with gunicorn"):
        subprocess.run([sys.executable, '-m', 'gunicorn', '-b 0.0.0.0:3000', 'textanalyzer.wsgi'])

    else:
        print('PLEASE REPLY WITH THESE KEYWORDS [ {0} ]'.format(', '.join(options))) 

if __name__ == "__main__":
    run()