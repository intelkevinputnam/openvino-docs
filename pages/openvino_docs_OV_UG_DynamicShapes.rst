.. index:: pair: page; Dynamic Shapes
.. _doxid-openvino_docs__o_v__u_g__dynamic_shapes:


Dynamic Shapes
==============

:target:`doxid-openvino_docs__o_v__u_g__dynamic_shapes_1md_openvino_docs_ov_runtime_ug_ov_dynamic_shapes`





.. toctree::
   :maxdepth: 1
   :hidden:

   openvino_docs_OV_UG_NoDynamicShapes

As it was demonstrated in the :ref:`Changing Input Shapes <doxid-openvino_docs__o_v__u_g__shape_inference>` article, there are models that support changing of input shapes before model compilation in ``Core::compile_model``. Reshaping models provides an ability to customize the model input shape for exactly that size that is required in the end application. This article explains how the ability of model to reshape can further be leveraged in more dynamic scenarios.

When to Apply Dynamic Shapes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Conventional "static" model reshaping works well when it can be done once per many model inference calls with the same shape. However, this approach doesn't perform efficiently if the input tensor shape is changed on every inference call: calling ``:ref:`reshape() <doxid-namespacengraph_1_1builder_1_1opset1_1ae436bb386fa882348f9a2a15148af42d>``` and ``compile_model()`` each time when a new size comes is extremely time-consuming. A popular example would be an inference of natural language processing models (like BERT) with arbitrarily-sized input sequences that come from the user. In this case, the sequence length cannot be predicted and may change every time you need to call inference. Below, such dimensions that can be frequently changed are called *dynamic dimensions*. When real shape of input is not known at ``compile_model`` time, that's the case when dynamic shapes should be considered.

Here are several examples of dimensions that can be naturally dynamic:

* Sequence length dimension for various sequence processing models, like BERT

* Spatial dimensions in segmentation and style transfer models

* Batch dimension

* Arbitrary number of detections in object detection models output

There are various tricks to address input dynamic dimensions through combining multiple pre-reshaped models and input data padding. The tricks are sensitive to model internals, do not always give optimal performance and cumbersome. Short overview of the methods you can find :ref:`here <doxid-openvino_docs__o_v__u_g__no_dynamic_shapes>`. Apply those methods only if native dynamic shape API described in the following sections doesn't work for you or doesn't give desired performance.

The decision about using dynamic shapes should be based on proper benchmarking of real application with real data. That's because unlike statically shaped models, inference of dynamically shaped ones takes different inference time depending on input data shape or input tensor content. Also using the dynamic shapes can bring more overheads in memory and running time per each inference call depending on hardware plugin and model used.

Dynamic Shapes without Tricks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section describes how to handle dynamically shaped models natively with OpenVINO Runtime API version 2022.1 and higher. There are three main parts in the flow that differ from static shapes:

* configure the model

* prepare data for inference

* read resulting data after inference

Configure the Model
-------------------

