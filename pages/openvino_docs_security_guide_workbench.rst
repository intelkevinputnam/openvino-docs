.. index:: pair: page; Deep Learning Workbench Security
.. _doxid-openvino_docs_security_guide_workbench:


Deep Learning Workbench Security
================================

:target:`doxid-openvino_docs_security_guide_workbench_1md_openvino_docs_security_guide_workbench` Deep Learning Workbench (DL Workbench) is a web application running within a Docker\* container.

Run DL Workbench
~~~~~~~~~~~~~~~~

Unless necessary, limit the connections to the DL Workbench to ``localhost`` (127.0.0.1), so that it is only accessible from the machine the Docker container is built on.

When using ``docker run`` to start the DL Workbench from Docker Hub, limit connections for the host IP 127.0.0.1. For example, limit the connections for the host IP to the port ``5665`` with the ``-p 127.0.0.1:5665:5665`` command . Refer to `Container networking <https://docs.docker.com/config/containers/container-networking/#published-ports>`__ for details.

Authentication Security
~~~~~~~~~~~~~~~~~~~~~~~

DL Workbench uses authentication tokens to access the application. The script starting the DL Workbench creates an authentication token each time the DL Workbench starts. Anyone who has the authentication token can use the DL Workbench.

When you finish working with the DL Workbench, log out to prevent the use of the DL Workbench from the same browser session without authentication.

To invalidate the authentication token completely, restart the DL Workbench.

Use TLS to Protect Communications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure Transport Layer Security (TLS) to keep the authentication token encrypted.

