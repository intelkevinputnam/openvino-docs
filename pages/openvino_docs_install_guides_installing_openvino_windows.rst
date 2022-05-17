.. index:: pair: page; Install and Configure Intel® Distribution of OpenVINO™ toolkit for Windows 10
.. _doxid-openvino_docs_install_guides_installing_openvino_windows:


Install and Configure Intel® Distribution of OpenVINO™ toolkit for Windows 10
================================================================================

:target:`doxid-openvino_docs_install_guides_installing_openvino_windows_1md_openvino_docs_install_guides_installing-openvino-windows`

.. note:: Since the OpenVINO™ 2022.1 release, the following development tools: Model Optimizer, Post-Training Optimization Tool, Model Downloader and other Open Model Zoo tools, Accuracy Checker, and Annotation Converter are not part of the installer. These tools are now only available on `pypi.org <https://pypi.org/project/openvino-dev/>`__.

System Requirements
~~~~~~~~~~~~~~~~~~~

.. tab:: Operating Systems

  Microsoft Windows 10, 64-bit

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

  * `Microsoft Visual Studio 2019 with MSBuild <http://visualstudio.microsoft.com/downloads/>`_
  * `CMake 3.14 or higher, 64-bit <https://cmake.org/download/>`_
  * `Python 3.6 - 3.9, 64-bit <https://www.python.org/downloads/windows/>`_

  .. note::
    You can choose to download Community version. Use `Microsoft Visual Studio installation guide <https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2019>`_ to walk you through the installation. During installation in the **Workloads** tab, choose **Desktop development with C++**.

  .. note::
    You can either use `cmake<version>.msi` which is the installation wizard or `cmake<version>.zip` where you have to go into the `bin` folder and then manually add the path to environmental variables.

  .. important::
    As part of this installation, make sure you click the option **Add Python 3.x to PATH** to `add Python <https://docs.python.org/3/using/windows.html#installation-steps>`_ to your `PATH` environment variable.

Overview
~~~~~~~~

This guide provides step-by-step instructions on how to install the Intel® Distribution of OpenVINO™ toolkit. Links are provided for each type of compatible hardware including downloads, initialization and configuration steps. The following steps will be covered:

#. `Install the Intel® Distribution of OpenVINO™ Toolkit <#install-openvino>`__

#. `Configure the Environment <#set-the-environment-variables>`__

#. `Download additional components (Optional) <#model-optimizer>`__

#. `Configure Inference on non-CPU Devices (Optional) <#optional-steps>`__

#. `What's next? <#get-started>`__

.. _install-openvino:

Step 1: Install the Intel® Distribution of OpenVINO™ toolkit Core Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Download the Intel® Distribution of OpenVINO™ toolkit package file from `Intel® Distribution of OpenVINO™ toolkit for Windows <https://software.intel.com/en-us/openvino-toolkit/choose-download>`__. Select the Intel® Distribution of OpenVINO™ toolkit for Windows package from the dropdown menu.

#. Go to the ``Downloads`` folder and double-click ``w_openvino_toolkit_p_<version>.exe``. In the opened window, you can select the folder where installer files will be placed. The directory will be referred to as <INSTALL_DIR> elsewhere in the documentation. Once the files are extracted, you should see the following dialog box open up:
   
   .. image:: _static/images/openvino-install.png
        :width: 400px
        :align: center

#. Follow the instructions on your screen. During the installation you will be asked to accept the license agreement. Your acceptance is required to continue. Check out the installation process in the image below:
   
   
   
   .. image:: openvino-install-win-run-boostrapper-script.gif
   
   Click on the image to see the details.
   
   
   
   By default, the Intel® Distribution of OpenVINO™ is installed to the following directory, referred to as ``<INSTALL_DIR>`` elsewhere in the documentation: ``C:\Program Files (x86)\Intel\openvino_<version>/``.
   
   For simplicity, a symbolic link to the latest installation is also created: ``C:\Program Files (x86)\Intel\openvino_2022/``.

To check **Release Notes** please visit: `Release Notes <https://software.intel.com/en-us/articles/OpenVINO-RelNotes>`__.

The core components are now installed. Continue to the next section to configure environment.

.. _set-the-environment-variables:

