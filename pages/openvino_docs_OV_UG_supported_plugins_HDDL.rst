.. index:: pair: page; HDDL device
.. _doxid-openvino_docs__o_v__u_g_supported_plugins__h_d_d_l:


HDDL device
===========

:target:`doxid-openvino_docs__o_v__u_g_supported_plugins__h_d_d_l_1md_openvino_docs_ov_runtime_ug_supported_plugins_hddl`

Introducing the HDDL Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The OpenVINO Runtime HDDL plugin was developed for inference with neural networks on Intel Vision Accelerator Design with Intel Movidius VPUs. It is designed for use cases that require large throughput for deep learning inference, up to dozens of times more than the MYRIAD Plugin.

Configuring the HDDL Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To configure your Intel® Vision Accelerator Design With Intel® Movidius™ on supported operating systems, refer to the Steps for Intel® Vision Accelerator Design with Intel® Movidius™ VPUs section in the installation guides for :ref:`Linux <doxid-openvino_docs_install_guides_installing_openvino_linux>` or :ref:`Windows <doxid-openvino_docs_install_guides_installing_openvino_windows>`.

.. note:: The HDDL and Myriad plugins may cause conflicts when used at the same time. To ensure proper operation in such a case, the number of booted devices needs to be limited in the 'hddl_autoboot.config' file. Otherwise, the HDDL plugin will boot all available Intel® Movidius™ Myriad™ X devices.

Supported networks
~~~~~~~~~~~~~~~~~~

To see the list of supported networks for the HDDL plugin, refer to the list on the :ref:`MYRIAD Plugin page <doxid-openvino_docs__o_v__u_g_supported_plugins__m_y_r_i_a_d>`.

Supported Configuration Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See VPU common configuration parameters for :ref:`VPU Plugins <doxid-openvino_docs__o_v__u_g_supported_plugins__v_p_u>`. When specifying key values as raw strings (that is, when using the Python API), omit the ``KEY_`` prefix.

In addition to common parameters for both VPU plugins, the HDDL plugin accepts the following options:

.. list-table::
    :header-rows: 1

    * - Parameter Name
      - Parameter Values
      - Default
      - Description
    * - KEY_PERF_COUNT
      - YES/NO
      - NO
      - Enable performance counter option.
    * - KEY_VPU_HDDL_GRAPH_TAG
      - string
      - empty string
      - Allows to execute network on specified count of devices.
    * - KEY_VPU_HDDL_STREAM_ID
      - string
      - empty string
      - Allows to execute inference on a specified device.
    * - KEY_VPU_HDDL_DEVICE_TAG
      - string
      - empty string
      - Allows to allocate/deallocate networks on specified devices.
    * - KEY_VPU_HDDL_BIND_DEVICE
      - YES/NO
      - NO
      - Whether the network should bind to a device. Refer to vpu_plugin_config.hpp.
    * - KEY_VPU_HDDL_RUNTIME_PRIORITY
      - signed int
      - 0
      - Specify the runtime priority of a device among all devices running the same network. Refer to vpu_plugin_config.hpp.

See Also
~~~~~~~~

* :ref:`Supported Devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`

* :ref:`VPU Plugins <doxid-openvino_docs__o_v__u_g_supported_plugins__v_p_u>`

* :ref:`MYRIAD Plugin <doxid-openvino_docs__o_v__u_g_supported_plugins__m_y_r_i_a_d>`

