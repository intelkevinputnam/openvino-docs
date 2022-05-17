.. index:: pair: page; Preprocessing
.. _doxid-openvino_2_0_preprocessing:


Preprocessing
=============

:target:`doxid-openvino_2_0_preprocessing_1md_openvino_docs_ov_runtime_ug_migration_ov_2_0_preprocessing`

Introduction
------------

Inference Engine API contains preprocessing capabilities in the ``:ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>``` class. Such preprocessing information is not a part of the main inference graph executed by :ref:`OpenVINO devices <doxid-openvino_docs__o_v__u_g__working_with_devices>`. Therefore, it is stored and executed separately before the inference stage.

* Preprocessing operations are executed on the CPU for most OpenVINO inference plugins. Thus, instead of occupying accelerators, they keep the CPU busy with computational tasks.

* Preprocessing information stored in ``:ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>``` is lost when saving back to the IR file format.

OpenVINO Runtime API 2.0 introduces a :ref:`new way of adding preprocessing operations to the model <doxid-openvino_docs__o_v__u_g__preprocessing__overview>` - each preprocessing or postprocessing operation is integrated directly into the model and compiled together with the inference graph.

* Add preprocessing operations first using ``:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>```

* Then, compile the model on the target, using ``:ref:`ov::Core::compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>```

Having preprocessing operations as a part of an OpenVINO opset makes it possible to read and serialize a preprocessed model as the IR file format.

More importantly, OpenVINO Runtime API 2.0 does not assume any default layouts, as Inference Engine did. For example, both ``{ 1, 224, 224, 3 }`` and ``{ 1, 3, 224, 224 }`` shapes are supposed to be in the ``NCHW`` layout, while only the latter is. Therefore, some preprocessing capabilities in the API require layouts to be set explicitly. To learn how to do it, refer to the :ref:`Layout overview <doxid-openvino_docs__o_v__u_g__layout__overview>`. For example, to perform image scaling by partial dimensions ``H`` and ``W``, preprocessing needs to know what dimensions ``H`` and ``W`` are.

.. note:: Use Model Optimizer preprocessing capabilities to insert preprocessing operations in your model for optimization. Thus, the application does not need to read the model and set preprocessing repeatedly. You can use the :ref:`model caching feature <doxid-openvino_docs__o_v__u_g__model_caching_overview>` to improve the time-to-inference.

The steps below demonstrate how to migrate preprocessing scenarios from Inference Engine API to OpenVINO Runtime API 2.0. The snippets assume we need to preprocess a model input with the ``tensor_name`` in Inference Engine API, using ``operation_name`` to address the data.

Importing Preprocessing in Python
+++++++++++++++++++++++++++++++++

In order to utilize preprocessing, the following imports must be added.

Inference Engine API:

.. ref-code-block:: cpp

	import openvino.inference_engine as ie

OpenVINO Runtime API 2.0:

.. ref-code-block:: cpp

	from openvino.runtime import Core, Layout, Type
	from openvino.preprocess import ColorFormat, PrePostProcessor, ResizeAlgorithm

There are two different namespaces: ``runtime``, which contains OpenVINO Runtime API classes; and ``preprocess``, which provides Preprocessing API.

Mean and Scale Values
---------------------

Inference Engine API:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto preProcess = network.:ref:`getInputsInfo <doxid-class_inference_engine_1_1_c_n_n_network_1a76de2a6101fe8276f56b0dc0f99c7ff7>`()[operation_name]->getPreProcess();
	preProcess.init(3);
	preProcess[0]->meanValue = 116.78f;
	preProcess[1]->meanValue = 116.78f;
	preProcess[2]->meanValue = 116.78f;
	preProcess[0]->stdScale = 57.21f;
	preProcess[1]->stdScale = 57.45f;
	preProcess[2]->stdScale = 57.73f;
	preProcess.setVariant(:ref:`InferenceEngine::MEAN_VALUE <doxid-namespace_inference_engine_1a02a50369bd2f3354578072f5e4e98161a782a36934a315c43f504c04924ca5f26>`);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	preProcess = network.getInputsInfo()[operation_name].getPreProcess()
	preProcess.init(3)
	preProcess[0].meanValue = 116.78
	preProcess[1].meanValue = 116.78
	preProcess[2].meanValue = 116.78
	preProcess[0].stdScale = 57.21
	preProcess[1].stdScale = 57.45
	preProcess[2].stdScale = 57.73
	preProcess.setVariant(ie.MEAN_VALUE)





.. raw:: html

   </div>







.. raw:: html

   </div>



OpenVINO Runtime API 2.0:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>` ppp(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);
	:ref:`ov::preprocess::InputInfo <doxid-classov_1_1preprocess_1_1_input_info>`& input = ppp.input(tensor_name);
	// we only need to know where is C dimension
	input.:ref:`model <doxid-classov_1_1preprocess_1_1_input_info_1af0210a5809c4721a07d006611b3dab98>`().:ref:`set_layout <doxid-classov_1_1preprocess_1_1_input_model_info_1aeac53aa90be5b8a6b86def31fab396b4>`("...C");
	// specify scale and mean values, order of operations is important
	input.:ref:`preprocess <doxid-classov_1_1preprocess_1_1_input_info_1a8d8f9165adf4f4c6249a7c52af8a5eff>`().:ref:`mean <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a73234aefee9b6f7c585ac7718c1e396e>`(116.78:ref:`f <doxid-namespacengraph_1_1runtime_1_1reference_1a4582949bb0b6082a5159f90c43a71ca9>`).:ref:`scale <doxid-classov_1_1preprocess_1_1_pre_process_steps_1ae32615f1a234e4c49c1eedf4cabf99ac>`({ 57.21f, 57.45f, 57.73f });
	// insert preprocessing operations to the 'model'
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = ppp.build();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp = PrePostProcessor(model)
	input = ppp.input(tensor_name)
	# we only need to know where is C dimension
	input.model().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('...C'))
	# specify scale and mean values, order of operations is important
	input.preprocess().:ref:`mean <doxid-namespacengraph_1_1builder_1_1opset1_1a3377b4f15f56daf79c96a94ccefdb489>`([116.78]).scale([57.21, 57.45, 57.73])
	# insert preprocessing operations to the 'model'
	model = ppp.build()





