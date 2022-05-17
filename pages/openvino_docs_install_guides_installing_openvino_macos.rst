.. index:: pair: page; Install and Configure Intel® Distribution of OpenVINO™ toolkit for macOS
.. _doxid-openvino_docs_install_guides_installing_openvino_macos:


Install and Configure Intel® Distribution of OpenVINO™ toolkit for macOS
===========================================================================

:target:`doxid-openvino_docs_install_guides_installing_openvino_macos_1md_openvino_docs_install_guides_installing-openvino-macos`

.. note:: Since the OpenVINO™ 2022.1 release, the following development tools: Model Optimizer, Post-Training Optimization Tool, Model Downloader and other Open Model Zoo tools, Accuracy Checker, and Annotation Converter are not part of the installer. These tools are now only available on `pypi.org <https://pypi.org/project/openvino-dev/>`__.

.. note:: The Intel® Distribution of OpenVINO™ toolkit is supported on macOS version 10.15 with Intel® processor-based machines.

System Requirements
~~~~~~~~~~~~~~~~~~~

.. tab:: Operating Systems

  macOS 10.15

.. tab:: Hardware

  Optimized for these processors:

  * 6th to 12th generation Intel® Core™ processors and Intel® Xeon® processors 
  * 3rd generation Intel® Xeon® Scalable processor (formerly code named Cooper Lake)
  * Intel® Xeon® Scalable processor (formerly Skylake and Cascade Lake)
  * Intel® Neural Compute Stick 2

  .. note::
    The current version of the Intel® Distribution of OpenVINO™ toolkit for macOS supports inference on Intel CPUs and Intel® Neural Compute Stick 2 devices only.

.. tab:: Software Requirements

  * `CMake 3.13 or higher <https://cmake.org/download/>`_ (choose "macOS 10.13 or later"). Add `/Applications/CMake.app/Contents/bin` to path (for default install). 
  * `Python 3.6 - 3.9 <https://www.python.org/downloads/mac-osx/>`_ (choose 3.6 - 3.9). Install and add to path.
  * Apple Xcode Command Line Tools. In the terminal, run `xcode-select --install` from any directory
  * (Optional) Apple Xcode IDE (not required for OpenVINO™, but useful for development)

Overview
~~~~~~~~

This guide provides step-by-step instructions on how to install the Intel® Distribution of OpenVINO™ toolkit for macOS. The following steps will be covered:

#. `Install the Intel® Distribution of OpenVINO™ Toolkit <#install-core>`__

#. `Configure the Environment <#set-the-environment-variables>`__

#. `Download additional components (Optional) <#model-optimizer>`__

#. `Configure the Intel® Neural Compute Stick 2 (Optional) <#configure-ncs2>`__

#. `What’s next? <#get-started>`__

.. _install-core:

Step 1: Install the Intel® Distribution of OpenVINO™ Toolkit Core Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Download the Intel® Distribution of OpenVINO™ toolkit package file from `Intel® Distribution of OpenVINO™ toolkit for macOS <https://software.intel.com/en-us/openvino-toolkit/choose-download/free-download-macos>`__. Select the Intel® Distribution of OpenVINO™ toolkit for macOS package from the dropdown menu.

#. Go to the directory where you downloaded the Intel® Distribution of OpenVINO™ toolkit. This document assumes this is your ``Downloads`` directory. By default, the disk image file is saved as ``m_openvino_toolkit_p_<version>.dmg``.

#. Double-click the ``m_openvino_toolkit_p_<version>.dmg`` file to mount. The disk image is mounted to ``/Volumes/m_openvino_toolkit_p_<version>`` and automatically opens in a separate window.

#. Run the installation wizard application ``bootstrapper.app``. You should see the following dialog box open up:
   
   .. image:: _static/images/openvino-install.png
         :width: 400px
         :align: center

#. Follow the instructions on your screen. During the installation you will be asked to accept the license agreement. Your acceptance is required to continue.
   
   .. image:: openvino-install-macos-run-boostrapper-script.gif
   
   Click on the image to see the details.
   
   By default, the Intel® Distribution of OpenVINO™ is installed in the following directory, referred to as ``<INSTALL_DIR>`` elsewhere in the documentation:
   
   ``/opt/intel/openvino_<version>/``
   
   For simplicity, a symbolic link to the latest installation is also created: ``/opt/intel/openvino_2022/``.

To check **Release Notes** please visit: `Release Notes <https://software.intel.com/en-us/articles/OpenVINO-RelNotes>`__.

