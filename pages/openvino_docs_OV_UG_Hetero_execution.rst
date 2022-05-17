.. index:: pair: page; Heterogeneous execution
.. _doxid-openvino_docs__o_v__u_g__hetero_execution:


Heterogeneous execution
=======================

:target:`doxid-openvino_docs__o_v__u_g__hetero_execution_1md_openvino_docs_ov_runtime_ug_hetero_execution` Heterogeneous execution enables executing inference of one model on several devices. Its purpose is to:

* Utilize the power of accelerators to process the heaviest parts of the model and to execute unsupported operations on fallback devices, like the CPU.

* Utilize all available hardware more efficiently during one inference.

Execution via the heterogeneous mode can be divided into two independent steps:

#. Setting hardware affinity to operations (``:ref:`ov::Core::query_model <doxid-classov_1_1_core_1acdf8e64824fe4cf147c3b52ab32c1aab>``` is used internally by the Hetero device)

#. Compiling a model to the Heterogeneous device assumes splitting the model to parts, compiling them on the specified devices (via ``:ref:`ov::device::priorities <doxid-group__ov__runtime__cpp__prop__api_1gae88af90a18871677f39739cb0ef0101e>```), and executing them in the Heterogeneous mode. The model is split to subgraphs in accordance with the affinities, where a set of connected operations with the same affinity is to be a dedicated subgraph. Each subgraph is compiled on a dedicated device and multiple ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` objects are made, which are connected via automatically allocated intermediate tensors.

These two steps are not interconnected and affinities can be set in one of two ways, used separately or in combination (as described below): in the ``manual`` or the ``automatic`` mode.

Defining and Configuring the Hetero Device
------------------------------------------

Following the OpenVINO™ naming convention, the Hetero execution plugin is assigned the label of ``"HETERO".`` It may be defined with no additional parameters, resulting in defaults being used, or configured further with the following setup options:

+-------------------------------+--------------------------------------------+-----------------------------------------------------------+
| Parameter Name & C++ property | Property values                            | Description                                               |
+===============================+============================================+===========================================================+
| | "MULTI_DEVICE_PRIORITIES"   | | HETERO: <device names>                   | | Lists the devices available for selection.              |
| | `ov::device::priorities`    | | comma-separated, no spaces               | | The device sequence will be taken as priority           |
| |                             | |                                          | | from high to low.                                       |
+-------------------------------+--------------------------------------------+-----------------------------------------------------------+

Manual and Automatic modes for assigning affinities
---------------------------------------------------

The Manual Mode
+++++++++++++++

It assumes setting affinities explicitly for all operations in the model using ``:ref:`ov::Node::get_rt_info <doxid-classov_1_1_node_1a5c73794fbc47e510198261d61682fe79>``` with the ``"affinity"`` key.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	for (auto && op : :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->get_ops()) {
	    op->get_rt_info()["affinity"] = "CPU";
	}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	for op in model.get_ops():
	    rt_info = op.get_rt_info()
	    rt_info["affinity"] = "CPU"





.. raw:: html

   </div>







.. raw:: html

   </div>

The Automatic Mode
++++++++++++++++++

It decides automatically which operation is assigned to which device according to the support from dedicated devices (``GPU``, ``CPU``, ``MYRIAD``, etc.) and query model step is called implicitly by Hetero device during model compilation.

