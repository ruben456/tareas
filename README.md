# Tareas REST API

Proyecto de django REST framework

# instalación

Crear ambiente virtual

```bash
python -m venv env
```

Activar ambiente virtual

```bash
source env/bin/activate
```

Instalar requerimientos

```bash
pip install -r requeriments.txt --upgrade pip
```

Iniciar sitio

```bash
python manage.py runserver
```

# Usuarios

superuser:  admin/1234
user:       prueba/123456789abc*

# Urls

Swagger: 
http://127.0.0.1:8000/api/swagger/

Login:
http://127.0.0.1:8000/api-auth/login/

Listado Tareas:
http://127.0.0.1:8000/api/tasks/

Listado de tareas por página:
http://127.0.0.1:8000/api/tasks/?page=1

Listado de tareas con búsqueda:
http://127.0.0.1:8000/api/tasks/?search=prueba

Detalle, actualización y eliminación de tareas:
http://127.0.0.1:8000/api/tasks/1/


