.. index:: pair: page; Frontend Extensions
.. _doxid-openvino_docs__extensibility__u_g__frontend__extensions:


Frontend Extensions
===================

:target:`doxid-openvino_docs__extensibility__u_g__frontend__extensions_1md_openvino_docs_extensibility_ug_frontend_extensions` The goal of this chapter is to explain how to use Frontend extension classes to facilitate mapping of custom operations from framework model representation to OpenVINO representation. Refer to :ref:`Introduction to OpenVINO Extension <doxid-openvino_docs__extensibility__u_g__intro>` to understand entire flow.

This API is applicable for new frontends only, which exist for ONNX and PaddlePaddle. If a different model format is used, follow legacy :ref:`Model Optimizer Extensions <doxid-openvino_docs__m_o__d_g_prepare_model_customize_model_optimizer__customize__model__optimizer>` guide.

.. note:: This documentation is written based on the `Template extension <https://github.com/openvinotoolkit/openvino/tree/master/docs/template_extension/new>`__, which demonstrates extension development details based on minimalistic ``Identity`` operation that is a placeholder for your real custom operation. You can review the complete code, which is fully compliable, to see how it works.

Single Operation Mapping with OpExtension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section covers the case when a single operation in framework representation is mapped to a single operation in OpenVINO representation. This is called *one-to-one mapping*. There is ``OpExtension`` class that works well if all the following conditions are satisfied:

#. Number of inputs to operation in the Framework representation is the same as in the OpenVINO representation.

#. Number of outputs is also the same in both representations.

#. Inputs can be indexed and are mapped in order correspondingly, e.g. input with index 0 in framework representation maps to input with index 0 in OpenVINO representation and so on.

#. The same for outputs.

#. Each attribute in OpenVINO operation can be initialized from one of the attributes of original operation or by some predefined constant value. Value of copied attributes cannot contain expressions, value is accepted as-is, so type of a value should be compatible.

.. note:: ``OpExtension`` class is currently available for ONNX frontend only. PaddlePaddle frontend has named inputs and outputs for operation (not indexed) therefore OpExtension mapping is not applicable for this case.

The next example maps ONNX operation with type `“Identity” <https://github.com/onnx/onnx/blob/main/docs/Operators.md#Identity>`__ to OpenVINO template extension ``Identity`` class.

.. ref-code-block:: cpp

	#include <openvino/frontend/extension.hpp>



.. ref-code-block:: cpp

	auto extension1 = :ref:`ov::frontend::OpExtension\<TemplateExtension::Identity> <doxid-classov_1_1frontend_1_1_op_extension_base>`("Identity");
	
	// or even simpler if original FW type and OV type of operations match, that is "Identity"
	auto extension2 = :ref:`ov::frontend::OpExtension\<TemplateExtension::Identity> <doxid-classov_1_1frontend_1_1_op_extension_base>`();

The mapping doesn’t involve any attributes, as operation Identity doesn’t have them.

Extension objects, like just constructed ``extension`` can be used to add to the OpenVINO runtime just before the loading a model that contains custom operations:

.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	// Add arbitrary number of extensions before calling read_model method
	core.:ref:`add_extension <doxid-classov_1_1_core_1a68d0dea1cbcd42a67bea32780e32acea>`(:ref:`ov::frontend::OpExtension\<TemplateExtension::Identity> <doxid-classov_1_1frontend_1_1_op_extension_base>`());
	core.:ref:`read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>`("/path/to/model.onnx");

Or extensions can be constructed in a separately compiled shared library. Separately compiled library can be used in Model Optimizer or ``benchmark_app``. Read about how to build and load such library in chapter “Create library with extensions” in :ref:`Introduction to OpenVINO Extension <doxid-openvino_docs__extensibility__u_g__intro>`.

If operation have multiple inputs and/or outputs they will be mapped in order. The type of elements in input/output tensors should match expected types in the surrounding operations. For example, if custom operation produces ``f32`` data type then operation that consumes this output should also support ``f32``. Otherwise, model conversion fails with an error, there are no automatic type conversion happens.

Converting to Standard OpenVINO Operation
-----------------------------------------

