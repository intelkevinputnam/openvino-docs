.. index:: pair: page; Preprocessing API - details
.. _doxid-openvino_docs__o_v__u_g__preprocessing__details:


Preprocessing API - details
===========================

:target:`doxid-openvino_docs__o_v__u_g__preprocessing__details_1md_openvino_docs_ov_runtime_ug_preprocessing_details`

Preprocessing capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~

Addressing particular input/output
----------------------------------

If your model has only one input, then simple ``:ref:`ov::preprocess::PrePostProcessor::input() <doxid-classov_1_1preprocess_1_1_pre_post_processor_1aacaaece6f739eeabac7b5c31f141471c>``` will get a reference to preprocessing builder for this input (tensor, steps, model):

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	ppp.input() // no index/name is needed if model has one input
	  .preprocess().scale(50.:ref:`f <doxid-namespacengraph_1_1runtime_1_1reference_1a4582949bb0b6082a5159f90c43a71ca9>`);
	
	ppp.output()   // same for output
	  .postprocess().convert_element_type(:ref:`ov::element::u8 <doxid-group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f>`);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# no index/name is needed if model has one input
	ppp.input().preprocess().scale(50.)
	
	# same for output
	ppp.output() \
	    .postprocess().convert_element_type(Type.u8)





.. raw:: html

   </div>







.. raw:: html

   </div>

In general, when model has multiple inputs/outputs, each one can be addressed by tensor name

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto &input_image = ppp.input("image");
	auto &output_result = ppp.output("result");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp.input('image')
	ppp.output('result')





.. raw:: html

   </div>







.. raw:: html

   </div>

Or by it's index

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto &input_1 = ppp.input(1); // Gets 2nd input in a model
	auto &output_1 = ppp.output(2); // Get output with index=2 (3rd one) in a model





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp.input(1) # Gets 2nd input in a model
	ppp.output(2) # Gets output with index=2 (3rd one) in a model





.. raw:: html

   </div>







.. raw:: html

   </div>



C++ references:

* ``:ref:`ov::preprocess::InputTensorInfo <doxid-classov_1_1preprocess_1_1_input_tensor_info>```

* ``:ref:`ov::preprocess::OutputTensorInfo <doxid-classov_1_1preprocess_1_1_output_tensor_info>```

* ``:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>```

Supported preprocessing operations
----------------------------------

C++ references:

* ``:ref:`ov::preprocess::PreProcessSteps <doxid-classov_1_1preprocess_1_1_pre_process_steps>```

Mean/Scale normalization
++++++++++++++++++++++++

Typical data normalization includes 2 operations for each data item: subtract mean value and divide to standard deviation. This can be done with the following code:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	ppp.input("input").preprocess().mean(128).scale(127);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp.input('input').preprocess().:ref:`mean <doxid-namespacengraph_1_1builder_1_1opset1_1a3377b4f15f56daf79c96a94ccefdb489>`(128).scale(127)





.. raw:: html

   </div>







.. raw:: html

   </div>



In Computer Vision area normalization is usually done separately for R, G, B values. To do this, :ref:`layout with 'C' dimension <doxid-openvino_docs__o_v__u_g__layout__overview>` shall be defined. Example:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Suppose model's shape is {1, 3, 224, 224}
	ppp.input("input").model().set_layout("NCHW"); // N=1, C=3, H=224, W=224
	// Mean/Scale has 3 values which matches with C=3
	ppp.input("input").preprocess()
	  .mean({103.94, 116.78, 123.68}).scale({57.21, 57.45, 57.73});





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Suppose model's shape is {1, 3, 224, 224}
	# N=1, C=3, H=224, W=224
	ppp.input('input').:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW'))
	# Mean/Scale has 3 values which matches with C=3
	ppp.input('input').preprocess() \
	    .:ref:`mean <doxid-namespacengraph_1_1builder_1_1opset1_1a3377b4f15f56daf79c96a94ccefdb489>`([103.94, 116.78, 123.68]).scale([57.21, 57.45, 57.73])





.. raw:: html

   </div>







.. raw:: html

   </div>



C++ references:

* ``:ref:`ov::preprocess::PreProcessSteps::mean() <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a73234aefee9b6f7c585ac7718c1e396e>```

* ``:ref:`ov::preprocess::PreProcessSteps::scale() <doxid-classov_1_1preprocess_1_1_pre_process_steps_1ae32615f1a234e4c49c1eedf4cabf99ac>```

Convert precision
+++++++++++++++++

In Computer Vision, image is represented by array of unsigned 8-but integer values (for each color), but model accepts floating point tensors

To integrate precision conversion into execution graph as a preprocessing step, just do:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// First define data type for your tensor
	ppp.input("input").tensor().set_element_type(:ref:`ov::element::u8 <doxid-group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f>`);
	
	// Then define preprocessing step
	ppp.input("input").preprocess().convert_element_type(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`);
	
	// If conversion is needed to `model's` element type, 'f32' can be omitted
	ppp.input("input").preprocess().convert_element_type();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# First define data type for your tensor
	ppp.input('input').tensor().set_element_type(Type.u8)
	
	# Then define preprocessing step
	ppp.input('input').preprocess().convert_element_type(Type.f32)
	
	# If conversion is needed to `model's` element type, 'f32' can be omitted
	ppp.input('input').preprocess().convert_element_type()





