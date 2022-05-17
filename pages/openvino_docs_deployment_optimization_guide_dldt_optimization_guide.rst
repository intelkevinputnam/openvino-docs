.. index:: pair: page; Runtime Inference Optimizations
.. _doxid-openvino_docs_deployment_optimization_guide_dldt_optimization_guide:


Runtime Inference Optimizations
===============================

:target:`doxid-openvino_docs_deployment_optimization_guide_dldt_optimization_guide_1md_openvino_docs_optimization_guide_dldt_deployment_optimization_guide`





.. toctree::
   :maxdepth: 1
   :hidden:

   openvino_docs_deployment_optimization_guide_common
   openvino_docs_deployment_optimization_guide_latency
   openvino_docs_deployment_optimization_guide_tput
   openvino_docs_deployment_optimization_guide_tput_advanced
   openvino_docs_deployment_optimization_guide_internals

Runtime or deployment optimizations are focused on tuning of the inference *parameters* (e.g. optimal number of the requests executed simultaneously) and other means of how a model is *executed*.

As referenced in the parent :ref:`performance introduction topic <doxid-openvino_docs_optimization_guide_dldt_optimization_guide>`, the :ref:`dedicated document <doxid-openvino_docs_model_optimization_guide>` covers the **model-level optimizations** like quantization that unlocks the 8-bit inference. Model-optimizations are most general and help any scenario and any device (that e.g. accelerates the quantized models). The relevant *runtime* configuration is ``:ref:`ov::hint::inference_precision <doxid-group__ov__runtime__cpp__prop__api_1gad605a888f3c9b7598ab55023fbf44240>``` which trades the accuracy for the performance (e.g. by allowing the fp16/bf16 execution for the layers that remain in fp32 after quantization of the original fp32 model).

Then, possible optimization should start with defining the use-case. For example, whether the target scenario emphasizes throughput over latency like processing millions of samples by overnight jobs in the data centers. In contrast, real-time usages would likely trade off the throughput to deliver the results at minimal latency. Often this is a combined scenario that targets highest possible throughput while maintaining a specific latency threshold. Below you can find summary on the associated tips.

How the full-stack application uses the inference component *end-to-end* is also important. For example, what are the stages that needs to be orchestrated? In some cases a significant part of the workload time is spent on bringing and preparing the input data. Below you can find multiple tips on connecting the data input pipeline and the model inference efficiently. These are also common performance tricks that help both latency and throughput scenarios.

Further documents cover the associated *runtime* performance optimizations topics. Please also consider :ref:`matrix support of the features by the individual devices <doxid-openvino_docs__o_v__u_g__working_with_devices_1features_support_matrix>`.

:ref:`General, application-level optimizations <doxid-openvino_docs_deployment_optimization_guide_common>`, and specifically:

* :ref:`Inputs Pre-processing with the OpenVINO <doxid-openvino_docs__o_v__u_g__preprocessing__overview>`

* :ref:`Async API and 'get_tensor' Idiom <doxid-openvino_docs_deployment_optimization_guide_common>`

* For variably-sized inputs, consider :ref:`dynamic shapes <doxid-openvino_docs__o_v__u_g__dynamic_shapes>`

**Use-case specific optimizations** such as optimizing for :ref:`latency <doxid-openvino_docs_deployment_optimization_guide_latency>` or :ref:`throughput <doxid-openvino_docs_deployment_optimization_guide_tput>`

Writing Performance Portable Inference Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each of the OpenVINO's :ref:`supported devices <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>` offers a bunch of low-level performance settings. Tweaking this detailed configuration requires deep architecture understanding.

Also, while the resulting performance may be optimal for the specific combination of the device and the model that is inferred, it is actually neither device/model nor future-proof:

* Even within a family of the devices (like various CPUs), different instruction set, or number of CPU cores would eventually result in different execution configuration to be optimal.

* Similarly the optimal batch size is very much specific to the particular instance of the GPU.

* Compute vs memory-bandwidth requirements for the model being inferenced, as well as inference precision, possible model's quantization also contribute to the optimal parameters selection.

* Finally, the optimal execution parameters of one device do not transparently map to another device type, for example:
  
  * Both the CPU and GPU devices support the notion of the :ref:`streams <doxid-openvino_docs_deployment_optimization_guide_tput_advanced>`, yet the optimal number of the streams is deduced very differently.

Here, to mitigate the performance configuration complexity the **Performance Hints** offer the high-level "presets" for the **latency** and **throughput**, as detailed in the :ref:`Performance Hints usage document <doxid-openvino_docs__o_v__u_g__performance__hints>`.

Beyond execution *parameters* there is a device-specific *scheduling* that greatly affects the performance. Specifically, GPU-oriented optimizations like batching, which combines many (potentially tens) of inputs to achieve optimal throughput, do not always map well to the CPU, as e.g. detailed in the :ref:`further internals <doxid-openvino_docs_deployment_optimization_guide_internals>` sections.

The hints really hide the *execution* specifics required to saturate the device. In the :ref:`internals <doxid-openvino_docs_deployment_optimization_guide_internals>` sections you can find the implementation details (particularly how the OpenVINO implements the 'throughput' approach) for the specific devices. Keep in mind that the hints make this transparent to the application. For example, the hints obviates the need for explicit (application-side) batching or streams.

With the hints, it is enough to keep separate infer requests per camera or another source of input and process the requests in parallel using Async API as explained in the :ref:`application design considerations section <doxid-openvino_docs_deployment_optimization_guide_tput_1throughput_app_design>`. The main requirement for the application to leverage the throughput is **running multiple inference requests in parallel**.

In summary, when the performance *portability* is of concern, consider the Performance Hints as a solution. You may find further details and API examples :ref:`here <doxid-openvino_docs__o_v__u_g__performance__hints>`.

