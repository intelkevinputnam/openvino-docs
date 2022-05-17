.. index:: pair: page; Install and Configure Intel® Distribution of OpenVINO™ Toolkit for Linux
.. _doxid-openvino_docs_install_guides_installing_openvino_linux:


Install and Configure Intel® Distribution of OpenVINO™ Toolkit for Linux
===========================================================================

:target:`doxid-openvino_docs_install_guides_installing_openvino_linux_1md_openvino_docs_install_guides_installing-openvino-linux`

.. note:: Since the OpenVINO™ 2022.1 release, the following development tools: Model Optimizer, Post-Training Optimization Tool, Model Downloader and other Open Model Zoo tools, Accuracy Checker, and Annotation Converter are not part of the installer. These tools are now only available on `pypi.org <https://pypi.org/project/openvino-dev/>`__.

System Requirements
~~~~~~~~~~~~~~~~~~~

.. tab:: Operating Systems

  * Ubuntu 18.04 long-term support (LTS), 64-bit
  * Ubuntu 20.04 long-term support (LTS), 64-bit

  .. note::
     Since the OpenVINO™ 2022.1 release, CentOS 7.6, 64-bit is not longer supported.

.. tab:: Hardware

  Optimized for these processors:

  * 6th to 12th generation Intel® Core™ processors and Intel® Xeon® processors 
  * 3rd generation Intel® Xeon® Scalable processor (formerly code named Cooper Lake)
  * Intel® Xeon® Scalable processor (formerly Skylake and Cascade Lake)
  * Intel Atom® processor with support for Intel® Streaming SIMD Extensions 4.1 (Intel® SSE4.1)
  * Intel Pentium® processor N4200/5, N3350/5, or N3450/5 with Intel® HD Graphics
  * Intel® Iris® Xe MAX Graphics
  * Intel® Neural Compute Stick 2
  * Intel® Vision Accelerator Design with Intel® Movidius™ VPUs

.. tab:: Processor Notes

  Processor graphics are not included in all processors. 
  See `Product Specifications`_ for information about your processor.

  .. _Product Specifications: https://ark.intel.com/

.. tab:: Software

  * `CMake 3.13 or higher, 64-bit <https://cmake.org/download/>`_
  * GCC 7.5.0 (for Ubuntu 18.04) or GCC 9.3.0 (for Ubuntu 20.04)
  * `Python 3.6 - 3.9, 64-bit <https://www.python.org/downloads/windows/>`_

Overview
~~~~~~~~

This guide provides step-by-step instructions on how to install the Intel® Distribution of OpenVINO™ toolkit. Links are provided for each type of compatible hardware including downloads, initialization and configuration steps. The following steps will be covered:

#. `Install the Intel® Distribution of OpenVINO™ Toolkit <#install-openvino>`__

#. `Install External Software Dependencies <#install-external-dependencies>`__

#. `Configure the Environment <#set-the-environment-variables>`__

#. `Download additional components (Optional) <#model-optimizer>`__

#. `Configure Inference on non-CPU Devices (Optional) <#optional-steps>`__

#. `What's next? <#get-started>`__

.. important::
   Before you start your journey with installation of the Intel® Distribution of OpenVINO™, we encourage you to check our :ref:`code samples <code samples>` in C, C++, Python and :ref:`notebook tutorials <notebook tutorials>` that we prepared for you, so you could see all the amazing things that you can achieve with our tool.

.. _install-openvino:

Step 1: Install the Intel® Distribution of OpenVINO™ Toolkit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Select and download the Intel® Distribution of OpenVINO™ toolkit installer file from `Intel® Distribution of OpenVINO™ toolkit for Linux <https://software.intel.com/en-us/openvino-toolkit/choose-download>`__.

#. Open a command prompt terminal window. You can use the keyboard shortcut: Ctrl+Alt+T

#. Change directories to where you downloaded the Intel Distribution of OpenVINO™ toolkit for Linux file.
   
   If you downloaded the starter script to the current user's ``Downloads`` directory:
   
   .. ref-code-block:: cpp
   
   	cd ~/Downloads/
   
   You should find there a bootstrapper script ``l_openvino_toolkit_p_<version>.sh``.

