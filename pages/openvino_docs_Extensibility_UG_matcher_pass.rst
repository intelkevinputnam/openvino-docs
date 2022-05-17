.. index:: pair: page; OpenVINO Matcher Pass
.. _doxid-openvino_docs__extensibility__u_g_matcher_pass:


OpenVINO Matcher Pass
=====================

:target:`doxid-openvino_docs__extensibility__u_g_matcher_pass_1md_openvino_docs_extensibility_ug_matcher_pass` ``:ref:`ov::pass::MatcherPass <doxid-classov_1_1pass_1_1_matcher_pass>``` is used for pattern-based transformations.

Template for MatcherPass transformation class

.. ref-code-block:: cpp

	// transformations/template_pattern_transformation.hpp
	/\*\*
	 \* @ingroup ie_transformation_common_api
	 \* @brief Add transformation description.
	 \*/
	class ov::pass::DecomposeDivideMatcher : public :ref:`ov::pass::MatcherPass <doxid-classov_1_1pass_1_1_matcher_pass>` {
	public:
	    :ref:`OPENVINO_RTTI <doxid-classov_1_1pass_1_1_matcher_pass_1a525c64de11717629f6599042761eb844>`("DecomposeDivideMatcher", "0");
	    DecomposeDivideMatcher();
	};



.. ref-code-block:: cpp

	// template_pattern_transformation.cpp
	ov::pass::DecomposeDivideMatcher::DecomposeDivideMatcher() {
	    :ref:`MATCHER_SCOPE <doxid-conditional__compilation_2include_2openvino_2cc_2pass_2itt_8hpp_1a3d1377542bcf3e305c33a1b683cc77df>`(DecomposeDivideMatcher);
	    // Pattern example
	    auto input0 = :ref:`pattern::any_input <doxid-namespaceov_1_1pass_1_1pattern_1aaaacfc27e6d09ca94625c3ee2c190aff>`();
	    auto input1 = :ref:`pattern::any_input <doxid-namespaceov_1_1pass_1_1pattern_1aaaacfc27e6d09ca94625c3ee2c190aff>`();
	    auto div = std::make_shared<ov::opset3::Divide>(input0, input1);
	
	    :ref:`ov::matcher_pass_callback <doxid-namespaceov_1a0a124d479a37653bc99b1b118d47fc79>` callback = [](pattern::Matcher& m) {
	        auto div = std::dynamic_pointer_cast<ov::opset3::Divide>(m.get_match_root());
	        // We can not apply this transformation in case with integer input data type
	        if (!div || div->input(0).get_element_type().is_integral()) {
	            return false;
	        }
	
	        // Decompose Divide into Multiply with Power operations
	        auto pow = std::make_shared<ov::opset3::Power>(
	            div->input_value(1),
	            opset3::Constant::create(div->get_input_element_type(1), Shape{1}, {-1}));
	
	        auto mul = std::make_shared<ov::opset3::Multiply>(div->input_value(0), pow);
	
	        // Save original name to last operation in replacement sub-graph
	        mul->set_friendly_name(div->get_friendly_name());
	
	        // Copy runtime info attributes to newly created operation
	        :ref:`ov::copy_runtime_info <doxid-namespaceov_1a3bb5969a95703b4b4fd77f6f58837207>`(div, {pow, mul});
	
	        // Replace Divide operation with Multiply
	        :ref:`ov::replace_node <doxid-namespaceov_1a75d84ee654edb73fe4fb18936a5dca6d>`(div, mul);
	
	        // Return true as the root node was changed
	        return true;
	    };
	
	    // Register pattern with Divide operation as a pattern root node
	    auto m = std::make_shared<ov::pass::pattern::Matcher>(div, "ConvertDivide");
	    // Register Matcher
	    register_matcher(m, callback);
	}

To use ``:ref:`ov::pass::MatcherPass <doxid-classov_1_1pass_1_1_matcher_pass>```, you need to complete these steps:

#. Create a pattern

#. Implement a callback

#. Register the pattern and Matcher

#. Execute MatcherPass

So let's go through each of these steps.

Create a pattern
~~~~~~~~~~~~~~~~

