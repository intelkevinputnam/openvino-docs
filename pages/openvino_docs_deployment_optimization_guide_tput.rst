.. index:: pair: page; Optimizing for Throughput
.. _doxid-openvino_docs_deployment_optimization_guide_tput:


Optimizing for Throughput
=========================

:target:`doxid-openvino_docs_deployment_optimization_guide_tput_1md_openvino_docs_optimization_guide_dldt_deployment_optimization_tput`

General Throughput Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As described in the section on the :ref:`latency-specific considerations <doxid-openvino_docs_deployment_optimization_guide_latency>` one possible use-case is *delivering every single request at the minimal delay*. Throughput on the other hand, is about inference scenarios in which potentially large **number of inference requests are served simultaneously to improve the device utilization**.

The associated increase in latency is not linearly dependent on the number of requests executed in parallel. Here, a trade-off between overall throughput and serial performance of individual requests can be achieved with the right OpenVINO performance configuration.

Basic and Advanced Ways of Leveraging Throughput
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the OpenVINO there are two means of leveraging the throughput with the individual device:

* **Basic (high-level)** flow with :ref:`OpenVINO performance hints <doxid-openvino_docs__o_v__u_g__performance__hints>` which is inherently **portable and future-proof**

* **Advanced (low-level)** approach of explicit **batching** and **streams**, explained in the separate :ref:`document <doxid-openvino_docs_deployment_optimization_guide_tput_advanced>`.

In both cases application should be designed to execute multiple inference requests in parallel as detailed in the :ref:`next section <doxid-openvino_docs_deployment_optimization_guide_tput_1throughput_app_design>`.

Finally, consider the *automatic* multi-device execution covered below.

:target:`doxid-openvino_docs_deployment_optimization_guide_tput_1throughput_app_design`

Throughput-Oriented Application Design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most generally, throughput-oriented inference applications should:

* Expose substantial amounts of *inputs* parallelism (e.g. process multiple video- or audio- sources, text documents, etc)

* Decompose the data flow into a collection of concurrent inference requests that are aggressively scheduled to be executed in parallel
  
  * Setup the configuration for the *device* (e.g. as parameters of the ``:ref:`ov::Core::compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>```) via either :ref:`low-level explicit options <doxid-openvino_docs_deployment_optimization_guide_tput_advanced>`, introduced in the previous section or :ref:`OpenVINO performance hints <doxid-openvino_docs__o_v__u_g__performance__hints>` (**preferable**):
    
    
    
    
    
       .. tab:: C++
    
          .. doxygensnippet:: docs/snippets/ov_auto_batching.cpp
             :language: cpp
             :fragment: [compile_model]
    
       .. tab:: Python
    
          .. doxygensnippet:: docs/snippets/ov_auto_batching.py
             :language: python
             :fragment: [compile_model]
  
  * Query the ``:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>``` from the ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` (resulted from compilation of the model for a device) to create the number of the requests required to saturate the device

* Use the Async API with callbacks, to avoid any dependency on the requests' completion order and possible device starvation, as explained in the :ref:`common-optimizations section <doxid-openvino_docs_deployment_optimization_guide_common>`

Multi-Device Execution
~~~~~~~~~~~~~~~~~~~~~~

OpenVINO offers automatic, :ref:`scalable multi-device inference <doxid-openvino_docs__o_v__u_g__running_on_multiple_devices>`. This is simple *application-transparent* way to improve the throughput. No need to re-architecture existing applications for any explicit multi-device support: no explicit network loading to each device, no separate per-device queues, no additional logic to balance the inference requests between devices, etc. From the application point of view, it is communicating to the single device that internally handles the actual machinery. Just like with other throughput-oriented scenarios, there are two major pre-requisites for optimal multi-device performance:

* Using the :ref:`Asynchronous API <doxid-openvino_docs_deployment_optimization_guide_common>` and :ref:`callbacks <doxid-openvino_docs__o_v__u_g__infer_request>` in particular

* Providing the multi-device (and hence the underlying devices) with enough data to crunch. As the inference requests are naturally independent data pieces, the multi-device performs load-balancing at the “requests” (outermost) level to minimize the scheduling overhead.

Notice that the resulting performance is usually a fraction of the “ideal” (plain sum) value, when the devices compete for a certain resources, like the memory-bandwidth which is shared between CPU and iGPU.

.. note:: While the legacy approach of optimizing the parameters of each device separately works, the :ref:`OpenVINO performance hints <doxid-openvino_docs__o_v__u_g__performance__hints>` allow to configure all devices (that are part of the specific multi-device configuration) at once.

