.. index:: pair: page; High-level Performance Hints
.. _doxid-openvino_docs__o_v__u_g__performance__hints:


High-level Performance Hints
============================

:target:`doxid-openvino_docs__o_v__u_g__performance__hints_1md_openvino_docs_ov_runtime_ug_performance_hints` Each of OpenVINO's :ref:`supported devices <doxid-openvino_docs__o_v__u_g__working_with_devices>` offers low-level performance settings. Tweaking this detailed configuration requires deep architecture understanding. Also, while the performance may be optimal for the specific combination of the device and the inferred model, the resulting configuration is not necessarily optimal for another device or model. The OpenVINO performance hints are the new way to configure the performance with *portability* in mind. As the hints are supported by every OpenVINO device, this is a future-proof solution that is fully compatible with the :ref:`automatic device selection <doxid-openvino_docs__o_v__u_g_supported_plugins__a_u_t_o>`.

The hints also "reverse" the direction of the configuration in the right fashion: rather than map the application needs to the low-level performance settings, and keep an associated application logic to configure each possible device separately, the idea is to express a target scenario with a single config key and let the *device* to configure itself in response.

Previously, a certain level of automatic configuration was coming from the *default* values of the parameters. For example, the number of CPU streams was deduced from the number of CPU cores, when ``:ref:`ov::streams::AUTO <doxid-group__ov__runtime__cpp__prop__api_1gaddb29425af71fbb6ad3379c59342ff0e>``` (``CPU_THROUGHPUT_AUTO`` in the pre-OpenVINO 2.0 parlance) is set. However, the resulting number of streams didn't account for actual compute requirements of the model to be inferred. The hints, in contrast, respect the actual model, so the parameters for optimal throughput are calculated for each model individually (based on its compute versus memory bandwidth requirements and capabilities of the device).

Performance Hints: Latency and Throughput
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As discussed in the :ref:`Optimization Guide <doxid-openvino_docs_optimization_guide_dldt_optimization_guide>` there are a few different metrics associated with inference speed. Throughput and latency are some of the most widely used metrics that measure the overall performance of an application.

This is why, to ease the configuration of the device, OpenVINO offers two dedicated hints, namely ``ov::hint::PerformanceMode::THROUGHPUT`` and ``ov::hint::PerformanceMode::LATENCY``. A special ``ov::hint::PerformanceMode::UNDEFINED`` acts the same as specifying no hint.

Please also see the last section in this document on conducting performance measurements with the benchmark_app`.

Note that a typical model may take significantly more time to load with ``ov::hint::PerformanceMode::THROUGHPUT`` and consume much more memory, compared with ``ov::hint::PerformanceMode::LATENCY``.

Performance Hints: How It Works?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Internally, every device "translates" the value of the hint to the actual performance settings. For example the ``ov::hint::PerformanceMode::THROUGHPUT`` selects number of CPU or GPU streams. For the GPU, additionally the optimal batch size is selected and the :ref:`automatic batching <doxid-openvino_docs__o_v__u_g__automatic__batching>` is applied whenever possible (and also if the device supports that :ref:`refer to the devices/features support matrix <doxid-openvino_docs__o_v__u_g__working_with_devices>`).

The resulting (device-specific) settings can be queried back from the instance of the ``ov:Compiled_Model``.

Notice that the ``benchmark_app``, outputs the actual settings for the THROUGHPUT hint, please the bottom of the output example:

.. ref-code-block:: cpp

	$benchmark_app -hint tput -d CPU -m 'path to your favorite model'
	...
	[Step 8/11] Setting optimal runtime parameters
	[ INFO ] Device: CPU
	[ INFO ]   { PERFORMANCE_HINT , THROUGHPUT }
	...
	[ INFO ]   { OPTIMAL_NUMBER_OF_INFER_REQUESTS , 4 }
	[ INFO ]   { NUM_STREAMS , 4 }
	...

Using the Performance Hints: Basic API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the example code-snippet below the ``ov::hint::PerformanceMode::THROUGHPUT`` is specified for the ``:ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>``` property for the compile_model:





.. tab:: C++

    .. doxygensnippet:: docs/snippets/ov_auto_batching.cpp
       :language: cpp
       :fragment: [compile_model]

