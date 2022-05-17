.. index:: pair: page; Model Creation in Runtime
.. _doxid-openvino_2_0_model_creation:


Model Creation in Runtime
=========================

:target:`doxid-openvino_2_0_model_creation_1md_openvino_docs_ov_runtime_ug_migration_ov_2_0_graph_construction` OpenVINO™ Runtime API 2.0 includes the nGraph engine as a common part. The ``ngraph`` namespace has been changed to ``ov``, but all other parts of the ngraph API have been preserved. The code snippets below show how to change application code for migration to OpenVINO™ Runtime API 2.0.

nGraph API
----------

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// _____________    _____________
	// | Parameter |    | Parameter |
	// |   data1   |    |   data2   |
	// |___________|    |___________|
	//         |            |
	// data1_t |            | data2_t
	//          \          /
	//           \        /
	//            \      /
	//         ____\____/____
	//         |   Concat   |
	//         |   concat   |
	//         |____________|
	//               |
	//               | concat_t
	//               |
	//        _______|_______
	//        |    Result   |
	//        |    result   |
	//        |_____________|
	auto data1 = std::make_shared<ngraph::opset8::Parameter>(:ref:`ngraph::element::i64 <doxid-group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6>`, :ref:`ngraph::Shape <doxid-classov_1_1_shape>`{1, 3, 2, 2});
	data1->set_friendly_name("data1");        // operation name
	data1->output(0).set_names({"data1_t"});  // tensor names
	auto data2 = std::make_shared<ngraph::opset8::Parameter>(:ref:`ngraph::element::i64 <doxid-group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6>`, :ref:`ngraph::Shape <doxid-classov_1_1_shape>`{1, 2, 2, 2});
	data2->set_friendly_name("data2");        // operation name
	data2->output(0).set_names({"data2_t"});  // tensor names

	auto :ref:`concat <doxid-namespacengraph_1_1runtime_1_1reference_1a697183f9ae579acade2cb21c5ebad1ca>` = std::make_shared<ngraph::opset8::Concat>(:ref:`ngraph::OutputVector <doxid-classngraph_1a161d36c81df2d1949272f525a8d73605>`{data1, data2}, 1);
	:ref:`concat <doxid-namespacengraph_1_1runtime_1_1reference_1a697183f9ae579acade2cb21c5ebad1ca>`->set_friendly_name("concat");        // operation name
	:ref:`concat <doxid-namespacengraph_1_1runtime_1_1reference_1a697183f9ae579acade2cb21c5ebad1ca>`->output(0).set_names({"concat_t"});  // tensor name

	auto :ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>` = std::make_shared<ngraph::opset8::Result>(:ref:`concat <doxid-namespacengraph_1_1runtime_1_1reference_1a697183f9ae579acade2cb21c5ebad1ca>`);
	:ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>`->set_friendly_name("result");  // operation name

	auto :ref:`f <doxid-namespacengraph_1_1runtime_1_1reference_1a4582949bb0b6082a5159f90c43a71ca9>` = std::make_shared<ngraph::Function>(:ref:`ngraph::ResultVector <doxid-classngraph_1aedfbc99202fbf343071141f5e0e26eff>`{:ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>`},
	                                            :ref:`ngraph::ParameterVector <doxid-classngraph_1a8288ec615d4e98f673d38597891c6e49>`{data1, data2},
	                                            "function_name");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# _____________    _____________
	# | Parameter |    | Parameter |
	# |   data1   |    |   data2   |
	# |___________|    |___________|
	#         |            |
	#         |            |
	#          \          /
	#           \        /
	#            \      /
	#         ____\____/____
	#         |   Concat   |
	#         |   concat   |
	#         |____________|
	#               |
	#               |
	#               |
	#        _______|_______
	#        |    Result   |
	#        |    result   |
	#        |_____________|
	
	import ngraph as ng
	import numpy as np
	
	
	data1 = ng.opset8.parameter([1, 3, 2, 2], np.int64)
	data1.friendly_name = "data1" # operation name
	data2 = ng.opset8.parameter([1, 2, 2, 2], np.int64)
	data2.friendly_name = "data2" # operation name
	
	concat = ng.opset8.concat([data1, data2], 1)
	concat.friendly_name = "concat" # operation name
	
	result = ng.opset8.result(concat)
	result.friendly_name = "result" # operation name
	
	f = ng.Function(result, [data1, data2], "function_name")





.. raw:: html

   </div>







.. raw:: html

   </div>





OpenVINO™ Runtime API 2.0:
----------------------------

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// _____________    _____________
	// | Parameter |    | Parameter |
	// |   data1   |    |   data2   |
	// |___________|    |___________|
	//         |            |
	// data1_t |            | data2_t
	//          \          /
	//           \        /
	//            \      /
	//         ____\____/____
	//         |   Concat   |
	//         |   concat   |
	//         |____________|
	//               |
	//               | concat_t
	//               |
	//        _______|_______
	//        |    Result   |
	//        |    result   |
	//        |_____________|
	auto data1 = std::make_shared<ov::opset8::Parameter>(:ref:`ov::element::i64 <doxid-group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`{1, 3, 2, 2});
	data1->set_friendly_name("data1");        // operation name
	data1->output(0).set_names({"data1_t"});  // tensor names
	auto data2 = std::make_shared<ov::opset8::Parameter>(:ref:`ov::element::i64 <doxid-group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`{1, 2, 2, 2});
	data2->set_friendly_name("data2");        // operation name
	data2->output(0).set_names({"data2_t"});  // tensor names

	auto :ref:`concat <doxid-namespacengraph_1_1runtime_1_1reference_1a697183f9ae579acade2cb21c5ebad1ca>` = std::make_shared<ov::opset8::Concat>(:ref:`ov::OutputVector <doxid-namespaceov_1a0a3841455b82c164b1b04b61a9c7c560>`{data1, data2}, 1);
	:ref:`concat <doxid-namespacengraph_1_1runtime_1_1reference_1a697183f9ae579acade2cb21c5ebad1ca>`->set_friendly_name("concat");        // operation name
	:ref:`concat <doxid-namespacengraph_1_1runtime_1_1reference_1a697183f9ae579acade2cb21c5ebad1ca>`->output(0).set_names({"concat_t"});  // tensor name

	auto :ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>` = std::make_shared<ov::opset8::Result>(:ref:`concat <doxid-namespacengraph_1_1runtime_1_1reference_1a697183f9ae579acade2cb21c5ebad1ca>`);
	:ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>`->set_friendly_name("result");  // operation name

	auto :ref:`f <doxid-namespacengraph_1_1runtime_1_1reference_1a4582949bb0b6082a5159f90c43a71ca9>` = std::make_shared<ov::Model>(:ref:`ov::ResultVector <doxid-namespaceov_1adf9015702d0f2f7e69c705651f19b72a>`{:ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>`}, :ref:`ov::ParameterVector <doxid-namespaceov_1a2fd9bce881f1d37b496cf2e098274098>`{data1, data2}, "function_name");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# _____________    _____________
	# | Parameter |    | Parameter |
	# |   data1   |    |   data2   |
	# |___________|    |___________|
	#         |            |
	# data1_t |            | data2_t
	#          \          /
	#           \        /
	#            \      /
	#         ____\____/____
	#         |   Concat   |
	#         |   concat   |
	#         |____________|
	#               |
	#               | concat_t
	#               |
	#        _______|_______
	#        |    Result   |
	#        |    result   |
	#        |_____________|
	
	import openvino.runtime as ov
	
	
	data1 = ov.opset8.parameter([1, 3, 2, 2], ov.Type.i64)
	data1.friendly_name = "data1"      # operation name
	data1.output(0).name = "data1_t" # tensor name
	data2 = ov.opset8.parameter([1, 2, 2, 2], ov.Type.i64)
	data2.friendly_name = "data2"      # operation name
	data2.output(0).name = "data2_t"   # tensor name
	
	concat = ov.opset8.concat([data1, data2], 1)
	concat.friendly_name = "concat"    # operation name
	concat.output(0).name = "concat_t" # tensor name
	
	result = ov.opset8.result(concat)
	result.friendly_name = "result"    # operation name
	
	model = :ref:`ov.Model <doxid-classov_1_1_model>`(result, [data1, data2], "model_name")





.. raw:: html

   </div>







.. raw:: html

   </div>



**See also:**

* :ref:`Hello Model Creation C++ Sample <doxid-openvino_inference_engine_samples_model_creation_sample__r_e_a_d_m_e>`

* :ref:`Hello Model Creation Python Sample <doxid-openvino_inference_engine_ie_bridges_python_sample_model_creation_sample__r_e_a_d_m_e>`