The automatic mode causes "greedy" behavior and assigns all operations that can be executed on a given device to it, according to the priorities you specify (for example, ``:ref:`ov::device::priorities <doxid-group__ov__runtime__cpp__prop__api_1gae88af90a18871677f39739cb0ef0101e>`("GPU,CPU")``). It does not take into account device peculiarities such as the inability to infer certain operations without other special operations placed before or after that layer. If the device plugin does not support the subgraph topology constructed by the HETERO device, then you should set affinity manually.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "HETERO:GPU,CPU");
	// or with ov::device::priorities with multiple args
	compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "HETERO", :ref:`ov::device::priorities <doxid-group__ov__runtime__cpp__prop__api_1gae88af90a18871677f39739cb0ef0101e>`("GPU", "CPU"));
	// or with ov::device::priorities with a single argument
	compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "HETERO", :ref:`ov::device::priorities <doxid-group__ov__runtime__cpp__prop__api_1gae88af90a18871677f39739cb0ef0101e>`("GPU,CPU"));





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	compiled_model = core.compile_model(model, device_name="HETERO:GPU,CPU")
	# device priorities via configuration property
	compiled_model = core.compile_model(model, device_name="HETERO", config={"MULTI_DEVICE_PRIORITIES": "GPU,CPU"})





.. raw:: html

   </div>







.. raw:: html

   </div>





Using Manual and Automatic Modes in Combination
+++++++++++++++++++++++++++++++++++++++++++++++

