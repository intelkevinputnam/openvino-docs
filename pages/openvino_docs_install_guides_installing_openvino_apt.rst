.. index:: pair: page; Install Intel® Distribution of OpenVINO™ Toolkit for Linux Using APT Repository
.. _doxid-openvino_docs_install_guides_installing_openvino_apt:


Install Intel® Distribution of OpenVINO™ Toolkit for Linux Using APT Repository
==================================================================================

:target:`doxid-openvino_docs_install_guides_installing_openvino_apt_1md_openvino_docs_install_guides_installing-openvino-apt` This guide provides installation steps for Intel® Distribution of OpenVINO™ toolkit for Linux distributed through the APT repository.

.. note:: From the 2022.1 release, the OpenVINO™ Development Tools can only be installed via PyPI. If you want to develop or optimize your models with OpenVINO, see :ref:`Install OpenVINO Development Tools <doxid-openvino_docs_install_guides_install_dev_tools>` for detailed steps.

.. warning:: By downloading and using this container and the included software, you agree to the terms and conditions of the `software license agreements <https://software.intel.com/content/dam/develop/external/us/en/documents/intel-openvino-license-agreements.pdf>`__. Please review the content inside the ``<INSTALL_DIR>/licensing`` folder for more details.

System Requirements
~~~~~~~~~~~~~~~~~~~

The complete list of supported hardware is available in the `Release Notes <https://software.intel.com/content/www/us/en/develop/articles/openvino-relnotes.html>`__.

**Operating Systems**

* Ubuntu 18.04 long-term support (LTS), 64-bit

* Ubuntu 20.04 long-term support (LTS), 64-bit

**Software**

* `CMake 3.13 or higher, 64-bit <https://cmake.org/download/>`__

* GCC 7.5.0 (for Ubuntu 18.04) or GCC 9.3.0 (for Ubuntu 20.04)

* `Python 3.6 - 3.9, 64-bit <https://www.python.org/downloads/windows/>`__

Install OpenVINO Runtime
~~~~~~~~~~~~~~~~~~~~~~~~

Step 1: Set Up the OpenVINO Toolkit APT Repository
--------------------------------------------------

#. Install the GPG key for the repository
   
   a. Download the `GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB <https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB>`__. You can also use the following command: ```sh wget `https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB <https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB>`__ ```
   
   b. Add this key to the system keyring: ```sh sudo apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB `` ``> \*\*NOTE\*\*: You might need to install GnuPG:`` sudo apt-get install gnupg`

#. Add the repository via the following command:
   
   
   
   
   
   .. tab:: Ubuntu 18
   
      .. code-block:: sh
   
         echo "deb https://apt.repos.intel.com/openvino/2022 bionic main" | sudo tee /etc/apt/sources.list.d/intel-openvino-2022.list
   
   .. tab:: Ubuntu 20
   
      .. code-block:: sh
   
         echo "deb https://apt.repos.intel.com/openvino/2022 focal main" | sudo tee /etc/apt/sources.list.d/intel-openvino-2022.list

#. Update the list of packages via the update command:
   
   .. ref-code-block:: cpp
   
   	sudo apt update

#. Verify that the APT repository is properly set up. Run the apt-cache command to see a list of all available OpenVINO packages and components:
   
   .. ref-code-block:: cpp
   
   	apt-cache search openvino

Step 2: Install OpenVINO Runtime Using the APT Package Manager
--------------------------------------------------------------

OpenVINO will be installed in: ``/opt/intel/openvino_<VERSION>.<UPDATE>.<PATCH>``

A symlink will be created: ``/opt/intel/openvino_<VERSION>``

To Install the Latest Version
+++++++++++++++++++++++++++++

Run the following command:

.. ref-code-block:: cpp

	sudo apt install openvino

To Install a Specific Version
+++++++++++++++++++++++++++++

#. Get a list of OpenVINO packages available for installation:
   
   .. ref-code-block:: cpp
   
   	sudo apt-cache search openvino

#. Install a specific version of an OpenVINO package:
   
   .. ref-code-block:: cpp
   
   	sudo apt install openvino-<VERSION>.<UPDATE>.<PATCH>
   
   
   
   .. code-block:: cpp
   
   	For example:
   
   
   
   .. ref-code-block:: cpp
   
   	sudo apt install openvino-2022.1.0

To Check for Installed Packages and Versions
++++++++++++++++++++++++++++++++++++++++++++

Run the following command:

.. ref-code-block:: cpp

	apt list --installed | grep openvino

To Uninstall the Latest Version
+++++++++++++++++++++++++++++++

Run the following command:

.. ref-code-block:: cpp

	sudo apt autoremove openvino

To Uninstall a Specific Version
+++++++++++++++++++++++++++++++

Run the following command:

.. ref-code-block:: cpp

	sudo apt autoremove openvino-<VERSION>.<UPDATE>.<PATCH>

Step 3 (Optional): Install OpenCV from APT
------------------------------------------

OpenCV is necessary to run C++ demos from Open Model Zoo. Some OpenVINO samples can also extend their capabilities when compiled with OpenCV as a dependency. OpenVINO provides a package to install OpenCV from APT:

To Install the Latest Version of OpenCV
+++++++++++++++++++++++++++++++++++++++

Run the following command:

.. ref-code-block:: cpp

	sudo apt install openvino-opencv

To Install a Specific Version of OpenCV
+++++++++++++++++++++++++++++++++++++++

Run the following command:

.. ref-code-block:: cpp

	sudo apt install openvino-opencv-<VERSION>.<UPDATE>.<PATCH>

Step 4 (Optional): Install Software Dependencies
------------------------------------------------

After you have installed OpenVINO Runtime, if you decided to :ref:`install OpenVINO Development Tools <doxid-openvino_docs_install_guides_install_dev_tools>`, make sure that you install external software dependencies first.

Refer to `Install External Software Dependencies <openvino_docs_install_guides_installing_openvino_linux.html#install-external-dependencies>`__ for detailed steps.

Step 5 (Optional): Configure Inference on Non-CPU Devices
---------------------------------------------------------

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

What's Next?
~~~~~~~~~~~~

Now you may continue with the following tasks:

* To convert models for use with OpenVINO, see :ref:`Model Optimizer Developer Guide <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`.

* See pre-trained deep learning models in our :ref:`Open Model Zoo <doxid-model_zoo>`.

* Try out OpenVINO via `OpenVINO Notebooks <https://docs.openvino.ai/latest/notebooks/notebooks.html>`__.

* To write your own OpenVINO™ applications, see :ref:`OpenVINO Runtime User Guide <doxid-openvino_docs__o_v__u_g__o_v__runtime__user__guide>`.

* See sample applications in :ref:`OpenVINO™ Toolkit Samples Overview <doxid-openvino_docs__o_v__u_g__samples__overview>`.

Additional Resources
~~~~~~~~~~~~~~~~~~~~

* Intel® Distribution of OpenVINO™ toolkit home page: `https://software.intel.com/en-us/openvino-toolkit <https://software.intel.com/en-us/openvino-toolkit>`__.

* For IoT Libraries & Code Samples see the `Intel® IoT Developer Kit <https://github.com/intel-iot-devkit>`__.

