![Logo](https://repository-images.githubusercontent.com/253698085/cce90300-78c3-11ea-8b94-604fad2c516d)

<p align="center">
  <img src="https://user-images.githubusercontent.com/29473781/180619084-a56960ab-7efa-4e34-9d33-4e3e581d62ff.png" />
</p>

\*Pre-requisitos 🗒️

Instalar librerías de Python, para ello debemos ejecutar en consola el siguiente comando :

### Comands

$ python pip install requirements.txt

\*Ejecución 💾🖥️🖱️

-   Clonar el repositorio
-   Dentro del proyecto abrir una terminal ejecutar python manage.py runserver
-   Ingresar a la ruta que nos brinda el terminal.

-   La pagina principal Home despliega:
    Barra de navegación que contiene Home, Pokédex, About, Login y Sing Up.

Una vez registrado y logeado se habilitaran otras opciones.

La primera es "Pokémon Uploader", donde podras registrar los Pokémons mediante un Formulario tipo Blog.

La segunda es "My Pokémons", donde podremos ver los Pokémons que agregamos con nuestro nombre de usuario, también podremos ver detalles, editar y borrar los Pokémons.

La tercera es "Edit user", donde podras hacer modificaciones a tus datos de registro.

La cuarta es "Log out": nos permite cerrar sesión de usuario.

-Home: se muestra la pagina principal en ella podremos ver:

Banner de la pagina y los ultimos 3 Pokemons agregados por nuestros usuarios de la web, siempre y cuando hayan Pokemons para mostrar.

-Pokedex: Se muestran todos los Pokémons agregados por nuestros usuarios, ademas nos permite acceder a cada uno de ellos para ver detalles.

-About: una sección donde se despliega información de los desarrolladores del sitio.

-Log in: Redirecciona a la vista donde podras logearte.

-Sing up: Redirecciona a la vista donde podras registrarte.

-   My Pokemons: Esta sección nos permite listar todos los Pokémons creados por el usuario logueado.
    -Ver: Permite ver el Pokémon selecciónado.
    -Editar: Permite editar dicho Pokémon.
    -Eliminar: Permite eliminar dicho Pokémon.

-   Edit User: Está sección nos permite editar información del usuario Email, nombre y apellido.

*   Save: nos permite guardar cambios.
*   Set avatar: nos permite mediante un Formulario seleccionar un avatar para el usuario en formato imagen.
*   Change password: nos permite mediante un Formulario cambiar nuestra contraseña.

```bash
├── db.sqlite3
├── manage.py
├── media
│   └── avatar
│       ├── 004.png
│       ├── 009.png
│       └── pokemon1.png
├── pfpython
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   ├── view.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── settings.py
│   ├── urls.py
│   ├── view.py
│   └── wsgi.py
├── Pokedex
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_avatar_user.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       ├── 0002_alter_avatar_user.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── Pages
│   │   ├── about.html
│   │   ├── add_avatar.html
│   │   ├── change_pass.html
│   │   ├── createpokemon.html
│   │   ├── draw_pokemon.html
│   │   ├── edit_pokemon.html
│   │   ├── edit_user.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── my_pokemons.html
│   │   ├── pokemons.html
│   │   └── register.html
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── forms.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── static
│   │   ├── css
│   │   │   ├── bootstrap.min.css
│   │   │   └── jumbotron.css
│   │   ├── images
│   │   │   ├── about.png
│   │   │   ├── coderhouse.jpg
│   │   │   ├── coderhouse_logo.webp
│   │   │   ├── create.png
│   │   │   ├── edit.png
│   │   │   ├── fondo.jpg
│   │   │   ├── fondo.png
│   │   │   ├── header-background-sticky.png
│   │   │   ├── latest.png
│   │   │   ├── login.png
│   │   │   ├── mypokemons.png
│   │   │   ├── navigation-background-left.png
│   │   │   ├── navigation-background-right.png
│   │   │   ├── Omar.jpg
│   │   │   ├── Pablo.jpg
│   │   │   ├── pokeball.png
│   │   │   ├── pokedex2.png
│   │   │   ├── pokedex.webp
│   │   │   ├── pokemon.png
│   │   │   ├── Python.png
│   │   │   ├── register.png
│   │   │   └── uploader.png
│   │   └── js
│   │       └── bootstrap.min.js
│   ├── Static
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── README.md
```

### Autores ✒️
[<img src="https://avatars.githubusercontent.com/u/111648308?v=4" width=115><br><sub>Herrera Omar</sub>](https://github.com/OHerrera1991)|[<img src="https://avatars.githubusercontent.com/u/86387410?v=4" width=115><br><sub>Pablo González</sub>](https://github.com/PabloGonzalez315)| :---: | :---: |



\*Version 1.0

![GITHUB](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![GIT](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![WINDOWS](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![LINUX](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![PYTHON](https://img.shields.io/badge/Python-0078D4?style=for-the-badge&logo=Python&logoColor=yellow)
![DJANGO](https://img.shields.io/badge/Django-100000?style=for-the-badge&logo=Django&logoColor=success)
