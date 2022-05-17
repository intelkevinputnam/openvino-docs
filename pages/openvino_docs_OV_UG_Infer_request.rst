.. index:: pair: page; OpenVINO™ Inference Request
.. _doxid-openvino_docs__o_v__u_g__infer_request:


OpenVINO™ Inference Request
=============================

:target:`doxid-openvino_docs__o_v__u_g__infer_request_1md_openvino_docs_ov_runtime_ug_ov_infer_request` OpenVINO™ Runtime uses Infer Request mechanism which allows to run models on different devices in asynchronous or synchronous manners. ``:ref:`ov::InferRequest <doxid-classov_1_1_infer_request>``` class is used for this purpose inside the OpenVINO™ Runtime. This class allows to set and get data for model inputs, outputs and run inference for the model.

Creating Infer Request
~~~~~~~~~~~~~~~~~~~~~~

``:ref:`ov::InferRequest <doxid-classov_1_1_infer_request>``` can be created from the ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` :

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto infer_request = compiled_model.:ref:`create_infer_request <doxid-classov_1_1_compiled_model_1ae3633c0eb5173ed776446fba32b95953>`();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	infer_request = compiled_model.create_infer_request()





.. raw:: html

   </div>







.. raw:: html

   </div>





Run inference
~~~~~~~~~~~~~

``:ref:`ov::InferRequest <doxid-classov_1_1_infer_request>``` supports synchronous and asynchronous modes for inference.

Synchronous mode
----------------

You can use ``:ref:`ov::InferRequest::infer <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>```, which blocks the application execution, to infer model in the synchronous mode:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	infer_request.:ref:`infer <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>`();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	infer_request.infer()





.. raw:: html

   </div>







.. raw:: html

   </div>





Asynchronous mode
-----------------

Asynchronous mode can improve application's overall frame-rate, because rather than wait for inference to complete, the app can keep working on the host, while the accelerator is busy. You can use ``:ref:`ov::InferRequest::start_async <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>``` to infer model in the asynchronous mode:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	infer_request.:ref:`start_async <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>`();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	infer_request.start_async()





.. raw:: html

   </div>







.. raw:: html

   </div>



Asynchronous mode supports two ways the application waits for inference results:

* ``:ref:`ov::InferRequest::wait_for <doxid-classov_1_1_infer_request_1a94d6d52e03d2ad20310a1e0fdd807e9e>``` - specifies the maximum duration in milliseconds to block the method. The method is blocked until the specified time has passed, or the result becomes available, whichever comes first.
  
  
  
  .. raw:: html
  
     <div class='sphinxtabset'>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="C++">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	infer_request.:ref:`wait_for <doxid-classov_1_1_infer_request_1a94d6d52e03d2ad20310a1e0fdd807e9e>`(std::chrono::milliseconds(10));
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="Python">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	infer_request.wait_for(10)
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     </div>

* ``:ref:`ov::InferRequest::wait <doxid-classov_1_1_infer_request_1ab0e0739da45789d816f8b5584a0b5691>``` - waits until inference result becomes available
  
  
  
  .. raw:: html
  
     <div class='sphinxtabset'>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="C++">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	infer_request.:ref:`wait <doxid-classov_1_1_infer_request_1ab0e0739da45789d816f8b5584a0b5691>`();
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="Python">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	infer_request.wait()
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  Both methods are thread-safe.

When you are running several inference requests in parallel, a device can process them simultaneously, with no garauntees on the completion order. This may complicate a possible logic based on the ``:ref:`ov::InferRequest::wait <doxid-classov_1_1_infer_request_1ab0e0739da45789d816f8b5584a0b5691>``` (unless your code needs to wait for the *all* requests). For multi-request scenarios, consider using the ``:ref:`ov::InferRequest::set_callback <doxid-classov_1_1_infer_request_1afba2a10162ab356728ec8901973e8f02>``` method to set a callback which is called upon completion of the request:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	infer_request.:ref:`set_callback <doxid-classov_1_1_infer_request_1afba2a10162ab356728ec8901973e8f02>`([&](std::exception_ptr ex_ptr) { 
	    if (!ex_ptr) {
	        // all done. Output data can be processed.
	        // You can fill the input data and run inference one more time:
	        infer_request.:ref:`start_async <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>`();
	    } else {
	        // Something wrong, you can analyze exception_ptr
	    }
	});





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	def callback(request, userdata):
	    request.start_async()
	
	infer_request.set_callback(callback)





.. raw:: html

   </div>







.. raw:: html

   </div>

.. note:: Use weak reference of infer_request (``:ref:`ov::InferRequest <doxid-classov_1_1_infer_request>`\*``, ``:ref:`ov::InferRequest <doxid-classov_1_1_infer_request>`&``, ``std::weal_ptr<:ref:`ov::InferRequest <doxid-classov_1_1_infer_request>`>``, etc.) in the callback. It is necessary to avoid cyclic references.



For more details, check :ref:`Classification Sample Async <doxid-openvino_inference_engine_samples_classification_sample_async__r_e_a_d_m_e>`.

You can use the ``:ref:`ov::InferRequest::cancel <doxid-classov_1_1_infer_request_1aa100b080271f057ab5f98d1832af414d>``` method if you want to abort execution of the current inference request:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	infer_request.:ref:`cancel <doxid-classov_1_1_infer_request_1aa100b080271f057ab5f98d1832af414d>`();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	infer_request.cancel()





.. raw:: html

   </div>







.. raw:: html

   </div>

Working with Input and Output tensors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``:ref:`ov::InferRequest <doxid-classov_1_1_infer_request>``` allows to get input/output tensors by tensor name, index, port and without any arguments in case if model has only one input or output.

* ``:ref:`ov::InferRequest::get_input_tensor <doxid-classov_1_1_infer_request_1a5f0bc1ab40de6a7a12136b4a4e6a8b54>```, ``:ref:`ov::InferRequest::set_input_tensor <doxid-classov_1_1_infer_request_1a5ddca7af7faffa2c90fd600a3f84aa6e>```, ``:ref:`ov::InferRequest::get_output_tensor <doxid-classov_1_1_infer_request_1a350159a8d967022db46633eed50d073a>```, ``:ref:`ov::InferRequest::set_output_tensor <doxid-classov_1_1_infer_request_1a3e93efd003301c4de6b0181163e7d14d>``` methods without arguments can be used to get or set input/output tensor for model with only one input/output:
  
  .. raw:: html
  
     <div class='sphinxtabset'>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="C++">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	auto input_tensor = infer_request.:ref:`get_input_tensor <doxid-classov_1_1_infer_request_1a5f0bc1ab40de6a7a12136b4a4e6a8b54>`();
  	auto output_tensor = infer_request.:ref:`get_output_tensor <doxid-classov_1_1_infer_request_1a350159a8d967022db46633eed50d073a>`();
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="Python">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	input_tensor = infer_request.get_input_tensor()
  	output_tensor = infer_request.get_output_tensor()
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     </div>

* ``:ref:`ov::InferRequest::get_input_tensor <doxid-classov_1_1_infer_request_1a5f0bc1ab40de6a7a12136b4a4e6a8b54>```, ``:ref:`ov::InferRequest::set_input_tensor <doxid-classov_1_1_infer_request_1a5ddca7af7faffa2c90fd600a3f84aa6e>```, ``:ref:`ov::InferRequest::get_output_tensor <doxid-classov_1_1_infer_request_1a350159a8d967022db46633eed50d073a>```, ``:ref:`ov::InferRequest::set_output_tensor <doxid-classov_1_1_infer_request_1a3e93efd003301c4de6b0181163e7d14d>``` methods with argument can be used to get or set input/output tensor by input/output index:
  
  .. raw:: html
  
     <div class='sphinxtabset'>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="C++">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	auto input_tensor = infer_request.:ref:`get_input_tensor <doxid-classov_1_1_infer_request_1a5f0bc1ab40de6a7a12136b4a4e6a8b54>`(0);
  	auto output_tensor = infer_request.:ref:`get_output_tensor <doxid-classov_1_1_infer_request_1a350159a8d967022db46633eed50d073a>`(1);
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="Python">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	input_tensor = infer_request.get_input_tensor(0)
  	output_tensor = infer_request.get_output_tensor(1)
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     </div>

* ``:ref:`ov::InferRequest::get_tensor <doxid-classov_1_1_infer_request_1a75b8da7c6b00686bede600dddceaffc4>```, ``:ref:`ov::InferRequest::set_tensor <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>``` methods can be used to get or set input/output tensor by tensor name:
  
  .. raw:: html
  
     <div class='sphinxtabset'>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="C++">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	auto tensor1 = infer_request.:ref:`get_tensor <doxid-classov_1_1_infer_request_1a75b8da7c6b00686bede600dddceaffc4>`("tensor_name1");
  	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` tensor2;
  	infer_request.:ref:`set_tensor <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>`("tensor_name2", tensor2);
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="Python">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	tensor1 = infer_request.get_tensor("tensor_name1")
  	tensor2 = :ref:`ov.Tensor <doxid-classov_1_1_tensor>`()
  	infer_request.set_tensor("tensor_name2", tensor2)
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     </div>

