.. index:: pair: page; Install Intel® Distribution of OpenVINO™ Toolkit from PyPI Repository
.. _doxid-openvino_docs_install_guides_installing_openvino_pip:


Install Intel® Distribution of OpenVINO™ Toolkit from PyPI Repository
========================================================================

:target:`doxid-openvino_docs_install_guides_installing_openvino_pip_1md_openvino_docs_install_guides_installing-openvino-pip` You can install both OpenVINO™ Runtime and OpenVINO Development Tools through the PyPI repository. This page provides the main steps for installing OpenVINO Runtime.

.. note:: From the 2022.1 release, the OpenVINO™ Development Tools can only be installed via PyPI. See :ref:`Install OpenVINO Development Tools <doxid-openvino_docs_install_guides_install_dev_tools>` for detailed steps.

Installing OpenVINO Runtime
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For system requirements and troubleshooting, see `https://pypi.org/project/openvino/ <https://pypi.org/project/openvino/>`__.

Step 1. Set Up Python Virtual Environment
-----------------------------------------

To avoid dependency conflicts, use a virtual environment. Skip this step only if you do want to install all dependencies globally.

Use the following command to create a virtual environment:

.. tab:: Linux and macOS

   .. code-block:: sh

      python3 -m venv openvino_env

.. tab:: Windows

   .. code-block:: sh

      python -m venv openvino_env

Step 2. Activate Virtual Environment
------------------------------------

.. tab:: On Linux and macOS

   .. code-block:: sh

      source openvino_env/bin/activate

.. tab:: On Windows

   .. code-block:: sh

      openvino_env\Scripts\activate

Step 3. Set Up and Update PIP to the Highest Version
----------------------------------------------------

Use the following command:

.. ref-code-block:: cpp

	python -m pip install --upgrade pip

Step 4. Install the Package
---------------------------

Use the following command:

.. ref-code-block:: cpp

	pip install openvino

Step 5. Verify that the Package Is Installed
--------------------------------------------

Run the command below:

.. ref-code-block:: cpp

	python -c "from openvino.runtime import Core"

If installation was successful, you will not see any error messages (no console output).

Installing OpenVINO Development Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenVINO Development Tools include Model Optimizer, Benchmark Tool, Accuracy Checker, Post-Training Optimization Tool and Open Model Zoo tools including Model Downloader. If you want to install OpenVINO Development Tools, OpenVINO Runtime will also be installed as a dependency, so you don't need to install OpenVINO Runtime separately.

See :ref:`Install OpenVINO™ Development Tools <doxid-openvino_docs_install_guides_install_dev_tools>` for detailed steps.

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

* Intel® Distribution of OpenVINO™ toolkit home page: `https://software.intel.com/en-us/openvino-toolkit <https://software.intel.com/en-us/openvino-toolkit>`__

* For IoT Libraries & Code Samples, see `Intel® IoT Developer Kit <https://github.com/intel-iot-devkit>`__.

