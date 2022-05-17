.. index:: pair: page; Overview
.. _doxid-openvino_docs_install_guides_overview:


Overview
========

:target:`doxid-openvino_docs_install_guides_overview_1md_openvino_docs_install_guides_installing-openvino-overview` Intel® Distribution of OpenVINO™ toolkit is a comprehensive toolkit for developing applications and solutions based on deep learning tasks, such as: emulation of human vision, automatic speech recognition, natural language processing, recommendation systems, etc. It provides high-performance and rich deployment options, from edge to cloud. Some of its advantages are:

* Enabling CNN-based deep learning inference on the edge.

* Supporting various execution modes across Intel® technologies: Intel® CPU, Intel® Integrated Graphics, Intel® Neural Compute Stick 2, and Intel® Vision Accelerator Design with Intel® Movidius™ VPUs.

* Speeding time-to-market via an easy-to-use library of computer vision functions and pre-optimized kernels.

Installation Options
~~~~~~~~~~~~~~~~~~~~

Since the 2022.1 release, the OpenVINO installation package has been distributed in two parts: OpenVINO Runtime and OpenVINO Development Tools. See the following instructions to choose your installation process.

Decide What to Install
----------------------

If you have already finished your model development and want to deploy your applications on various devices, :ref:`install OpenVINO Runtime <doxid-openvino_docs_install_guides_install_runtime>`, which contains a set of libraries for easy inference integration with your products.

If you want to download models from :ref:`Open Model Zoo <doxid-model_zoo>`, :ref:`convert your own models to OpenVINO IR <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`, or :ref:`optimize and tune pre-trained deep learning models <doxid-openvino_docs_model_optimization_guide>`, :ref:`install OpenVINO Development Tools <doxid-openvino_docs_install_guides_install_dev_tools>`, which provides the following tools:

* Model Optimizer

* Post-Training Optimization Tool

* Benchmark Tool

* Accuracy Checker and Annotation Converter

* Model Downloader and other Open Model Zoo tools

Choose Your Installation Method
-------------------------------

For Python developers, you can :ref:`install OpenVINO from PyPI <doxid-openvino_docs_install_guides_installing_openvino_pip>`, which contains both OpenVINO Runtime and Development Tools, while requiring fewer steps.

For C++ developers, you may choose one of the following installation options for OpenVINO Runtime on your specific operating system:

* Linux: You can install OpenVINO Runtime using an :ref:`Installer <doxid-openvino_docs_install_guides_installing_openvino_linux>`, :ref:`APT <doxid-openvino_docs_install_guides_installing_openvino_apt>`, :ref:`YUM <doxid-openvino_docs_install_guides_installing_openvino_yum>`, :ref:`Anaconda Cloud <doxid-openvino_docs_install_guides_installing_openvino_conda>`, or :ref:`Docker <doxid-openvino_docs_install_guides_installing_openvino_docker_linux>`.

* Windows: You can install OpenVINO Runtime using an :ref:`Installer <doxid-openvino_docs_install_guides_installing_openvino_windows>`, :ref:`Anaconda Cloud <doxid-openvino_docs_install_guides_installing_openvino_conda>`, or :ref:`Docker <doxid-openvino_docs_install_guides_installing_openvino_docker_windows>`.

* macOS: You can install OpenVINO Runtime using an :ref:`Installer <doxid-openvino_docs_install_guides_installing_openvino_macos>` or :ref:`Anaconda Cloud <doxid-openvino_docs_install_guides_installing_openvino_conda>`.

* :ref:`Raspbian OS <doxid-openvino_docs_install_guides_installing_openvino_raspbian>`.

.. note:: With the introduction of the 2022.1 release, the OpenVINO Development Tools can be installed **only** via PyPI. See :ref:`Install OpenVINO Development Tools <doxid-openvino_docs_install_guides_install_dev_tools>` for detailed steps.



Source files are also available in the `OpenVINO toolkit GitHub repository <https://github.com/openvinotoolkit/openvino/>`__, so you can build your own package for the supported platforms, as described in `OpenVINO Build Instructions <https://github.com/openvinotoolkit/openvino/wiki/BuildingCode>`__.