To avoid the tricks mentioned in the previous section there is a way to directly specify one or multiple dimensions in the model inputs to be dynamic. This is achieved with the same reshape method that is used for alternating static shape of inputs. Dynamic dimensions are specified as ``-1`` or ``:ref:`ov::Dimension() <doxid-classov_1_1_dimension>``` instead of a positive number used for static dimensions:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>`("model.xml");
	
	// Set one static dimension (= 1) and another dynamic dimension (= Dimension())
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape({{1, :ref:`ov::Dimension <doxid-classov_1_1_dimension>`()}});  // {1,?}
	
	// The same as above
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape({{1, -1}}); // {1,?}
	
	// Or set both dimensions as dynamic if both are going to be changed dynamically
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape({{:ref:`ov::Dimension <doxid-classov_1_1_dimension>`(), :ref:`ov::Dimension <doxid-classov_1_1_dimension>`()}});  // {?,?}
	
	// The same as above
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape({{-1, -1}});  // {?,?}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core = :ref:`ov.Core <doxid-classov_1_1_core>`()
	model = core.read_model("model.xml")
	
	# Set one static dimension (= 1) and another dynamic dimension (= Dimension())
	model.reshape([1, :ref:`ov.Dimension <doxid-classov_1_1_dimension>`()])
	
	# The same as above
	model.reshape([1, -1])
	
	# The same as above
	model.reshape("1, ?")
	
	# Or set both dimensions as dynamic if both are going to be changed dynamically
	model.reshape([:ref:`ov.Dimension <doxid-classov_1_1_dimension>`(), :ref:`ov.Dimension <doxid-classov_1_1_dimension>`()])
	
	# The same as above
	model.reshape([-1, -1])
	
	# The same as above
	model.reshape("?, ?")





.. raw:: html

   </div>







.. raw:: html

   </div>



To simplify the code, the examples assume that the model has a single input and single output. However, there are no limitations on the number of inputs and outputs to apply dynamic shapes.

Undefined Dimensions "Out Of the Box"
-------------------------------------

Dynamic dimensions may appear in the input model without calling reshape. Many DL frameworks support undefined dimensions. If such a model is converted with Model Optimizer or read directly by Core::read_model, undefined dimensions are preserved. Such dimensions automatically treated as dynamic ones. So you don't need to call reshape if undefined dimensions are already configured in the original model or in the IR file.

If the input model has undefined dimensions that you are not going to change during the inference, it is recommended to set them to static values, using the same ``reshape`` method of the model. From the API perspective any combination of dynamic and static dimensions can be configured.

Model Optimizer provides identical capability to reshape the model during the conversion, including specifying dynamic dimensions. Use this capability to save time on calling ``reshape`` method in the end application. To get information about setting input shapes using Model Optimizer, refer to :ref:`Setting Input Shapes <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__converting__model>`

Dimension Bounds
----------------

Besides marking a dimension just dynamic, you can also specify lower and/or upper bounds that define a range of allowed values for the dimension. Bounds are coded as arguments for ``:ref:`ov::Dimension <doxid-classov_1_1_dimension>``` :

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Both dimensions are dynamic, first has a size within 1..10 and the second has a size within 8..512
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape({{:ref:`ov::Dimension <doxid-classov_1_1_dimension>`(1, 10), :ref:`ov::Dimension <doxid-classov_1_1_dimension>`(8, 512)}});  // {1..10,8..512}
	
	// Both dimensions are dynamic, first doesn't have bounds, the second is in the range of 8..512
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->reshape({{-1, :ref:`ov::Dimension <doxid-classov_1_1_dimension>`(8, 512)}});   // {?,8..512}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Both dimensions are dynamic, first has a size within 1..10 and the second has a size within 8..512
	model.reshape([:ref:`ov.Dimension <doxid-classov_1_1_dimension>`(1, 10), :ref:`ov.Dimension <doxid-classov_1_1_dimension>`(8, 512)])
	
	# The same as above
	model.reshape([(1, 10), (8, 512)])
	
	# The same as above
	model.reshape("1..10, 8..512")
	
	# Both dimensions are dynamic, first doesn't have bounds, the second is in the range of 8..512
	model.reshape([-1, (8, 512)])





.. raw:: html

   </div>







.. raw:: html

   </div>



Information about bounds gives opportunity for the inference plugin to apply additional optimizations. Using dynamic shapes assumes the plugins apply more loose optimization technique during model compilation It may require more time/memory for model compilation and inference. So providing any additional information like bounds can be beneficial. For the same reason it is not recommended to leave dimensions as undefined without the real need.

When specifying bounds, the lower bound is not so important as upper bound, because knowing of upper bound allows inference devices to more precisely allocate memory for intermediate tensors for inference and use lesser number of tuned kernels for different sizes. Precisely speaking benefits of specifying lower or upper bound is device dependent. Depending on the plugin specifying upper bounds can be required. For information about dynamic shapes support on different devices, see the :ref:`Features Support Matrix <doxid-openvino_docs__o_v__u_g__working_with_devices_1features_support_matrix>`.

If users known lower and upper bounds for dimension it is recommended to specify them even when plugin can execute model without the bounds.

Setting Input Tensors
---------------------

Preparing model with the reshape method was the first step. The second step is passing a tensor with an appropriate shape to infer request. This is similar to :ref:`regular steps <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>`, but now we can pass tensors with different shapes for the same executable model and even for the same inference request:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// The first inference call
	
	// Create tensor compatible with the model input
	// Shape {1, 128} is compatible with any reshape statements made in previous examples
	auto input_tensor_1 = :ref:`ov::Tensor <doxid-classov_1_1_tensor>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->input().get_element_type(), {1, 128});
	// ... write values to input_tensor_1
	
	// Set the tensor as an input for the infer request
	infer_request.:ref:`set_input_tensor <doxid-classov_1_1_infer_request_1a5ddca7af7faffa2c90fd600a3f84aa6e>`(input_tensor_1);
	
	// Do the inference
	infer_request.:ref:`infer <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>`();
	
	// Retrieve a tensor representing the output data
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` output_tensor = infer_request.:ref:`get_output_tensor <doxid-classov_1_1_infer_request_1a350159a8d967022db46633eed50d073a>`();
	
	// For dynamic models output shape usually depends on input shape,
	// that means shape of output tensor is initialized after the first inference only
	// and has to be queried after every infer request
	auto output_shape_1 = output_tensor.:ref:`get_shape <doxid-classov_1_1_tensor_1a706163e01fb555eb9ccdfb5204cf7834>`();
	
	// Take a pointer of an appropriate type to tensor data and read elements according to the shape
	// Assuming model output is f32 data type
	auto data_1 = output_tensor.:ref:`data <doxid-classov_1_1_tensor_1ac1b8835f54d67d92969d7979e666e2a8>`<float>();
	// ... read values
	
	// The second inference call, repeat steps:
	
	// Create another tensor (if the previous one cannot be utilized)
	// Notice, the shape is different from input_tensor_1
	auto input_tensor_2 = :ref:`ov::Tensor <doxid-classov_1_1_tensor>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->input().get_element_type(), {1, 200});
	// ... write values to input_tensor_2
	
	infer_request.:ref:`set_input_tensor <doxid-classov_1_1_infer_request_1a5ddca7af7faffa2c90fd600a3f84aa6e>`(input_tensor_2);
	
	infer_request.:ref:`infer <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>`();
	
	// No need to call infer_request.get_output_tensor() again
	// output_tensor queried after the first inference call above is valid here.
	// But it may not be true for the memory underneath as shape changed, so re-take a pointer:
	auto data_2 = output_tensor.:ref:`data <doxid-classov_1_1_tensor_1ac1b8835f54d67d92969d7979e666e2a8>`<float>();
	
	// and new shape as well
	auto output_shape_2 = output_tensor.:ref:`get_shape <doxid-classov_1_1_tensor_1a706163e01fb555eb9ccdfb5204cf7834>`();
	
	// ... read values in data_2 according to the shape output_shape_2





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# The first inference call
	
	# Create tensor compatible to the model input
	# Shape {1, 128} is compatible with any reshape statements made in previous examples
	input_tensor1 = :ref:`ov.Tensor <doxid-classov_1_1_tensor>`(model.input().element_type, [1, 128])
	# ... write values to input_tensor_1
	
	# Set the tensor as an input for the infer request
	infer_request.set_input_tensor(input_tensor1)
	
	# Do the inference
	infer_request.infer()
	
	# Or pass a tensor in infer to set the tensor as a model input and make the inference
	infer_request.infer([input_tensor1])
	
	# Or pass the numpy array to set inputs of the infer request
	input_data = np.ones(shape=[1, 128])
	infer_request.infer([input_data])
	
	# Retrieve a tensor representing the output data
	output_tensor = infer_request.get_output_tensor()
	
	# Copy data from tensor to numpy array
	data1 = output_tensor.data[:]
	
	# The second inference call, repeat steps:
	
	# Create another tensor (if the previous one cannot be utilized)
	# Notice, the shape is different from input_tensor_1
	input_tensor2 = :ref:`ov.Tensor <doxid-classov_1_1_tensor>`(model.input().element_type, [1, 200])
	# ... write values to input_tensor_2
	
	infer_request.infer([input_tensor2])
	
	# No need to call infer_request.get_output_tensor() again
	# output_tensor queried after the first inference call above is valid here.
	# But it may not be true for the memory underneath as shape changed, so re-take an output data:
	data2 = output_tensor.data[:]





