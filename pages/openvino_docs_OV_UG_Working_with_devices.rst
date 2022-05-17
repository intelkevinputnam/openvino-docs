.. index:: pair: page; Working with devices
.. _doxid-openvino_docs__o_v__u_g__working_with_devices:


Working with devices
====================

:target:`doxid-openvino_docs__o_v__u_g__working_with_devices_1md_openvino_docs_ov_runtime_ug_supported_plugins_device_plugins`





.. toctree::
   :maxdepth: 1
   :hidden:

   openvino_docs_OV_UG_query_api
   openvino_docs_OV_UG_supported_plugins_CPU
   openvino_docs_OV_UG_supported_plugins_GPU
   openvino_docs_OV_UG_supported_plugins_VPU
   openvino_docs_OV_UG_supported_plugins_GNA
   openvino_docs_OV_UG_supported_plugins_ARM_CPU

The OpenVINO Runtime provides capabilities to infer deep learning models on the following device types with corresponding plugins:

.. list-table::
    :header-rows: 1

    * - Plugin
      - Device types
    * - :ref:`CPU <doxid-openvino_docs__o_v__u_g_supported_plugins__c_p_u>`
      - Intel® Xeon®, Intel® Core™ and Intel® Atom® processors with Intel® Streaming SIMD Extensions (Intel® SSE4.2), Intel® Advanced Vector Extensions 2 (Intel® AVX2), Intel® Advanced Vector Extensions 512 (Intel® AVX-512), Intel® Vector Neural Network Instructions (Intel® AVX512-VNNI) and bfloat16 extension for AVX-512 (Intel® AVX-512_BF16 Extension)
    * - :ref:`GPU <doxid-openvino_docs__o_v__u_g_supported_plugins__g_p_u>`
      - Intel® Graphics, including Intel® HD Graphics, Intel® UHD Graphics, Intel® Iris® Graphics, Intel® Xe Graphics, Intel® Xe MAX Graphics
    * - :ref:`VPUs <doxid-openvino_docs__o_v__u_g_supported_plugins__v_p_u>`
      - Intel® Neural Compute Stick 2 powered by the Intel® Movidius™ Myriad™ X, Intel® Vision Accelerator Design with Intel® Movidius™ VPUs
    * - :ref:`GNA <doxid-openvino_docs__o_v__u_g_supported_plugins__g_n_a>`
      - `Intel® Speech Enabling Developer Kit <https://www.intel.com/content/www/us/en/support/articles/000026156/boards-and-kits/smart-home.html>`__ ; `Amazon Alexa\* Premium Far-Field Developer Kit <https://developer.amazon.com/en-US/alexa/alexa-voice-service/dev-kits/amazon-premium-voice>`__ ; `Intel® Pentium® Silver Processors N5xxx, J5xxx and Intel® Celeron® Processors N4xxx, J4xxx (formerly codenamed Gemini Lake) <https://ark.intel.com/content/www/us/en/ark/products/codename/83915/gemini-lake.html>`__ : `Intel® Pentium® Silver J5005 Processor <https://ark.intel.com/content/www/us/en/ark/products/128984/intel-pentium-silver-j5005-processor-4m-cache-up-to-2-80-ghz.html>`__ , `Intel® Pentium® Silver N5000 Processor <https://ark.intel.com/content/www/us/en/ark/products/128990/intel-pentium-silver-n5000-processor-4m-cache-up-to-2-70-ghz.html>`__ , `Intel® Celeron® J4005 Processor <https://ark.intel.com/content/www/us/en/ark/products/128992/intel-celeron-j4005-processor-4m-cache-up-to-2-70-ghz.html>`__ , `Intel® Celeron® J4105 Processor <https://ark.intel.com/content/www/us/en/ark/products/128989/intel-celeron-j4105-processor-4m-cache-up-to-2-50-ghz.html>`__ , `Intel® Celeron® J4125 Processor <https://ark.intel.com/content/www/us/en/ark/products/197305/intel-celeron-processor-j4125-4m-cache-up-to-2-70-ghz.html>`__ , `Intel® Celeron® Processor N4100 <https://ark.intel.com/content/www/us/en/ark/products/128983/intel-celeron-processor-n4100-4m-cache-up-to-2-40-ghz.html>`__ , `Intel® Celeron® Processor N4000 <https://ark.intel.com/content/www/us/en/ark/products/128988/intel-celeron-processor-n4000-4m-cache-up-to-2-60-ghz.html>`__ ; `Intel® Pentium® Processors N6xxx, J6xxx, Intel® Celeron® Processors N6xxx, J6xxx and Intel Atom® x6xxxxx (formerly codenamed Elkhart Lake) <https://ark.intel.com/content/www/us/en/ark/products/codename/128825/products-formerly-elkhart-lake.html>`__ ; `Intel® Core™ Processors (formerly codenamed Cannon Lake) <https://ark.intel.com/content/www/us/en/ark/products/136863/intel-core-i3-8121u-processor-4m-cache-up-to-3-20-ghz.html>`__ ; `10th Generation Intel® Core™ Processors (formerly codenamed Ice Lake) <https://ark.intel.com/content/www/us/en/ark/products/codename/74979/ice-lake.html>`__ : `Intel® Core™ i7-1065G7 Processor <https://ark.intel.com/content/www/us/en/ark/products/196597/intel-core-i71065g7-processor-8m-cache-up-to-3-90-ghz.html>`__ , `Intel® Core™ i7-1060G7 Processor <https://ark.intel.com/content/www/us/en/ark/products/197120/intel-core-i71060g7-processor-8m-cache-up-to-3-80-ghz.html>`__ , `Intel® Core™ i5-1035G4 Processor <https://ark.intel.com/content/www/us/en/ark/products/196591/intel-core-i51035g4-processor-6m-cache-up-to-3-70-ghz.html>`__ , `Intel® Core™ i5-1035G7 Processor <https://ark.intel.com/content/www/us/en/ark/products/196592/intel-core-i51035g7-processor-6m-cache-up-to-3-70-ghz.html>`__ , `Intel® Core™ i5-1035G1 Processor <https://ark.intel.com/content/www/us/en/ark/products/196603/intel-core-i51035g1-processor-6m-cache-up-to-3-60-ghz.html>`__ , `Intel® Core™ i5-1030G7 Processor <https://ark.intel.com/content/www/us/en/ark/products/197119/intel-core-i51030g7-processor-6m-cache-up-to-3-50-ghz.html>`__ , `Intel® Core™ i5-1030G4 Processor <https://ark.intel.com/content/www/us/en/ark/products/197121/intel-core-i51030g4-processor-6m-cache-up-to-3-50-ghz.html>`__ , `Intel® Core™ i3-1005G1 Processor <https://ark.intel.com/content/www/us/en/ark/products/196588/intel-core-i31005g1-processor-4m-cache-up-to-3-40-ghz.html>`__ , `Intel® Core™ i3-1000G1 Processor <https://ark.intel.com/content/www/us/en/ark/products/197122/intel-core-i31000g1-processor-4m-cache-up-to-3-20-ghz.html>`__ , `Intel® Core™ i3-1000G4 Processor <https://ark.intel.com/content/www/us/en/ark/products/197123/intel-core-i31000g4-processor-4m-cache-up-to-3-20-ghz.html>`__ ; `11th Generation Intel® Core™ Processors (formerly codenamed Tiger Lake) <https://ark.intel.com/content/www/us/en/ark/products/codename/88759/tiger-lake.html>`__ ; `12th Generation Intel® Core™ Processors (formerly codenamed Alder Lake) <https://ark.intel.com/content/www/us/en/ark/products/codename/147470/products-formerly-alder-lake.html>`__
    * - :ref:`Arm® CPU <doxid-openvino_docs__o_v__u_g_supported_plugins__a_r_m__c_p_u>`
      - Raspberry Pi™ 4 Model B, Apple® Mac mini with M1 chip, NVIDIA® Jetson Nano™, Android™ devices