.. raw:: html

   </div>







.. raw:: html

   </div>





Precision and Layout Conversions
--------------------------------

Inference Engine API:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto inputInfo = network.:ref:`getInputsInfo <doxid-class_inference_engine_1_1_c_n_n_network_1a76de2a6101fe8276f56b0dc0f99c7ff7>`()[operation_name];
	inputInfo->setPrecision(:ref:`InferenceEngine::Precision::U8 <doxid-class_inference_engine_1_1_precision_1ade75bd7073b4aa966c0dda4025bcd0f5a046eaf31a4345f526ed54271c9fcd39c>`);
	inputInfo->setLayout(:ref:`InferenceEngine::Layout::NHWC <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8aa5bfc87d4f0e3d8d55738659e9f54a0f>`);
	// model input layout is always NCHW in Inference Engine
	// for shapes with 4 dimensions





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	inputInfo = network.getInputsInfo()[operation_name]
	inputInfo.setPrecision(ie.Precision.U8)
	inputInfo.setLayout(ie.Layout.NHWC)
	# model input layout is always NCHW in Inference Engine
	# for shapes with 4 dimensions





.. raw:: html

   </div>







.. raw:: html

   </div>



OpenVINO Runtime API 2.0:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>` ppp(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);
	:ref:`ov::preprocess::InputInfo <doxid-classov_1_1preprocess_1_1_input_info>`& input = ppp.input(tensor_name);
	input.:ref:`tensor <doxid-classov_1_1preprocess_1_1_input_info_1ac7dbfe9df70c8961d9c58af5745dc4f6>`().:ref:`set_layout <doxid-classov_1_1preprocess_1_1_input_tensor_info_1af10932e00c45bb0ef09b2f856fab5268>`("NHWC").:ref:`set_element_type <doxid-classov_1_1preprocess_1_1_input_tensor_info_1a320c54e50d794da07852ccecf9468e2a>`(:ref:`ov::element::u8 <doxid-group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f>`);
	input.:ref:`model <doxid-classov_1_1preprocess_1_1_input_info_1af0210a5809c4721a07d006611b3dab98>`().:ref:`set_layout <doxid-classov_1_1preprocess_1_1_input_model_info_1aeac53aa90be5b8a6b86def31fab396b4>`("NCHW");
	// layout and precision conversion is inserted automatically,
	// because tensor format != model input format
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = ppp.build();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp = PrePostProcessor(model)
	input = ppp.input(tensor_name)
	input.tensor().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW')).set_element_type(Type.u8)
	input.model().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW'))
	# layout and precision conversion is inserted automatically,
	# because tensor format != model input format
	model = ppp.build()





.. raw:: html

   </div>







.. raw:: html

   </div>





Image Scaling
-------------

Inference Engine API:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto preProcess = network.:ref:`getInputsInfo <doxid-class_inference_engine_1_1_c_n_n_network_1a76de2a6101fe8276f56b0dc0f99c7ff7>`()[operation_name]->getPreProcess();
	// Inference Engine supposes input for resize is always in NCHW layout
	// while for OpenVINO Runtime API 2.0 `H` and `W` dimensions must be specified
	// Also, current code snippet supposed resize from dynamic shapes
	preProcess.setResizeAlgorithm(:ref:`InferenceEngine::ResizeAlgorithm::RESIZE_BILINEAR <doxid-namespace_inference_engine_1a805a09efb0e7b327ffa078f8d02222e9a069d0555eb598a08d5540adb10b759c5>`);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	preProcess = network.getInputsInfo()[operation_name].getPreProcess()
	# Inference Engine supposes input for resize is always in NCHW layout
	# while for OpenVINO Runtime API 2.0 `H` and `W` dimensions must be specified
	# Also, current code snippet supposed resize from dynamic shapes
	preProcess.setResizeAlgorithm(ie.ResizeAlgorithm.RESIZE_BILINEAR)





.. raw:: html

   </div>







.. raw:: html

   </div>



OpenVINO Runtime API 2.0:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>` ppp(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);
	:ref:`ov::preprocess::InputInfo <doxid-classov_1_1preprocess_1_1_input_info>`& input = ppp.input(tensor_name);
	// scale from the specified tensor size
	input.:ref:`tensor <doxid-classov_1_1preprocess_1_1_input_info_1ac7dbfe9df70c8961d9c58af5745dc4f6>`().:ref:`set_spatial_static_shape <doxid-classov_1_1preprocess_1_1_input_tensor_info_1a03db58db580f2974469a01da5b03f511>`(448, 448);
	// need to specify H and W dimensions in model, others are not important
	input.:ref:`model <doxid-classov_1_1preprocess_1_1_input_info_1af0210a5809c4721a07d006611b3dab98>`().:ref:`set_layout <doxid-classov_1_1preprocess_1_1_input_model_info_1aeac53aa90be5b8a6b86def31fab396b4>`("??HW");
	// scale to model shape
	input.:ref:`preprocess <doxid-classov_1_1preprocess_1_1_input_info_1a8d8f9165adf4f4c6249a7c52af8a5eff>`().:ref:`resize <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a910dfdc8dc19b1890b2e8f111162a8d6>`(ov::preprocess::ResizeAlgorithm::RESIZE_LINEAR);
	// and insert operations to the model
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = ppp.build();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp = PrePostProcessor(model)
	input = ppp.input(tensor_name)
	# need to specify H and W dimensions in model, others are not important
	input.model().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('??HW'))
	# scale to model shape
	input.preprocess().resize(ResizeAlgorithm.RESIZE_LINEAR, 448, 448)
	# and insert operations to the model
	model = ppp.build()





