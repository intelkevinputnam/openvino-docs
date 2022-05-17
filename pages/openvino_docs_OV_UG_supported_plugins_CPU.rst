.. index:: pair: page; CPU device
.. _doxid-openvino_docs__o_v__u_g_supported_plugins__c_p_u:


CPU device
==========

:target:`doxid-openvino_docs__o_v__u_g_supported_plugins__c_p_u_1md_openvino_docs_ov_runtime_ug_supported_plugins_cpu` The CPU plugin is a part of the Intel® Distribution of OpenVINO™ toolkit and is developed to achieve high performance inference of neural networks on Intel® x86-64 CPUs. For an in-depth description of the plugin, see:

* `CPU plugin developers documentation <https://github.com/openvinotoolkit/openvino/wiki/CPUPluginDevelopersDocs>`__

* `OpenVINO Runtime CPU plugin source files <https://github.com/openvinotoolkit/openvino/tree/master/src/plugins/intel_cpu/>`__

Device name
~~~~~~~~~~~

The CPU device plugin uses the label of ``"CPU"`` and is the only device of this kind, even if multiple sockets are present on the platform. On multi-socket platforms, load balancing and memory usage distribution between NUMA nodes are handled automatically.

In order to use CPU for inference the device name should be passed to the ``:ref:`ov::Core::compile_model() <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>``` method:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>`("model.xml");
	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "CPU");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	from openvino.runtime import Core
	
	core = Core()
	model = core.read_model("model.xml")
	compiled_model = core.compile_model(model, "CPU")





.. raw:: html

   </div>







.. raw:: html

   </div>





Supported inference data types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CPU device plugin supports the following data types as inference precision of internal primitives:

* Floating-point data types:
  
  * f32
  
  * bf16

* Integer data types:
  
  * i32

* Quantized data types:
  
  * u8
  
  * i8
  
  * u1

:ref:`Hello Query Device C++ Sample <doxid-openvino_inference_engine_samples_hello_query_device__r_e_a_d_m_e>` can be used to print out the supported data types for all detected devices.

Quantized data type specifics
-----------------------------

Selected precision of each primitive depends on the operation precision in IR, quantization primitives, and available hardware capabilities. u1/u8/i8 data types are used for quantized operations only, i.e. those are not selected automatically for non-quantized operations.

See the :ref:`low-precision optimization guide <doxid-openvino_docs_model_optimization_guide>` for more details on how to get a quantized model.

.. note:: Platforms that do not support Intel® AVX512-VNNI have a known "saturation issue" which in some cases leads to reduced computational accuracy for u8/i8 precision calculations. See the :ref:`saturation (overflow) issue section <doxid-pot_saturation_issue>` to get more information on how to detect such issues and find possible workarounds.

Floating point data type specifics
----------------------------------

The default floating-point precision of a CPU primitive is f32. To support f16 IRs, the plugin internally converts all the f16 values to f32 and all the calculations are performed using the native f32 precision. On platforms that natively support bfloat16 calculations (have AVX512_BF16 extension), the bf16 type is automatically used instead of f32 to achieve better performance, thus no special steps are required to run a model with bf16 precision. See the `BFLOAT16 – Hardware Numerics Definition white paper <https://software.intel.com/content/dam/develop/external/us/en/documents/bf16-hardware-numerics-definition-white-paper.pdf>`__ for more details about bfloat16.

Using bf16 provides the following performance benefits:

* Faster multiplication of two bfloat16 numbers because of shorter mantissa of bfloat16 data.

* Reduced memory consumption since bfloat16 data is half the size of 32-bit float.