Pattern is a single root ``:ref:`ov::Model <doxid-classov_1_1_model>```. But the only difference is that you do not need to create a model object, you just need to create and connect opset or special pattern operations. Then you need to take the last created operation and put it as a root of the pattern. This root node will be used as a root node in pattern matching.

.. note:: Any nodes in a pattern that have no consumers and are not registered as root will not be used in pattern matching.

.. ref-code-block:: cpp

	// Pattern example
	auto input = std::make_shared<ov::opset8::Parameter>(:ref:`ov::element::i64 <doxid-group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`{1});
	auto shapeof = std::make_shared<ov::opset8::ShapeOf>(input);
	
	// Create Matcher with Parameter->ShapeOf pattern
	auto m = std::make_shared<ov::pass::pattern::Matcher>(shapeof, "MyPatternBasedTransformation");

The ``Parameter`` operation in the example above has type and shape specified. These attributes are needed only to create Parameter operation class and will not be used in pattern matching.

For more pattern examples, refer to the `pattern matching <#pattern_matching>`__ section.

Implement callback
~~~~~~~~~~~~~~~~~~

Callback is an action applied to every pattern entrance. In general, callback is the lambda function that takes Matcher object with detected subgraph.

.. ref-code-block:: cpp

	:ref:`ov::graph_rewrite_callback <doxid-namespaceov_1a5fe08faf69e9897c58d168a54359047e>` callback = [](:ref:`ov::pass::pattern::Matcher <doxid-classov_1_1pass_1_1pattern_1_1_matcher>`& m) {
	    // Get root node
	    std::shared_ptr<ov::Node> root_node = m.get_match_root();
	
	    // Get all nodes matched by pattern
	    :ref:`ov::NodeVector <doxid-namespaceov_1a750141ccb27d75af03e91a5295645c7f>` nodes = m.get_matched_nodes();
	
	    // Transformation code
	    return false;
	};

The example above shows the callback structure and how Matcher can be used for accessing nodes detected by pattern. Callback return value is ``true`` if root node was replaced and another pattern cannot be applied to the same root node; otherwise, it is ``false``.

.. note:: It is not recommended to manipulate with nodes that are under root node. This may affect GraphRewrite execution as it is expected that all nodes that come after root node in topological order are valid and can be used in pattern matching.

MatcherPass also provides functionality that allows reporting of the newly created nodes that can be used in additional pattern matching. If MatcherPass was registered in ``:ref:`ov::pass::Manager <doxid-classov_1_1pass_1_1_manager>``` or ``:ref:`ov::pass::GraphRewrite <doxid-classov_1_1pass_1_1_graph_rewrite>```, these registered nodes will be added for additional pattern matching. That means that matcher passes registered in ``:ref:`ov::pass::GraphRewrite <doxid-classov_1_1pass_1_1_graph_rewrite>``` will be applied to these nodes.

The example below shows how single MatcherPass can fuse sequence of operations using the ``register_new_node`` method.

.. ref-code-block:: cpp

	ov::pass::ReluReluFusionMatcher::ReluReluFusionMatcher() {
	    :ref:`MATCHER_SCOPE <doxid-conditional__compilation_2include_2openvino_2cc_2pass_2itt_8hpp_1a3d1377542bcf3e305c33a1b683cc77df>`(ReluReluFusionMatcher);
	    auto m_relu1 = ov::pass::pattern::wrap_type<ov::opset3::Relu>(:ref:`pattern::consumers_count <doxid-namespaceov_1_1pass_1_1pattern_1a3a149c6c14b37244cfa997cd0048b390>`(1));
	    auto m_relu2 = ov::pass::pattern::wrap_type<ov::opset3::Relu>({m_relu1});
	
	    :ref:`ov::matcher_pass_callback <doxid-namespaceov_1a0a124d479a37653bc99b1b118d47fc79>` callback = [=](pattern::Matcher& m) {
	        // Map that helps to connect labels with matched outputs
	        auto& node_to_output = m.get_pattern_value_map();
	
	        // Create new Relu operation and add register it for additional execution
	        auto new_relu =
	            register_new_node<ov::opset3::Relu>(node_to_output.at(m_relu1).get_node_shared_ptr()->input_value(0));
	
	        // Copy runtime info attributes to newly created operation
	        :ref:`ov::copy_runtime_info <doxid-namespaceov_1a3bb5969a95703b4b4fd77f6f58837207>`(m.get_matched_nodes(), new_relu);
	
	        // Save last Relu name to new Relu operation
	        new_relu->set_friendly_name(m.get_match_root()->get_friendly_name());
	
	        // Replace Relu->Relu with Relu
	        :ref:`ov::replace_node <doxid-namespaceov_1a75d84ee654edb73fe4fb18936a5dca6d>`(m.get_match_root(), new_relu);
	
	        // Return true as the root node was changed
	        return true;
	    };
	
	    // Register pattern with Relu operation as a pattern root node
	    auto m = std::make_shared<ov::pass::pattern::Matcher>(m_relu2, "ReluReluFusion");
	    // Register Matcher
	    register_matcher(m, callback);
	}



