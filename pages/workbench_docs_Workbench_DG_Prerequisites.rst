.. index:: pair: page; Prerequisites
.. _doxid-workbench_docs__workbench__d_g__prerequisites:


Prerequisites
=============

:target:`doxid-workbench_docs__workbench__d_g__prerequisites_1md_openvino_workbench_docs_workbench_dg_prerequisites` Follow these steps before running DL Workbench:

#. Make sure you have met the `recommended requirements <#recommended>`__.

#. Configure `Docker <https://docs.docker.com/get-docker/>`__ on your machine.

#. Optional. `Set proxy <#proxy>`__ if you are behind a firewall.

#. Optional. Install Python 3.6 or higher if you want to run the DL Workbench with Python Starter.

.. _recommended:

Recommended Requirements
~~~~~~~~~~~~~~~~~~~~~~~~

Use these requirements to make sure all features are available.

.. list-table::
    :header-rows: 1

    * - Prerequisite
      - Linux\*
      - Windows\*
      - macOS\*
    * - Operating system
      - Ubuntu\* 18.04
      - Windows\* 10
      - macOS\* 10.15 Catalina
    * - Available RAM space
      - 8 GB\*\*
      - 8 GB\*\*
      - 8 GB\*\*
    * - Available storage space
      - 10 GB + space for imported artifacts
      - 10 GB + space for imported artifacts
      - 10 GB + space for imported artifacts
    * - Docker\*
      - Docker CE 18.06.1
      - Docker Desktop 2.3.0.3
      - Docker CE 18.06.1
    * - Browser\*
      - Google Chrome\* 88
      - Google Chrome\* 88
      - Google Chrome\* 88

\*\* You need more space if you optimize or measure accuracy of computationally expensive models, such as mask_rcnn_inception_v2_coco or faster-rcnn-resnet101-coco-sparse-60-0001.

.. note:: Windows\*, Linux\* and MacOS\* support CPU targets. GPU, Intel® Neural Compute Stick 2 and Intel® Vision Accelerator Design with Intel® Movidius™ VPUs are supported only for Linux\*.

.. _proxy:

Set Proxy
~~~~~~~~~

If you are behind a firewall, Docker Desktop allows you to configure HTTP/HTTPS Proxy Settings, which are then automatically passed to Docker. If you `specify proxy settings <https://docs.docker.com/network/proxy>`__, Docker will use them when pulling images.

However, your proxy settings will not be automatically passed to the containers you want to start. You must specify your proxy parameters when creating each container if you want to set proxy settings for them. Use the :ref:`installation form <doxid-workbench_docs__workbench__d_g__run__locally>` to specify proxy for containers.

Set proxy for Linux
-------------------

Use `Docker official guide <https://docs.docker.com/network/proxy/>`__ to configure proxy for containers.

Set proxy for macOS and Windows
-------------------------------

#. Open **Docker Desktop**.

#. Go to *Settings*>> *Proxies*>> Select *Manual proxy configuration*. Add your http-proxy to both *Web Server* and *Secure Web Server*.

#. Add your no-proxy to *Bypass for these hosts & domains*.

#. Press *Apply settings*.
   
   .. image:: docker-proxy_1.png

See Also
~~~~~~~~

* :ref:`Next Step: Install DL Workbench <doxid-workbench_docs__workbench__d_g__install>`

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

