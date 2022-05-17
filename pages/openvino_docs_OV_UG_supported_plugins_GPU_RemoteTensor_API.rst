.. index:: pair: page; Remote Tensor API of GPU Plugin
.. _doxid-openvino_docs__o_v__u_g_supported_plugins__g_p_u__remote_tensor__a_p_i:


Remote Tensor API of GPU Plugin
===============================

:target:`doxid-openvino_docs__o_v__u_g_supported_plugins__g_p_u__remote_tensor__a_p_i_1md_openvino_docs_ov_runtime_ug_supported_plugins_gpu_remotetensor_api` The GPU plugin implementation of the ``:ref:`ov::RemoteContext <doxid-classov_1_1_remote_context>``` and ``:ref:`ov::RemoteTensor <doxid-classov_1_1_remote_tensor>``` interfaces supports GPU pipeline developers who need video memory sharing and interoperability with existing native APIs, such as OpenCL, Microsoft DirectX, or VAAPI. Using these interfaces allows you to avoid any memory copy overhead when plugging OpenVINO™ inference into an existing GPU pipeline. It also enables OpenCL kernels participating in the pipeline to become native buffer consumers or producers of the OpenVINO™ inference.

There are two interoperability scenarios supported by the Remote Tensor API:

* The GPU plugin context and memory objects can be constructed from low-level device, display, or memory handles and used to create the OpenVINO™ ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` or ``:ref:`ov::Tensor <doxid-classov_1_1_tensor>``` objects.

* The OpenCL context or buffer handles can be obtained from existing GPU plugin objects, and used in OpenCL processing on the application side.

Class and function declarations for the API are defined in the following files:

* Windows\*: ``openvino/runtime/intel_gpu/ocl/ocl.hpp`` and ``openvino/runtime/intel_gpu/ocl/dx.hpp``

* Linux\*: ``openvino/runtime/intel_gpu/ocl/ocl.hpp`` and ``openvino/runtime/intel_gpu/ocl/va.hpp``

The most common way to enable the interaction of your application with the Remote Tensor API is to use user-side utility classes and functions that consume or produce native handles directly.

Context sharing between application and GPU plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GPU plugin classes that implement the ``:ref:`ov::RemoteContext <doxid-classov_1_1_remote_context>``` interface are responsible for context sharing. Obtaining a context object is the first step of sharing pipeline objects. The context object of the GPU plugin directly wraps OpenCL context, setting a scope for sharing ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` and ``:ref:`ov::RemoteTensor <doxid-classov_1_1_remote_tensor>``` objects. ``:ref:`ov::RemoteContext <doxid-classov_1_1_remote_context>``` object can be either created on top of an existing handle from native api or retrieved from the GPU plugin.

Once you obtain the context, you can use it to compile a new ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` or create ``:ref:`ov::RemoteTensor <doxid-classov_1_1_remote_tensor>``` objects. For network compilation, use a dedicated flavor of ``:ref:`ov::Core::compile_model() <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>```, which accepts the context as an additional parameter.

Creation of RemoteContext from native handle
--------------------------------------------

To create ``:ref:`ov::RemoteContext <doxid-classov_1_1_remote_context>``` object for user context, explicitly provide the context to the plugin using constructor for one of ``:ref:`ov::RemoteContext <doxid-classov_1_1_remote_context>``` derived classes.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Linux">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Create from cl_context">





.. ref-code-block:: cpp

	cl_context ctx = get_cl_context();
	:ref:`ov::intel_gpu::ocl::ClContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_context>` gpu_context(core, ctx);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Create from cl_queue">





.. ref-code-block:: cpp

	cl_command_queue queue = get_cl_queue();
	:ref:`ov::intel_gpu::ocl::ClContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_context>` gpu_context(core, queue);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Create from VADisplay">





.. ref-code-block:: cpp

	VADisplay display = get_va_display();
	:ref:`ov::intel_gpu::ocl::VAContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_v_a_context>` gpu_context(core, display);





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Windows">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Create from cl_context">





.. ref-code-block:: cpp

	cl_context ctx = get_cl_context();
	:ref:`ov::intel_gpu::ocl::ClContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_context>` gpu_context(core, ctx);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Create from cl_queue">





.. ref-code-block:: cpp

	cl_command_queue queue = get_cl_queue();
	:ref:`ov::intel_gpu::ocl::ClContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_context>` gpu_context(core, queue);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Create from ID3D11Device">





.. ref-code-block:: cpp

	ID3D11Device\* device = get_d3d_device();
	:ref:`ov::intel_gpu::ocl::D3DContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_d3_d_context>` gpu_context(core, device);





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>

Getting RemoteContext from the plugin
-------------------------------------

If you do not provide any user context, the plugin uses its default internal context. The plugin attempts to use the same internal context object as long as plugin options are kept the same. Therefore, all ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` objects created during this time share the same context. Once the plugin options are changed, the internal context is replaced by the new one.

