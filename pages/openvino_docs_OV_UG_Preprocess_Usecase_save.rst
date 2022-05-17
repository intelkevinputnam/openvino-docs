.. index:: pair: page; Use Case - Integrate and Save Preprocessing Steps Into IR
.. _doxid-openvino_docs__o_v__u_g__preprocess__usecase_save:


Use Case - Integrate and Save Preprocessing Steps Into IR
=========================================================

:target:`doxid-openvino_docs__o_v__u_g__preprocess__usecase_save_1md_openvino_docs_ov_runtime_ug_preprocessing_usecase_save`

Introduction
~~~~~~~~~~~~

In previous sections we've covered how to add :ref:`preprocessing steps <doxid-openvino_docs__o_v__u_g__preprocessing__details>` and got the overview of :ref:`Layout <doxid-openvino_docs__o_v__u_g__layout__overview>` API.

For many applications it is also important to minimize model's read/load time, so performing integration of preprocessing steps every time on application startup after ``ov::runtime::Core::read_model`` may look not convenient. In such cases, after adding of Pre- and Post-processing steps it can be useful to store new execution model to Intermediate Representation (IR, .xml format).

Most part of existing preprocessing steps can also be performed via command line options using Model Optimizer tool. Refer to :ref:`Model Optimizer - Optimize Preprocessing Computation <doxid-openvino_docs__m_o__d_g__additional__optimization__use__cases>` for details os such command line options.

Code example - saving model with preprocessing to IR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case if you have some preprocessing steps which can't be integrated into execution graph using Model Optimizer command line options (e.g. ``YUV->RGB`` color space conversion, Resize, etc.) it is possible to write simple code which:

* Reads original model (IR, ONNX, Paddle)

* Adds preprocessing/postprocessing steps

* Saves resulting model as IR (.xml/.bin)

Let's consider the example, there is an original ``ONNX`` model which takes one ``float32`` input with shape ``{1, 3, 224, 224}`` with ``RGB`` channels order, with mean/scale values applied. User's application can provide ``BGR`` image buffer with not fixed size. Additionally, we'll also imagine that our application provides input images as batches, each batch contains 2 images. Here is how model conversion code may look like in your model preparation script

* Includes / Imports

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	#include <openvino/runtime/core.hpp>
	#include <openvino/core/preprocess/pre_post_process.hpp>
	#include <openvino/pass/serialize.hpp>





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	from openvino.preprocess import PrePostProcessor, ColorFormat, ResizeAlgorithm
	from openvino.runtime import Core, Layout, Type, set_batch
	from openvino.runtime.passes import Manager





.. raw:: html

   </div>







.. raw:: html

   </div>