``OpExtension`` class can be used when mapping to one of the operations from standard OpenVINO operation set is what you need and there is no class like ``TemplateExtension::Identity`` implemented.

Here is an example for a custom framework operation “MyRelu”. Suppose it is mathematically equivalent to standard ``Relu`` that exists in OpenVINO operation set, but for some reason has type name “MyRelu”. In this case you can directly say that “MyRelu” -> ``Relu`` mapping should be used:

.. ref-code-block:: cpp

	core.:ref:`add_extension <doxid-classov_1_1_core_1a68d0dea1cbcd42a67bea32780e32acea>`(:ref:`ov::frontend::OpExtension\<> <doxid-classov_1_1frontend_1_1_op_extension_base>`("Relu", "MyRelu"));

In the resulting converted OpenVINO model, “MyRelu” operation will be replaced by the standard operation ``Relu`` from the latest available OpenVINO operation set. Notice that when standard operation is used, it can be specified using just a type string (“Relu”) instead of using a ``ov::opset8::Relu`` class name as a template parameter for ``OpExtension``. This method is available for operations from the standard operation set only. For a user custom OpenVINO operation the corresponding class should be always specified as a template parameter as it was demonstrated with ``TemplateExtension::Identity``.

Attributes Mapping
------------------

As described above, ``OpExtension`` is useful when attributes can be mapped one by one or initialized by a constant. If the set of attributes in framework representation and OpenVINO representation completely match by their names and types, nothing should be specified in OpExtension constructor parameters. The attributes are discovered and mapped automatically based on ``visit_attributes`` method that should be defined for any OpenVINO operation.

Imagine you have CustomOperation class implementation that has two attributes with names ``attr1`` and ``attr2`` :