Step 2: Configure the Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: If you installed the Intel® Distribution of OpenVINO™ to a non-default install directory, replace ``C:\Program Files (x86)\Intel`` with that directory in this guide's instructions.

You must update several environment variables before you can compile and run OpenVINO™ applications. Open the Command Prompt, and run the ``setupvars.bat`` batch file to temporarily set your environment variables:

.. ref-code-block:: cpp

	"<INSTALL_DIR>\setupvars.bat"

**Optional** : OpenVINO™ toolkit environment variables are removed when you close the command prompt window. You can permanently set the environment variables manually.

.. note:: If you see an error indicating Python is not installed when you know you installed it, your computer might not be able to find the program. Check your system environment variables, and add Python if necessary.

The environment variables are set. Next, you can download some additional tools.

.. _model-optimizer:

Step 3 (Optional): Download Additional Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: Since the OpenVINO™ 2022.1 release, the following development tools: Model Optimizer, Post-Training Optimization Tool, Model Downloader and other Open Model Zoo tools, Accuracy Checker, and Annotation Converter are not part of the installer. The OpenVINO™ Development Tools can only be installed via PyPI now. See :ref:`Install OpenVINO™ Development Tools <doxid-openvino_docs_install_guides_install_dev_tools>` for detailed steps.

.. dropdown:: OpenCV

   OpenCV is necessary to run demos from Open Model Zoo (OMZ). Some OpenVINO samples can also extend their capabilities when compiled with OpenCV as a dependency. The Intel® Distribution of OpenVINO™ provides a script to install OpenCV: ``<INSTALL_DIR>/extras/scripts/download_opencv.sh``.

   .. note::
      No prerequisites are needed.

   There are three ways to run the script:

   * GUI: right-click the script and select ``Run with PowerShell``.

   * Command prompt (CMD) console:

   .. code-block:: sh

      powershell <INSTALL_DIR>\extras\scripts\download_opencv.ps1


   * PowerShell console:

   .. code-block:: sh

      .\<INSTALL_DIR>\scripts\download_opencv.ps1 


   If the Intel® Distribution of OpenVINO™ is installed to the system location (e.g. ``Program Files (x86)``) then privilege elevation dialog will be shown. The script can be run from CMD/PowerShell Administrator console to avoid this dialog in case of system-wide installation. 
   The script is interactive by default, so during the execution it will wait for user to press ``Enter`` If you want to avoid this, use the ``-batch`` option, e.g. ``powershell <openvino>\extras\scripts\download_opencv.ps1 -batch``. After the execution of the script, you will find OpenCV extracted to ``<INSTALL_DIR>/extras/opencv``.

.. _optional-steps:

Step 4 (Optional): Configure Inference on non-CPU Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tab:: GNA

   To enable the toolkit components to use Intel® Gaussian & Neural Accelerator (GNA) on your system, follow the steps in :ref:`GNA Setup Guide <gna guide windows>`.

.. tab:: GPU

   To enable the toolkit components to use processor graphics (GPU) on your system, follow the steps in :ref:`GPU Setup Guide <gpu guide windows>`.

.. tab:: VPU

   To install and configure your Intel® Vision Accelerator Design with Intel® Movidius™ VPUs, see the :ref:`VPU Configuration Guide <vpu guide windows>`.

.. tab:: NCS 2

   No additional configurations are needed.

.. _get-started:

Step 5: What's next?
~~~~~~~~~~~~~~~~~~~~

Now you are ready to try out the toolkit.

Developing in Python:

* `Start with tensorflow models with OpenVINO™ <https://docs.openvino.ai/latest/notebooks/101-tensorflow-to-openvino-with-output.html>`__

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

.. dropdown:: Additional Resources

   * Converting models for use with OpenVINO™: :ref:`Model Optimizer Developer Guide <deep learning model optimizer>`
   * Writing your own OpenVINO™ applications: :ref:`OpenVINO™ Runtime User Guide <deep learning openvino runtime>`
   * Sample applications: :ref:`OpenVINO™ Toolkit Samples Overview <code samples>`
   * Pre-trained deep learning models: :ref:`Overview of OpenVINO™ Toolkit Pre-Trained Models <model zoo>`
   * IoT libraries and code samples in the GitHUB repository: `Intel® IoT Developer Kit`_ 


   .. _Intel® IoT Developer Kit: https://github.com/intel-iot-devkit