* Preprocessing & Saving to IR code

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// ========  Step 0: read original model =========
	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	std::shared_ptr<ov::Model> :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = core.:ref:`read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>`("/path/to/some_model.onnx");

	// ======== Step 1: Preprocessing ================
	:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>` prep(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`);
	// Declare section of desired application's input format
	prep.input().tensor()
	       .set_element_type(:ref:`ov::element::u8 <doxid-group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f>`)
	       .set_layout("NHWC")
	       .set_color_format(:ref:`ov::preprocess::ColorFormat::BGR <doxid-namespace_inference_engine_1a5ee5ca7708cc67a9a0becc2593d0558aa0fb221afef06def7c25b82d6fa9efc1b>`)
	       .set_spatial_dynamic_shape();
	// Specify actual model layout
	prep.input().model()
	       .set_layout("NCHW");
	// Explicit preprocessing steps. Layout conversion will be done automatically as last step
	prep.input().preprocess()
	       .convert_element_type()
	       .convert_color(:ref:`ov::preprocess::ColorFormat::RGB <doxid-namespace_inference_engine_1a5ee5ca7708cc67a9a0becc2593d0558aae2262afdcd9754598dbc87e4a4725246>`)
	       .resize(ov::preprocess::ResizeAlgorithm::RESIZE_LINEAR)
	       .mean({123.675, 116.28, 103.53}) // Subtract mean after color conversion
	       .scale({58.624, 57.12, 57.375});
	// Dump preprocessor
	std::cout << "Preprocessor: " << prep << std::endl;
	:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = prep.build();

	// ======== Step 2: Change batch size ================
	// In this example we also want to change batch size to increase throughput
	:ref:`ov::set_batch <doxid-namespaceov_1a3314e2ff91fcc9ffec05b1a77c37862b>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, 2);

	// ======== Step 3: Save the model ================
	std::string xml = "/path/to/some_model_saved.xml";
	std::string bin = "/path/to/some_model_saved.bin";
	:ref:`ov::serialize <doxid-namespaceov_1a9eb5ed541b9130617bfee541a9679464>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, xml, bin);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# ========  Step 0: read original model =========
	core = Core()
	model = core.read_model(model='/path/to/some_model.onnx')
	
	# ======== Step 1: Preprocessing ================
	ppp = PrePostProcessor(model)
	# Declare section of desired application's input format
	ppp.input().tensor() \
	    .set_element_type(Type.u8) \
	    .set_spatial_dynamic_shape() \
	    .:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NHWC')) \
	    .set_color_format(ColorFormat.BGR)
	
	# Specify actual model layout
	ppp.input().:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`().:ref:`set_layout <doxid-group__ov__layout__cpp__api_1ga18464fb8ed029acb5fdc2bb1737358d9>`(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW'))
	
	# Explicit preprocessing steps. Layout conversion will be done automatically as last step
	ppp.input().preprocess() \
	    .convert_element_type() \
	    .convert_color(ColorFormat.RGB) \
	    .resize(ResizeAlgorithm.RESIZE_LINEAR) \
	    .:ref:`mean <doxid-namespacengraph_1_1builder_1_1opset1_1a3377b4f15f56daf79c96a94ccefdb489>`([123.675, 116.28, 103.53]) \
	    .scale([58.624, 57.12, 57.375])
	
	# Dump preprocessor
	print(f'Dump preprocessor: {ppp}')
	model = ppp.build()
	
	# ======== Step 2: Change batch size ================
	# In this example we also want to change batch size to increase throughput
	:ref:`set_batch <doxid-namespaceov_1a3314e2ff91fcc9ffec05b1a77c37862b>`(model, 2)
	
	# ======== Step 3: Save the model ================
	:ref:`serialize <doxid-namespaceov_1a9eb5ed541b9130617bfee541a9679464>`(model, '/path/to/some_model_saved.xml', '/path/to/some_model_saved.bin')





.. raw:: html

   </div>







.. raw:: html

   </div>

Application code - load model to target device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After this, your application's code can load saved file and don't perform preprocessing anymore. In this example we'll also enable :ref:`model caching <doxid-openvino_docs__o_v__u_g__model_caching_overview>` to minimize load time when cached model is available

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	core.:ref:`set_property <doxid-classov_1_1_core_1aa953cb0a1601dbc9a34ef6ba82b8476e>`(:ref:`ov::cache_dir <doxid-group__ov__runtime__cpp__prop__api_1ga3276fc4ed7cc7d0bbdcf0ae12063728d>`("/path/to/cache/dir"));

	// In case that no preprocessing is needed anymore, we can load model on target device directly
	// With cached model available, it will also save some time on reading original model
	:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>` compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`("/path/to/some_model_saved.xml", "CPU");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core = Core()
	core.set_property({'CACHE_DIR': '/path/to/cache/dir'})
	
	# In case that no preprocessing is needed anymore, we can load model on target device directly
	# With cached model available, it will also save some time on reading original model
	compiled_model = core.compile_model('/path/to/some_model_saved.xml', 'CPU')





.. raw:: html

   </div>







.. raw:: html

   </div>

See Also
~~~~~~~~

* :ref:`Preprocessing Details <doxid-openvino_docs__o_v__u_g__preprocessing__details>`

* :ref:`Layout API overview <doxid-openvino_docs__o_v__u_g__layout__overview>`

* :ref:`Model Optimizer - Optimize Preprocessing Computation <doxid-openvino_docs__m_o__d_g__additional__optimization__use__cases>`

* :ref:`Model Caching Overview <doxid-openvino_docs__o_v__u_g__model_caching_overview>`

* ``:ref:`ov::preprocess::PrePostProcessor <doxid-classov_1_1preprocess_1_1_pre_post_processor>``` C++ class documentation

* ``:ref:`ov::pass::Serialize <doxid-classov_1_1pass_1_1_serialize>``` - pass to serialize model to XML/BIN

* ``:ref:`ov::set_batch <doxid-namespaceov_1a3314e2ff91fcc9ffec05b1a77c37862b>``` - update batch dimension for a given model