#. Add executable rights for the current user:
   
   .. ref-code-block:: cpp
   
   	chmod +x l_openvino_toolkit_p_<version>.sh

#. If you want to use graphical user interface (GUI) installation wizard, run the script without any parameters:
   
   .. ref-code-block:: cpp
   
   	./l_openvino_toolkit_p_<version>.sh
   
   You should see the following dialog box open up:
   
   .. image:: _static/images/openvino-install.png
         :width: 400px
         :align: center
   
   Otherwise, you can add parameters ``-a`` for additional arguments and ``--cli`` to run installation in command line (CLI):
   
   .. ref-code-block:: cpp
   
   	./l_openvino_toolkit_p_<version>.sh -a --cli

.. note:: To get additional information on all parameters that can be used, use the help option: ``--help``. Among others, you can find there ``-s`` option which offers silent mode, which together with ``--eula approve`` allows you to run whole installation with default values without any user inference.

#. Follow the instructions on your screen. During the installation you will be asked to accept the license agreement. Your acceptance is required to continue. Check the installation process on the image below:
   
   .. image:: openvino-install-linux-run-boostrapper-script.gif
   
   Click on the image to see the details.
   
   
   
   By default, the Intel® Distribution of OpenVINO™ is installed to the following directory, referred to as ``<INSTALL_DIR>`` elsewhere in the documentation:
   
   * For root or administrator: ``/opt/intel/openvino_<version>/``
   
   * For regular users: ``/home/<USER>/intel/openvino_<version>/``
   
   For simplicity, a symbolic link to the latest installation is also created: ``/opt/intel/openvino_2022/`` or ``/home/<USER>/intel/openvino_2022/``.

To check **Release Notes** please visit: `Release Notes <https://software.intel.com/en-us/articles/OpenVINO-RelNotes>`__.

The core components are now installed. Continue to the next section to install additional dependencies.

.. _install-external-dependencies:

Step 2: Install External Software Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This script enables you to install Linux platform development tools and components to work with the product.

#. Go to the ``install_dependencies`` directory:
   
   .. ref-code-block:: cpp
   
   	cd <INSTALL_DIR>/install_dependencies

#. Run a script to download and install the external software dependencies:
   
   .. ref-code-block:: cpp
   
   	sudo -E ./install_openvino_dependencies.sh
   
   Once the dependencies are installed, continue to the next section to set your environment variables.

.. _set-the-environment-variables:

Step 3: Configure the Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You must update several environment variables before you can compile and run OpenVINO™ applications. Set environment variables as follows:

.. ref-code-block:: cpp

	source <INSTALL_DIR>/setupvars.sh

If you have more than one OpenVINO™ version on your machine, you can easily switch its version by sourcing ``setupvars.sh`` of your choice.

.. note:: You can also run this script every time when you start new terminal session. Open ``~/.bashrc`` in your favorite editor, and add ``source <INSTALL_DIR>/setupvars.sh``. Next time when you open a terminal, you will see ``[setupvars.sh] OpenVINO™ environment initialized``. Changing ``.bashrc`` is not recommended when you have many OpenVINO™ versions on your machine and want to switch among them, as each may require different setup.

The environment variables are set. Next, you can download some additional tools.

.. _model-optimizer:

Step 4 (Optional): Download Additional Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: Since the OpenVINO™ 2022.1 release, the following development tools: Model Optimizer, Post-Training Optimization Tool, Model Downloader and other Open Model Zoo tools, Accuracy Checker, and Annotation Converter are not part of the installer. The OpenVINO™ Development Tools can only be installed via PyPI now. See :ref:`Install OpenVINO™ Development Tools <doxid-openvino_docs_install_guides_install_dev_tools>` for detailed steps.

.. dropdown:: OpenCV

   OpenCV is necessary to run demos from Open Model Zoo (OMZ). Some OpenVINO samples can also extend their capabilities when compiled with OpenCV as a dependency. The Intel® Distribution of OpenVINO™ provides a script to install OpenCV: ``<INSTALL_DIR>/extras/scripts/download_opencv.sh``.

   .. note::
      Make sure you have 2 prerequisites installed: ``curl`` and ``tar``.

   Depending on how you have installed the Intel® Distribution of OpenVINO™, the script should be run either as root or regular user. After the execution of the script, you will find OpenCV extracted to ``<INSTALL_DIR>/extras/opencv``.