To request the current default context of the plugin use one of the following methods:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Get context from Core">





.. ref-code-block:: cpp

	auto gpu_context = core.:ref:`get_default_context <doxid-classov_1_1_core_1a0ae465fb50e92fa63054c2d0acfd25ae>`("GPU").:ref:`as <doxid-classov_1_1_remote_context_1a54021126344109640e35a18842d22654>`<:ref:`ov::intel_gpu::ocl::ClContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_context>`>();
	// Extract ocl context handle from RemoteContext
	cl_context context_handle = gpu_context.:ref:`get <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_context_1a9a8d57332c8bb376487fe5b4a0bfb6fe>`();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Bacthing via throughput hint">





.. ref-code-block:: cpp

	auto gpu_context = compiled_model.:ref:`get_context <doxid-classov_1_1_compiled_model_1a22c5537d4c7182072d327077c386b01a>`().:ref:`as <doxid-classov_1_1_remote_context_1a54021126344109640e35a18842d22654>`<:ref:`ov::intel_gpu::ocl::ClContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_context>`>();
	// Extract ocl context handle from RemoteContext
	cl_context context_handle = gpu_context.:ref:`get <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_context_1a9a8d57332c8bb376487fe5b4a0bfb6fe>`();





.. raw:: html

   </div>







.. raw:: html

   </div>





Memory sharing between application and GPU plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The classes that implement the ``:ref:`ov::RemoteTensor <doxid-classov_1_1_remote_tensor>``` interface are the wrappers for native API memory handles (which can be obtained from them at any time).

To create a shared tensor from a native memory handle, use dedicated ``create_tensor`` or ``create_tensor_nv12`` methods of the ``:ref:`ov::RemoteContext <doxid-classov_1_1_remote_context>``` sub-classes. ``:ref:`ov::intel_gpu::ocl::ClContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_context>``` has multiple overloads of ``create_tensor`` methods which allow to wrap pre-allocated native handles with ``:ref:`ov::RemoteTensor <doxid-classov_1_1_remote_tensor>``` object or request plugin to allocate specific device memory. See code snippets below for more details.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Wrap native handles">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="USM pointer">





.. ref-code-block:: cpp

	void\* shared_buffer = allocate_usm_buffer(input_size);
	auto remote_tensor = gpu_context.create_tensor(in_element_type, :ref:`in_shape <doxid-namespacengraph_1_1runtime_1_1reference_1a9ca739ccf7da267b87ff139b4ad05a17>`, shared_buffer);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="cl_mem">





.. ref-code-block:: cpp

	cl_mem shared_buffer = allocate_cl_mem(input_size);
	auto remote_tensor = gpu_context.create_tensor(in_element_type, :ref:`in_shape <doxid-namespacengraph_1_1runtime_1_1reference_1a9ca739ccf7da267b87ff139b4ad05a17>`, shared_buffer);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="cl::Buffer">





.. ref-code-block:: cpp

	cl::Buffer shared_buffer = allocate_buffer(input_size);
	auto remote_tensor = gpu_context.create_tensor(in_element_type, :ref:`in_shape <doxid-namespacengraph_1_1runtime_1_1reference_1a9ca739ccf7da267b87ff139b4ad05a17>`, shared_buffer);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="cl::Image2D">





.. ref-code-block:: cpp

	cl::Image2D shared_buffer = allocate_image(input_size);
	auto remote_tensor = gpu_context.create_tensor(in_element_type, :ref:`in_shape <doxid-namespacengraph_1_1runtime_1_1reference_1a9ca739ccf7da267b87ff139b4ad05a17>`, shared_buffer);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="biplanar NV12 surface">





.. ref-code-block:: cpp

	cl::Image2D y_plane_surface = allocate_image(y_plane_size);
	cl::Image2D uv_plane_surface = allocate_image(uv_plane_size);
	auto remote_tensor = gpu_context.create_tensor_nv12(y_plane_surface, uv_plane_surface);
	auto y_tensor = remote_tensor.first;
	auto uv_tensor = remote_tensor.second;





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Allocate device memory">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="USM host memory">





