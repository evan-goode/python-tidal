tidalapi
========

.. image:: https://badge.fury.io/py/tidalapi4mopidy.png
    :target: http://badge.fury.io/py/tidalapi4mopidy


Unofficial Python API for TIDAL music streaming service used by Mopidy-Tidal plugin.


Installation
------------

Install from `PyPI <https://pypi.python.org/pypi/tidalapi4mopidy/>`_ using ``pip``:

.. code-block:: bash

    $ pip install tidalapi4mopidy



Example usage
-------------

.. code-block:: python

    import tidalapi4mopidy

    session = tidalapi4mopidy.Session()
    session.login('username', 'password')
    tracks = session.get_album_tracks(album_id=16909093)
    for track in tracks:
        print(track.name)
