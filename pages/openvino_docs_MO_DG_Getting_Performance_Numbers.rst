.. index:: pair: page; Getting Performance Numbers
.. _doxid-openvino_docs__m_o__d_g__getting__performance__numbers:


Getting Performance Numbers
===========================

:target:`doxid-openvino_docs__m_o__d_g__getting__performance__numbers_1md_openvino_docs_mo_dg_prepare_model_getting_performance_numbers`

Tip 1. Measure the Proper Set of Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When evaluating performance of your model with the OpenVINO Runtime, you must measure the proper set of operations. To do so, consider the following tips:

* Avoid including one-time costs like model loading.

* Track separately the operations that happen outside the OpenVINO Runtime, like video decoding.

.. note:: Some image pre-processing can be baked into the IR and accelerated accordingly. For more information, refer to :ref:`Embedding the Preprocessing <doxid-openvino_docs__m_o__d_g__additional__optimization__use__cases>`. Also consider `Runtime Optimizations of the Preprocessing <../../optimization_guide/dldt_deployment_optimization_common>`__.

Tip 2. Getting Credible Performance Numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to build your performance conclusions on reproducible data. Do the performance measurements with a large number of invocations of the same routine. Since the first iteration is almost always significantly slower than the subsequent ones, you can use an aggregated value for the execution time for final projections:

* If the warm-up run does not help or execution time still varies, you can try running a large number of iterations and then average or find a mean of the results.

* For time values that range too much, consider geomean.

* Beware of the throttling and other power oddities. A device can exist in one of several different power states. When optimizing your model, for better performance data reproducibility consider fixing the device frequency. However the end to end (application) benchmarking should be also performed under real operational conditions.

Tip 3. Measure Reference Performance Numbers with OpenVINO's benchmark_app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get performance numbers, use the dedicated :ref:`Benchmark App <doxid-openvino_inference_engine_samples_benchmark_app__r_e_a_d_m_e>` sample which is the best way to produce the performance reference. It has a lot of device-specific knobs, but the primary usage is as simple as:

.. ref-code-block:: cpp

	$ ./benchmark_app –d GPU –m <model> -i <input>

to measure the performance of the model on the GPU. Or

.. ref-code-block:: cpp

	$ ./benchmark_app –d CPU –m <model> -i <input>

to execute on the CPU instead.

Each of the :ref:`OpenVINO supported devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>` offers performance settings that have command-line equivalents in the :ref:`Benchmark App <doxid-openvino_inference_engine_samples_benchmark_app__r_e_a_d_m_e>`. While these settings provide really low-level control and allow to leverage the optimal model performance on the *specific* device, we suggest always starting the performance evaluation with the :ref:`OpenVINO High-Level Performance Hints <doxid-openvino_docs__o_v__u_g__performance__hints>` first:

* benchmark_app **-hint tput** -d 'device' -m 'path to your model'

* benchmark_app **-hint latency** -d 'device' -m 'path to your model'

Comparing Performance with Native/Framework Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When comparing the OpenVINO Runtime performance with the framework or another reference code, make sure that both versions are as similar as possible:

* Wrap exactly the inference execution (refer to the :ref:`Benchmark App <doxid-openvino_inference_engine_samples_benchmark_app__r_e_a_d_m_e>` for examples).

* Do not include model loading time.

* Ensure the inputs are identical for the OpenVINO Runtime and the framework. For example, beware of random values that can be used to populate the inputs.

* Consider :ref:`Image Pre-processing and Conversion <doxid-openvino_docs__o_v__u_g__preprocessing__overview>`, while any user-side pre-processing should be tracked separately.

* When applicable, leverage the :ref:`Dynamic Shapes support <doxid-openvino_docs__o_v__u_g__dynamic_shapes>`

* If possible, demand the same accuracy. For example, TensorFlow allows ``FP16`` execution, so when comparing to that, make sure to test the OpenVINO Runtime with the ``FP16`` as well.

.. _performance-counters:

Internal Inference Performance Counters and Execution Graphs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Further, finer-grained insights into inference performance breakdown can be achieved with device-specific performance counters and/or execution graphs. Both :ref:`C++ <doxid-openvino_inference_engine_samples_benchmark_app__r_e_a_d_m_e>` and :ref:`Python <doxid-openvino_inference_engine_tools_benchmark_tool__r_e_a_d_m_e>` versions of the ``benchmark_app`` supports a ``-pc`` command-line parameter that outputs internal execution breakdown.

