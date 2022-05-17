.. index:: pair: page; Custom OpenVINO™ Operations
.. _doxid-openvino_docs__extensibility__u_g_add_openvino_ops:


Custom OpenVINO™ Operations
=============================

:target:`doxid-openvino_docs__extensibility__u_g_add_openvino_ops_1md_openvino_docs_extensibility_ug_add_openvino_ops` OpenVINO™ Extension API allows you to register custom operations to support models with operations which OpenVINO™ does not support out-of-the-box.

Operation Class
~~~~~~~~~~~~~~~

To add your custom operation, create a new class that extends ``ov::Op``, which is in turn derived from ``:ref:`ov::Node <doxid-classov_1_1_node>```, the base class for all graph operations in OpenVINO™. To add ``ov::Op`` please include next file:

.. ref-code-block:: cpp

	#include <openvino/op/op.hpp>

Follow the steps below to add a custom operation:

#. Add the ``OPENVINO_OP`` macro which defines a ``NodeTypeInfo`` object that identifies the type of the operation to the graph users and helps with dynamic type resolution. The type info of an operation currently consists of a string operation identifier and a string for operation version.

#. Implement default constructor and constructors that optionally take the operation inputs and attributes as parameters.

#. Override the shape inference method ``validate_and_infer_types``. This method is called multiple times during graph manipulations to determine the shapes and element types of the operations outputs. To access the input shapes and input element types, use the ``get_input_partial_shape()`` and ``get_input_element_type()`` methods of ``:ref:`ov::Node <doxid-classov_1_1_node>```. Set the inferred shape and element type of the output using ``set_output_type``.

#. Override the ``clone_with_new_inputs`` method, which enables graph manipulation routines to create copies of this operation and connect it to different nodes during optimization.

#. Override the ``visit_attributes`` method, which enables serialization and deserialization of operation attributes. An ``AttributeVisitor`` is passed to the method, and the implementation is expected to walk over all the attributes in the op using the type-aware ``on_attribute`` helper. Helpers are already implemented for standard C++ types like ``int64_t``, ``float``, ``bool``, ``vector``, and for existing OpenVINO defined types.

#. Override ``evaluate``, which is an optional method that enables fallback of some devices to this implementation and the application of constant folding if there is a custom operation on the constant branch. If your operation contains ``evaluate`` method you also need to override the ``has_evaluate`` method, this method allows to get information about availability of ``evaluate`` method for the operation.

Based on that, declaration of an operation class can look as follows:

Operation Constructors
----------------------

OpenVINO™ operation contains two constructors:

* Default constructor, which enables you to create an operation without attributes

* Constructor that creates and validates an operation with specified inputs and attributes

.. ref-code-block:: cpp

	Identity::Identity(const :ref:`ov::Output\<ov::Node> <doxid-classov_1_1_output>`& arg) : Op({arg}) {
	    constructor_validate_and_infer_types();
	}



.. rubric::

``:ref:`ov::Node::validate_and_infer_types <doxid-classov_1_1_node_1ac5224b5be848ec670d2078d9816d12e7>``` method validates operation attributes and calculates output shapes using attributes of the operation.

.. ref-code-block:: cpp

	void Identity::validate_and_infer_types() {
	    // Operation doesn't change shapes end element type
	    set_output_type(0, get_input_element_type(0), get_input_partial_shape(0));
	}



.. rubric::

``:ref:`ov::Node::clone_with_new_inputs <doxid-classov_1_1_node_1a177d1a61e81d506d190ee18818ff851f>``` method creates a copy of the operation with new inputs.

.. ref-code-block:: cpp

	std::shared_ptr<ov::Node> Identity::clone_with_new_inputs(const :ref:`ov::OutputVector <doxid-namespaceov_1a0a3841455b82c164b1b04b61a9c7c560>`& new_args) const {
	    :ref:`OPENVINO_ASSERT <doxid-openvino_2core_2except_8hpp_1a7ff78e5accf3159b30b4b32bbb72d272>`(new_args.size() == 1, "Incorrect number of new arguments");
	
	    return std::make_shared<Identity>(new_args.at(0));
	}



.. rubric::

``:ref:`ov::Node::visit_attributes <doxid-classov_1_1_node_1a9743b56d352970486d17dae2416d958e>``` method enables you to visit all operation attributes.

.. ref-code-block:: cpp

	bool Identity::visit_attributes(:ref:`ov::AttributeVisitor <doxid-classov_1_1_attribute_visitor>`& visitor) {
	    return true;
	}



evaluate() and has_evaluate()
-----------------------------

``:ref:`ov::Node::evaluate <doxid-classov_1_1_node_1acfb82acc8349d7138aeaa05217c7014e>``` method enables you to apply constant folding to an operation.

.. ref-code-block:: cpp

	bool Identity::evaluate(:ref:`ov::TensorVector <doxid-namespaceov_1aa2127061451ba4f5a6e6904b88e72c6e>`& outputs, const :ref:`ov::TensorVector <doxid-namespaceov_1aa2127061451ba4f5a6e6904b88e72c6e>`& inputs) const {
	    auto in = inputs[0];
	    auto :ref:`out <doxid-namespacengraph_1_1runtime_1_1reference_1ac9d07fc6d49867bb411a4f4132777aae>` = outputs[0];
	    :ref:`out <doxid-namespacengraph_1_1runtime_1_1reference_1ac9d07fc6d49867bb411a4f4132777aae>`.set_shape(in.get_shape());
	    memcpy(:ref:`out <doxid-namespacengraph_1_1runtime_1_1reference_1ac9d07fc6d49867bb411a4f4132777aae>`.data(), in.data(), in.get_byte_size());
	    return true;
	}
	
	bool Identity::has_evaluate() const {
	    return true;
	}

