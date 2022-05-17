.. index:: pair: page; Hello Query Device C++ Sample
.. _doxid-openvino_inference_engine_samples_hello_query_device__r_e_a_d_m_e:


Hello Query Device C++ Sample
=============================

:target:`doxid-openvino_inference_engine_samples_hello_query_device__r_e_a_d_m_e_1md_openvino_samples_cpp_hello_query_device_readme` This sample demonstrates how to execute an query OpenVINO™ Runtime devices, prints their metrics and default configuration values, using :ref:`Properties API <doxid-openvino_docs__o_v__u_g_query_api>`.

The following C++ API is used in the application:

.. list-table::
    :header-rows: 1

    * - Feature
      - API
      - Description
    * - Available Devices
      - ``:ref:`ov::Core::get_available_devices <doxid-classov_1_1_core_1ac4efa134a1f874cffa38c7f48f222e3a>``` , ``:ref:`ov::Core::get_property <doxid-classov_1_1_core_1a4fb9fc7375d04f744a27a9588cbcff1a>```
      - Get available devices information and configuration for inference

Basic OpenVINO™ Runtime API is covered by :ref:`Hello Classification C++ sample <doxid-openvino_inference_engine_samples_hello_classification__r_e_a_d_m_e>`.

.. list-table::
    :header-rows: 1

    * - Options
      - Values
    * - Supported devices
      - :ref:`All <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`
    * - Other language realization
      - :ref:`Python <doxid-openvino_inference_engine_ie_bridges_python_sample_hello_query_device__r_e_a_d_m_e>`

How It Works
~~~~~~~~~~~~

The sample queries all available OpenVINO™ Runtime devices, prints their supported metrics and plugin configuration parameters.

Building
~~~~~~~~

To build the sample, please use instructions available at :ref:`Build the Sample Applications <doxid-openvino_docs__o_v__u_g__samples__overview>` section in OpenVINO™ Toolkit Samples guide.

Running
~~~~~~~

To see quired information, run the following:

.. ref-code-block:: cpp

	hello_query_device

Sample Output
~~~~~~~~~~~~~

The application prints all available devices with their supported metrics and default values for configuration parameters:

.. ref-code-block:: cpp

	[ INFO ] OpenVINO Runtime version ......... <version>
	[ INFO ] Build ........... <build>
	[ INFO ]
	[ INFO ] Available devices:
	[ INFO ] CPU
	[ INFO ]        SUPPORTED_METRICS:
	[ INFO ]                AVAILABLE_DEVICES : [  ]
	[ INFO ]                FULL_DEVICE_NAME : Intel(R) Core(TM) i5-8350U CPU @ 1.70GHz
	[ INFO ]                OPTIMIZATION_CAPABILITIES : [ FP32 FP16 INT8 BIN ]
	[ INFO ]                RANGE_FOR_ASYNC_INFER_REQUESTS : { 1, 1, 1 }
	[ INFO ]                RANGE_FOR_STREAMS : { 1, 8 }
	[ INFO ]                IMPORT_EXPORT_SUPPORT : true
	[ INFO ]        SUPPORTED_CONFIG_KEYS (default values):
	[ INFO ]                CACHE_DIR : ""
	[ INFO ]                CPU_BIND_THREAD : NO
	[ INFO ]                CPU_THREADS_NUM : 0
	[ INFO ]                CPU_THROUGHPUT_STREAMS : 1
	[ INFO ]                DUMP_EXEC_GRAPH_AS_DOT : ""
	[ INFO ]                DYN_BATCH_ENABLED : NO
	[ INFO ]                DYN_BATCH_LIMIT : 0
	[ INFO ]                ENFORCE_BF16 : NO
	[ INFO ]                EXCLUSIVE_ASYNC_REQUESTS : NO
	[ INFO ]                PERFORMANCE_HINT : ""
	[ INFO ]                PERFORMANCE_HINT_NUM_REQUESTS : 0
	[ INFO ]                PERF_COUNT : NO
	[ INFO ]
	[ INFO ] GNA
	[ INFO ]        SUPPORTED_METRICS:
	[ INFO ]                AVAILABLE_DEVICES : [ GNA_SW_EXACT ]
	[ INFO ]                OPTIMAL_NUMBER_OF_INFER_REQUESTS : 1
	[ INFO ]                FULL_DEVICE_NAME : GNA_SW_EXACT
	[ INFO ]                GNA_LIBRARY_FULL_VERSION : 3.0.0.1455
	[ INFO ]                IMPORT_EXPORT_SUPPORT : true
	[ INFO ]        SUPPORTED_CONFIG_KEYS (default values):
	[ INFO ]                EXCLUSIVE_ASYNC_REQUESTS : NO
	[ INFO ]                GNA_COMPACT_MODE : YES
	[ INFO ]                GNA_COMPILE_TARGET : ""
	[ INFO ]                GNA_DEVICE_MODE : GNA_SW_EXACT
	[ INFO ]                GNA_EXEC_TARGET : ""
	[ INFO ]                GNA_FIRMWARE_MODEL_IMAGE : ""
	[ INFO ]                GNA_FIRMWARE_MODEL_IMAGE_GENERATION : ""
	[ INFO ]                GNA_LIB_N_THREADS : 1
	[ INFO ]                GNA_PRECISION : I16
	[ INFO ]                GNA_PWL_MAX_ERROR_PERCENT : 1.000000
	[ INFO ]                GNA_PWL_UNIFORM_DESIGN : NO
	[ INFO ]                GNA_SCALE_FACTOR : 1.000000
	[ INFO ]                GNA_SCALE_FACTOR_0 : 1.000000
	[ INFO ]                LOG_LEVEL : LOG_NONE
	[ INFO ]                PERF_COUNT : NO
	[ INFO ]                SINGLE_THREAD : YES

See Also
~~~~~~~~

* :ref:`Integrate the OpenVINO™ Runtime with Your Application <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>`

* :ref:`Using OpenVINO™ Toolkit Samples <doxid-openvino_docs__o_v__u_g__samples__overview>`

