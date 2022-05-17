.. index:: pair: page; Model Representation in OpenVINO™ Runtime
.. _doxid-openvino_docs__o_v__u_g__model__representation:


Model Representation in OpenVINO™ Runtime
===========================================

:target:`doxid-openvino_docs__o_v__u_g__model__representation_1md_openvino_docs_ov_runtime_ug_model_representation` In OpenVINO™ Runtime a model is represented by the ``:ref:`ov::Model <doxid-classov_1_1_model>``` class.

The ``:ref:`ov::Model <doxid-classov_1_1_model>``` object stores shared pointers to ``:ref:`ov::op::v0::Parameter <doxid-classov_1_1op_1_1v0_1_1_parameter>```, ``:ref:`ov::op::v0::Result <doxid-classov_1_1op_1_1v0_1_1_result>``` and ``:ref:`ov::op::Sink <doxid-classov_1_1op_1_1_sink>``` operations that are inputs, outputs and sinks of the graph. Sinks of the graph have no consumers and are not included in the results vector. All other operations hold each other via shared pointers: child operation holds its parent (hard link). If an operation has no consumers and it's not the ``Result`` or ``Sink`` operation (shared pointer counter is zero), then it will be destructed and won't be accessible anymore.

Each operation in ``:ref:`ov::Model <doxid-classov_1_1_model>``` has the ``std::shared_ptr<:ref:`ov::Node <doxid-classov_1_1_node>`>`` type.

For details on how to build a model in OpenVINO™ Runtime, see the :ref:`Build a Model in OpenVINO™ Runtime <doxid-openvino_docs__o_v__u_g__model__representation_1ov_ug_build_model>` section.

OpenVINO™ Runtime allows to use different approaches to work with model inputs/outputs:

* ``:ref:`ov::Model::inputs() <doxid-classov_1_1_model_1a7121b50a2990b63eb6a73945f0cae089>``` / ``:ref:`ov::Model::outputs() <doxid-classov_1_1_model_1a89c629856666f1064cf0418c432004f0>``` methods allow to get vector of all input/output ports.

* For a model which has only one input or output you can use methods ``:ref:`ov::Model::input() <doxid-classov_1_1_model_1a9bf0166a1f9005222cb9a2f68a3b9a4c>``` or ``:ref:`ov::Model::output() <doxid-classov_1_1_model_1a77b209dd9632a199c20fd48b0e5cab62>``` without arguments to get input or output port respectively.

* Methods ``:ref:`ov::Model::input() <doxid-classov_1_1_model_1a9bf0166a1f9005222cb9a2f68a3b9a4c>``` and ``:ref:`ov::Model::output() <doxid-classov_1_1_model_1a77b209dd9632a199c20fd48b0e5cab62>``` can be used with index of input or output from the framework model to get specific port by index.

* You can use tensor name of input or output from the original framework model together with methods ``:ref:`ov::Model::input() <doxid-classov_1_1_model_1a9bf0166a1f9005222cb9a2f68a3b9a4c>``` or ``:ref:`ov::Model::output() <doxid-classov_1_1_model_1a77b209dd9632a199c20fd48b0e5cab62>``` to get specific port. It means that you don't need to have any additional mapping of names from framework to OpenVINO, as it was before, OpenVINO™ Runtime allows using of native framework tensor names.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	/\* Take information about all topology inputs \*/
	auto inputs = :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->inputs();
	/\* Take information about all topology outputs \*/
	auto outputs = :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`->outputs();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	inputs = model.inputs
	outputs = model.outputs





.. raw:: html

   </div>







.. raw:: html

   </div>



OpenVINO™ Runtime model representation uses special classes to work with model data types and shapes. For data types the ``:ref:`ov::element::Type <doxid-classov_1_1element_1_1_type>``` is used.

Shapes Representation
~~~~~~~~~~~~~~~~~~~~~

OpenVINO™ Runtime provides two types for shape representation:

* ``:ref:`ov::Shape <doxid-classov_1_1_shape>``` - Represents static (fully defined) shapes.

* ``:ref:`ov::PartialShape <doxid-classov_1_1_partial_shape>``` - Represents dynamic shapes. That means that the rank or some of dimensions are dynamic (dimension defines an interval or undefined). ``:ref:`ov::PartialShape <doxid-classov_1_1_partial_shape>``` can be converted to ``:ref:`ov::Shape <doxid-classov_1_1_shape>``` using the ``get_shape()`` method if all dimensions are static; otherwise the conversion raises an exception.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Shape <doxid-classov_1_1_shape>` static_shape;
	:ref:`ov::PartialShape <doxid-classov_1_1_partial_shape>` partial_shape = node->output(0).get_partial_shape(); // get zero output partial shape
	if (!partial_shape.:ref:`is_dynamic <doxid-classov_1_1_partial_shape_1a3c2f6e07a5415648ce1654831d6be035>`() /\* or partial_shape.is_static() \*/) {
	    static_shape = partial_shape.:ref:`get_shape <doxid-classov_1_1_partial_shape_1a7973b448c76e208993190d2e1e5d7a4a>`();
	}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	partial_shape = node.output(0).get_partial_shape() # get zero output partial shape
	if not partial_shape.is_dynamic: # or partial_shape.is_static
	    static_shape = partial_shape.get_shape()