* ``:ref:`ov::InferRequest::get_tensor <doxid-classov_1_1_infer_request_1a75b8da7c6b00686bede600dddceaffc4>```, ``:ref:`ov::InferRequest::set_tensor <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>``` methods can be used to get or set input/output tensor by port:
  
  .. raw:: html
  
     <div class='sphinxtabset'>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="C++">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	auto input_port = :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->input(0);
  	auto output_port = :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->output("tensor_name");
  	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` input_tensor;
  	infer_request.:ref:`set_tensor <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>`(input_port, input_tensor);
  	auto output_tensor = infer_request.:ref:`get_tensor <doxid-classov_1_1_infer_request_1a75b8da7c6b00686bede600dddceaffc4>`(output_port);
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="Python">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	input_port = model.input(0)
  	output_port = model.input("tensor_name")
  	input_tensor = :ref:`ov.Tensor <doxid-classov_1_1_tensor>`()
  	infer_request.set_tensor(input_port, input_tensor)
  	output_tensor = infer_request.get_tensor(output_port)
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  Examples of InferRequest usages
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cascade of models
-----------------

``:ref:`ov::InferRequest <doxid-classov_1_1_infer_request>``` can be used to organize cascade of models. You need to have infer requests for each model. In this case you can get output tensor from the first request using ``:ref:`ov::InferRequest::get_tensor <doxid-classov_1_1_infer_request_1a75b8da7c6b00686bede600dddceaffc4>``` and set it as input for the second request using ``:ref:`ov::InferRequest::set_tensor <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>```. But be careful, shared tensors across compiled models can be rewritten by the first model if the first infer request is run once again, while the second model has not started yet.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto output = infer_request1.get_output_tensor(0);
	infer_request2.set_input_tensor(0, output);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	output = infer_request1.get_output_tensor(0)
	infer_request2.set_input_tensor(0, output)





.. raw:: html

   </div>







.. raw:: html

   </div>





Using of ROI tensors
--------------------

It is possible to re-use shared input by several models. You do not need to allocate separate input tensor for a model if it processes a ROI object located inside of already allocated input of a previous model. For instance, when the first model detects objects in a video frame (stored as input tensor) and the second model accepts detected bounding boxes (ROI inside of the frame) as input. In this case, it is allowed to re-use pre-allocated input tensor (used by the first model) by the second model and just crop ROI without allocation of new memory using ``:ref:`ov::Tensor <doxid-classov_1_1_tensor>``` with passing of ``:ref:`ov::Tensor <doxid-classov_1_1_tensor>``` and ``:ref:`ov::Coordinate <doxid-classov_1_1_coordinate>``` as parameters.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	/\*\* input_tensor points to input of a previous network and
	    cropROI contains coordinates of output bounding box \*\*/
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` input_tensor(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`({1, 3, 20, 20}));
	:ref:`ov::Coordinate <doxid-classov_1_1_coordinate>` begin({0, 0, 0, 0});
	:ref:`ov::Coordinate <doxid-classov_1_1_coordinate>` end({1, 2, 3, 3});
	//...
	
	/\*\* roi_tensor uses shared memory of input_tensor and describes cropROI
	    according to its coordinates \*\*/
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` roi_tensor(input_tensor, begin, end);
	infer_request2.set_tensor("input_name", roi_tensor);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# input_tensor points to input of a previous network and
	# cropROI contains coordinates of output bounding box \*\*/
	input_tensor = :ref:`ov.Tensor <doxid-classov_1_1_tensor>`(type=ov.Type.f32, shape=:ref:`ov.Shape <doxid-classov_1_1_shape>`([1, 3, 20, 20]))
	begin = [0, 0, 0, 0]
	end = [1, 2, 3, 3]
	# ...
	
	# roi_tensor uses shared memory of input_tensor and describes cropROI
	# according to its coordinates \*\*/
	roi_tensor = :ref:`ov.Tensor <doxid-classov_1_1_tensor>`(input_tensor, begin, end)
	infer_request2.set_tensor("input_name", roi_tensor)





.. raw:: html

   </div>







.. raw:: html

   </div>





Using of remote tensors
-----------------------

You can create a remote tensor to work with remote device memory. ``:ref:`ov::RemoteContext <doxid-classov_1_1_remote_context>``` allows to create remote tensor.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::RemoteContext <doxid-classov_1_1_remote_context>` context = core.:ref:`get_default_context <doxid-classov_1_1_core_1a0ae465fb50e92fa63054c2d0acfd25ae>`("GPU");
	auto input_port = compiled_model.:ref:`input <doxid-classov_1_1_compiled_model_1a55f2867a43fb78829f9901c52f9ccea9>`("tensor_name");
	:ref:`ov::RemoteTensor <doxid-classov_1_1_remote_tensor>` remote_tensor = context.:ref:`create_tensor <doxid-classov_1_1_remote_context_1ac1735cf031cfde65e2ced782b21cc256>`(input_port.get_element_type(), input_port.get_shape());
	infer_request.:ref:`set_tensor <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>`(input_port, remote_tensor);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# NOT SUPPORTED





.. raw:: html

   </div>







.. raw:: html

   </div>