To check if the CPU device can support the bfloat16 data type use the :ref:`query device properties interface <doxid-openvino_docs__o_v__u_g_query_api>` to query :ref:`ov::device::capabilities <doxid-group__ov__runtime__cpp__prop__api_1gadb13d62787fc4485733329f044987294>` property, which should contain ``BF16`` in the list of CPU capabilities:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	auto cpuOptimizationCapabilities = core.:ref:`get_property <doxid-classov_1_1_core_1a4fb9fc7375d04f744a27a9588cbcff1a>`("CPU", :ref:`ov::device::capabilities <doxid-group__ov__runtime__cpp__prop__api_1gadb13d62787fc4485733329f044987294>`);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core = Core()
	cpu_optimization_capabilities = core.get_property("CPU", "OPTIMIZATION_CAPABILITIES")





.. raw:: html

   </div>







.. raw:: html

   </div>



If the model has been converted to bf16, :ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>` is set to :ref:`ov::element::bf16 <doxid-group__ov__element__cpp__api_1ga57b838ff7f62e66151e0b53b24c27819>` and can be checked via :ref:`ov::CompiledModel::get_property <doxid-classov_1_1_compiled_model_1a109d701ffe8b5de096961c7c98ff0bed>` call. The code below demonstrates how to get the element type:

.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	auto network = core.:ref:`read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>`("sample.xml");
	auto exec_network = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(network, "CPU");
	auto :ref:`inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>` = exec_network.get_property(:ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>`);

To infer the model in f32 instead of bf16 on targets with native bf16 support, set the :ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>` to :ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	core.:ref:`set_property <doxid-classov_1_1_core_1aa953cb0a1601dbc9a34ef6ba82b8476e>`("CPU", :ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>`(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`));





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core = Core()
	core.set_property("CPU", {"INFERENCE_PRECISION_HINT": "f32"})





.. raw:: html

   </div>







.. raw:: html

   </div>



Bfloat16 software simulation mode is available on CPUs with Intel® AVX-512 instruction set which does not support the native ``avx512_bf16`` instruction. This mode is used for development purposes and it does not guarantee good performance. To enable the simulation, you have to explicitly set :ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>` to :ref:`ov::element::bf16 <doxid-group__ov__element__cpp__api_1ga57b838ff7f62e66151e0b53b24c27819>`.

.. note:: An exception is thrown if :ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>` is set to :ref:`ov::element::bf16 <doxid-group__ov__element__cpp__api_1ga57b838ff7f62e66151e0b53b24c27819>` on a CPU without native bfloat16 support or bfloat16 simulation mode.

.. note:: Due to the reduced mantissa size of the bfloat16 data type, the resulting bf16 inference accuracy may differ from the f32 inference, especially for models that were not trained using the bfloat16 data type. If the bf16 inference accuracy is not acceptable, it is recommended to switch to the f32 precision.

Supported features
~~~~~~~~~~~~~~~~~~

Multi-device execution
----------------------

If a machine has OpenVINO-supported devices other than the CPU (for example an integrated GPU), then any supported model can be executed on CPU and all the other devices simultaneously. This can be achieved by specifying ``"MULTI:CPU,GPU.0"`` as a target device in case of simultaneous usage of CPU and GPU.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>`("model.xml");
	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "MULTI:CPU,GPU.0");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core = Core()
	model = core.read_model("model.xml")
	compiled_model = core.compile_model(model, "MULTI:CPU,GPU.0")





.. raw:: html

   </div>







.. raw:: html

   </div>



See :ref:`Multi-device execution page <doxid-openvino_docs__o_v__u_g__running_on_multiple_devices>` for more details.

Multi-stream execution
----------------------

If either ``ov::num_streams(n_streams)`` with ``n_streams > 1`` or the ``ov::hint::performance_mode(ov::hint::PerformanceMode::THROUGHPUT)`` property is set for the CPU plugin, multiple streams are created for the model. In the case of the CPU plugin, each stream has its own host thread, which means that incoming infer requests can be processed simultaneously. Each stream is pinned to its own group of physical cores with respect to NUMA nodes physical memory usage to minimize overhead on data transfer between NUMA nodes.

See :ref:`optimization guide <doxid-openvino_docs_deployment_optimization_guide_dldt_optimization_guide>` for more details.

