.. index:: pair: page; Configurations for Intel® Processor Graphics (GPU) with Intel® Distribution of OpenVINO™ toolkit
.. _doxid-openvino_docs_install_guides_configurations_for_intel_gpu:


Configurations for Intel® Processor Graphics (GPU) with Intel® Distribution of OpenVINO™ toolkit
====================================================================================================

:target:`doxid-openvino_docs_install_guides_configurations_for_intel_gpu_1md_openvino_docs_install_guides_configurations-for-intel-gpu`

.. _gpu guide:

This page introduces additional configurations for Intel® Processor Graphics (GPU) with Intel® Distribution of OpenVINO™ toolkit on Linux and Windows.

Linux
~~~~~

Once you have your OpenVINO installed, follow the steps to be able to work on GPU:

#. Go to the install_dependencies directory:
   
   .. ref-code-block:: cpp
   
   	cd <INSTALL_DIR>/install_dependencies/

#. Install the **Intel® Graphics Compute Runtime for OpenCL™** driver components required to use the GPU plugin and write custom layers for Intel® Integrated Graphics. The drivers are not included in the package. To install, run this script:
   
   .. ref-code-block:: cpp
   
   	sudo -E ./install_NEO_OCL_driver.sh

.. note:: To use the **Intel® Iris® Xe MAX Graphics**, see the `Intel® Iris® Xe MAX Graphics with Linux\* <https://dgpu-docs.intel.com/devices/iris-xe-max-graphics/index.html>`__ page for driver installation instructions.

The script compares the driver version on the system to the current version. If the driver version on the system is higher or equal to the current version, the script does not install a new driver. If the version of the driver is lower than the current version, the script uninstalls the lower version and installs the current version with your permission:

.. image:: NEO_check_agreement.png

Higher hardware versions require a higher driver version, namely 20.35 instead of 19.41. If the script fails to uninstall the driver, uninstall it manually. During the script execution, you may see the following command line output:



.. ref-code-block:: cpp

	Add OpenCL user to video group

Ignore this suggestion and continue.

You can also find the most recent version of the driver, installation procedure and other information on the `Intel® software for general purpose GPU capabilities <https://dgpu-docs.intel.com/index.html>`__ site.

#. **Optional:** Install header files to allow compilation of new code. You can find the header files at `Khronos OpenCL™ API Headers <https://github.com/KhronosGroup/OpenCL-Headers.git>`__.

You've completed all required configuration steps to perform inference on processor graphics. Proceed to the `Start Using the Toolkit <openvino_docs_install_guides_installing_openvino_linux.html#get-started>`__ section to learn the basic OpenVINO™ toolkit workflow and run code samples and demo applications.

.. _gpu guide windows:

Windows
~~~~~~~

This section will help you check if you require driver installation. Install indicated version or higher.

If your applications offload computation to **Intel® Integrated Graphics**, you must have the Intel Graphics Driver for Windows installed on your hardware. `Download and install the recommended version <https://downloadcenter.intel.com/download/30079/Intel-Graphics-Windows-10-DCH-Drivers>`__.

To check if you have this driver installed:

#. Type **device manager** in your **Search Windows** box and press Enter. The **Device Manager** opens.

#. Click the drop-down arrow to view the **Display adapters**. You can see the adapter that is installed in your computer:
   
   .. image:: DeviceManager.PNG

#. Right-click the adapter name and select **Properties**.

#. Click the **Driver** tab to see the driver version.
   
   .. image:: DeviceDriverVersion.PNG

You are done updating your device driver and are ready to use your GPU. Proceed to the `Start Using the Toolkit <openvino_docs_install_guides_installing_openvino_windows.html#get-started>`__ section to learn the basic OpenVINO™ toolkit workflow and run code samples and demo applications.