.. raw:: html

   </div>







.. raw:: html

   </div>



C++ references:

* ``:ref:`ov::preprocess::InputTensorInfo::set_element_type() <doxid-classov_1_1preprocess_1_1_input_tensor_info_1a320c54e50d794da07852ccecf9468e2a>```

* ``:ref:`ov::preprocess::PreProcessSteps::convert_element_type() <doxid-classov_1_1preprocess_1_1_pre_process_steps_1ab9e7979668e7403a72b07786f76ec0e0>```

Convert layout (transpose)
++++++++++++++++++++++++++

Transposing of matrices/tensors is a typical operation in Deep Learning - you may have a BMP image 640x480 which is an array of ``{480, 640, 3}`` elements, but Deep Learning model can require input with shape ``{1, 3, 480, 640}``

Using :ref:`layout <doxid-openvino_docs__o_v__u_g__layout__overview>` of user's tensor and layout of original model conversion can be done implicitly

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// First define layout for your tensor
	ppp.input("input").tensor().set_layout("NHWC");
	
	// Then define layout of model
	ppp.input("input").model().set_layout("NCHW");
	
	std::cout << ppp; // Will print 'implicit layout conversion step'





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# First define layout for your tensor
	ppp.input('input').tensor().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NHWC'))
	
	# Then define layout of model
	ppp.input('input').:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW'))
	
	print(ppp)  # Will print 'implicit layout conversion step'





.. raw:: html

   </div>







.. raw:: html

   </div>

Or if you prefer manual transpose of axes without usage of :ref:`layout <doxid-openvino_docs__o_v__u_g__layout__overview>` in your code, just do:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	ppp.input("input").tensor().set_shape({1, 480, 640, 3});
	// Model expects shape {1, 3, 480, 640}
	ppp.input("input").preprocess().convert_layout({0, 3, 1, 2});
	// 0 -> 0; 3 -> 1; 1 -> 2; 2 -> 3





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp.input('input').tensor().set_shape([1, 480, 640, 3])
	
	# Model expects shape {1, 3, 480, 640}
	ppp.input('input').preprocess()\
	    .convert_layout([0, 3, 1, 2])
	# 0 -> 0; 3 -> 1; 1 -> 2; 2 -> 3





.. raw:: html

   </div>







.. raw:: html

   </div>



It performs the same transpose, but we believe that approach using source and destination layout can be easier to read and understand

C++ references:

* ``:ref:`ov::preprocess::PreProcessSteps::convert_layout() <doxid-classov_1_1preprocess_1_1_pre_process_steps_1ab5a0cd9d0090f82e0489171a057fcfd4>```

* ``:ref:`ov::preprocess::InputTensorInfo::set_layout() <doxid-classov_1_1preprocess_1_1_input_tensor_info_1af10932e00c45bb0ef09b2f856fab5268>```

* ``:ref:`ov::preprocess::InputModelInfo::set_layout() <doxid-classov_1_1preprocess_1_1_input_model_info_1aeac53aa90be5b8a6b86def31fab396b4>```

* ``:ref:`ov::Layout <doxid-classov_1_1_layout>```

Resize image
++++++++++++

Resizing of image is a typical preprocessing step for computer vision tasks. With preprocessing API this step can also be integrated into execution graph and performed on target device.

To resize the input image, it is needed to define ``H`` and ``W`` dimensions of :ref:`layout <doxid-openvino_docs__o_v__u_g__layout__overview>`

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	ppp.input("input").tensor().set_shape({1, 3, 960, 1280});
	ppp.input("input").model().set_layout("??HW");
	ppp.input("input").preprocess().resize(ov::preprocess::ResizeAlgorithm::RESIZE_LINEAR, 480, 640);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp.input('input').tensor().set_shape([1, 3, 960, 1280])
	ppp.input('input').:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('??HW'))
	ppp.input('input').preprocess()\
	    .resize(ResizeAlgorithm.RESIZE_LINEAR, 480, 640)