.. note:: When it comes to latency, keep in mind that running only one stream on a multi-socket platform may introduce additional overheads on data transfer between NUMA nodes. In that case it is better to use ov::hint::PerformanceMode::LATENCY performance hint (please see :ref:`performance hints overview <doxid-openvino_docs__o_v__u_g__performance__hints>` for details).

Dynamic shapes
--------------

The CPU device plugin provides full functional support for models with dynamic shapes in terms of the opset coverage.

.. note:: CPU does not support tensors with a dynamically changing rank. If you try to infer a model with such tensors, an exception will be thrown.

Dynamic shapes support introduces additional overhead on memory management and may limit internal runtime optimizations. The more degrees of freedom are used, the more difficult it is to achieve the best performance. The most flexible configuration and the most convenient approach is the fully undefined shape, where no constraints to the shape dimensions are applied. But reducing the level of uncertainty brings gains in performance. You can reduce memory consumption through memory reuse and achieve better cache locality, leading to better inference performance, if you explicitly set dynamic shapes with defined upper bounds.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>`("model.xml");

	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape({{:ref:`ov::Dimension <doxid-classov_1_1_dimension>`(1, 10), :ref:`ov::Dimension <doxid-classov_1_1_dimension>`(1, 20), :ref:`ov::Dimension <doxid-classov_1_1_dimension>`(1, 30), :ref:`ov::Dimension <doxid-classov_1_1_dimension>`(1, 40)}});





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core = Core()
	model = core.read_model("model.xml")
	model.reshape([(1, 10), (1, 20), (1, 30), (1, 40)])





.. raw:: html

   </div>







.. raw:: html

   </div>





.. note:: Using fully undefined shapes may result in significantly higher memory consumption compared to inferring the same model with static shapes. If the level of memory consumption is unacceptable but dynamic shapes are still required, you can reshape the model using shapes with defined upper bounds to reduce memory footprint.

Some runtime optimizations work better if the model shapes are known in advance. Therefore, if the input data shape is not changed between inference calls, it is recommended to use a model with static shapes or reshape the existing model with the static input shape to get the best performance.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>`("model.xml");
	:ref:`ov::Shape <doxid-classov_1_1_shape>` static_shape = {10, 20, 30, 40};

	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape(static_shape);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core = Core()
	model = core.read_model("model.xml")
	model.reshape([10, 20, 30, 40])





.. raw:: html

   </div>







.. raw:: html

   </div>



See :ref:`dynamic shapes guide <doxid-openvino_docs__o_v__u_g__dynamic_shapes>` for more details.

Preprocessing acceleration
--------------------------

CPU plugin supports a full set of the preprocessing operations, providing high performance implementations for them.

See :ref:`preprocessing API guide <doxid-openvino_docs__o_v__u_g__preprocessing__overview>` for more details.

.. dropdown:: The CPU plugin support for handling tensor precision conversion is limited to the following ov::element types:

    * bf16
    * f16
    * f32
    * f64
    * i8
    * i16
    * i32
    * i64
    * u8
    * u16
    * u32
    * u64
    * boolean

Model caching
-------------

The CPU device plugin supports Import/Export network capability. If model caching is enabled via the common OpenVINO™ ``:ref:`ov::cache_dir <doxid-group__ov__runtime__cpp__prop__api_1ga3276fc4ed7cc7d0bbdcf0ae12063728d>``` property, the plugin will automatically create a cached blob inside the specified directory during model compilation. This cached blob contains partial representation of the network, having performed common runtime optimizations and low precision transformations. At the next attempt to compile the model, the cached representation will be loaded to the plugin instead of the initial IR, so the aforementioned steps will be skipped. These operations take a significant amount of time during model compilation, so caching their results makes subsequent compilations of the model much faster, thus reducing first inference latency (FIL).

See :ref:`model caching overview <doxid-openvino_docs__o_v__u_g__model_caching_overview>` for more details.

Extensibility
-------------