.. note:: If you register multiple nodes, please add them in topological order. We do not topologically sort these nodes as it is a time-consuming operation.

Register pattern and Matcher
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The last step is to register Matcher and callback inside the MatcherPass pass. To do this, call the ``register_matcher`` method.

.. note:: Only one matcher can be registered for a single MatcherPass class.

.. ref-code-block:: cpp

	// Register matcher and callback
	register_matcher(m, callback);

Execute MatcherPass
~~~~~~~~~~~~~~~~~~~

MatcherPass has multiple ways to be executed:

* Run on a single node - it can be useful if you want to run MatcherPass inside another transformation.
  
  .. ref-code-block:: cpp
  
  	if (ov::pass::DecomposeDivideMatcher().apply(node)) {
  	    // successful execution (root node was replaced)
  	}

* Run on ``:ref:`ov::Model <doxid-classov_1_1_model>``` using GraphRewrite - this approach gives ability to run MatcherPass on whole ``:ref:`ov::Model <doxid-classov_1_1_model>```. Moreover, multiple MatcherPass transformation can be registered in a single GraphRewite to be executed in a single graph traversal.
  
  .. ref-code-block:: cpp
  
  	// Two matcher passes will run simultaneously in a single graph traversal
  	:ref:`ov::pass::GraphRewrite <doxid-classov_1_1pass_1_1_graph_rewrite>` pass;
  	pass.:ref:`add_matcher <doxid-classov_1_1pass_1_1_graph_rewrite_1aa51d9ab71470eb93e0e8ce8f59c44eac>`<ov::pass::DecomposeDivideMatcher>();
  	pass.:ref:`add_matcher <doxid-classov_1_1pass_1_1_graph_rewrite_1aa51d9ab71470eb93e0e8ce8f59c44eac>`<ov::pass::ReluReluFusionMatcher>();
  	pass.:ref:`run_on_model <doxid-classov_1_1pass_1_1_graph_rewrite_1ad27ed8542330330ce9a524ff17564c21>`(:ref:`f <doxid-namespacengraph_1_1runtime_1_1reference_1a4582949bb0b6082a5159f90c43a71ca9>`);

* .. _pattern_matching:
  
  Run on ``:ref:`ov::Model <doxid-classov_1_1_model>``` using ``:ref:`ov::pass::Manager <doxid-classov_1_1pass_1_1_manager>``` - this approach helps you to register MatcherPass for execution on ``:ref:`ov::Model <doxid-classov_1_1_model>``` as another transformation types.
  
  .. ref-code-block:: cpp
  
  	// Two matchers will run independently (two independent graph traversals)
  	// pass::Manager automatically creates GraphRewrite container for each MatcherPass
  	:ref:`ov::pass::Manager <doxid-classov_1_1pass_1_1_manager>` manager;
  	manager.:ref:`register_pass <doxid-classov_1_1pass_1_1_manager_1affc722b2463a786b66398472141d45f2>`<ov::pass::DecomposeDivideMatcher>();
  	manager.:ref:`register_pass <doxid-classov_1_1pass_1_1_manager_1affc722b2463a786b66398472141d45f2>`<ov::pass::ReluReluFusionMatcher>();
  	manager.:ref:`run_passes <doxid-classov_1_1pass_1_1_manager_1a8b155191130f2c15e294cfd259d4ca0d>`(:ref:`f <doxid-namespacengraph_1_1runtime_1_1reference_1a4582949bb0b6082a5159f90c43a71ca9>`);
  
  
  
  Pattern Matching
  ~~~~~~~~~~~~~~~~

