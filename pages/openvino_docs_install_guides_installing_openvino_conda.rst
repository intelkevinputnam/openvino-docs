.. index:: pair: page; Install Intel® Distribution of OpenVINO™ toolkit from Anaconda Cloud
.. _doxid-openvino_docs_install_guides_installing_openvino_conda:


Install Intel® Distribution of OpenVINO™ toolkit from Anaconda Cloud
=======================================================================

:target:`doxid-openvino_docs_install_guides_installing_openvino_conda_1md_openvino_docs_install_guides_installing-openvino-conda` This guide provides installation steps for Intel® Distribution of OpenVINO™ toolkit for Linux distributed through the Anaconda Cloud.

.. note:: From the 2022.1 release, the OpenVINO™ Development Tools can only be installed via PyPI. If you want to develop or optimize your models with OpenVINO, see :ref:`Install OpenVINO Development Tools <doxid-openvino_docs_install_guides_install_dev_tools>` for detailed steps.

System Requirements
~~~~~~~~~~~~~~~~~~~

**Software**

* `Anaconda distribution <https://www.anaconda.com/products/individual/>`__

**Operating Systems**

.. list-table::
    :header-rows: 1

    * - Supported Operating System
      - `Python Version (64-bit) <https://www.python.org/>`__
    * - Ubuntu 18.04 long-term support (LTS), 64-bit
      - 3.6, 3.7, 3.8, 3.9
    * - Ubuntu 20.04 long-term support (LTS), 64-bit
      - 3.6, 3.7, 3.8, 3.9
    * - Red Hat Enterprise Linux 8, 64-bit
      - 3.6, 3.7, 3.8, 3.9
    * - macOS 10.15
      - 3.6, 3.7, 3.8, 3.9
    * - Windows 10, 64-bit
      - 3.6, 3.7, 3.8, 3.9

Install OpenVINO Runtime Using the Anaconda Package Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Set up the Anaconda environment (taking Python 3.7 for example):
   
   .. ref-code-block:: cpp
   
   	conda create --name py37 python=3.7
   	conda activate py37

#. Update Anaconda environment to the latest version:
   
   .. ref-code-block:: cpp
   
   	conda update --all

#. Install the Intel® Distribution of OpenVINO™ toolkit:
   
   * Ubuntu\* 20.04
     
     .. ref-code-block:: cpp
     
     	conda install openvino-ie4py-ubuntu20 -c intel
   
   * Ubuntu\* 18.04
     
     .. ref-code-block:: cpp
     
     	conda install openvino-ie4py-ubuntu18 -c intel
   
   * Red Hat Enterprise Linux 8, 64-bit
     
     .. ref-code-block:: cpp
     
     	conda install openvino-ie4py-rhel8 -c intel
   
   * Windows 10 and macOS
     
     .. ref-code-block:: cpp
     
     	conda install openvino-ie4py -c intel

#. Verify the package is installed:
   
   .. ref-code-block:: cpp
   
   	python -c "from openvino.runtime import Core"
   
   If installation was successful, you will not see any error messages (no console output).

Now you can start developing your application.

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

* Intel® Distribution of OpenVINO™ toolkit Anaconda home page: `https://anaconda.org/intel/openvino-ie4py <https://anaconda.org/intel/openvino-ie4py>`__