.. ref-code-block:: cpp

	:ref:`ov::intel_gpu::ocl::USMTensor <doxid-classov_1_1intel__gpu_1_1ocl_1_1_u_s_m_tensor>` remote_tensor = gpu_context.create_usm_host_tensor(in_element_type, :ref:`in_shape <doxid-namespacengraph_1_1runtime_1_1reference_1a9ca739ccf7da267b87ff139b4ad05a17>`);
	// Extract raw usm pointer from remote tensor
	void\* usm_ptr = remote_tensor.:ref:`get <doxid-classov_1_1intel__gpu_1_1ocl_1_1_u_s_m_tensor_1a362bb5315074e1068214b3c1b59e76a3>`();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="USM device memory">





.. ref-code-block:: cpp

	auto remote_tensor = gpu_context.create_usm_device_tensor(in_element_type, :ref:`in_shape <doxid-namespacengraph_1_1runtime_1_1reference_1a9ca739ccf7da267b87ff139b4ad05a17>`);
	// Extract raw usm pointer from remote tensor
	void\* usm_ptr = remote_tensor.:ref:`get <doxid-classov_1_1intel__gpu_1_1ocl_1_1_u_s_m_tensor_1a362bb5315074e1068214b3c1b59e76a3>`();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="cl::Buffer">





.. ref-code-block:: cpp

	:ref:`ov::RemoteTensor <doxid-classov_1_1_remote_tensor>` remote_tensor = gpu_context.create_tensor(in_element_type, :ref:`in_shape <doxid-namespacengraph_1_1runtime_1_1reference_1a9ca739ccf7da267b87ff139b4ad05a17>`);
	// Cast from base to derived class and extract ocl memory handle
	auto buffer_tensor = remote_tensor.:ref:`as <doxid-classov_1_1_tensor_1a345f8ade85da6fe30bcf8a3ae15a4bca>`<:ref:`ov::intel_gpu::ocl::ClBufferTensor <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_buffer_tensor>`>();
	cl_mem :ref:`handle <doxid-group__ie__dev__profiling_1ga8579f29ef5313d519bcaee20dd543a1b>` = buffer_tensor.get();





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>



``:ref:`ov::intel_gpu::ocl::D3DContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_d3_d_context>``` and ``:ref:`ov::intel_gpu::ocl::VAContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_v_a_context>``` classes are derived from ``:ref:`ov::intel_gpu::ocl::ClContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_context>```, thus they provide the functionality described above and extend it to allow creation of ``:ref:`ov::RemoteTensor <doxid-classov_1_1_remote_tensor>``` objects from ``ID3D11Buffer``, ``ID3D11Texture2D`` pointers or the ``VASurfaceID`` handle respectively.

Direct NV12 video surface input
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To support the direct consumption of a hardware video decoder output, the plugin accepts two-plane video surfaces as arguments for the ``create_tensor_nv12()`` function, which creates a pair or ``:ref:`ov::RemoteTensor <doxid-classov_1_1_remote_tensor>``` objects which represent the Y and UV planes.

To ensure that the plugin generates the correct execution graph for the NV12 dual-plane input, static preprocessing should be added before model compilation:

