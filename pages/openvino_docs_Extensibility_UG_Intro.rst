.. index:: pair: page; OpenVINO Extensibility Mechanism
.. _doxid-openvino_docs__extensibility__u_g__intro:


OpenVINO Extensibility Mechanism
================================

:target:`doxid-openvino_docs__extensibility__u_g__intro_1md_openvino_docs_extensibility_ug_intro`





.. toctree::
   :maxdepth: 1
   :hidden:

   openvino_docs_Extensibility_UG_add_openvino_ops
   openvino_docs_Extensibility_UG_Frontend_Extensions
   openvino_docs_Extensibility_UG_GPU
   openvino_docs_IE_DG_Extensibility_DG_VPU_Kernel
   openvino_docs_MO_DG_prepare_model_customize_model_optimizer_Customize_Model_Optimizer

The Intel® Distribution of OpenVINO™ toolkit supports neural network models trained with various frameworks, including TensorFlow, PyTorch, ONNX, PaddlePaddle, MXNet, Caffe, and Kaldi. The list of supported operations is different for each of the supported frameworks. To see the operations supported by your framework, refer to :ref:`Supported Framework Operations <doxid-openvino_docs__m_o__d_g_prepare_model__supported__frameworks__layers>`.

Custom operations, that is those not included in the list, are not recognized by OpenVINO™ out-of-the-box. The need for a custom operation may appear in two main cases:

#. A regular framework operation that is new or rarely used, which is why it hasn’t been implemented in OpenVINO yet.

#. A new user operation that was created for some specific model topology by a model author using framework extension capabilities.

Importing models with such operations requires additional steps. This guide illustrates the workflow for running inference on models featuring custom operations, allowing you to plug in your own implementation for them. OpenVINO™ Extensibility API lets you add support for those custom operations and use one implementation for Model Optimizer and OpenVINO™ Runtime.

Defining a new custom operation basically consist of two parts:

#. Definition of operation semantics in OpenVINO, the code that describes how this operation should be inferred consuming input tensor(s) and producing output tensor(s). How to implement execution kernels for :ref:`GPU <doxid-openvino_docs__extensibility__u_g__g_p_u>` and :ref:`VPU <doxid-openvino_docs__i_e__d_g__extensibility__d_g__v_p_u__kernel>` is described in separate guides.

#. Mapping rule that facilitates conversion of framework operation representation to OpenVINO defined operation semantics.

The first part is required for inference, the second part is required for successful import of a model containing such operations from the original framework model format. There are several options to implement each part, the next sections will describe them in detail.

Definition of Operation Semantics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the custom operation can be mathematically represented as a combination of exiting OpenVINO operations and such decomposition gives desired performance, then low-level operation implementation is not required. When deciding feasibility of such decomposition refer to the latest OpenVINO operation set. You can use any valid combination of exiting operations. How to map a custom operation is described in the next section of this document.

If such decomposition is not possible or appears too bulky with lots of consisting operations that are not performing well, then a new class for the custom operation should be implemented as described in the :ref:`Custom Operation Guide <doxid-openvino_docs__extensibility__u_g_add_openvino_ops>`.

Prefer implementing a custom operation class if you already have a generic C++ implementation of operation kernel. Otherwise try to decompose the operation first as described above and then after verifying correctness of inference and resulting performance, optionally invest to implementing bare metal C++ implementation.

Mapping from Framework Operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Depending on model format used for import, mapping of custom operation is implemented differently, choose one of:

#. If model is represented in ONNX (including models exported from Pytorch in ONNX) or PaddlePaddle formats, then one of the classes from :ref:`Frontend Extension API <doxid-openvino_docs__extensibility__u_g__frontend__extensions>` should be used. It consists of several classes available in C++ which can be used with Model Optimizer ``--extensions`` option or when model is imported directly to OpenVINO run-time using read_model method. Python API is also available for run-time model importing.

#. If model is represented in TensorFlow, Caffe, Kaldi or MXNet formats, then :ref:`Model Optimizer Extensions <doxid-openvino_docs__m_o__d_g_prepare_model_customize_model_optimizer__customize__model__optimizer>` should be used. This approach is available for model conversion in Model Optimizer only.

Existing of two approaches simultaneously is explained by two different types of frontends used for model conversion in OpenVINO: new frontends (ONNX, PaddlePaddle) and legacy frontends (TensorFlow, Caffe, Kaldi and MXNet). Model Optimizer can use both front-ends in contrast to the direct import of model with ``read_model`` method which can use new frontends only. Follow one of the appropriate guides referenced above to implement mappings depending on framework frontend.

If you are implementing extensions for ONNX or PaddlePaddle new frontends and plan to use Model Optimizer ``--extension`` option for model conversion, then the extensions should be

#. Implemented in C++ only

#. Compiled as a separate shared library (see details how to do that later in this guide).

You cannot write new frontend extensions using Python API if you plan to use them with Model Optimizer.

Remaining part of this guide uses Frontend Extension API applicable for new frontends.

Registering Extensions
~~~~~~~~~~~~~~~~~~~~~~

A custom operation class and a new mapping frontend extension class object should be registered to be usable in OpenVINO runtime.

.. note:: This documentation is written based on the `Template extension <https://github.com/openvinotoolkit/openvino/tree/master/docs/template_extension/new>`__, which demonstrates extension development details based on minimalistic ``Identity`` operation that is a placeholder for your real custom operation. You can review the complete code, which is fully compliable, to see how it works.