.. raw:: html

   </div>







.. raw:: html

   </div>



In the example above ``set_input_tensor`` is used to specify input tensors. The real dimensions of the tensor is always static, because it is a concrete tensor and it doesn't have any dimension variations in contrast to model inputs.

Similar to static shapes, ``get_input_tensor`` can be used instead of ``set_input_tensor``. In contrast to static input shapes, when using ``get_input_tensor`` for dynamic inputs, ``set_shape`` method for the returned tensor should be called to define the shape and allocate memory. Without doing that, the tensor returned by ``get_input_tensor`` is an empty tensor, it's shape is not initialized and memory is not allocated, because infer request doesn't have information about real shape you are going to feed. Setting shape for input tensor is required when the corresponding input has at least one dynamic dimension regardless of bounds information. The following example makes the same sequence of two infer request as the previous example but using ``get_input_tensor`` instead of ``set_input_tensor`` :

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// The first inference call
	
	// Get the tensor; shape is not initialized
	auto input_tensor = infer_request.:ref:`get_input_tensor <doxid-classov_1_1_infer_request_1a5f0bc1ab40de6a7a12136b4a4e6a8b54>`();
	
	// Set shape is required
	input_tensor.:ref:`set_shape <doxid-classov_1_1_tensor_1a7a513a53ac7221d1a52006c34bce6c18>`({1, 128});
	// ... write values to input_tensor
	
	infer_request.:ref:`infer <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>`();
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` output_tensor = infer_request.:ref:`get_output_tensor <doxid-classov_1_1_infer_request_1a350159a8d967022db46633eed50d073a>`();
	auto output_shape_1 = output_tensor.:ref:`get_shape <doxid-classov_1_1_tensor_1a706163e01fb555eb9ccdfb5204cf7834>`();
	auto data_1 = output_tensor.:ref:`data <doxid-classov_1_1_tensor_1ac1b8835f54d67d92969d7979e666e2a8>`<float>();
	// ... read values
	
	// The second inference call, repeat steps:
	
	// Set a new shape, may reallocate tensor memory
	input_tensor.set_shape({1, 200});
	// ... write values to input_tensor memory
	
	infer_request.:ref:`infer <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>`();
	auto data_2 = output_tensor.:ref:`data <doxid-classov_1_1_tensor_1ac1b8835f54d67d92969d7979e666e2a8>`<float>();
	auto output_shape_2 = output_tensor.:ref:`get_shape <doxid-classov_1_1_tensor_1a706163e01fb555eb9ccdfb5204cf7834>`();
	// ... read values in data_2 according to the shape output_shape_2





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Get the tensor, shape is not initialized
	input_tensor = infer_request.get_input_tensor()
	
	# Set shape is required
	input_tensor.shape = [1, 128]
	# ... write values to input_tensor
	
	infer_request.infer()
	output_tensor = infer_request.get_output_tensor()
	data1 = output_tensor.data[:]
	
	# The second inference call, repeat steps:
	
	# Set a new shape, may reallocate tensor memory
	input_tensor.shape = [1, 200]
	# ... write values to input_tensor
	
	infer_request.infer()
	data2 = output_tensor.data[:]





.. raw:: html

   </div>







.. raw:: html

   </div>





Dynamic Shapes in Outputs
-------------------------

Examples above handle correctly case when dynamic dimensions in output may be implied by propagating of dynamic dimension from the inputs. For example, batch dimension in input shape is usually propagated through the whole model and appears in the output shape. The same is true for other dimensions, like sequence length for NLP models or spatial dimensions for segmentation models, that are propagated through the entire network.

Whether or not output has dynamic dimensions can be examined by querying output partial shape after model read or reshape. The same is applicable for inputs. For example:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Print output partial shape
	std::cout << :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->output().get_partial_shape() << "\n";
	
	// Print input partial shape
	std::cout << :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->input().get_partial_shape() << "\n";





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Print output partial shape
	print(model.output().partial_shape)
	
	# Print input partial shape
	print(model.input().partial_shape)





.. raw:: html

   </div>







.. raw:: html

   </div>



Appearing ``?`` or ranges like ``1..10`` means there are dynamic dimensions in corresponding inputs or outputs.

Or more programmatically:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>`("model.xml");
	
	if (:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->input(0).get_partial_shape().is_dynamic()) {
	    // input is dynamic
	}
	
	if (:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->output(0).get_partial_shape().is_dynamic()) {
	    // output is dynamic
	}
	
	if (:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->output(0).get_partial_shape()[1].is_dynamic()) {
	    // 1-st dimension of output is dynamic
	}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	model = core.read_model("model.xml")
	
	if model.input(0).partial_shape.is_dynamic():
	    # input is dynamic
	    pass
	
	if model.output(0).partial_shape.is_dynamic():
	    # output is dynamic
	    pass
	
	if model.output(0).partial_shape[1].is_dynamic():
	    # 1-st dimension of output is dynamic
	    pass





.. raw:: html

   </div>







.. raw:: html

   </div>

If at least one dynamic dimension exists in output of the model, shape of the corresponding output tensor will be set as the result of inference call. Before the first inference, memory for such a tensor is not allocated and has shape ``[0]``. If user call ``set_output_tensor`` with pre-allocated tensor, the inference will call ``set_shape`` internally, and the initial shape is replaced by the really calculated shape. So setting shape for output tensors in this case is useful only if you want to pre-allocate enough memory for output tensor, because ``Tensor`` 's ``set_shape`` method will re-allocate memory only if new shape requires more storage.