OpenVINO Runtime also offers several execution modes which work on top of other devices:

.. list-table::
    :header-rows: 1

    * - Capability
      - Description
    * - :ref:`Multi-Device execution <doxid-openvino_docs__o_v__u_g__running_on_multiple_devices>`
      - Multi-Device enables simultaneous inference of the same model on several devices in parallel
    * - :ref:`Auto-Device selection <doxid-openvino_docs__o_v__u_g_supported_plugins__a_u_t_o>`
      - Auto-Device selection enables selecting Intel device for inference automatically
    * - :ref:`Heterogeneous execution <doxid-openvino_docs__o_v__u_g__hetero_execution>`
      - Heterogeneous execution enables automatic inference splitting between several devices (for example if a device doesn't `support certain operation <#supported-layers>`__ )
    * - :ref:`Automatic Batching <doxid-openvino_docs__o_v__u_g__automatic__batching>`
      - the Auto-Batching plugin enables batching (on top of the specified device) that is completely transparent to the application

Devices similar to the ones we use for benchmarking can be accessed using `Intel® DevCloud for the Edge <https://devcloud.intel.com/edge/>`__, a remote development environment with access to Intel® hardware and the latest versions of the Intel® Distribution of the OpenVINO™ Toolkit. `Learn more <https://devcloud.intel.com/edge/get_started/devcloud/>`__ or `Register here <https://inteliot.force.com/DevcloudForEdge/s/>`__.

:target:`doxid-openvino_docs__o_v__u_g__working_with_devices_1features_support_matrix`

Feature Support Matrix
~~~~~~~~~~~~~~~~~~~~~~

The table below demonstrates support of key features by OpenVINO device plugins.

.. list-table::
    :header-rows: 1

    * - Capability
      - :ref:`CPU <doxid-openvino_docs__o_v__u_g_supported_plugins__c_p_u>`
      - :ref:`GPU <doxid-openvino_docs__o_v__u_g_supported_plugins__g_p_u>`
      - :ref:`GNA <doxid-openvino_docs__o_v__u_g_supported_plugins__g_n_a>`
      - :ref:`Arm® CPU <doxid-openvino_docs__o_v__u_g_supported_plugins__a_r_m__c_p_u>`
    * - :ref:`Heterogeneous execution <doxid-openvino_docs__o_v__u_g__hetero_execution>`
      - Yes
      - Yes
      - No
      - Yes
    * - :ref:`Multi-device execution <doxid-openvino_docs__o_v__u_g__running_on_multiple_devices>`
      - Yes
      - Yes
      - Partial
      - Yes
    * - :ref:`Automatic batching <doxid-openvino_docs__o_v__u_g__automatic__batching>`
      - No
      - Yes
      - No
      - No
    * - :ref:`Multi-stream execution <doxid-openvino_docs_deployment_optimization_guide_tput>`
      - Yes
      - Yes
      - No
      - Yes
    * - :ref:`Models caching <doxid-openvino_docs__o_v__u_g__model_caching_overview>`
      - Yes
      - Partial
      - Yes
      - No
    * - :ref:`Dynamic shapes <doxid-openvino_docs__o_v__u_g__dynamic_shapes>`
      - Yes
      - Partial
      - No
      - No
    * - :ref:`Import/Export <doxid-openvino_inference_engine_tools_compile_tool__r_e_a_d_m_e>`
      - Yes
      - No
      - Yes
      - No
    * - :ref:`Preprocessing acceleration <doxid-openvino_docs__o_v__u_g__preprocessing__overview>`
      - Yes
      - Yes
      - No
      - Partial
    * - :ref:`Stateful models <doxid-openvino_docs__o_v__u_g_network_state_intro>`
      - Yes
      - No
      - Yes
      - No
    * - :ref:`Extensibility <doxid-openvino_docs__extensibility__u_g__intro>`
      - Yes
      - Yes
      - No
      - No

For more details on plugin-specific feature limitations, refer to the corresponding plugin pages.