.. ref-code-block:: cpp

	using namespace :ref:`ov::preprocess <doxid-namespaceov_1_1preprocess>`;
	auto p = :ref:`PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);
	p.input().tensor().set_element_type(:ref:`ov::element::u8 <doxid-group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f>`)
	                  .set_color_format(ov::preprocess::ColorFormat::NV12_TWO_PLANES, {"y", "uv"})
	                  .set_memory_type(:ref:`ov::intel_gpu::memory_type::surface <doxid-group__ov__runtime__ocl__gpu__prop__cpp__api_1gaec0856a3b996876371138961269b742d>`);
	p.input().preprocess().convert_color(:ref:`ov::preprocess::ColorFormat::BGR <doxid-namespace_inference_engine_1a5ee5ca7708cc67a9a0becc2593d0558aa0fb221afef06def7c25b82d6fa9efc1b>`);
	p.input().model().set_layout("NCHW");
	auto model_with_preproc = p.build();

Since ``:ref:`ov::intel_gpu::ocl::ClImage2DTensor <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor>``` (and derived classes) doesn't support batched surfaces, if batching and surface sharing are required at the same time, inputs need to be set via the ``:ref:`ov::InferRequest::set_tensors <doxid-classov_1_1_infer_request_1a935a952c07cc7130a64614d0952db997>``` method with vector of shared surfaces for each plane:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Single batch">





.. ref-code-block:: cpp

	:ref:`ov::intel_gpu::ocl::ClImage2DTensor <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor>` y_tensor = get_y_tensor();
	:ref:`ov::intel_gpu::ocl::ClImage2DTensor <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_image2_d_tensor>` uv_tensor = get_uv_tensor();
	infer_request.:ref:`set_tensor <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>`("y", y_tensor);
	infer_request.:ref:`set_tensor <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>`("uv", uv_tensor);
	infer_request.:ref:`infer <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>`();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Multiple batches">





.. ref-code-block:: cpp

	std::vector<ov::Tensor> y_tensors = {y_tensor_0, y_tensor_1};
	std::vector<ov::Tensor> uv_tensors = {uv_tensor_0, uv_tensor_1};
	infer_request.:ref:`set_tensors <doxid-classov_1_1_infer_request_1a935a952c07cc7130a64614d0952db997>`("y", y_tensors);
	infer_request.:ref:`set_tensors <doxid-classov_1_1_infer_request_1a935a952c07cc7130a64614d0952db997>`("uv", uv_tensors);
	infer_request.:ref:`infer <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>`();





.. raw:: html

   </div>







.. raw:: html

   </div>

I420 color format can be processed in a similar way

Context & queue sharing
~~~~~~~~~~~~~~~~~~~~~~~

The GPU plugin supports creation of shared context from ``cl_command_queue`` handle. In that case opencl context handle is extracted from the given queue via OpenCL™ API, and the queue itself is used inside the plugin for further execution of inference primitives. Sharing the queue changes the behavior of the ``:ref:`ov::InferRequest::start_async() <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>``` method to guarantee that submission of inference primitives into the given queue is finished before returning control back to the calling thread.

This sharing mechanism allows to do pipeline synchronization on the app side and avoid blocking the host thread on waiting for the completion of inference. The pseudo-code may look as follows:

.. raw:: html

   <div class="collapsible-section" data-title="Queue and context sharing example">

.. ref-code-block:: cpp


	// ...

	// initialize the core and read the model
	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>`("model.xml");

	// get opencl queue object
	cl::CommandQueue queue = get_ocl_queue();
	cl::Context cl_context = get_ocl_context();

	// share the queue with GPU plugin and compile model
	auto remote_context = :ref:`ov::intel_gpu::ocl::ClContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_context>`(core, queue.get());
	auto exec_net_shared = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, remote_context);

	auto input = :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->get_parameters().at(0);
	auto input_size = :ref:`ov::shape_size <doxid-group__ov__model__cpp__api_1gafe8cdd6477ae9810c2bf368602d35883>`(input->get_shape());
	auto output = :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->get_results().at(0);
	auto output_size = :ref:`ov::shape_size <doxid-group__ov__model__cpp__api_1gafe8cdd6477ae9810c2bf368602d35883>`(output->get_shape());
	cl_int err;

	// create the OpenCL buffers within the context
	cl::Buffer shared_in_buffer(cl_context, CL_MEM_READ_WRITE, input_size, NULL, &err);
	cl::Buffer shared_out_buffer(cl_context, CL_MEM_READ_WRITE, output_size, NULL, &err);
	// wrap in and out buffers into RemoteTensor and set them to infer request
	auto shared_in_blob = remote_context.create_tensor(input->get_element_type(), input->get_shape(), shared_in_buffer);
	auto shared_out_blob = remote_context.create_tensor(output->get_element_type(), output->get_shape(), shared_out_buffer);
	auto infer_request = exec_net_shared.create_infer_request();
	infer_request.:ref:`set_tensor <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>`(input, shared_in_blob);
	infer_request.:ref:`set_tensor <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>`(output, shared_out_blob);

	// ...
	// execute user kernel
	cl::Program program;
	cl::Kernel kernel_preproc(program, "user_kernel_preproc");
	kernel_preproc.setArg(0, shared_in_buffer);
	queue.enqueueNDRangeKernel(kernel_preproc,
	                           cl::NDRange(0),
	                           cl::NDRange(input_size),
	                           cl::NDRange(1),
	                           nullptr,
	                           nullptr);
	// Blocking clFinish() call is not required, but this barrier is added to the queue to guarantee that user kernel is finished
	// before any inference primitive is started
	queue.enqueueBarrierWithWaitList(nullptr, nullptr);
	// ...

	// pass results to the inference
	// since the remote context is created with queue sharing, start_async() guarantees that scheduling is finished
	infer_request.:ref:`start_async <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>`();

	// execute some postprocessing kernel.
	// infer_request.wait() is not called, synchonization between inference and post-processing is done via
	// enqueueBarrierWithWaitList call.
	cl::Kernel kernel_postproc(program, "user_kernel_postproc");
	kernel_postproc.setArg(0, shared_out_buffer);
	queue.enqueueBarrierWithWaitList(nullptr, nullptr);
	queue.enqueueNDRangeKernel(kernel_postproc,
	                           cl::NDRange(0),
	                           cl::NDRange(output_size),
	                           cl::NDRange(1),
	                           nullptr,
	                           nullptr);

	// Wait for pipeline completion
	queue.finish();