The core components are now installed. Continue to the next section to configure environment.

.. _set-the-environment-variables:

Step 2: Configure the Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You must update several environment variables before you can compile and run OpenVINO™ applications. Set environment variables as follows:

.. ref-code-block:: cpp

	source <INSTALL_DIR>/setupvars.sh

If you have more than one OpenVINO™ version on your machine, you can easily switch its version by sourcing ``setupvars.sh`` of your choice.

.. note:: You can also run this script every time when you start new terminal session. Open ``~/.bashrc`` in your favorite editor, and add ``source <INSTALL_DIR>/setupvars.sh``. Next time when you open a terminal, you will see ``[setupvars.sh] OpenVINO™ environment initialized``. Changing ``.bashrc`` is not recommended when you have many OpenVINO™ versions on your machine and want to switch among them, as each may require different setup.

The environment variables are set. Continue to the next section if you want to download any additional components.

.. _model-optimizer:

Step 3 (Optional): Download Additional Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: Since the OpenVINO™ 2022.1 release, the following development tools: Model Optimizer, Post-Training Optimization Tool, Model Downloader and other Open Model Zoo tools, Accuracy Checker, and Annotation Converter are not part of the installer. The OpenVINO™ Development Tools can only be installed via PyPI now. See :ref:`Install OpenVINO™ Development Tools <doxid-openvino_docs_install_guides_install_dev_tools>` for detailed steps.

.. dropdown:: OpenCV

   OpenCV is necessary to run demos from Open Model Zoo (OMZ). Some OpenVINO samples can also extend their capabilities when compiled with OpenCV as a dependency. The Intel® Distribution of OpenVINO™ provides a script to install OpenCV: ``<INSTALL_DIR>/extras/scripts/download_opencv.sh``.

   .. note::
      Make sure you have 2 prerequisites installed: ``curl`` and ``tar``.

   Depending on how you have installed the Intel® Distribution of OpenVINO™, the script should be run either as root or regular user. After the execution of the script, you will find OpenCV extracted to ``<INSTALL_DIR>/extras/opencv``.

.. _configure-ncs2:

Step 4 (Optional): Configure the Intel® Neural Compute Stick 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to run inference on Intel® Neural Compute Stick 2 use the following instructions to setup the device: :ref:`NCS2 Setup Guide <ncs guide macos>`.

.. _get-started:

Step 5: What's next?
~~~~~~~~~~~~~~~~~~~~

Now you are ready to try out the toolkit. You can use the following tutorials to write your applications using Python and C++.

Developing in Python:

* `Start with tensorflow models with OpenVINO™ <https://docs.openvino.ai/latest/notebooks/101-tensorflow-to-openvino-with-output.html>`__

* `Start with ONNX and PyTorch models with OpenVINO™ <https://docs.openvino.ai/latest/notebooks/102-pytorch-onnx-to-openvino-with-output.html>`__

* `Start with PaddlePaddle models with OpenVINO™ <https://docs.openvino.ai/latest/notebooks/103-paddle-onnx-to-openvino-classification-with-output.html>`__

Developing in C++:

* :ref:`Image Classification Async C++ Sample <doxid-openvino_inference_engine_samples_classification_sample_async__r_e_a_d_m_e>`

* :ref:`Hello Classification C++ Sample <doxid-openvino_inference_engine_samples_hello_classification__r_e_a_d_m_e>`

* :ref:`Hello Reshape SSD C++ Sample <doxid-openvino_inference_engine_samples_hello_reshape_ssd__r_e_a_d_m_e>`

.. _uninstall:

Uninstall the Intel® Distribution of OpenVINO™ Toolkit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To uninstall the toolkit, follow the steps on the :ref:`Uninstalling page <doxid-openvino_docs_install_guides_uninstalling_openvino>`.

.. raw:: html

   </div>

.. dropdown:: Additional Resources

   * Converting models for use with OpenVINO™: :ref:`Model Optimizer Developer Guide <deep learning model optimizer>`
   * Writing your own OpenVINO™ applications: :ref:`OpenVINO™ Runtime User Guide <deep learning openvino runtime>`
   * Sample applications: :ref:`OpenVINO™ Toolkit Samples Overview <code samples>`
   * Pre-trained deep learning models: :ref:`Overview of OpenVINO™ Toolkit Pre-Trained Models <model zoo>`
   * IoT libraries and code samples in the GitHUB repository: `Intel® IoT Developer Kit`_ 


   .. _Intel® IoT Developer Kit: https://github.com/intel-iot-devkit