.. raw:: html

   </div>







.. raw:: html

   </div>



But in most cases before getting static shape using ``get_shape()`` method, you need to check that shape is static.

Operations
~~~~~~~~~~

The ``ov::Op`` class represents any abstract operation in the model representation. Use this class to create :ref:`custom operations <doxid-openvino_docs__extensibility__u_g_add_openvino_ops>`.

Operation Sets
~~~~~~~~~~~~~~

Operation set (opset) is a collection of operations that can be used to construct a model. The ``:ref:`ov::OpSet <doxid-classov_1_1_op_set>``` class provides a functionality to work with operation sets. For each operation set, OpenVINO™ Runtime provides a separate namespace, for example ``opset8``. Each OpenVINO™ Release introduces new operations and add these operations to a new operation set. New operation sets help to introduce a new version of operations that change behavior of previous operations. Using operation sets allows you to avoid changes in your application if new operations have been introduced. For a complete list of operation sets supported in OpenVINO™ toolkit, see :ref:`Available Operations Sets <doxid-openvino_docs_ops_opset>`. To add support of custom operations, see the :ref:`Add Custom OpenVINO Operations <doxid-openvino_docs__extensibility__u_g__intro>` document.



.. _doxid-openvino_docs__o_v__u_g__model__representation_1ov_ug_build_model:

Build a Model in OpenVINO™ Runtime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can create a model from source. This section illustrates how to construct a model composed of operations from an available operation set.

Operation set ``opsetX`` integrates a list of pre-compiled operations that work for this purpose. In other words, ``opsetX`` defines a set of operations for building a graph.

To build an ``:ref:`ov::Model <doxid-classov_1_1_model>``` instance from ``opset8`` operations, include the following files:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	#include <openvino/core/model.hpp>
	#include <openvino/opsets/opset8.hpp>





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	import openvino.runtime as ov





.. raw:: html

   </div>







.. raw:: html

   </div>



