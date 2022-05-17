.. index:: pair: page; Integrate OpenVINO™ with Your Application
.. _doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application:


Integrate OpenVINO™ with Your Application
===========================================

:target:`doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application_1md_openvino_docs_ov_runtime_ug_integrate_with_your_application`





.. toctree::
   :maxdepth: 1
   :hidden:

   openvino_docs_OV_UG_Model_Representation
   openvino_docs_OV_UG_Infer_request
   openvino_docs_OV_UG_Python_API_exclusives

.. note:: Before start using OpenVINO™ Runtime, make sure you set all environment variables during the installation. To do so, follow the instructions from the *Set the Environment Variables* section in the installation guides:

* :ref:`For Windows\* 10 <doxid-openvino_docs_install_guides_installing_openvino_windows>`

* :ref:`For Linux\* <doxid-openvino_docs_install_guides_installing_openvino_linux>`

* :ref:`For macOS\* <doxid-openvino_docs_install_guides_installing_openvino_macos>`

* To build an open source version, use the `OpenVINO™ Runtime Build Instructions <https://github.com/openvinotoolkit/openvino/wiki/BuildingCode>`__.

Use OpenVINO™ Runtime API to Implement Inference Pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section provides step-by-step instructions to implement a typical inference pipeline with the OpenVINO™ Runtime C++ or Python API:

.. image:: IMPLEMENT_PIPELINE_with_API_C.svg

Step 1. Create OpenVINO™ Runtime Core
---------------------------------------

Include next files to work with OpenVINO™ Runtime:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	#include <openvino/openvino.hpp>





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



Use the following code to create OpenVINO™ Core to manage available devices and read model objects:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::Core <doxid-classov_1_1_core>` core;





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	core = :ref:`ov.Core <doxid-classov_1_1_core>`()





.. raw:: html

   </div>







.. raw:: html

   </div>





Step 2. Compile the Model
-------------------------

``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` class represents a device specific compiled model. ``:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>``` allows you to get information inputs or output ports by a tensor name or index. This approach is aligned with the majority of frameworks.

Compile the model for a specific device using ``:ref:`ov::Core::compile_model() <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>``` :

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="IR">





.. ref-code-block:: cpp

	:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>` compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`("model.xml", "AUTO");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="ONNX">





.. ref-code-block:: cpp

	:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>` compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`("model.onnx", "AUTO");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="PaddlePaddle">





.. ref-code-block:: cpp

	:ref:`ov::CompiledModel <doxid-classov_1_1_compiled_model>` compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`("model.pdmodel", "AUTO");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="ov::Model">





