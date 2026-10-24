# Festival Vallenato - Sistema de Votaciones

Proyecto desarrollado con Python, Django y MySQL.

## Instalación

### Crear entorno virtual

```powershell
python -m venv env_festival
.\env_festival\Scripts\Activate.ps1
```

### Instalar dependencias

```powershell
pip install django mysqlclient
```

### Crear la base de datos

```sql
CREATE DATABASE festival_db;
```

### Ejecutar migraciones

```powershell
python manage.py migrate
```

### Iniciar el servidor

```powershell
python manage.py runserver
```


## Tecnologías

- Python
- Django
- MySQL
- Bootstrap
- HTML
- CSS