The following code demonstrates how to create a simple model:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	std::shared_ptr<ov::Model> create_simple_model() {
	    // This example shows how to create ov::Model
	    //
	    // Parameter--->Multiply--->Add--->Result
	    //    Constant---'          /
	    //              Constant---'
	
	    // Create opset8::Parameter operation with static shape
	    auto data = std::make_shared<ov::opset8::Parameter>(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`{3, 1, 2});
	
	    auto mul_constant = ov::opset8::Constant::create(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`{1}, {1.5});
	    auto mul = std::make_shared<ov::opset8::Multiply>(data, mul_constant);
	
	    auto add_constant = ov::opset8::Constant::create(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`{1}, {0.5});
	    auto :ref:`add <doxid-namespacengraph_1_1runtime_1_1reference_1a12956a756feab4106f4f12a6a372db41>` = std::make_shared<ov::opset8::Add>(mul, add_constant);
	
	    // Create opset8::Result operation
	    auto res = std::make_shared<ov::opset8::Result>(mul);
	
	    // Create nGraph function
	    return std::make_shared<ov::Model>(:ref:`ov::ResultVector <doxid-namespaceov_1adf9015702d0f2f7e69c705651f19b72a>`{res}, :ref:`ov::ParameterVector <doxid-namespaceov_1a2fd9bce881f1d37b496cf2e098274098>`{data});
	}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	def create_simple_model():
	    # This example shows how to create ov::Function
	    #
	    # Parameter--->Multiply--->Add--->Result
	    #    Constant---'          /
	    #              Constant---'
	    data = ov.opset8.parameter([3, 1, 2], ov.Type.f32)
	    mul_constant = ov.opset8.constant([1.5], ov.Type.f32)
	    mul = ov.opset8.multiply(data, mul_constant)
	    add_constant = ov.opset8.constant([0.5], ov.Type.f32)
	    add = ov.opset8.add(mul, add_constant)
	    res = ov.opset8.result(add)
	    return :ref:`ov.Model <doxid-classov_1_1_model>`([res], [data], "model")





.. raw:: html

   </div>







.. raw:: html

   </div>



The following code creates a model with several outputs:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	std::shared_ptr<ov::Model> create_advanced_model() {
	    // Advanced example with multi output operation
	    //
	    // Parameter->Split---0-->Result
	    //               | `--1-->Relu-->Result
	    //               `----2-->Result
	
	    auto data = std::make_shared<ov::opset8::Parameter>(:ref:`ov::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`{1, 3, 64, 64});
	
	    // Create Constant for axis value
	    auto axis_const = ov::opset8::Constant::create(:ref:`ov::element::i64 <doxid-group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6>`, :ref:`ov::Shape <doxid-classov_1_1_shape>`{} /\*scalar shape\*/, {1});
	
	    // Create opset8::Split operation that splits input to three slices across 1st dimension
	    auto :ref:`split <doxid-namespaceov_1_1util_1aa7286e4cc2f3fc985397a6839f1e02e6>` = std::make_shared<ov::opset8::Split>(data, axis_const, 3);
	
	    // Create opset8::Relu operation that takes 1st Split output as input
	    auto :ref:`relu <doxid-namespaceov_1_1op_1_1util_1_1detail_1ab226e58ed2f3e7bbdea890077afe523f>` = std::make_shared<ov::opset8::Relu>(:ref:`split <doxid-namespaceov_1_1util_1aa7286e4cc2f3fc985397a6839f1e02e6>`->output(1) /\*specify explicit output\*/);
	
	    // Results operations will be created automatically based on provided OutputVector
	    return std::make_shared<ov::Model>(:ref:`ov::OutputVector <doxid-namespaceov_1a0a3841455b82c164b1b04b61a9c7c560>`{:ref:`split <doxid-namespaceov_1_1util_1aa7286e4cc2f3fc985397a6839f1e02e6>`->output(0), :ref:`relu <doxid-namespaceov_1_1op_1_1util_1_1detail_1ab226e58ed2f3e7bbdea890077afe523f>`, :ref:`split <doxid-namespaceov_1_1util_1aa7286e4cc2f3fc985397a6839f1e02e6>`->output(2)},
	                                       :ref:`ov::ParameterVector <doxid-namespaceov_1a2fd9bce881f1d37b496cf2e098274098>`{data});
	}





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	def create_advanced_model():
	    # Advanced example with multi output operation
	    #
	    # Parameter->Split---0-->Result
	    #               | `--1-->Relu-->Result
	    #               `----2-->Result
	    data = ov.opset8.parameter(:ref:`ov.Shape <doxid-classov_1_1_shape>`([1, 3, 64, 64]), ov.Type.f32)
	    # Create Constant for axis value
	    axis_const = ov.opset8.constant(ov.Type.i64, :ref:`ov.Shape <doxid-classov_1_1_shape>`({}), [1])
	
	    # Create opset8::Split operation that splits input to three slices across 1st dimension
	    split = ov.opset8.split(data, axis_const, 3)
	
	    # Create opset8::Relu operation that takes 1st Split output as input
	    relu = ov.opset8.relu(split.output(1))
	
	    # Results operations will be created automatically based on provided OutputVector
	    return :ref:`ov.Model <doxid-classov_1_1_model>`([split.output(0), relu, split.output[2]], [data], "model")





.. raw:: html

   </div>







.. raw:: html

   </div>





Model debug capabilities
~~~~~~~~~~~~~~~~~~~~~~~~

OpenVINO™ provides several debug capabilities:

* To receive additional messages about applied model modifications, rebuild the OpenVINO™ Runtime library with the ``-DENABLE_OPENVINO_DEBUG=ON`` option.

* Model can be visualized to image from the xDot format:
  
  .. raw:: html
  
     <div class='sphinxtabset'>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="C++">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	void visualize_example(const std::shared_ptr<ov::Model>& m) {
  	    // Need include:
  	    // \* openvino/pass/manager.hpp
  	    // \* openvino/pass/visualize_tree.hpp
  	    :ref:`ov::pass::Manager <doxid-classov_1_1pass_1_1_manager>` manager;
  	
  	    // Serialize ov::Model to before.svg file before transformation
  	    manager.:ref:`register_pass <doxid-classov_1_1pass_1_1_manager_1affc722b2463a786b66398472141d45f2>`<:ref:`ov::pass::VisualizeTree <doxid-classov_1_1pass_1_1_visualize_tree>`>("image.svg");
  	
  	    manager.:ref:`run_passes <doxid-classov_1_1pass_1_1_manager_1a8b155191130f2c15e294cfd259d4ca0d>`(m);
  	}
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="Python">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	def visualize_example(m : ov.Model):
  	    # Need import:
  	    # \* import openvino.runtime.passes as passes
  	    pass_manager = passes.Manager()
  	    pass_manager.register_pass(pass_name="VisualTree", file_name='image.svg')
  	    pass_manager.run_passes(m)
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  .. code-block:: cpp
  
  	`ov::pass::VisualizeTree` can be parametrized via environment variables:
  	
  	    OV_VISUALIZE_TREE_OUTPUT_SHAPES=1       - visualize shapes
  	    OV_VISUALIZE_TREE_OUTPUT_TYPES=1        - visualize types
  	    OV_VISUALIZE_TREE_MIN_MAX_DENORMAL=1    - pretty denormal values
  	    OV_VISUALIZE_TREE_RUNTIME_INFO=1        - print runtime information
  	    OV_VISUALIZE_TREE_IO=1                  - print I/O ports
  	    OV_VISUALIZE_TREE_MEMBERS_NAME=1        - print member names

* Also model can be serialized to IR:
  
  .. raw:: html
  
     <div class='sphinxtabset'>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="C++">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	void serialize_example(const std::shared_ptr<ov::Model>& :ref:`f <doxid-namespacengraph_1_1runtime_1_1reference_1a4582949bb0b6082a5159f90c43a71ca9>`) {
  	    // Need include:
  	    // \* openvino/pass/manager.hpp
  	    // \* openvino/pass/serialize.hpp
  	    :ref:`ov::pass::Manager <doxid-classov_1_1pass_1_1_manager>` manager;
  	
  	    // Serialize ov::Model to IR
  	    manager.:ref:`register_pass <doxid-classov_1_1pass_1_1_manager_1affc722b2463a786b66398472141d45f2>`<:ref:`ov::pass::Serialize <doxid-classov_1_1pass_1_1_serialize>`>("/path/to/file/model.xml", "/path/to/file/model.bin");
  	
  	    manager.:ref:`run_passes <doxid-classov_1_1pass_1_1_manager_1a8b155191130f2c15e294cfd259d4ca0d>`(:ref:`f <doxid-namespacengraph_1_1runtime_1_1reference_1a4582949bb0b6082a5159f90c43a71ca9>`);
  	}
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  
  
  .. raw:: html
  
     <div class="sphinxtab" data-sphinxtab-value="Python">
  
  
  
  
  
  .. ref-code-block:: cpp
  
  	def serialize_example(m : ov.Model):
  	    # Need import:
  	    # \* import openvino.runtime.passes as passes
  	    pass_manager = passes.Manager()
  	    pass_manager.register_pass(pass_name="Serialize", xml_path='model.xml', bin_path='model.bin')
  	    pass_manager.run_passes(m)
  
  
  
  
  
  .. raw:: html
  
     </div>
  
  
  
  
  
  See Also
  ~~~~~~~~

:ref:`Available Operation Sets <doxid-openvino_docs_ops_opset>`

* :ref:`OpenVINO™ Runtime Extensibility Developer Guide <doxid-openvino_docs__extensibility__u_g__intro>`

* :ref:`Transformations Developer Guide <doxid-openvino_docs_transformations>`.