.. raw:: html

   </div>

Limitations
-----------

* Some primitives in the GPU plugin may block the host thread on waiting for the previous primitives before adding its kernels to the command queue. In such cases the ``:ref:`ov::InferRequest::start_async() <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>``` call takes much more time to return control to the calling thread as internally it waits for a partial or full network completion. Examples of operations: Loop, TensorIterator, DetectionOutput, NonMaxSuppression

* Synchronization of pre/post processing jobs and inference pipeline inside a shared queue is user's responsibility

* Throughput mode is not available when queue sharing is used, i.e. only a single stream can be used for each compiled model.

Low-Level Methods for RemoteContext and RemoteTensor creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The high-level wrappers mentioned above bring a direct dependency on native APIs to the user program. If you want to avoid the dependency, you still can directly use the ``:ref:`ov::Core::create_context() <doxid-classov_1_1_core_1ab9a3eef07c3471037070242f8da2fb01>```, ``:ref:`ov::RemoteContext::create_tensor() <doxid-classov_1_1_remote_context_1ac1735cf031cfde65e2ced782b21cc256>```, and ``:ref:`ov::RemoteContext::get_params() <doxid-classov_1_1_remote_context_1a45f1cad216e6d44b811b89b78fe4e638>``` methods. On this level, native handles are re-interpreted as void pointers and all arguments are passed using ``:ref:`ov::AnyMap <doxid-namespaceov_1a51d339c5ba0d88c4a1397c791430af88>``` containers that are filled with ``std::string, :ref:`ov::Any <doxid-classov_1_1_any>``` pairs. Two types of map entries are possible: descriptor and container. The first map entry is a descriptor, which sets the expected structure and possible parameter values of the map.

Refer to ``openvino/runtime/intel_gpu/remote_properties.hpp`` header file for possible low-level properties and their description.

Examples
~~~~~~~~

Refer to the sections below to see pseudo-code of usage examples.

.. note:: For low-level parameter usage examples, see the source code of user-side wrappers from the include files mentioned above.

.. raw:: html

   <div class="collapsible-section" data-title="OpenCL Kernel Execution on a Shared Buffer">

This example uses the OpenCL context obtained from a compiled model object.

