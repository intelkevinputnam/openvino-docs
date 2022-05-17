.. index:: pair: page; Automatic Batching
.. _doxid-openvino_docs__o_v__u_g__automatic__batching:


Automatic Batching
==================

:target:`doxid-openvino_docs__o_v__u_g__automatic__batching_1md_openvino_docs_ov_runtime_ug_automatic_batching`

(Automatic) Batching Execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Automatic-Batching is a preview of the new functionality in the OpenVINO™ toolkit. It performs on-the-fly automatic batching (i.e. grouping inference requests together) to improve device utilization, with no programming effort from the user. Inputs gathering and outputs scattering from the individual inference requests required for the batch happen transparently, without affecting the application code.

The feature primarily targets existing code written for inferencing many requests (each instance with the batch size 1). To obtain corresponding performance improvements, the application must be *running many inference requests simultaneously*. As explained below, the auto-batching functionality can be also used via a special *virtual* device.

Batching is a straightforward way of leveraging the GPU compute power and saving on communication overheads. The automatic batching is *implicitly* triggered on the GPU when the ``ov::hint::PerformanceMode::THROUGHPUT`` is specified for the ``:ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>``` property for the compile_model or set_property calls.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GPU",
	    :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`(:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-namespace_inference_engine_1_1_plugin_config_params_1a0902fd7a7ca168b6a188daf4b75db92f>`));





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	config = {"PERFORMANCE_HINT": "THROUGHPUT"}
	compiled_model = core.compile_model(model, "GPU", config)





.. raw:: html

   </div>







.. raw:: html

   </div>

.. note:: You can disable the Auto-Batching (for example, for the GPU device) from being triggered by the ``ov::hint::PerformanceMode::THROUGHPUT``. To do that, pass the ``:ref:`ov::hint::allow_auto_batching <doxid-group__ov__runtime__cpp__prop__api_1ga445a111e7219955c585eb418d2f4f80d>``` set to **false** in addition to the ``:ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>``` :

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// disabling the automatic batching
	// leaving intact other configurations options that the device selects for the 'throughput' hint 
	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GPU", 
	    :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`(:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-namespace_inference_engine_1_1_plugin_config_params_1a0902fd7a7ca168b6a188daf4b75db92f>`),
	    :ref:`ov::hint::allow_auto_batching <doxid-group__ov__runtime__cpp__prop__api_1ga445a111e7219955c585eb418d2f4f80d>`(false));





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# disabling the automatic batching
	# leaving intact other configurations options that the device selects for the 'throughput' hint 
	config = {"PERFORMANCE_HINT": "THROUGHPUT",
	          "ALLOW_AUTO_BATCHING": False}
	compiled_model = core.compile_model(model, "GPU", config)





.. raw:: html

   </div>







.. raw:: html

   </div>

