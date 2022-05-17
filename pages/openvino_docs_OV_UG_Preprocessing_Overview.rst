.. index:: pair: page; Optimize Preprocessing
.. _doxid-openvino_docs__o_v__u_g__preprocessing__overview:


Optimize Preprocessing
======================

:target:`doxid-openvino_docs__o_v__u_g__preprocessing__overview_1md_openvino_docs_ov_runtime_ug_preprocessing_overview`





.. toctree::
   :maxdepth: 1
   :hidden:

   openvino_docs_OV_UG_Preprocessing_Details
   openvino_docs_OV_UG_Layout_Overview
   openvino_docs_OV_UG_Preprocess_Usecase_save

Introduction
~~~~~~~~~~~~

When your input data don't perfectly fit to Neural Network model input tensor - this means that additional operations/steps are needed to transform your data to format expected by model. These operations are known as "preprocessing".

Example
-------

Consider the following standard example: deep learning model expects input with shape ``{1, 3, 224, 224}``, ``FP32`` precision, ``RGB`` color channels order, and requires data normalization (subtract mean and divide by scale factor). But you have just a ``640x480`` ``BGR`` image (data is ``{480, 640, 3}``). This means that we need some operations which will:

* Convert U8 buffer to FP32

* Transform to ``planar`` format: from ``{1, 480, 640, 3}`` to ``{1, 3, 480, 640}``

* Resize image from 640x480 to 224x224

* Make ``BGR->RGB`` conversion as model expects ``RGB``

* For each pixel, subtract mean values and divide by scale factor

.. image:: preprocess_not_fit.png

Even though all these steps can be relatively easy implemented manually in application's code before actual inference, it is possible to do it with Preprocessing API. Reasons to use this API are:

* Preprocessing API is easy to use

* Preprocessing steps will be integrated into execution graph and will be performed on selected device (CPU/GPU/VPU/etc.) rather than always being executed on CPU. This will improve selected device utilization which is always good.

Preprocessing API
~~~~~~~~~~~~~~~~~

Intuitively, Preprocessing API consists of the following parts:

#. **Tensor:** Declare user's data format, like shape, :ref:`layout <doxid-openvino_docs__o_v__u_g__layout__overview>`, precision, color format of actual user's data

#. **Steps:** Describe sequence of preprocessing steps which need to be applied to user's data

#. **Model:** Specify Model's data format. Usually, precision and shape are already known for model, only additional information, like :ref:`layout <doxid-openvino_docs__o_v__u_g__layout__overview>` can be specified

**Note:** All model's graph modification shall be performed after model is read from disk and **before** it is being loaded on actual device.

PrePostProcessor object
-----------------------

``:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>``` class allows specifying preprocessing and postprocessing steps for model read from disk.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	std::shared_ptr<ov::Model> :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>`(model_path);
	:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>` ppp(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	from openvino.preprocess import PrePostProcessor
	from openvino.runtime import Core
	
	core = Core()
	model = core.read_model(model=xml_path)
	ppp = PrePostProcessor(model)





.. raw:: html

   </div>







.. raw:: html

   </div>





Declare user's data format
--------------------------

To address particular input of model/preprocessor, use ``ov::preprocess::PrePostProcessor::input(input_name)`` method

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::preprocess::InputInfo <doxid-classov_1_1preprocess_1_1_input_info>`& input = ppp.input(input_name);
	input.:ref:`tensor <doxid-classov_1_1preprocess_1_1_input_info_1ac7dbfe9df70c8961d9c58af5745dc4f6>`()
	  .:ref:`set_element_type <doxid-classov_1_1preprocess_1_1_input_tensor_info_1a320c54e50d794da07852ccecf9468e2a>`(:ref:`ov::element::u8 <doxid-group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f>`)
	  .:ref:`set_shape <doxid-classov_1_1preprocess_1_1_input_tensor_info_1aea4706c76671f054a4f87cec441b7a2f>`({1, 480, 640, 3})
	  .:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`("NHWC")
	  .set_color_format(:ref:`ov::preprocess::ColorFormat::BGR <doxid-namespace_inference_engine_1a5ee5ca7708cc67a9a0becc2593d0558aa0fb221afef06def7c25b82d6fa9efc1b>`);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	from openvino.preprocess import ColorFormat
	from openvino.runtime import Layout, Type
	ppp.input(input_name).tensor() \
	        .set_element_type(Type.u8) \
	        .set_shape([1, 480, 640, 3]) \
	        .:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NHWC')) \
	        .set_color_format(ColorFormat.BGR)





.. raw:: html

   </div>







.. raw:: html

   </div>



Here we've specified all information about user's input:

* Precision is U8 (unsigned 8-bit integer)

* Data represents tensor with {1,480,640,3} shape

* :ref:`Layout <doxid-openvino_docs__o_v__u_g__layout__overview>` is "NHWC". It means that 'height=480, width=640, channels=3'

* Color format is ``BGR``

:target:`doxid-openvino_docs__o_v__u_g__preprocessing__overview_1declare_model_s_layout`

Declare model's layout
----------------------

Model's input already has information about precision and shape. Preprocessing API is not intended to modify this. The only thing that may be specified is input's data :ref:`layout <doxid-openvino_docs__o_v__u_g__layout__overview>`

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// `model's input` already `knows` it's shape and data type, no need to specify them here
	input.:ref:`model <doxid-classov_1_1preprocess_1_1_input_info_1af0210a5809c4721a07d006611b3dab98>`().:ref:`set_layout <doxid-classov_1_1preprocess_1_1_input_model_info_1aeac53aa90be5b8a6b86def31fab396b4>`("NCHW");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# `model's input` already `knows` it's shape and data type, no need to specify them here
	ppp.input(input_name).:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW'))





