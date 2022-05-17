.. index:: pair: page; OpenVINO Model Pass
.. _doxid-openvino_docs__extensibility__u_g_model_pass:


OpenVINO Model Pass
===================

:target:`doxid-openvino_docs__extensibility__u_g_model_pass_1md_openvino_docs_extensibility_ug_model_pass` ``:ref:`ov::pass::ModelPass <doxid-classov_1_1pass_1_1_model_pass>``` is used for transformations that take entire ``:ref:`ov::Model <doxid-classov_1_1_model>``` as an input and process it.

Template for ModelPass transformation class

.. ref-code-block:: cpp

	// template_model_transformation.hpp
	class ov::pass::MyModelTransformation : public :ref:`ov::pass::ModelPass <doxid-classov_1_1pass_1_1_model_pass>` {
	public:
	    :ref:`OPENVINO_RTTI <doxid-classov_1_1pass_1_1_model_pass_1a718f43e809339887547f5c96b84ea00a>`("MyModelTransformation", "0");
	    bool :ref:`run_on_model <doxid-classov_1_1pass_1_1_model_pass_1afdce6ef577b36b5127115dd574b6615e>`(const std::shared_ptr<ov::Model>& :ref:`f <doxid-namespacengraph_1_1runtime_1_1reference_1a4582949bb0b6082a5159f90c43a71ca9>`) override;
	};



.. ref-code-block:: cpp

	// template_function_transformation.cpp
	
	bool ov::pass::MyModelTransformation::run_on_model(const std::shared_ptr<ov::Model>& :ref:`f <doxid-namespacengraph_1_1runtime_1_1reference_1a4582949bb0b6082a5159f90c43a71ca9>`) {
	    :ref:`RUN_ON_MODEL_SCOPE <doxid-conditional__compilation_2include_2openvino_2cc_2pass_2itt_8hpp_1ab308561b849d47b9c820506ec73c4a30>`(MyModelTransformation);
	    // Example transformation code
	    :ref:`NodeVector <doxid-namespaceov_1a750141ccb27d75af03e91a5295645c7f>` nodes;
	
	    // Traverse nGraph Function in topological order
	    for (auto& node : :ref:`f <doxid-namespacengraph_1_1runtime_1_1reference_1a4582949bb0b6082a5159f90c43a71ca9>`->get_ordered_ops()) {
	        // Check that number of input and output ports are equal to 1
	        if (node->inputs().size() == 1 && node->outputs().size() == 1) {
	            // Check that input and output shape a fully defined (not dynamic) and number of consumers equal to 1
	            Input<Node> input = node->input(0);
	            Output<Node> output = node->output(0);
	            if (input.get_partial_shape().is_static() && output.get_partial_shape().is_static() &&
	                output.get_target_inputs().size() == 1) {
	                nodes.push_back(node);
	            }
	        }
	    }
	
	    // Print types and names for collected nodes
	    for (auto& node : nodes) {
	        std::cout << "Type: " << node->get_type_info().name << std::endl
	                  << "Name: " << node->get_friendly_name() << std::endl;
	    }
	
	    // Return false because we didn't change nGraph Function
	    return false;
	}

Using ``:ref:`ov::pass::ModelPass <doxid-classov_1_1pass_1_1_model_pass>```, you need to override the ``run_on_model`` method where you will write the transformation code. Return value is ``true`` if the original model has changed during transformation (new operation was added, or operations replacement was made, or node attributes were changed); otherwise, it is ``false``. Also ``:ref:`ov::pass::ModelPass <doxid-classov_1_1pass_1_1_model_pass>``` based transformations can be executed via ``:ref:`ov::pass::Manager <doxid-classov_1_1pass_1_1_manager>```.

See Also
~~~~~~~~

* :ref:`OpenVINO™ Transformations <doxid-openvino_docs_transformations>`