.. _optional-steps:

Step 5 (Optional): Configure Inference on Non-CPU Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tab:: GNA

   To enable the toolkit components to use Intel® Gaussian & Neural Accelerator (GNA) on your system, follow the steps in :ref:`GNA Setup Guide <gna guide>`.

.. tab:: GPU

   To enable the toolkit components to use processor graphics (GPU) on your system, follow the steps in :ref:`GPU Setup Guide <gpu guide>`.

.. tab:: NCS 2

   To perform inference on Intel® Neural Compute Stick 2 powered by the Intel® Movidius™ Myriad™ X VPU, follow the steps on :ref:`NCS2 Setup Guide <ncs guide>`.
   

.. tab:: VPU

   To install and configure your Intel® Vision Accelerator Design with Intel® Movidius™ VPUs, see the :ref:`VPU Configuration Guide <vpu guide>`.
   After configuration is done, you are ready to run the verification scripts with the HDDL Plugin for your Intel® Vision Accelerator Design with Intel® Movidius™ VPUs. 

   .. warning::
      While working with either HDDL or NCS, choose one of them as they cannot run simultaneously on the same machine.

.. _get-started:

Step 6: What's Next?
~~~~~~~~~~~~~~~~~~~~

Now you are ready to try out the toolkit.

Developing in Python:

* `Start with TensorFlow models with OpenVINO™ <https://docs.openvino.ai/latest/notebooks/101-tensorflow-to-openvino-with-output.html>`__

* `Start with ONNX and PyTorch models with OpenVINO™ <https://docs.openvino.ai/latest/notebooks/102-pytorch-onnx-to-openvino-with-output.html>`__

* `Start with PaddlePaddle models with OpenVINO™ <https://docs.openvino.ai/latest/notebooks/103-paddle-onnx-to-openvino-classification-with-output.html>`__

Developing in C++:

* :ref:`Image Classification Async C++ Sample <doxid-openvino_inference_engine_samples_classification_sample_async__r_e_a_d_m_e>`

* :ref:`Hello Classification C++ Sample <doxid-openvino_inference_engine_samples_hello_classification__r_e_a_d_m_e>`

* :ref:`Hello Reshape SSD C++ Sample <doxid-openvino_inference_engine_samples_hello_reshape_ssd__r_e_a_d_m_e>`

.. _uninstall:

Uninstalling the Intel® Distribution of OpenVINO™ Toolkit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To uninstall the toolkit, follow the steps on the :ref:`Uninstalling page <doxid-openvino_docs_install_guides_uninstalling_openvino>`.

.. dropdown:: Troubleshooting

   PRC developers might encounter pip errors during Intel® Distribution of OpenVINO™ installation. To resolve the issues, try one of the following options:

   * Add the download source using the ``-i`` parameter with the Python ``pip`` command. For example: 

   .. code-block:: sh

      pip install openvino-dev -i https://mirrors.aliyun.com/pypi/simple/

   Use the ``--trusted-host`` parameter if the URL above is ``http`` instead of ``https``.

   * If you run into incompatibility issues between components after installing new Intel® Distribution of OpenVINO™ version, try running ``requirements.txt`` with the following command:

   .. code-block:: sh

      pip install -r <INSTALL_DIR>/tools/requirements.txt

.. dropdown:: Additional Resources

   * Converting models for use with OpenVINO™: :ref:`Model Optimizer Developer Guide <deep learning model optimizer>`
   * Writing your own OpenVINO™ applications: :ref:`OpenVINO™ Runtime User Guide <deep learning openvino runtime>`
   * Sample applications: :ref:`OpenVINO™ Toolkit Samples Overview <code samples>`
   * Pre-trained deep learning models: :ref:`Overview of OpenVINO™ Toolkit Pre-Trained Models <model zoo>`
   * IoT libraries and code samples in the GitHUB repository: `Intel® IoT Developer Kit`_ 


   .. _Intel® IoT Developer Kit: https://github.com/intel-iot-devkit

