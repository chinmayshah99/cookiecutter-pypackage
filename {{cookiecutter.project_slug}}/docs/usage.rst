=====
Usage
=====

💬 You can use the which program to check which {{cookiecutter.project_slug}} program is available (if any)
which {{cookiecutter.project_slug}}

💬 You get the one from your environment
/home/rick/.cache/pypoetry/virtualenvs/{{cookiecutter.project_slug}}-w31dJa0b-py3.6/bin/{{cookiecutter.project_slug}}

💬 Try it

.. code-block:: console

    {{cookiecutter.project_slug}}


    💬 You get all the standard help
    Usage: {{cookiecutter.project_slug}} [OPTIONS] COMMAND [ARGS]...

    Awesome Portal Gun

    Options:
    --install-completion  Install completion for the current shell.
    --show-completion     Show completion for the current shell, to copy it or customize the installation.

    --help                Show this message and exit.

    Commands:
    hello   Load the portal gun
    goodbye  Shoot the portal gun


Build the packge
----------------

.. code-block:: console

    poetry build

    Building {{cookiecutter.project_slug}} (0.1.0)
    - Building sdist
    - Built {{cookiecutter.project_slug}}-0.1.0.tar.gz

    - Building wheel
    - Built {{cookiecutter.project_slug}}-0.1.0-py3-none-any.whl


{{cookiecutter.project_slug}} hello chinmay

💬 It works 🎉
Hello chinmay
