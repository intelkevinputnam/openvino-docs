.. index:: pair: page; Configurations for Intel® Vision Accelerator Design with Intel® Movidius™ VPUs
.. _doxid-openvino_docs_install_guides_installing_openvino_ivad_vpu:


Configurations for Intel® Vision Accelerator Design with Intel® Movidius™ VPUs
==================================================================================

:target:`doxid-openvino_docs_install_guides_installing_openvino_ivad_vpu_1md_openvino_docs_install_guides_installing-openvino-config-ivad-vpu`





.. _vpu guide:

.. toctree::
   :maxdepth: 2
   :hidden:

   Configurations for IEI Mustang-V100-MX8-R10 card <openvino_docs_install_guides_movidius_setup_guide>

The steps in this guide are only required if you want to perform inference on Intel® Vision Accelerator Design with Intel® Movidius™ VPUs with OpenVINO™ on Linux or Windows.

For troubleshooting issues, please see the :ref:`Troubleshooting Guide <doxid-openvino_docs_get_started_guide_troubleshooting>` for more information.

Linux
~~~~~

For Intel® Vision Accelerator Design with Intel® Movidius™ VPUs, the following additional installation steps are required.

.. note:: If you installed the Intel® Distribution of OpenVINO™ toolkit to the non-default install directory, replace ``/opt/intel`` with the directory in which you installed the software.

#. Set the environment variables:
   
   .. ref-code-block:: cpp
   
   	source /opt/intel/openvino_2022/setupvars.sh

.. note:: The ``HDDL_INSTALL_DIR`` variable is set to ``<openvino_install_dir>/runtime/3rdparty/hddl``. If you installed the Intel® Distribution of OpenVINO™ to the default install directory, the ``HDDL_INSTALL_DIR`` was set to ``/opt/intel/openvino_2022/runtime/3rdparty/hddl``.

#. Install dependencies:
   
   .. ref-code-block:: cpp
   
   	${HDDL_INSTALL_DIR}/install_IVAD_VPU_dependencies.sh

Note, if the Linux kernel is updated after the installation, it is required to install drivers again:

.. ref-code-block:: cpp

	cd ${HDDL_INSTALL_DIR}/drivers

.. ref-code-block:: cpp

	sudo ./setup.sh install

Now the dependencies are installed and you are ready to use the Intel® Vision Accelerator Design with Intel® Movidius™ with the Intel® Distribution of OpenVINO™ toolkit.

Optional Steps
--------------

For advanced configuration steps for your **IEI Mustang-V100-MX8-R10** accelerator, see :ref:`Configurations for IEI Mustang-V100-MX8-R10 card <doxid-openvino_docs_install_guides_movidius_setup_guide>`. **IEI Mustang-V100-MX8-R11** accelerator doesn't require any additional steps.

.. _vpu guide windows:

Windows
~~~~~~~

To enable inference on Intel® Vision Accelerator Design with Intel® Movidius™ VPUs, the following additional installation steps are required:

#. Download and install `Visual C++ Redistributable for Visual Studio 2017 <https://www.microsoft.com/en-us/download/details.aspx?id=48145>`__

#. Check with a support engineer if your Intel® Vision Accelerator Design with Intel® Movidius™ VPUs card requires SMBUS connection to PCIe slot (most unlikely). Install the SMBUS driver only if confirmed (by default, it's not required):
   
   #. Go to the ``<INSTALL_DIR>\runtime\3rdparty\hddl\drivers\SMBusDriver`` directory, where ``<INSTALL_DIR>`` is the directory in which the Intel® Distribution of OpenVINO™ toolkit is installed.
   
   #. Right click on the ``hddlsmbus.inf`` file and choose **Install** from the pop up menu.

You are done installing your device driver and are ready to use your Intel® Vision Accelerator Design with Intel® Movidius™ VPUs.

For advanced configuration steps for your IEI Mustang-V100-MX8 accelerator, see :ref:`Configurations for IEI Mustang-V100-MX8-R10 card <doxid-openvino_docs_install_guides_movidius_setup_guide>`.

After configuration is done, you are ready to go to `Start Using the Toolkit <openvino_docs_install_guides_installing_openvino_windows.html#get-started>`__ section to learn the basic OpenVINO™ toolkit workflow and run code samples and demo applications.