.. ref-code-block:: cpp

	auto create_model = []() {
	    std::shared_ptr<ov::Model> :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`;
	    // To construct a model, please follow 
	    // https://docs.openvino.ai/latest/openvino_docs_OV_UG_Model_Representation.html
	    return :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`;
	};
	std::shared_ptr<ov::Model> :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>` = create_model();
	compiled_model = core.:ref:`compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>`(:ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, "AUTO");





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">







.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="IR">





.. ref-code-block:: cpp

	compiled_model = core.compile_model("model.xml", "AUTO")





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="ONNX">





.. ref-code-block:: cpp

	compiled_model = core.compile_model("model.onnx", "AUTO")





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="PaddlePaddle">





.. ref-code-block:: cpp

	compiled_model = core.compile_model("model.pdmodel", "AUTO")





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="ov::Model">





.. ref-code-block:: cpp

	def create_model():
	    # This example shows how to create ov::Function
	    #
	    # To construct a model, please follow 
	    # https://docs.openvino.ai/latest/openvino_docs_OV_UG_Model_Representation.html
	    data = ov.opset8.parameter([3, 1, 2], ov.Type.f32)
	    res = ov.opset8.result(data)
	    return :ref:`ov.Model <doxid-classov_1_1_model>`([res], [data], "model")
	
	model = create_model()
	compiled_model = core.compile_model(model, "AUTO")





.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>







.. raw:: html

   </div>



The ``:ref:`ov::Model <doxid-classov_1_1_model>``` object represents any models inside the OpenVINO™ Runtime. For more details please read article about :ref:`OpenVINO™ Model representation <doxid-openvino_docs__o_v__u_g__model__representation>`.

The code above creates a compiled model associated with a single hardware device from the model object. It is possible to create as many compiled models as needed and use them simultaneously (up to the limitation of the hardware resources). To learn how to change the device configuration, read the :ref:`Query device properties <doxid-openvino_docs__o_v__u_g_query_api>` article.

Step 3. Create an Inference Request
-----------------------------------

``:ref:`ov::InferRequest <doxid-classov_1_1_infer_request>``` class provides methods for model inference in OpenVINO™ Runtime. Create an infer request using the following code (see :ref:`InferRequest detailed documentation <doxid-openvino_docs__o_v__u_g__infer_request>` for more details):

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	:ref:`ov::InferRequest <doxid-classov_1_1_infer_request>` infer_request = compiled_model.:ref:`create_infer_request <doxid-classov_1_1_compiled_model_1ae3633c0eb5173ed776446fba32b95953>`();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	infer_request = compiled_model.create_infer_request()





.. raw:: html

   </div>







.. raw:: html

   </div>





Step 4. Set Inputs
------------------

You can use external memory to create ``:ref:`ov::Tensor <doxid-classov_1_1_tensor>``` and use the ``:ref:`ov::InferRequest::set_input_tensor <doxid-classov_1_1_infer_request_1a5ddca7af7faffa2c90fd600a3f84aa6e>``` method to put this tensor on the device:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Get input port for model with one input
	auto input_port = compiled_model.:ref:`input <doxid-classov_1_1_compiled_model_1a55f2867a43fb78829f9901c52f9ccea9>`();
	// Create tensor from external memory
	:ref:`ov::Tensor <doxid-classov_1_1_tensor>` input_tensor(input_port.get_element_type(), input_port.get_shape(), memory_ptr);
	// Set input tensor for model with one input
	infer_request.:ref:`set_input_tensor <doxid-classov_1_1_infer_request_1a5ddca7af7faffa2c90fd600a3f84aa6e>`(input_tensor);





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Create tensor from external memory
	input_tensor = :ref:`ov.Tensor <doxid-classov_1_1_tensor>`(array=memory, shared_memory=True)
	# Set input tensor for model with one input
	infer_request.set_input_tensor(input_tensor)





.. raw:: html

   </div>







.. raw:: html

   </div>





Step 5. Start Inference
-----------------------

OpenVINO™ Runtime supports inference in either synchronous or asynchronous mode. Using the Async API can improve application's overall frame-rate: instead of waiting for inference to complete, the app can keep working on the host while the accelerator is busy. You can use ``:ref:`ov::InferRequest::start_async <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>``` to start model inference in the asynchronous mode and call ``:ref:`ov::InferRequest::wait <doxid-classov_1_1_infer_request_1ab0e0739da45789d816f8b5584a0b5691>``` to wait for the inference results:

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	infer_request.:ref:`start_async <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>`();
	infer_request.:ref:`wait <doxid-classov_1_1_infer_request_1ab0e0739da45789d816f8b5584a0b5691>`();





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	infer_request.start_async()
	infer_request.wait()





.. raw:: html

   </div>







.. raw:: html

   </div>



This section demonstrates a simple pipeline. To get more information about other ways to perform inference, read the dedicated :ref:`OpenVINO™ Inference Request <doxid-openvino_docs__o_v__u_g__infer_request>` Run inference" section".

Step 6. Process the Inference Results
-------------------------------------

Go over the output tensors and process the inference results.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Get output tensor by tensor name
	auto output = infer_request.:ref:`get_tensor <doxid-classov_1_1_infer_request_1a75b8da7c6b00686bede600dddceaffc4>`("tensor_name");
	const float \*output_buffer = output.data<const float>();
	/\* output_buffer[] - accessing output tensor data \*/





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Get output tensor for model with one output
	output = infer_request.get_output_tensor()
	output_buffer = output.data
	# output_buffer[] - accessing output tensor data





.. raw:: html

   </div>







.. raw:: html

   </div>





Link and Build Your C++ Application with OpenVINO™ Runtime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The example uses CMake for project configuration.

#. **Create a structure** for the project:
   
   .. ref-code-block:: cpp
   
   	project/
   	    ├── CMakeLists.txt  - CMake file to build
   	    ├── ...             - Additional folders like includes/
   	    └── src/            - source folder
   	        └── main.cpp
   	build/                  - build directory
   	    ...

#. **Include OpenVINO™ Runtime libraries** in ``project/CMakeLists.txt``
   
   .. ref-code-block:: cpp
   
   	cmake_minimum_required(VERSION 3.10)
   	set(CMAKE_CXX_STANDARD 11)
   	
   	find_package(OpenVINO REQUIRED)
   	
   	add_executable(${TARGET_NAME} src/main.cpp)
   	
   	target_link_libraries(${TARGET_NAME} PRIVATE openvino::runtime)
   
   To build your project using CMake with the default build tools currently available on your machine, execute the following commands:

.. note:: Make sure you set environment variables first by running ``<INSTALL_DIR>/setupvars.sh`` (or ``setupvars.bat`` for Windows). Otherwise the ``OpenVINO_DIR`` variable won't be configured properly to pass ``find_package`` calls.

.. ref-code-block:: cpp

	cd build/
	cmake ../project
	cmake --build .

You can also specify additional build options (e.g. to build CMake project on Windows with a specific build tools). Please refer to the `CMake page <https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1)>`__ for details.

Run Your Application
~~~~~~~~~~~~~~~~~~~~

Congratulations, you have made your first application with OpenVINO™ toolkit, now you may run it.

Additional Resources
~~~~~~~~~~~~~~~~~~~~

* See the :ref:`OpenVINO Samples <doxid-openvino_docs__o_v__u_g__samples__overview>` page or the `Open Model Zoo Demos <https://docs.openvino.ai/latest/omz_demos.html>`__ page for specific examples of how OpenVINO pipelines are implemented for applications like image classification, text prediction, and many others.

* :ref:`OpenVINO™ Runtime Preprocessing <doxid-openvino_docs__o_v__u_g__preprocessing__overview>`

* :ref:`Using Encrypted Models with OpenVINO <doxid-openvino_docs__o_v__u_g_protecting_model_guide>`

* :ref:`OpenVINO Samples <doxid-openvino_docs__o_v__u_g__samples__overview>`

* `Open Model Zoo Demos <https://docs.openvino.ai/latest/omz_demos.html>`__