Sometimes patterns cannot be expressed via regular operations or it is too complicated. For example, if you want to detect **Convolution->Add** sub-graph without specifying particular input type for Convolution operation or you want to create a pattern where some of operations can have different types. And for these cases OpenVINO™ provides additional helpers to construct patterns for GraphRewrite transformations.

There are two main helpers:

#. ``:ref:`ov::pass::pattern::any_input <doxid-namespaceov_1_1pass_1_1pattern_1aaaacfc27e6d09ca94625c3ee2c190aff>``` - helps to express inputs if their types are undefined.

#. ``:ref:`ov::pass::pattern::wrap_type <doxid-namespaceov_1_1pass_1_1pattern_1a2fd26ffb1c9bf414b99a15439fc94656>`<T>`` - helps to express nodes of pattern without specifying node attributes.

Let's go through the example to have better understanding of how it works:

.. note:: Node attributes do not participate in pattern matching and are needed only for operations creation. Only operation types participate in pattern matching.

The example below shows basic usage of ``ov::passpattern::any_input``. Here we construct Multiply pattern with arbitrary first input and Constant as a second input. Also as Multiply is commutative operation, it does not matter in which order we set inputs (any_input/Constant or Constant/any_input) because both cases will be matched.

.. ref-code-block:: cpp

	// Detect Multiply with arbitrary first input and second as Constant
	// ov::pattern::op::Label - represent arbitrary input
	auto input = :ref:`ov::pass::pattern::any_input <doxid-namespaceov_1_1pass_1_1pattern_1aaaacfc27e6d09ca94625c3ee2c190aff>`();
	auto value = ov::opset8::Constant::create(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`{1}, {0.5});
	auto mul = std::make_shared<ov::opset8::Multiply>(input, value);
	auto m = std::make_shared<ov::pass::pattern::Matcher>(mul, "MultiplyMatcher");

This example shows how we can construct a pattern when operation has arbitrary number of inputs.

.. ref-code-block:: cpp

	// Detect Concat operation with arbitrary number of inputs
	auto :ref:`concat <doxid-namespacengraph_1_1runtime_1_1reference_1a697183f9ae579acade2cb21c5ebad1ca>` = ov::pass::pattern::wrap_type<ov::opset8::Concat>();
	auto m = std::make_shared<ov::pass::pattern::Matcher>(:ref:`concat <doxid-namespacengraph_1_1runtime_1_1reference_1a697183f9ae579acade2cb21c5ebad1ca>`, "ConcatMatcher");

This example shows how to use predicate to construct a pattern. Also it shows how to match pattern manually on given node.

.. ref-code-block:: cpp

	// Detect Multiply->Add sequence where mul has exactly one consumer
	auto mul = ov::pass::pattern::wrap_type<ov::opset8::Multiply>(:ref:`ov::pass::pattern::consumers_count <doxid-namespaceov_1_1pass_1_1pattern_1a3a149c6c14b37244cfa997cd0048b390>`(1)/\*сheck consumers count\*/);
	auto :ref:`add <doxid-namespacengraph_1_1runtime_1_1reference_1a12956a756feab4106f4f12a6a372db41>` = ov::pass::pattern::wrap_type<ov::opset8::Add>({mul, :ref:`ov::pass::pattern::any_input <doxid-namespaceov_1_1pass_1_1pattern_1aaaacfc27e6d09ca94625c3ee2c190aff>`()});
	auto m = std::make_shared<ov::pass::pattern::Matcher>(:ref:`add <doxid-namespacengraph_1_1runtime_1_1reference_1a12956a756feab4106f4f12a6a372db41>`, "MultiplyAddMatcher");
	// Matcher can be used to match pattern manually on given node
	if (m->match(node->output(0))) {
	    // Successfully matched
	}



.. note:: Be careful with manual matching because Matcher object holds matched nodes. To clear a match, use the m->clear_state() method.

See Also
~~~~~~~~

* :ref:`OpenVINO™ Transformations <doxid-openvino_docs_transformations>`

