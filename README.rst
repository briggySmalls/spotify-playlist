=================
birthday playlist
=================

.. image:: https://img.shields.io/travis/briggySmalls/birthday_playlist.svg
        :target: https://travis-ci.com/briggySmalls/birthday_playlist

Project for creating a birthday playlist from a list of URLs

* Free software: MIT

Installation
------------

- Clone the source
- Install poetry_
- Install dependencies: `poetry install`

.. _poetry: https://python-poetry.org/

Usage
-----

- Log in to your Spotify account and spotify_developer_`create an application`
- Copy the :code:`.env.example` file to :code:`.env` and supply the information obtained in the previous step
- Activate the poetry shell `poetry shell`
- Execute the tool:

.. code-block:: bash
    birthday_playlist --help

.. _spotify_developer: https://developer.spotify.com/dashboard/applications

Credits
-------

This package was created with Cookiecutter_ and the `briggysmalls/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`briggysmalls/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
