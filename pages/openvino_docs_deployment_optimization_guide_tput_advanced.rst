.. index:: pair: page; Using Advanced Throughput Options: Streams and Batching
.. _doxid-openvino_docs_deployment_optimization_guide_tput_advanced:


Using Advanced Throughput Options: Streams and Batching
=======================================================

:target:`doxid-openvino_docs_deployment_optimization_guide_tput_advanced_1md_openvino_docs_optimization_guide_dldt_deployment_optimization_tput_advanced`

OpenVINO Streams
~~~~~~~~~~~~~~~~

As detailed in the :ref:`common-optimizations section <doxid-openvino_docs_deployment_optimization_guide_common>` running multiple inference requests asynchronously is important for general application efficiency. Internally, every device implements a queue. The queue acts as a buffer, storing the inference requests until retrieved by the device at its own pace. The devices may actually process multiple inference requests in parallel in order to improve the device utilization and overall throughput. This configurable mean of this device-side parallelism is commonly referred as **streams**.

.. note:: Notice that streams are **really executing the requests in parallel, but not in the lock step** (as e.g. the batching does), which makes the streams fully compatible with :ref:`dynamically-shaped inputs <doxid-openvino_docs__o_v__u_g__dynamic_shapes>` when individual requests can have different shapes.

.. note:: Most OpenVINO devices (including CPU, GPU and VPU) support the streams, yet the *optimal* number of the streams is deduced very differently, please see the a dedicated section below.

Few general considerations:

* Using the streams does increase the latency of an individual request
  
  * When no number of streams is not specified, a device creates a bare minimum of streams (usually just one), as the latency-oriented case is default
  
  * Please find further tips for the optimal number of the streams :ref:`below <doxid-openvino_docs_deployment_optimization_guide_tput_advanced_1throughput_advanced>`

* Streams are memory-hungry, as every stream duplicates the intermediate buffers to do inference in parallel to the rest of streams
  
  * Always prefer streams over creating multiple ``ov:Compiled_Model`` instances for the same model, as weights memory is shared across streams, reducing the memory consumption

* Notice that the streams also inflate the model load (compilation) time.

For efficient asynchronous execution, the streams are actually handling the inference with a special pool of the threads (a thread per stream). Each time you start inference requests (potentially from different application threads), they are actually muxed into a inference queue of the particular ``ov:Compiled_Model``. If there is a vacant stream, it pops the request from the queue and actually expedites that to the on-device execution. There are further device-specific details e.g. for the CPU, that you may find in the :ref:`internals <doxid-openvino_docs_deployment_optimization_guide_internals>` section.

Batching
~~~~~~~~

Hardware accelerators like GPUs are optimized for massive compute parallelism, so the batching helps to saturate the device and leads to higher throughput. While the streams (described earlier) already help to hide the communication overheads and certain bubbles in the scheduling, running multiple OpenCL kernels simultaneously is less GPU-efficient, compared to calling a kernel on the multiple inputs at once.

As explained in the next section, the batching is a must to leverage maximum throughput on the GPUs.

There are two primary ways of using the batching to help application performance:

* Collecting the inputs explicitly on the application side and then *sending these batched requests to the OpenVINO*
  
  * Although this gives flexibility with the possible batching strategies, the approach requires redesigning the application logic

* *Sending individual requests*, while configuring the OpenVINO to collect and perform inference on the requests in batch :ref:`automatically <doxid-openvino_docs__o_v__u_g__automatic__batching>`. In both cases, optimal batch size is very device-specific. Also as explained below, the optimal batch size depends on the model, inference precision and other factors.

:target:`doxid-openvino_docs_deployment_optimization_guide_tput_advanced_1throughput_advanced`

Choosing the Number of Streams and/or Batch Size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Predicting the inference performance is difficult and finding optimal execution parameters requires direct experiments with measurements. Run performance testing in the scope of development, and make sure to validate overall (end-to-end) application performance.

Different devices behave differently with the batch sizes. The optimal batch size depends on the model, inference precision and other factors. Similarly, different devices require different number of execution streams to saturate. Finally, in some cases combination of streams and batching may be required to maximize the throughput.

One possible throughput optimization strategy is to **set an upper bound for latency and then increase the batch size and/or number of the streams until that tail latency is met (or the throughput is not growing anymore)**. Also, consider OpenVINO Deep Learning Workbench that builds handy latency vs throughput charts, iterating over possible values of the batch size and number of streams.

.. note:: When playing with :ref:`dynamically-shaped inputs <doxid-openvino_docs__o_v__u_g__dynamic_shapes>` use only the streams (no batching), as they tolerate individual requests having different shapes.

.. note:: Using the :ref:`High-Level Performance Hints <doxid-openvino_docs__o_v__u_g__performance__hints>` is the alternative, portable and future-proof option, allowing the OpenVINO to find best combination of streams and batching for a given scenario and model.

Number of Streams Considerations
--------------------------------

* Select the number of streams is it is **less or equal** to the number of requests that your application would be able to runs simultaneously

* To avoid wasting resources, the number of streams should be enough to meet the *average* parallel slack rather than the peak load

* As a more portable option (that also respects the underlying hardware configuration) use the ``:ref:`ov::streams::AUTO <doxid-group__ov__runtime__cpp__prop__api_1gaddb29425af71fbb6ad3379c59342ff0e>```

* It is very important to keep these streams busy, by running as many inference requests as possible (e.g. start the newly-arrived inputs immediately)
  
  * Bare minimum of requests to saturate the device can be queried as ``:ref:`ov::optimal_number_of_infer_requests <doxid-group__ov__runtime__cpp__prop__api_1ga087c6da667f7c3d8374aec5f6cbba027>``` of the ``ov:Compiled_Model``

* *Maximum number of streams* for the device (per model) can be queried as the ``:ref:`ov::range_for_streams <doxid-group__ov__runtime__cpp__prop__api_1ga8a5d84196f6873729167aa512c34a94a>```

Batch Size Considerations
-------------------------

* Select the batch size that is **equal** to the number of requests that your application is able to runs simultaneously
  
  * Otherwise (or if the number of "available" requests fluctuates), you may need to keep several instances of the network (reshaped to the different batch size) and select the properly sized instance in the runtime accordingly

* For OpenVINO devices that internally implement a dedicated heuristic, the ``:ref:`ov::optimal_batch_size <doxid-group__ov__runtime__cpp__prop__api_1ga129bad2da2fc2a40a7d746d86fc9c68d>``` is a *device* property (that accepts the actual model as a parameter) to query the recommended batch size for the model.

Few Device Specific Details
---------------------------

* For the **GPU** :
  
  * When the parallel slack is small (e.g. only 2-4 requests executed simultaneously), then using only the streams for the GPU may suffice
    
    * Notice that the GPU runs 2 request per stream, so 4 requests can be served by 2 streams
    
    * Alternatively, consider single stream with with 2 requests (each with a small batch size like 2), which would total the same 4 inputs in flight
  
  * Typically, for 4 and more requests the batching delivers better throughput
  
  * Batch size can be calculated as "number of inference requests executed in parallel" divided by the "number of requests that the streams consume"
    
    * E.g. if you process 16 cameras (by 16 requests inferenced *simultaneously*) by the two GPU streams (each can process two requests), the batch size per request is 16/(2\*2)=4

* For the **CPU always use the streams first**
  
  * On the high-end CPUs, using moderate (2-8) batch size *in addition* to the maximum number of streams, may further improve the performance.