For example, below is the part of performance counters for quantized `TensorFlow\* implementation of ResNet-50 <https://github.com/openvinotoolkit/open_model_zoo/tree/master/models/public/resnet-50-tf>`__ model inference on :ref:`CPU Plugin <doxid-openvino_docs__o_v__u_g_supported_plugins__c_p_u>`. Notice that since the device is CPU, the layers wall clock ``realTime`` and the ``cpu`` time are the same. Information about layer precision is also stored in the performance counters.

.. list-table::
    :header-rows: 1

    * - layerName
      - execStatus
      - layerType
      - execType
      - realTime (ms)
      - cpuTime (ms)
    * - resnet_model/batch_normalization_15/FusedBatchNorm/Add
      - EXECUTED
      - Convolution
      - jit_avx512_1x1_I8
      - 0.377
      - 0.377
    * - resnet_model/conv2d_16/Conv2D/fq_input_0
      - NOT_RUN
      - FakeQuantize
      - undef
      - 0
      - 0
    * - resnet_model/batch_normalization_16/FusedBatchNorm/Add
      - EXECUTED
      - Convolution
      - jit_avx512_I8
      - 0.499
      - 0.499
    * - resnet_model/conv2d_17/Conv2D/fq_input_0
      - NOT_RUN
      - FakeQuantize
      - undef
      - 0
      - 0
    * - resnet_model/batch_normalization_17/FusedBatchNorm/Add
      - EXECUTED
      - Convolution
      - jit_avx512_1x1_I8
      - 0.399
      - 0.399
    * - resnet_model/add_4/fq_input_0
      - NOT_RUN
      - FakeQuantize
      - undef
      - 0
      - 0
    * - resnet_model/add_4
      - NOT_RUN
      - Eltwise
      - undef
      - 0
      - 0
    * - resnet_model/add_5/fq_input_1
      - NOT_RUN
      - FakeQuantize
      - undef
      - 0
      - 0

The ``exeStatus`` column of the table includes possible values:

* ``EXECUTED`` - layer was executed by standalone primitive,

* ``NOT_RUN`` - layer was not executed by standalone primitive or was fused with another operation and executed in another layer primitive.

The ``execType`` column of the table includes inference primitives with specific suffixes. The layers have the following marks:

* Suffix ``I8`` for layers that had 8-bit data type input and were computed in 8-bit precision

* Suffix ``FP32`` for layers computed in 32-bit precision

All ``Convolution`` layers are executed in int8 precision. Rest layers are fused into Convolutions using post operations optimization technique, which is described in :ref:`Internal CPU Plugin Optimizations <doxid-openvino_docs__o_v__u_g_supported_plugins__c_p_u>`. This contains layers name (as seen in IR), layers type and execution statistics.

Both benchmark_app versions also support "exec_graph_path" command-line option governing the OpenVINO to output the same per-layer execution statistics, but in the form of the plugin-specific `Netron-viewable <https://netron.app/>`__ graph to the specified file.

Notice that on some devices, the execution graphs/counters may be pretty intrusive overhead-wise. Also, especially when performance-debugging the :ref:`latency case <doxid-openvino_docs_deployment_optimization_guide_latency>` notice that the counters do not reflect the time spent in the plugin/device/driver/etc queues. If the sum of the counters is too different from the latency of an inference request, consider testing with less inference requests. For example running single :ref:`OpenVINO stream <doxid-openvino_docs_deployment_optimization_guide_tput>` with multiple requests would produce nearly identical counters as running single inference request, yet the actual latency can be quite different.

Finally, the performance statistics with both performance counters and execution graphs is averaged, so such a data for the :ref:`dynamically-shaped inputs <doxid-openvino_docs__o_v__u_g__dynamic_shapes>` should be measured carefully (ideally by isolating the specific shape and executing multiple times in a loop, to gather the reliable data).

OpenVINO in general and individual plugins are heavily instrumented with Intel® instrumentation and tracing technology (ITT), so another option is to compile the OpenVINO from the source code with the ITT enabled and using tools like `Intel® VTune™ Profiler <https://software.intel.com/en-us/vtune>`__ to get detailed inference performance breakdown and additional insights in the application-level performance on the timeline view.

