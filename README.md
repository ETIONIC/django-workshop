## Iniciar proyecto
1. Tener viertualenv instalado
```sh
> sudo apt install python3.8-venvsource env/bin/activate
```
2. Parado en la carpeta del repo crear el venv
```sh
> python3 -m venv env
```

3. Instalar las dependencias
```sh
> pip install -r requirements.txt
```

4. Correr migraciones
```sh
> python3 manage.py migrate
```

5. Correr el servidor de desarrollo
```sh
> python3 manage.py runserver
```