To load the extensions to the ``:ref:`ov::Core <doxid-classov_1_1_core>``` object, use the ``:ref:`ov::Core::add_extension <doxid-classov_1_1_core_1a68d0dea1cbcd42a67bea32780e32acea>``` method, this method allows to load library with extensions or extensions from the code.

Load extensions to core
-----------------------

Extensions can be loaded from code with ``:ref:`ov::Core::add_extension <doxid-classov_1_1_core_1a68d0dea1cbcd42a67bea32780e32acea>``` method:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	
	// Use operation type to add operation extension
	core.:ref:`add_extension <doxid-classov_1_1_core_1a68d0dea1cbcd42a67bea32780e32acea>`<TemplateExtension::Identity>();
	
	// or you can add operation extension object which is equivalent form
	core.:ref:`add_extension <doxid-classov_1_1_core_1a68d0dea1cbcd42a67bea32780e32acea>`(:ref:`ov::OpExtension\<TemplateExtension::Identity> <doxid-classov_1_1_op_extension>`());





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Not implemented





.. raw:: html

   </div>







.. raw:: html

   </div>



``Identity`` is custom operation class defined in :ref:`Custom Operation Guide <doxid-openvino_docs__extensibility__u_g_add_openvino_ops>`. This is enough to enable reading IR which uses ``Identity`` extension operation emitted by Model Optimizer. To be able to load original model directly to the runtime, you need to add also a mapping extension:

.. tab:: C++

    .. doxygensnippet:: docs/snippets/ov_extensions.cpp
       :language: cpp
       :fragment: add_frontend_extension

.. tab:: Python

    .. doxygensnippet:: docs/snippets/ov_extensions.py
       :language: python
       :fragment: add_frontend_extension

When Python API is used there is no way to implement a custom OpenVINO operation. Also, even if custom OpenVINO operation is implemented in C++ and loaded to the runtime through a shared library, there is still no way to add a frontend mapping extension that refers to this custom operation. Use C++ shared library approach to implement both operations semantics and framework mapping in this case.

You still can use Python for operation mapping and decomposition in case if operations from the standard OpenVINO operation set is used only.

Create library with extensions
------------------------------

You need to create extension library in the following cases:

* Convert model with custom operations in Model Optimizer

* Load model with custom operations in Python application. It is applicable for both framework model and IR.

* Loading models with custom operations in tools that support loading extensions from a library, for example ``benchmark_app``.

If you want to create an extension library, for example in order to load these extensions to the Model Optimizer, you need to do next steps: Create an entry point for extension library. OpenVINO™ provides an ``:ref:`OPENVINO_CREATE_EXTENSIONS() <doxid-core_2include_2openvino_2core_2extension_8hpp_1acdadcfa0eff763d8b4dadb8a9cb6f6e6>``` macro, which allows to define an entry point to a library with OpenVINO™ Extensions. This macro should have a vector of all OpenVINO™ Extensions as an argument.

Based on that, the declaration of an extension class can look as follows:

.. ref-code-block:: cpp

	:ref:`OPENVINO_CREATE_EXTENSIONS <doxid-core_2include_2openvino_2core_2extension_8hpp_1acdadcfa0eff763d8b4dadb8a9cb6f6e6>`(
	    std::vector<ov::Extension::Ptr>({
	
	        // Register operation itself, required to be read from IR
	        std::make_shared<ov::OpExtension<TemplateExtension::Identity>>(),
	
	        // Register operaton mapping, required when converted from framework model format
	        std::make_shared<:ref:`ov::frontend::OpExtension\<TemplateExtension::Identity> <doxid-classov_1_1frontend_1_1_op_extension_base>`>()
	    }));

To configure the build of your extension library, use the following CMake script:

.. ref-code-block:: cpp

	set(CMAKE_CXX_STANDARD 11)
	
	set(TARGET_NAME "openvino_template_extension")
	
	find_package(OpenVINO REQUIRED)
	
	set(SRC identity.cpp ov_extension.cpp)
	
	add_library(${TARGET_NAME} MODULE ${SRC})
	
	target_compile_definitions(${TARGET_NAME} PRIVATE IMPLEMENT_OPENVINO_EXTENSION_API)
	target_link_libraries(${TARGET_NAME} PRIVATE openvino::runtime)

This CMake script finds the OpenVINO™ using the ``find_package`` CMake command.

To build the extension library, run the commands below:

.. ref-code-block:: cpp

	$ cd docs/template_extension/new
	$ mkdir build
	$ cd build
	$ cmake -DOpenVINO_DIR=<OpenVINO_DIR> ../
	$ cmake --build .

After the build you can use path to your extension library to load your extensions to OpenVINO™ Runtime:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;
	// Load extensions library to ov::Core
	core.:ref:`add_extension <doxid-classov_1_1_core_1a68d0dea1cbcd42a67bea32780e32acea>`("openvino_template_extension.so");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core = :ref:`ov.Core <doxid-classov_1_1_core>`()
	# Load extensions library to ov.Core
	core.add_extension("openvino_template_extension.so")





.. raw:: html

   </div>







.. raw:: html

   </div>





See Also
~~~~~~~~

* :ref:`OpenVINO Transformations <doxid-openvino_docs_transformations>`

* :ref:`Using OpenVINO Runtime Samples <doxid-openvino_docs__o_v__u_g__samples__overview>`

* :ref:`Hello Shape Infer SSD sample <doxid-openvino_inference_engine_samples_hello_reshape_ssd__r_e_a_d_m_e>`