In some cases you may need to consider manually adjusting affinities which were set automatically. It usually serves minimizing the number of total subgraphs to optimize memory transfers. To do it, you need to "fix" the automatically assigned affinities like so:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// This example demonstrates how to perform default affinity initialization and then
	// correct affinity manually for some layers
	const std::string device = "HETERO:GPU,CPU";
	
	// query_model result contains mapping of supported operations to devices
	auto supported_ops = core.:ref:`query_model <doxid-classov_1_1_core_1acdf8e64824fe4cf147c3b52ab32c1aab>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, device);
	
	// update default affinities manually for specific operations
	supported_ops["operation_name"] = "CPU";
	
	// set affinities to a model
	for (auto&& node : :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->get_ops()) {
	    auto& :ref:`affinity <doxid-group__ov__runtime__cpp__prop__api_1ga9c99a177a56685a70875302c59541887>` = supported_ops[node->get_friendly_name()];
	    // Store affinity mapping using op runtime information
	    node->get_rt_info()["affinity"] = :ref:`affinity <doxid-group__ov__runtime__cpp__prop__api_1ga9c99a177a56685a70875302c59541887>`;
	}
	
	// load model with manually set affinities
	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, device);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# This example demonstrates how to perform default affinity initialization and then
	# correct affinity manually for some layers
	device = "HETERO:GPU,CPU"
	
	# query_model result contains mapping of supported operations to devices
	supported_ops = core.query_model(model, device)
	
	# update default affinities manually for specific operations
	supported_ops["operation_name"] = "CPU"
	
	# set affinities to a model
	for node in model.get_ops():
	    affinity = supported_ops[node.get_friendly_name()]
	    node.get_rt_info()["affinity"] = "CPU"
	
	# load model with manually set affinities
	compiled_model = core.compile_model(model, device)





.. raw:: html

   </div>







.. raw:: html

   </div>



Importantly, the automatic mode will not work if any operation in a model has its ``"affinity"`` already initialized.

.. note:: ``:ref:`ov::Core::query_model <doxid-classov_1_1_core_1acdf8e64824fe4cf147c3b52ab32c1aab>``` does not depend on affinities set by a user. Instead, it queries for an operation support based on device capabilities.

Configure fallback devices
--------------------------

If you want different devices in Hetero execution to have different device-specific configuration options, you can use the special helper property ``:ref:`ov::device::properties <doxid-group__ov__runtime__cpp__prop__api_1ga794d09f2bd8aad506508b2c53ef6a6fc>``` :

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "HETERO",
	    // GPU with fallback to CPU
	    :ref:`ov::device::priorities <doxid-group__ov__runtime__cpp__prop__api_1gae88af90a18871677f39739cb0ef0101e>`("GPU", "CPU"),
	    // profiling is enabled only for GPU
	    :ref:`ov::device::properties <doxid-group__ov__runtime__cpp__prop__api_1ga794d09f2bd8aad506508b2c53ef6a6fc>`("GPU", :ref:`ov::enable_profiling <doxid-group__ov__runtime__cpp__prop__api_1gafc5bef2fc2b5cfb5a0709cfb04346438>`(true)),
	    // FP32 inference precision only for CPU
	    :ref:`ov::device::properties <doxid-group__ov__runtime__cpp__prop__api_1ga794d09f2bd8aad506508b2c53ef6a6fc>`("CPU", :ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>`(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`))
	);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core.set_property("HETERO", {"MULTI_DEVICE_PRIORITIES": "GPU,CPU"})
	core.set_property("GPU", {"PERF_COUNT": "YES"})
	core.set_property("CPU", {"INFERENCE_PRECISION_HINT": "f32"})
	compiled_model = core.compile_model(model=model, device_name="HETERO")





.. raw:: html

   </div>







.. raw:: html

   </div>



In the example above, the ``GPU`` device is configured to enable profiling data and uses the default execution precision, while ``CPU`` has the configuration property to perform inference in ``fp32``.

Handling of Difficult Topologies
--------------------------------

Some topologies are not friendly to heterogeneous execution on some devices, even to the point of being unable to execute. For example, models having activation operations that are not supported on the primary device are split by Hetero into multiple sets of subgraphs which leads to suboptimal execution. If transmitting data from one subgraph to another part of the model in the heterogeneous mode takes more time than under normal execution, heterogeneous execution may be unsubstantiated. In such cases, you can define the heaviest part manually and set the affinity to avoid sending data back and forth many times during one inference.

Analyzing Performance of Heterogeneous Execution
------------------------------------------------

After enabling the ``OPENVINO_HETERO_VISUALIZE`` environment variable, you can dump GraphViz ``.dot`` files with annotations of operations per devices.

The Heterogeneous execution mode can generate two files:

* ``hetero_affinity_<model name>.dot`` - annotation of affinities per operation.

* ``hetero_subgraphs_<model name>.dot`` - annotation of affinities per graph.

You can use the GraphViz utility or a file converter to view the images. On the Ubuntu operating system, you can use xdot:

* ``sudo apt-get install xdot``

* ``xdot hetero_subgraphs.dot``

You can use performance data (in sample applications, it is the option ``-pc``) to get the performance data on each subgraph.

Here is an example of the output for Googlenet v1 running on HDDL with fallback to CPU:

.. ref-code-block:: cpp

	subgraph1: 1. input preprocessing (mean data/HDDL):EXECUTED layerType:          realTime: 129   cpu: 129  execType:
	subgraph1: 2. input transfer to DDR:EXECUTED                layerType:          realTime: 201   cpu: 0    execType:
	subgraph1: 3. HDDL execute time:EXECUTED                    layerType:          realTime: 3808  cpu: 0    execType:
	subgraph1: 4. output transfer from DDR:EXECUTED             layerType:          realTime: 55    cpu: 0    execType:
	subgraph1: 5. HDDL output postprocessing:EXECUTED           layerType:          realTime: 7     cpu: 7    execType:
	subgraph1: 6. copy to IE blob:EXECUTED                      layerType:          realTime: 2     cpu: 2    execType:
	subgraph2: out_prob:          NOT_RUN                       layerType: Output   realTime: 0     cpu: 0    execType: unknown
	subgraph2: prob:              EXECUTED                      layerType: SoftMax  realTime: 10    cpu: 10   execType: ref
	Total time: 4212 microseconds

Sample Usage
------------

OpenVINO™ sample programs can use the Heterogeneous execution used with the ``-d`` option:

.. ref-code-block:: cpp

	./hello_classification <path_to_model>/squeezenet1.1.xml <path_to_pictures>/picture.jpg HETERO:GPU,CPU

where:

* ``HETERO`` stands for the Heterogeneous execution

* ``GPU,CPU`` points to a fallback policy with the priority on GPU and fallback to CPU

You can also point to more than two devices: ``-d HETERO:MYRIAD,GPU,CPU``

See Also
--------

:ref:`Supported Devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`

