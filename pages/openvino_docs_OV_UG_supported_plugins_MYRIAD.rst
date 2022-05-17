.. index:: pair: page; MYRIAD device
.. _doxid-openvino_docs__o_v__u_g_supported_plugins__m_y_r_i_a_d:


MYRIAD device
=============

:target:`doxid-openvino_docs__o_v__u_g_supported_plugins__m_y_r_i_a_d_1md_openvino_docs_ov_runtime_ug_supported_plugins_myriad`

Introducing MYRIAD Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~

The OpenVINO Runtime MYRIAD plugin has been developed for inference of neural networks on Intel Neural Compute Stick 2.

Configuring the MYRIAD Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To configure your Intel® Vision Accelerator Design With Intel® Movidius™ on supported operating systemss, refer to the Steps for Intel® Vision Accelerator Design with Intel® Movidius™ VPUs section in the installation guides for :ref:`Linux <doxid-openvino_docs_install_guides_installing_openvino_linux>` or :ref:`Windows <doxid-openvino_docs_install_guides_installing_openvino_windows>`.

.. note:: The HDDL and MYRIAD plugins may cause conflicts when used at the same time. To ensure proper operation in such a case, the number of booted devices needs to be limited in the 'hddl_autoboot.config' file. Otherwise, the HDDL plugin will boot all available Intel® Movidius™ Myriad™ X devices.

Supported Configuration Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See VPU common configuration parameters for the :ref:`VPU Plugins <doxid-openvino_docs__o_v__u_g_supported_plugins__v_p_u>`. When specifying key values as raw strings (that is, when using the Python API), omit the ``KEY_`` prefix.

In addition to common parameters, the MYRIAD plugin accepts the following options:

.. list-table::
    :header-rows: 1

    * - Parameter Name
      - Parameter Values
      - Default
      - Description
    * - ``KEY_VPU_MYRIAD_PROTOCOL``
      - empty string/ ``VPU_MYRIAD_USB`` / ``VPU_MYRIAD_PCIE``
      - empty string
      - If set, the plugin will use a device with specific protocol to allocate a network.
    * - ``KEY_VPU_MYRIAD_FORCE_RESET``
      - ``YES`` / ``NO``
      - ``NO``
      - Enables force reset of all booted devices when new ExecutableNetwork is created. This is a plugin scope option and must be used with the plugin's SetConfig method only. See `Device allocation <#MYRIAD_DEVICE_ALLOC>`__ section for details.
    * - ``KEY_VPU_FORCE_RESET``
      - ``YES`` / ``NO``
      - ``NO``
      - **Deprecated** Use ``KEY_VPU_MYRIAD_FORCE_RESET`` instead. Enables force reset of all booted devices when new ExecutableNetwork is created. This is a plugin scope option and must be used with the plugin's SetConfig method only. See `Device allocation <#MYRIAD_DEVICE_ALLOC>`__ section for details.

.. _MYRIAD_DEVICE_ALLOC:

Device allocation
~~~~~~~~~~~~~~~~~

Each ``IExecutableNetwork`` instance tries to allocate new device on ``:ref:`InferenceEngine::Core::LoadNetwork <doxid-class_inference_engine_1_1_core_1a7b0b5ab0009abc572762422105b5c666>```, but if all available devices are already allocated it will use the one with the minimal number of uploaded networks. The maximum number of networks a single device can handle depends on device memory capacity and the size of the networks.

If the ``KEY_VPU_MYRIAD_FORCE_RESET`` option is set to ``YES``, the plugin will reset all VPU devices in the system.

Single device cannot be shared across multiple processes.

See Also
~~~~~~~~

* :ref:`Supported Devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`

* :ref:`VPU Plugins <doxid-openvino_docs__o_v__u_g_supported_plugins__v_p_u>`

* `Intel Neural Compute Stick 2 Get Started <https://software.intel.com/en-us/neural-compute-stick/get-started>`__