The CPU device plugin supports fallback on ``ov::Op`` reference implementation if it lacks own implementation of such operation. This means that :ref:`OpenVINO™ Extensibility Mechanism <doxid-openvino_docs__extensibility__u_g__intro>` can be used for the plugin extension as well. To enable fallback on a custom operation implementation, override the ``ov::Op::evaluate`` method in the derived operation class (see :ref:`custom OpenVINO™ operations <doxid-openvino_docs__extensibility__u_g_add_openvino_ops>` for details).

.. note:: At the moment, custom operations with internal dynamism (when the output tensor shape can only be determined as a result of performing the operation) are not supported by the plugin.

Stateful models
---------------

The CPU device plugin supports stateful models without any limitations.

See :ref:`stateful models guide <doxid-openvino_docs__o_v__u_g_network_state_intro>` for details.

Supported properties
~~~~~~~~~~~~~~~~~~~~

The plugin supports the following properties:

Read-write properties
---------------------

All parameters must be set before calling ``:ref:`ov::Core::compile_model() <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>``` in order to take effect or passed as additional argument to ``:ref:`ov::Core::compile_model() <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>```

* :ref:`ov::enable_profiling <doxid-group__ov__runtime__cpp__prop__api_1gafc5bef2fc2b5cfb5a0709cfb04346438>`

* :ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>`

* :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`

* ov::hint::num_request

* :ref:`ov::num_streams <doxid-group__ov__runtime__cpp__prop__api_1ga6c63a0223565f650475450fdb466bc0c>`

* :ref:`ov::affinity <doxid-group__ov__runtime__cpp__prop__api_1ga9c99a177a56685a70875302c59541887>`

* :ref:`ov::inference_num_threads <doxid-group__ov__runtime__cpp__prop__api_1gae73c9d9977901744090317e2afe09440>`

Read-only properties
--------------------

* :ref:`ov::cache_dir <doxid-group__ov__runtime__cpp__prop__api_1ga3276fc4ed7cc7d0bbdcf0ae12063728d>`

* :ref:`ov::supported_properties <doxid-group__ov__runtime__cpp__prop__api_1ga097f1274f26f3f4e1aa4fc3928748592>`

* :ref:`ov::available_devices <doxid-group__ov__runtime__cpp__prop__api_1gac4d3e86ef4fc43b1a80ec28c7be39ef1>`

* :ref:`ov::range_for_async_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga3549425153790834c212d905b8216196>`

* :ref:`ov::range_for_streams <doxid-group__ov__runtime__cpp__prop__api_1ga8a5d84196f6873729167aa512c34a94a>`

* :ref:`ov::device::full_name <doxid-group__ov__runtime__cpp__prop__api_1gaabacd9ea113b966be7b53b1d70fd6f42>`

* :ref:`ov::device::capabilities <doxid-group__ov__runtime__cpp__prop__api_1gadb13d62787fc4485733329f044987294>`

External dependencies
~~~~~~~~~~~~~~~~~~~~~

For some performance-critical DL operations, the CPU plugin uses optimized implementations from the oneAPI Deep Neural Network Library (`oneDNN <https://github.com/oneapi-src/oneDNN>`__).

.. dropdown:: The following operations are implemented using primitives from the OneDNN library:

    * AvgPool
    * Concat
    * Convolution
    * ConvolutionBackpropData
    * GroupConvolution
    * GroupConvolutionBackpropData
    * GRUCell
    * GRUSequence
    * LRN
    * LSTMCell
    * LSTMSequence
    * MatMul
    * MaxPool
    * RNNCell
    * RNNSequence
    * SoftMax

See Also
~~~~~~~~

* :ref:`Supported Devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`

* :ref:`Optimization guide <doxid-openvino_docs_optimization_guide_dldt_optimization_guide>`

* `СPU plugin developers documentation <https://github.com/openvinotoolkit/openvino/wiki/CPUPluginDevelopersDocs>`__