Alternatively, to enable the Auto-Batching in the legacy apps not akin to the notion of the performance hints, you may need to use the **explicit** device notion, such as 'BATCH:GPU'. In both cases (the *throughput* hint or explicit BATCH device), the optimal batch size selection happens automatically (the implementation queries the ``:ref:`ov::optimal_batch_size <doxid-group__ov__runtime__cpp__prop__api_1ga129bad2da2fc2a40a7d746d86fc9c68d>``` property from the device, passing the model's graph as the parameter). The actual value depends on the model and device specifics, for example, on-device memory for the dGPUs. Auto-Batching support is not limited to the GPUs, but if a device does not support the ``:ref:`ov::optimal_batch_size <doxid-group__ov__runtime__cpp__prop__api_1ga129bad2da2fc2a40a7d746d86fc9c68d>``` yet, it can work with the auto-batching only when specifying an explicit batch size, for example, "BATCH:<device>(16)".

This *automatic batch size selection* assumes that the application queries the ``:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>``` to create and run the returned number of requests simultaneously:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// when the batch size is automatically selected by the implementation
	// it is important to query/create and run the sufficient #requests
	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GPU",
	    :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`(:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-namespace_inference_engine_1_1_plugin_config_params_1a0902fd7a7ca168b6a188daf4b75db92f>`));
	auto num_requests = compiled_model.:ref:`get_property <doxid-classov_1_1_compiled_model_1a109d701ffe8b5de096961c7c98ff0bed>`(:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>`);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# when the batch size is automatically selected by the implementation
	# it is important to query/create and run the sufficient requests
	config = {"PERFORMANCE_HINT": "THROUGHPUT"}
	compiled_model = core.compile_model(model, "GPU", config)
	num_requests = compiled_model.get_property("OPTIMAL_NUMBER_OF_INFER_REQUESTS")





.. raw:: html

   </div>







.. raw:: html

   </div>



If not enough inputs were collected, the ``timeout`` value makes the transparent execution fall back to the execution of individual requests. Configuration-wise, this is the AUTO_BATCH_TIMEOUT property. The timeout, which adds itself to the execution time of the requests, heavily penalizes the performance. To avoid this, in cases when your parallel slack is bounded, give the OpenVINO an additional hint.

For example, the application processes only 4 video streams, so there is no need to use a batch larger than 4. The most future-proof way to communicate the limitations on the parallelism is to equip the performance hint with the optional ``ov::hint::num_requests`` configuration key set to 4. For the GPU this will limit the batch size, for the CPU - the number of inference streams, so each device uses the ``ov::hint::num_requests`` while converting the hint to the actual device configuration options:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// limiting the available parallel slack for the 'throughput' hint via the ov::hint::num_requests
	// so that certain parameters (like selected batch size) are automatically accommodated accordingly 
	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GPU",
	    :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`(:ref:`ov::hint::PerformanceMode::THROUGHPUT <doxid-namespace_inference_engine_1_1_plugin_config_params_1a0902fd7a7ca168b6a188daf4b75db92f>`),
	    ov::hint::num_requests(4));





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	config = {"PERFORMANCE_HINT": "THROUGHPUT",
	          "PERFORMANCE_HINT_NUM_REQUESTS": "4"}
	# limiting the available parallel slack for the 'throughput'
	# so that certain parameters (like selected batch size) are automatically accommodated accordingly 
	compiled_model = core.compile_model(model, "GPU", config)





.. raw:: html

   </div>







.. raw:: html

   </div>

For the *explicit* usage, you can limit the batch size using "BATCH:GPU(4)", where 4 is the number of requests running in parallel.

Other Performance Considerations
--------------------------------

To achieve the best performance with the Automatic Batching, the application should:

* Operate the number of inference requests that represents the multiple of the batch size. In the above example, for batch size 4, the application should operate 4, 8, 12, 16, etc. requests.

* Use the requests, grouped by the batch size, together. For example, the first 4 requests are inferred, while the second group of the requests is being populated. Essentially, the Automatic Batching shifts the asynchronousity from the individual requests to the groups of requests that constitute the batches.
  
  * Balance the 'timeout' value vs the batch size. For example, in many cases having a smaller timeout value/batch size may yield better performance than large batch size, but with the timeout value that is not large enough to accommodate the full number of the required requests.
  
  * When the Automatic Batching is enabled, the 'timeout' property of the ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` can be changed any time, even after model loading/compilation. For example, setting the value to 0 effectively disables the auto-batching, as requests' collection would be omitted.
  
  * Carefully apply the auto-batching to the pipelines. For example for the conventional video-sources->detection->classification flow, it is the most benefical to do auto-batching over the inputs to the detection stage. Whereas the resulting number of detections is usually fluent, which makes the auto-batching less applicable for the classification stage.

The following are limitations of the current implementations:

* Although less critical for the throughput-oriented scenarios, the load-time with auto-batching increases by almost 2x.

* Certain networks are not safely reshape-able by the "batching" dimension (specified as 'N' in the layouts terms). Also, if the batching dimension is not zero-th, the auto-batching is not triggered *implicitly* by the throughput hint.

* The *explicit* notion, for example, "BATCH:GPU", uses the relaxed dimensions tracking, often making the auto-batching possible. For example, this trick unlocks most **detection networks**.

* - When *forcing* the auto-batching via the explicit device notion, make sure to validate the results for correctness.

* Performance improvements happen at the cost of the memory footprint growth, yet the auto-batching queries the available memory (especially for the dGPUs) and limits the selected batch size accordingly.

Configuring the Automatic Batching
----------------------------------

Following the OpenVINO convention for devices names, the *batching* device is named *BATCH*. The configuration options are as follows:

.. list-table::
    :header-rows: 1

    * - Parameter name
      - Parameter description
      - Default
      - Examples
    * - "AUTO_BATCH_DEVICE"
      - Device name to apply the automatic batching and optional batch size in brackets
      - N/A
      - "BATCH:GPU" which triggers the automatic batch size selection. Another example is the device name (to apply the batching) with directly specified batch size "BATCH:GPU(4)"
    * - "AUTO_BATCH_TIMEOUT"
      - timeout value, in ms
      - 1000
      - you can reduce the timeout value (to avoid performance penalty when the data arrives too non-evenly) e.g. pass the "100", or in contrast make it large enough e.g. to accommodate inputs preparation (e.g. when it is serial process)

Testing Automatic Batching Performance with the Benchmark_App
-------------------------------------------------------------

The ``benchmark_app``, that exists in both :ref:`C++ <doxid-openvino_inference_engine_samples_benchmark_app__r_e_a_d_m_e>` and :ref:`Python <doxid-openvino_inference_engine_tools_benchmark_tool__r_e_a_d_m_e>` versions, is the best way to evaluate the performance of the Automatic Batching:

* The most straighforward way is performance hints:
  
  * benchmark_app **-hint tput** -d GPU -m 'path to your favorite model'

* Overriding the strict rules of implicit reshaping by the batch dimension via the explicit device notion:
  
  * benchmark_app **-hint none -d BATCH:GPU** -m 'path to your favorite model'

* Finally, overriding the automatically-deduced batch size as well:
  
  * $benchmark_app -hint none -d **BATCH:GPU(16)** -m 'path to your favorite model'
  
  * notice that some shell versions (e.g. ``bash``) may require adding quotes around complex device names, i.e. -d "BATCH:GPU(16)"

The last example is also applicable to the CPU or any other device that generally supports the batched execution.

See Also
--------

:ref:`Supported Devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`

