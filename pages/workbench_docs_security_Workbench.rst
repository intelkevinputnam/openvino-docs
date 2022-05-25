.. index:: pair: page; Deep Learning Workbench Security
.. _doxid-workbench_docs_security__workbench:


Deep Learning Workbench Security
================================

:target:`doxid-workbench_docs_security__workbench_1md_openvino_workbench_docs_workbench_dg_security`





.. toctree::
   :maxdepth: 1
   :hidden:

   workbench_docs_Workbench_DG_Authentication
   workbench_docs_Workbench_DG_Configure_TLS

Deep Learning Workbench (DL Workbench) is a web application running within a Docker\* container.

Run DL Workbench
~~~~~~~~~~~~~~~~

Unless necessary, limit the connections to the DL Workbench to ``localhost`` (127.0.0.1), so that it is only accessible from the machine the Docker container is built on:

* When using ``docker run`` to :ref:`start the DL Workbench from Docker Hub <doxid-workbench_docs__workbench__d_g__run__locally>`, limit connections for the host IP 127.0.0.1. For example, limit the connections for the host IP to the port ``5665`` with the ``-p 127.0.0.1:5665:5665`` command . Refer to `Container networking <https://docs.docker.com/config/containers container-networking/#published-ports>`__ for details.

Authentication Security
~~~~~~~~~~~~~~~~~~~~~~~

DL Workbench uses :ref:`authentication tokens <doxid-workbench_docs__workbench__d_g__authentication>` to access the application. The script starting the DL Workbench creates an authentication token each time the DL Workbench starts. Anyone who has the authentication token can use the DL Workbench.

When you finish working with the DL Workbench, log out to prevent the use of the DL Workbench from the same browser session without authentication.

To invalidate the authentication token completely, :ref:`restart the DL Workbench <doxid-workbench_docs__workbench__d_g__docker__container>`.

Use TLS to Protect Communications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`Configure Transport Layer Security (TLS) <doxid-workbench_docs__workbench__d_g__configure__t_l_s>` to keep the authentication token encrypted.

See Also
~~~~~~~~

* :ref:`Configure Transport Layer Security (TLS) <doxid-workbench_docs__workbench__d_g__configure__t_l_s>`

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