.. tab:: Python

    .. doxygensnippet:: docs/snippets/ov_auto_batching.py
       :language: python
       :fragment: [compile_model]

Additional (Optional) Hints from the App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's take an example of an application that processes 4 video streams. The most future-proof way to communicate the limitation of the parallel slack is to equip the performance hint with the optional ``ov::hint::num_requests`` configuration key set to 4. As discussed previosly, for the GPU this will limit the batch size, for the CPU - the number of inference streams, so each device uses the ``ov::hint::num_requests`` while converting the hint to the actual device configuration options:





.. tab:: C++

    .. doxygensnippet:: docs/snippets/ov_auto_batching.cpp
       :language: cpp
       :fragment: [hint_num_requests]

.. tab:: Python

    .. doxygensnippet:: docs/snippets/ov_auto_batching.py
       :language: python
       :fragment: [hint_num_requests]

Optimal Number of Inference Requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the hints assumes that the application queries the ``:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>``` to create and run the returned number of requests simultaneously:





.. tab:: C++

    .. doxygensnippet:: docs/snippets/ov_auto_batching.cpp
       :language: cpp
       :fragment: [query_optimal_num_requests]

.. tab:: Python

    .. doxygensnippet:: docs/snippets/ov_auto_batching.py
       :language: python
       :fragment: [query_optimal_num_requests]

While an application is free to create more requests if needed (for example to support asynchronous inputs population) it is very important to at least run the ``:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>``` of the inference requests in parallel, for efficiency (device utilization) reasons.

Also, notice that ``ov::hint::PerformanceMode::LATENCY`` does not necessarily imply using single inference request. For example, multi-socket CPUs can deliver as high number of requests (at the same minimal latency) as there are NUMA nodes the machine features. To make your application fully scalable, prefer to query the ``:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>``` directly.

Prefer Async API
~~~~~~~~~~~~~~~~

The API of the inference requests offers Sync and Async execution. While the ``:ref:`ov::InferRequest::infer() <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>``` is inherently synchronous and simple to operate (as it serializes the execution flow in the current application thread), the Async "splits" the ``infer()`` into ``:ref:`ov::InferRequest::start_async() <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>``` and use of the ``:ref:`ov::InferRequest::wait() <doxid-classov_1_1_infer_request_1ab0e0739da45789d816f8b5584a0b5691>``` (or callbacks). Please consider the :ref:`API examples <doxid-openvino_docs__o_v__u_g__infer_request>`. Although the Synchronous API can be somewhat easier to start with, in the production code always prefer to use the Asynchronous (callbacks-based) API, as it is the most general and scalable way to implement the flow control for any possible number of requests (and hence both latency and throughput scenarios).

Combining the Hints and Individual Low-Level Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While sacrificing the portability at a some extent, it is possible to combine the hints with individual device-specific settings. For example, you can let the device prepare a configuration ``ov::hint::PerformanceMode::THROUGHPUT`` while overriding any specific value:







.. tab:: C++

    .. doxygensnippet:: docs/snippets/ov_auto_batching.cpp
       :language: cpp
       :fragment: [hint_plus_low_level]

.. tab:: Python

    .. doxygensnippet:: docs/snippets/ov_auto_batching.py
       :language: python
       :fragment: [hint_plus_low_level]






Testing the Performance of The Hints with the Benchmark_App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``benchmark_app``, that exists in both :ref:`C++ <doxid-openvino_inference_engine_samples_benchmark_app__r_e_a_d_m_e>` and :ref:`Python <doxid-openvino_inference_engine_tools_benchmark_tool__r_e_a_d_m_e>` versions, is the best way to evaluate the performance of the performance hints for a particular device:

* benchmark_app **-hint tput** -d 'device' -m 'path to your model'

* benchmark_app **-hint latency** -d 'device' -m 'path to your model'

Disabling the hints to emulate the pre-hints era (highly recommended before trying the individual low-level settings, such as the number of streams as below, threads, etc):

* - benchmark_app **-hint none -nstreams 1** -d 'device' -m 'path to your model'

See Also
--------

:ref:`Supported Devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`