.. raw:: html

   </div>







.. raw:: html

   </div>



Or in case if original model has known spatial dimensions (widht+height), target width/height can be omitted

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	ppp.input("input").tensor().set_shape({1, 3, 960, 1280});
	ppp.input("input").model().set_layout("??HW"); // Model accepts {1, 3, 480, 640} shape
	// Resize to model's dimension
	ppp.input("input").preprocess().resize(ov::preprocess::ResizeAlgorithm::RESIZE_LINEAR);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp.input('input').tensor().set_shape([1, 3, 960, 1280])
	# Model accepts {1, 3, 480, 640} shape, thus last dimensions are 'H' and 'W'
	ppp.input('input').:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('??HW'))
	# Resize to model's dimension
	ppp.input('input').preprocess().resize(ResizeAlgorithm.RESIZE_LINEAR)





.. raw:: html

   </div>







.. raw:: html

   </div>



C++ references:

* ``:ref:`ov::preprocess::PreProcessSteps::resize() <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a910dfdc8dc19b1890b2e8f111162a8d6>```

* ``:ref:`ov::preprocess::ResizeAlgorithm <doxid-namespaceov_1_1preprocess_1a8665e295e222dc2120be3550e04db8f3>```

Color conversion
++++++++++++++++

Typical use case is to reverse color channels from RGB to BGR and wise versa. To do this, specify source color format in ``tensor`` section and perform ``convert_color`` preprocessing operation. In example below, user has ``BGR`` image and needs to convert it to ``RGB`` as required for model's input

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	ppp.input("input").tensor().set_color_format(:ref:`ov::preprocess::ColorFormat::BGR <doxid-namespace_inference_engine_1a5ee5ca7708cc67a9a0becc2593d0558aa0fb221afef06def7c25b82d6fa9efc1b>`);
	ppp.input("input").preprocess().convert_color(:ref:`ov::preprocess::ColorFormat::RGB <doxid-namespace_inference_engine_1a5ee5ca7708cc67a9a0becc2593d0558aae2262afdcd9754598dbc87e4a4725246>`);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp.input('input').tensor().set_color_format(ColorFormat.BGR)
	
	ppp.input('input').preprocess().convert_color(ColorFormat.RGB)





.. raw:: html

   </div>







.. raw:: html

   </div>





Color conversion - NV12/I420
++++++++++++++++++++++++++++

Preprocessing also support YUV-family source color formats, i.e. NV12 and I420. In advanced cases such YUV images can be splitted into separate planes, e.g. for NV12 images Y-component may come from one source and UV-component comes from another source. Concatenating such components in user's application manually is not a perfect solution from performance and device utilization perspectives, so there is a way to use Preprocessing API. For such cases there is ``NV12_TWO_PLANES`` and ``I420_THREE_PLANES`` source color formats, which will split original ``input`` to 2 or 3 inputs

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// This will split original `input` to 2 separate inputs: `input/y' and 'input/uv'
	ppp.input("input").tensor().set_color_format(ov::preprocess::ColorFormat::NV12_TWO_PLANES);
	ppp.input("input").preprocess().convert_color(:ref:`ov::preprocess::ColorFormat::RGB <doxid-namespace_inference_engine_1a5ee5ca7708cc67a9a0becc2593d0558aae2262afdcd9754598dbc87e4a4725246>`);
	std::cout << ppp;  // Dump preprocessing steps to see what will happen





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# This will split original `input` to 2 separate inputs: `input/y' and 'input/uv'
	ppp.input('input').tensor()\
	    .set_color_format(ColorFormat.NV12_TWO_PLANES)
	
	ppp.input('input').preprocess()\
	    .convert_color(ColorFormat.RGB)
	print(ppp)  # Dump preprocessing steps to see what will happen





.. raw:: html

   </div>







.. raw:: html

   </div>



In this example, original ``input`` is being split to ``input/y`` and ``input/uv`` inputs. You can fill ``input/y`` from one source, and ``input/uv`` from another source. Color conversion to ``RGB`` will be performed using these sources, it is more optimal as there will be no additional copies of NV12 buffers.

C++ references:

* ``:ref:`ov::preprocess::ColorFormat <doxid-namespaceov_1_1preprocess_1ab027f26e58038e454e1b50a5243f1707>```

* ``:ref:`ov::preprocess::PreProcessSteps::convert_color <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a1cc7cc3fc7afb5992c1920c483ce3332>```

Custom operations
-----------------

Preprocessing API also allows adding custom preprocessing steps into execution graph. Custom step is a function which accepts current 'input' node and returns new node after adding preprocessing step

**Note:** Custom preprocessing function shall only insert node(s) after input, it will be done during model compilation. This function will NOT be called during execution phase. This may look not trivial and require some knowledge of :ref:`OpenVINO™ operations <doxid-openvino_docs_ops_opset>`

If there is a need to insert some additional operations to execution graph right after input, like some specific crops and/or resizes - Preprocessing API can be a good choice to implement this

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	ppp.input("input_image").preprocess()
	   .custom([](const :ref:`ov::Output\<ov::Node> <doxid-classov_1_1_output>`& node) {
	       // Custom nodes can be inserted as Pre-processing steps
	       return std::make_shared<ov::opset8::Abs>(node);
	   });





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# It is possible to insert some custom operations
	import openvino.runtime.opset8 as ops
	from openvino.runtime import Output
	from openvino.runtime.utils.decorators import custom_preprocess_function
	
	@custom_preprocess_function
	def custom_abs(output: Output):
	    # Custom nodes can be inserted as Preprocessing steps
	    return ops.abs(output)
	
	ppp.input("input_image").preprocess() \
	    .custom(custom_abs)





.. raw:: html

   </div>







.. raw:: html

   </div>



C++ references:

* ``:ref:`ov::preprocess::PreProcessSteps::custom() <doxid-classov_1_1preprocess_1_1_pre_process_steps_1af09aed52169c79fcea85a10e8f91d43d>```

* :ref:`Available Operations Sets <doxid-openvino_docs_ops_opset>`

Postprocessing
~~~~~~~~~~~~~~

Postprocessing steps can be added to model outputs. As for preprocessing, these steps will be also integrated into graph and executed on selected device.

Preprocessing uses flow **User tensor** -> **Steps** -> **Model input**

Postprocessing is wise versa: **Model output** -> **Steps** -> **User tensor**

Comparing to preprocessing, there is not so much operations needed to do in post-processing stage, so right now only following postprocessing operations are supported:

* Convert :ref:`layout <doxid-openvino_docs__o_v__u_g__layout__overview>`

* Convert element type

* Custom operations

Usage of these operations is similar to Preprocessing. Some example is shown below:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Model's output has 'NCHW' layout
	ppp.output("result_image").model().set_layout("NCHW");

	// Set target user's tensor to U8 type + 'NHWC' layout
	// Precision & layout conversions will be done implicitly
	ppp.output("result_image").tensor()
	   .set_layout("NHWC")
	   .set_element_type(:ref:`ov::element::u8 <doxid-group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f>`);

	// Also it is possible to insert some custom operations
	ppp.output("result_image").postprocess()
	   .custom([](const :ref:`ov::Output\<ov::Node> <doxid-classov_1_1_output>`& node) {
	       // Custom nodes can be inserted as Post-processing steps
	       return std::make_shared<ov::opset8::Abs>(node);
	   });





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Model's output has 'NCHW' layout
	ppp.output('result_image').:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW'))
	
	# Set target user's tensor to U8 type + 'NHWC' layout
	# Precision & layout conversions will be done implicitly
	ppp.output('result_image').tensor()\
	    .:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("NHWC"))\
	    .set_element_type(Type.u8)
	
	# Also it is possible to insert some custom operations
	import openvino.runtime.opset8 as ops
	from openvino.runtime import Output
	from openvino.runtime.utils.decorators import custom_preprocess_function
	
	@custom_preprocess_function
	def custom_abs(output: Output):
	    # Custom nodes can be inserted as Post-processing steps
	    return ops.abs(output)
	
	ppp.output("result_image").postprocess()\
	    .custom(custom_abs)





.. raw:: html

   </div>







.. raw:: html

   </div>



C++ references:

* ``:ref:`ov::preprocess::PostProcessSteps <doxid-classov_1_1preprocess_1_1_post_process_steps>```

* ``:ref:`ov::preprocess::OutputModelInfo <doxid-classov_1_1preprocess_1_1_output_model_info>```

* ``:ref:`ov::preprocess::OutputTensorInfo <doxid-classov_1_1preprocess_1_1_output_tensor_info>```