.. ref-code-block:: cpp

	class CustomOperation : public :ref:`ov::op::Op <doxid-classov_1_1op_1_1_op>` {
	
	    std::string attr1;
	    int attr2;
	
	public:
	
	    :ref:`OPENVINO_OP <doxid-core_2include_2openvino_2op_2op_8hpp_1afe347dcc52f829ca1c7693241f35957b>`("CustomOperation");
	
	    bool :ref:`visit_attributes <doxid-classov_1_1_node_1a9743b56d352970486d17dae2416d958e>`(:ref:`ov::AttributeVisitor <doxid-classov_1_1_attribute_visitor>`& visitor) override {
	        visitor.:ref:`on_attribute <doxid-classov_1_1_attribute_visitor_1a8323bb5b84f0a074a6fbedf32e0efa6f>`("attr1", attr1);
	        visitor.:ref:`on_attribute <doxid-classov_1_1_attribute_visitor_1a8323bb5b84f0a074a6fbedf32e0efa6f>`("attr2", attr2);
	        return true;
	    }
	
	    // ... implement other required methods

And original model in framework representation also has operation with name “CustomOperatoin” with the same ``attr1`` and ``attr2`` attributes. Then with the following code:

.. ref-code-block:: cpp

	core.:ref:`add_extension <doxid-classov_1_1_core_1a68d0dea1cbcd42a67bea32780e32acea>`(:ref:`ov::frontend::OpExtension\<CustomOperation> <doxid-classov_1_1frontend_1_1_op_extension_base>`());

both ``attr1`` and ``attr2`` are copied from framework representation to OpenVINO representation automatically. If for some reason names of attributes are different but values still can be copied “as-is” you can pass attribute names mapping in ``OpExtension`` constructor:

.. ref-code-block:: cpp

	core.:ref:`add_extension <doxid-classov_1_1_core_1a68d0dea1cbcd42a67bea32780e32acea>`(:ref:`ov::frontend::OpExtension\<CustomOperation> <doxid-classov_1_1frontend_1_1_op_extension_base>`(
	    { {"attr1", "fw_attr1"}, {"attr2", "fw_attr2"} },
	    {}
	));

Where ``fw_attr1`` and ``fw_attr2`` are names for corresponding attributes in framework operation representation.

If copying of an attribute is not what you need, ``OpExtension`` also can set attribute to predefined constant value. For the same ``CustomOperation``, imagine you want to set ``attr2`` to value 5 instead of copying from ``fw_attr2``, to achieve that do the following:

.. ref-code-block:: cpp

	core.:ref:`add_extension <doxid-classov_1_1_core_1a68d0dea1cbcd42a67bea32780e32acea>`(:ref:`ov::frontend::OpExtension\<CustomOperation> <doxid-classov_1_1frontend_1_1_op_extension_base>`(
	    { {"attr1", "fw_attr1"} },
	    { {"attr2", 5} }
	));

So the conclusion is that each attribute of target OpenVINO operation should be initialized either by

#. Setting automatically due to name matching

#. Mapped by attribute name

#. Set to a constant value

This is achieved by specifying maps as arguments for ``OpExtension`` constructor.

Mapping to Multiple Operations with ConversionExtension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previous sections cover the case when a single operation is mapped to a single operation with optional adjustment in names and attribute values. That is likely enough for your own custom operation with existing C++ kernel implementation. In this case your framework representation and OpenVINO representation for the operation are under your control and inputs/outpus/attributes can be aligned to make ``OpExtension`` usable.

In case if one-to-one mapping is not possible, *decomposition to multiple operations* should be considered. It is achieved by using more verbose and less automated ``ConversionExtension`` class. It enables writing arbitrary code to replace a single framework operation by multiple connected OpenVINO operations constructing dependency graph of any complexity.

``ConversionExtension`` maps a single operation to a function which builds a graph using OpenVINO operation classes. Follow chapter :ref:`Build a Model in OpenVINO Runtime <doxid-openvino_docs__o_v__u_g__model__representation_1ov_ug_build_model>` to learn how to use OpenVINO operation classes to build a fragment of model for replacement.

The next example illustrates using ``ConversionExtension`` for conversion of “ThresholdedRelu” from ONNX according to the formula: ``ThresholdedRelu(x, alpha) -> Multiply(x, Convert(Greater(x, alpha), type=float))``.

.. note:: ``ThresholdedRelu`` is one of the standard ONNX operators which is supported by ONNX frontend natively out-of-the-box. Here we are re-implementing it to illustrate how you can add a similar support for your custom operation instead of ``ThresholdedRelu``.

.. ref-code-block:: cpp

	#include <openvino/opsets/opset8.hpp>



.. ref-code-block:: cpp

	core.:ref:`add_extension <doxid-classov_1_1_core_1a68d0dea1cbcd42a67bea32780e32acea>`(:ref:`ov::frontend::ConversionExtension <doxid-classov_1_1frontend_1_1_conversion_extension>`(
	    "ThresholdedReLU",
	    [](const :ref:`ov::frontend::NodeContext <doxid-classov_1_1frontend_1_1_node_context>`& node) {
	        auto :ref:`greater <doxid-namespacengraph_1_1runtime_1_1reference_1a57392ae82f5b22607d69470afd59139a>` = std::make_shared<ov::opset8::Greater>(
	            node.:ref:`get_input <doxid-classov_1_1frontend_1_1_node_context_1aefd6066f0f721dee2e1cb68a41f8adfa>`(0),
	            ov::opset8::Constant::create(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`, {}, {node.get_attribute<float>("alpha")}));
	        auto casted = std::make_shared<ov::opset8::Convert>(:ref:`greater <doxid-namespacengraph_1_1runtime_1_1reference_1a57392ae82f5b22607d69470afd59139a>`, :ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`);
	        return :ref:`ov::OutputVector <doxid-namespaceov_1a0a3841455b82c164b1b04b61a9c7c560>`{ std::make_shared<ov::opset8::Multiply>(node.:ref:`get_input <doxid-classov_1_1frontend_1_1_node_context_1aefd6066f0f721dee2e1cb68a41f8adfa>`(0), casted) };
	    }));

To access original framework operation attribute value and connect to inputs, ``node`` object of type ``NodeContext`` is used. It has two main methods:

* ``NodeContext::get_input`` to get input with a given index,

* ``NodeContext::get_attribute`` to get attribute value with a given name.

The conversion function should return a vector of node outputs that are mapped to corresponding outputs of the original framework operation in the same order.

