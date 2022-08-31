.. solarmon documentation master file, original created by
   sphinx-quickstart on Thu Aug 11 21:16:56 2022.

solarmon documentation
======================

|SolarEdge logo|

Python scripts using the `SolarEdge`_ Cloud-Based Monitoring Platform API.
Documentation for the SolarEdge API is available `here`_.

.. |SolarEdge logo| image:: ../images/SolarEdge_logo.png
   :alt: SolarEdge logo
.. _SolarEdge: https://www.solaredge.com/
.. _here: https://www.solaredge.com/sites/default/files/se_monitoring_api.pdf

Python virtual environment creation
===================================
To create a Python virtual environment containing packages required to run
the Python scripts and build this documentation::

   python3 -m venv solarmon_venv
   source solarmon_venv/bin/activate
   pip install -U pip
   pip install -U pylint -U plac -U pyyaml -U pandas -U sphinx -U sphinx_rtd_theme


.. toctree::
   :maxdepth: 2
   :caption: Scripts:

   energy.rst
   stats.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
