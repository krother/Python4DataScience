.. SPDX-FileCopyrightText: 2021 Veit Schiele
..
.. SPDX-License-Identifier: BSD-3-Clause

Read, persist and provide data
==============================

You can get an overview of public repositories with research data e.g. in
:doc:`opendata`.

In addition to specific Python libraries for accessing
:doc:`/data-processing/remote-file-systems` and :doc:`/data-processing/geodata`, we will
introduce you to different :doc:`serialisation formats <serialisation-formats/index>` and
three tools in more detail that make data accessible:

* :doc:`/data-processing/pandas-io`
* :doc:`requests/index`
* :doc:`intake/index`

.. seealso::
    `pandas I/O API <https://pandas.pydata.org/docs/user_guide/io.html>`_
        The pandas I/O API is a set of top level ``reader`` functions that
        return a  pandas object. In most cases corresponding ``write`` methods
        are also available.
    `Scrapy <https://scrapy.org/>`_
        Framework for extracting data from websites as JSON, CSV or XML files.
    `Pattern <https://github.com/clips/pattern>`_
        Python module for data mining, natural language processing, ML and
        network analysis.
    `Web Scraping Reference <https://blog.hartleybrody.com/web-scraping-cheat-sheet/#javascript-heavy-websites>`_
        Overview of web scraping with Python.


We introduce :doc:`postgresql/index`, :doc:`postgresql/sqlalchemy` and
:doc:`postgresql/postgis/index` for storing relational data, Python objects and
geodata.

For the storage of other data types we introduce you to different
:doc:`NoSQL databases and concepts <nosql/index>`.

Next, we will show you how to provide the data via an :doc:`apis/index`.

With :doc:`DVC <../productive/dvc/index>` we present you a tool that allows data
provenance, i.e. the traceability of the origin of the data and the way they are
created.

Finally in the next chapter you will learn some good practices and helpful
Python packages to :doc:`clean up and validate data <../clean-prep/index>`.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    opendata
    pandas-io
    serialisation-formats/index
    intake/index
    requests/index
    remote-file-systems
    geodata
    postgresql/index
    nosql/index
    apis/index
    glossary