.. raw:: html

   </div>







.. raw:: html

   </div>

Now, if model's input has ``{1,3,224,224}`` shape, preprocessing will be able to identify that model's ``height=224``, ``width=224``, ``channels=3``. Height/width information is necessary for 'resize', and ``channels`` is needed for mean/scale normalization

Preprocessing steps
-------------------

Now we can define sequence of preprocessing steps:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	input.:ref:`preprocess <doxid-classov_1_1preprocess_1_1_input_info_1a8d8f9165adf4f4c6249a7c52af8a5eff>`()
	  .:ref:`convert_element_type <doxid-classov_1_1preprocess_1_1_pre_process_steps_1ab9e7979668e7403a72b07786f76ec0e0>`(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`)
	  .:ref:`convert_color <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a1cc7cc3fc7afb5992c1920c483ce3332>`(:ref:`ov::preprocess::ColorFormat::RGB <doxid-namespace_inference_engine_1a5ee5ca7708cc67a9a0becc2593d0558aae2262afdcd9754598dbc87e4a4725246>`)
	  .:ref:`resize <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a910dfdc8dc19b1890b2e8f111162a8d6>`(ov::preprocess::ResizeAlgorithm::RESIZE_LINEAR)
	  .:ref:`mean <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a73234aefee9b6f7c585ac7718c1e396e>`({100.5, 101, 101.5})
	  .scale({50., 51., 52.});
	  // Not needed, such conversion will be added implicitly
	  // .convert_layout("NCHW");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	from openvino.preprocess import ResizeAlgorithm
	ppp.input(input_name).preprocess() \
	    .convert_element_type(Type.f32) \
	    .convert_color(ColorFormat.RGB) \
	    .resize(ResizeAlgorithm.RESIZE_LINEAR) \
	    .:ref:`mean <doxid-namespacengraph_1_1builder_1_1opset1_1a3377b4f15f56daf79c96a94ccefdb489>`([100.5, 101, 101.5]) \
	    .scale([50., 51., 52.])
	# .convert_layout(Layout('NCHW')); # Not needed, such conversion will be added implicitly





.. raw:: html

   </div>







.. raw:: html

   </div>



Here:

* Convert U8 to FP32 precision

* Convert current color format (BGR) to RGB

* Resize to model's height/width. **Note** that if model accepts dynamic size, e.g. {?, 3, ?, ?}, ``resize`` will not know how to resize the picture, so in this case you should specify target height/width on this step. See also ``:ref:`ov::preprocess::PreProcessSteps::resize() <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a910dfdc8dc19b1890b2e8f111162a8d6>```

* Subtract mean from each channel. On this step, color format is RGB already, so ``100.5`` will be subtracted from each Red component, and ``101.5`` will be subtracted from ``Blue`` one.

* Divide each pixel data to appropriate scale value. In this example each ``Red`` component will be divided by 50, ``Green`` by 51, ``Blue`` by 52 respectively

* **Note:** last ``convert_layout`` step is commented out as it is not necessary to specify last layout conversion. PrePostProcessor will do such conversion automatically

Integrate steps into model
--------------------------

We've finished with preprocessing steps declaration, now it is time to build it. For debugging purposes it is possible to print ``PrePostProcessor`` configuration on screen:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	std::cout << "Dump preprocessor: " << ppp << std::endl;
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = ppp.build();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	print(f'Dump preprocessor: {ppp}')
	model = ppp.build()





.. raw:: html

   </div>







.. raw:: html

   </div>

After this, ``model`` will accept U8 input with ``{1, 480, 640, 3}`` shape, with ``BGR`` channels order. All conversion steps will be integrated into execution graph. Now you can load model on device and pass your image to model as is, without any data manipulation on application's side

See Also
~~~~~~~~

* :ref:`Preprocessing Details <doxid-openvino_docs__o_v__u_g__preprocessing__details>`

* :ref:`Layout API overview <doxid-openvino_docs__o_v__u_g__layout__overview>`

* ``:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>``` C++ class documentation

