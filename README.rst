=================
birthday playlist
=================


.. image:: https://img.shields.io/pypi/v/birthday_playlist.svg
        :target: https://pypi.python.org/pypi/birthday_playlist

.. image:: https://img.shields.io/travis/briggySmalls/birthday_playlist.svg
        :target: https://travis-ci.com/briggySmalls/birthday_playlist

.. image:: https://readthedocs.org/projects/birthday-playlist/badge/?version=latest
        :target: https://birthday-playlist.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

Project for creating a birthday playlist from a list of URLs

* Free software: MIT

Installation
------------

- Clone the source
- Install poetry_
- Install dependencies: `poetry install`

poetry_: https://python-poetry.org/

Usage
-----

- Log in to your Spotify account and spotify_developer_`create an application`
- Copy the `.env.example` file to `.env` and supply the information obtained in the previous step
- Activate the poetry shell `poetry shell`
- Execute the tool:

.. code-block:: bash
    birthday_playlist --help

spotify_developer_: https://developer.spotify.com/dashboard/applications

Credits
-------

This package was created with Cookiecutter_ and the `briggysmalls/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`briggysmalls/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
