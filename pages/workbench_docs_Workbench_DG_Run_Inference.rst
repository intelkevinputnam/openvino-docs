.. index:: pair: page; OpenVINO Inference
.. _doxid-workbench_docs__workbench__d_g__run__inference:


OpenVINO Inference
==================

:target:`doxid-workbench_docs__workbench__d_g__run__inference_1md_openvino_workbench_docs_workbench_dg_run_inference`





.. toctree::
   :maxdepth: 1
   :hidden:

   workbench_docs_Workbench_DG_Run_Single_Inference
   workbench_docs_Workbench_DG_View_Inference_Results
   workbench_docs_Workbench_DG_Compare_Performance_between_Two_Versions_of_Models
   workbench_docs_Workbench_DG_Visualize_Model

Inference is a single execution of the model that consists in feeding the data to the model and obtaining the results. Inferencing performance is a key characteristic of the model quality. OpenVINO has `several techniques <https://docs.openvino.ai/latest/openvino_docs_optimization_guide_dldt_optimization_guide.html#how-to-improve-performance>`__ to evaluate and accelerate model performance.

The DL Workbench allows users to assess the model performance in one of two inference modes:

* `Latency <https://docs.openvino.ai/latest/openvino_docs_optimization_guide_dldt_optimization_guide.html#what-is-performance>`__
  
  Latency is the time required to complete a unit of work, for example, the time required to infer a single image. The lower the value, the better. The latency mode is typical for lightweight models and real-time services.

* `Throughput <https://docs.openvino.ai/latest/openvino_docs_deployment_optimization_guide_dldt_optimization_guide.html#throughput-mode>`__
  
  Throughput is the number of input data processed in a given amount of time. It is recommended to use the throughput mode for models designed for high-performant applications. For example, there are several surveillance cameras and they work simultaneously passing the video frames to the accelerator at once. Using `asynchronous inference <https://docs.openvino.ai/latest/openvino_docs_deployment_optimization_guide_dldt_optimization_guide.html#inference-engine-async-api>`__ can significantly improve performance and ensure that models process as many frames as possible.

.. image:: LATENCY_VS_THROUGHPUT.svg

OpenVINO allows users to parallelize the neural model and propagate several input data instances to speed up the model by specifying the following parameters:

* `Streams <https://docs.openvino.ai/latest/openvino_docs_deployment_optimization_guide_dldt_optimization_guide.html#throughput-mode-for-cpu>`__ : stream is the number of instances of your model running simultaneously. Inferring the same model in several streams simultaneously leads to higher model performance.

* :ref:`Batches <doxid-openvino_docs__o_v__glossary>` : batch is the number of input data instances propagated to the model at a time.

Using one of the methods or a combination of them allows getting a noticeable performance boost (especially for lightweight topologies) without any accuracy loss. Another optimization technique is the `INT8 Calibration <https://docs.openvino.ai/latest/openvino_docs_IE_DG_Int8Inference.html#doxid-openvino-docs-i-e-d-g-int8-inference>`__ which results in a controllable accuracy drop.

The DL Workbench allows you to evaluate the performance of the model and provides a set of analytical capabilities which includes:

* :ref:`detailed performance assessment <doxid-workbench_docs__workbench__d_g__view__inference__results>`, including evaluation by layers, precision, kernel

* :ref:`visualization of the computational graph <doxid-workbench_docs__workbench__d_g__visualize__model>` of the model with the detection of bottlenecks

* :ref:`comparison <doxid-workbench_docs__workbench__d_g__compare__performance_between__two__versions_of__models>` within different configurations of the model (batches and streams), different versions of the model (optimized and parent) by a variety of criteria.

See Also
~~~~~~~~

* :ref:`Run Inference <doxid-workbench_docs__workbench__d_g__run__single__inference>`

* :ref:`View Inference Results <doxid-workbench_docs__workbench__d_g__view__inference__results>`

* :ref:`OpenVINO™ Runtime documentation <doxid-openvino_docs__o_v__u_g__o_v__runtime__user__guide>`

* :ref:`Benchmark Tool <doxid-openvino_inference_engine_tools_benchmark_tool__r_e_a_d_m_e>`

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