.. raw:: html

   </div>







.. raw:: html

   </div>





Color Space Conversions
-----------------------

Inference Engine API:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	auto preProcess = network.:ref:`getInputsInfo <doxid-class_inference_engine_1_1_c_n_n_network_1a76de2a6101fe8276f56b0dc0f99c7ff7>`()[operation_name]->getPreProcess();
	// Inference Engine supposes NV12 as two inputs which need to be passed
	// as InferenceEngine::NV12Blob composed of two Y and UV planes
	preProcess.setColorFormat(:ref:`InferenceEngine::NV12 <doxid-namespace_inference_engine_1a5ee5ca7708cc67a9a0becc2593d0558aa502b46f938a363e107246de8b1c90dc7>`);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	
	preProcess = network.getInputsInfo()[operation_name].getPreProcess()
	# Inference Engine supposes NV12 as two inputs which need to be passed
	# as InferenceEngine::NV12Blob composed of two Y and UV planes
	preProcess.setColorFormat(ie.NV12)





.. raw:: html

   </div>







.. raw:: html

   </div>



OpenVINO Runtime API 2.0:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>` ppp(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);
	:ref:`ov::preprocess::InputInfo <doxid-classov_1_1preprocess_1_1_input_info>`& input = ppp.input(tensor_name);
	input.:ref:`tensor <doxid-classov_1_1preprocess_1_1_input_info_1ac7dbfe9df70c8961d9c58af5745dc4f6>`().:ref:`set_color_format <doxid-classov_1_1preprocess_1_1_input_tensor_info_1a32df813b541b01ac7df6ae93d7f1f163>`(ov::preprocess::ColorFormat::NV12_TWO_PLANES);
	// add NV12 to BGR conversion
	input.:ref:`preprocess <doxid-classov_1_1preprocess_1_1_input_info_1a8d8f9165adf4f4c6249a7c52af8a5eff>`().:ref:`convert_color <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a1cc7cc3fc7afb5992c1920c483ce3332>`(:ref:`ov::preprocess::ColorFormat::BGR <doxid-namespace_inference_engine_1a5ee5ca7708cc67a9a0becc2593d0558aa0fb221afef06def7c25b82d6fa9efc1b>`);
	// and insert operations to the model
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = ppp.build();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	ppp = PrePostProcessor(model)
	input = ppp.input(tensor_name)
	input.tensor().set_color_format(ColorFormat.NV12_TWO_PLANES)
	# add NV12 to BGR conversion
	input.preprocess().convert_color(ColorFormat.BGR)
	# and insert operations to the model
	model = ppp.build()





.. raw:: html

   </div>







.. raw:: html

   </div>

**See also:**

* :ref:`Preprocessing details <doxid-openvino_docs__o_v__u_g__preprocessing__details>`

* :ref:`NV12 classification sample <doxid-openvino_inference_engine_samples_hello_nv12_input_classification__r_e_a_d_m_e>`