.. ref-code-block:: cpp


	// ...

	// initialize the core and load the network
	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>`("model.xml");
	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "GPU");
	auto infer_request = compiled_model.:ref:`create_infer_request <doxid-classov_1_1_compiled_model_1ae3633c0eb5173ed776446fba32b95953>`();


	// obtain the RemoteContext from the compiled model object and cast it to ClContext
	auto gpu_context = compiled_model.:ref:`get_context <doxid-classov_1_1_compiled_model_1a22c5537d4c7182072d327077c386b01a>`().:ref:`as <doxid-classov_1_1_remote_context_1a54021126344109640e35a18842d22654>`<:ref:`ov::intel_gpu::ocl::ClContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_context>`>();
	// obtain the OpenCL context handle from the RemoteContext,
	// get device info and create a queue
	cl::Context cl_context = gpu_context;
	cl::Device device = cl::Device(cl_context.getInfo<CL_CONTEXT_DEVICES>()[0].get(), true);
	cl_command_queue_properties props = CL_QUEUE_OUT_OF_ORDER_EXEC_MODE_ENABLE;
	cl::CommandQueue queue = cl::CommandQueue(cl_context, device, props);

	// create the OpenCL buffer within the obtained context
	auto input = :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->get_parameters().at(0);
	auto input_size = :ref:`ov::shape_size <doxid-group__ov__model__cpp__api_1gafe8cdd6477ae9810c2bf368602d35883>`(input->get_shape());
	cl_int err;
	cl::Buffer shared_buffer(cl_context, CL_MEM_READ_WRITE, input_size, NULL, &err);
	// wrap the buffer into RemoteBlob
	auto shared_blob = gpu_context.create_tensor(input->get_element_type(), input->get_shape(), shared_buffer);

	// ...
	// execute user kernel
	cl::Program program;
	cl::Kernel kernel(program, "user_kernel");
	kernel.setArg(0, shared_buffer);
	queue.enqueueNDRangeKernel(kernel,
	                           cl::NDRange(0),
	                           cl::NDRange(input_size),
	                           cl::NDRange(1),
	                           nullptr,
	                           nullptr);
	queue.finish();
	// ...
	// pass results to the inference
	infer_request.:ref:`set_tensor <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>`(input, shared_blob);
	infer_request.:ref:`infer <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>`();






.. raw:: html

   </div>

.. raw:: html

   <div class="collapsible-section" data-title="Running GPU Plugin Inference within User-Supplied Shared Context">

.. ref-code-block:: cpp

	cl::Context ctx = get_ocl_context();

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>`("model.xml");

	// share the context with GPU plugin and compile ExecutableNetwork
	auto remote_context = :ref:`ov::intel_gpu::ocl::ClContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_cl_context>`(core, ctx.get());
	auto exec_net_shared = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, remote_context);
	auto inf_req_shared = exec_net_shared.:ref:`create_infer_request <doxid-classov_1_1_compiled_model_1ae3633c0eb5173ed776446fba32b95953>`();


	// ...
	// do OpenCL processing stuff
	// ...

	// run the inference
	inf_req_shared.:ref:`infer <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>`();






.. raw:: html

   </div>

.. raw:: html

   <div class="collapsible-section" data-title="Direct Consuming of the NV12 VAAPI Video Decoder Surface on Linux">

.. ref-code-block:: cpp


	// ...

	using namespace :ref:`ov::preprocess <doxid-namespaceov_1_1preprocess>`;
	auto p = :ref:`PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);
	p.input().tensor().set_element_type(:ref:`ov::element::u8 <doxid-group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f>`)
	                  .set_color_format(ov::preprocess::ColorFormat::NV12_TWO_PLANES, {"y", "uv"})
	                  .set_memory_type(:ref:`ov::intel_gpu::memory_type::surface <doxid-group__ov__runtime__ocl__gpu__prop__cpp__api_1gaec0856a3b996876371138961269b742d>`);
	p.input().preprocess().convert_color(:ref:`ov::preprocess::ColorFormat::BGR <doxid-namespace_inference_engine_1a5ee5ca7708cc67a9a0becc2593d0558aa0fb221afef06def7c25b82d6fa9efc1b>`);
	p.input().model().set_layout("NCHW");
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = p.build();

	VADisplay disp = get_va_display();
	// create the shared context object
	auto shared_va_context = :ref:`ov::intel_gpu::ocl::VAContext <doxid-classov_1_1intel__gpu_1_1ocl_1_1_v_a_context>`(core, disp);
	// compile model within a shared context
	auto compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, shared_va_context);

	auto input = :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->get_parameters().at(0);
	size_t width = 1024;
	size_t height = 768;

	// execute decoding and obtain decoded surface handle
	VASurfaceID va_surface = decode_va_surface();
	//     ...
	//wrap decoder output into RemoteBlobs and set it as inference input
	auto nv12_blob = shared_va_context.create_tensor_nv12(height, width, va_surface);

	auto infer_request = compiled_model.:ref:`create_infer_request <doxid-classov_1_1_compiled_model_1ae3633c0eb5173ed776446fba32b95953>`();
	infer_request.:ref:`set_tensor <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>`("y", nv12_blob.first);
	infer_request.:ref:`set_tensor <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>`("uv", nv12_blob.second);
	infer_request.:ref:`start_async <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>`();
	infer_request.:ref:`wait <doxid-classov_1_1_infer_request_1ab0e0739da45789d816f8b5584a0b5691>`();






.. raw:: html

   </div>

See Also
~~~~~~~~

* :ref:`ov::Core <doxid-classov_1_1_core>`

* :ref:`ov::RemoteTensor <doxid-classov_1_1_remote_tensor>`

