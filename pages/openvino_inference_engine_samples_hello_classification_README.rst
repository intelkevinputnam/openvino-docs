.. index:: pair: page; Hello Classification C++ Sample
.. _doxid-openvino_inference_engine_samples_hello_classification__r_e_a_d_m_e:


Hello Classification C++ Sample
===============================

:target:`doxid-openvino_inference_engine_samples_hello_classification__r_e_a_d_m_e_1md_openvino_samples_cpp_hello_classification_readme` This sample demonstrates how to do inference of image classification models using Synchronous Inference Request API.

Models with only one input and output are supported.

The following C++ API is used in the application:

.. list-table::
    :header-rows: 1

    * - Feature
      - API
      - Description
    * - OpenVINO Runtime Version
      - ``ov::get_openvino_version``
      - Get Openvino API version
    * - Basic Infer Flow
      - ``:ref:`ov::Core::read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>``` , ``:ref:`ov::Core::compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>``` , ``:ref:`ov::CompiledModel::create_infer_request <doxid-classov_1_1_compiled_model_1ae3633c0eb5173ed776446fba32b95953>``` , ``:ref:`ov::InferRequest::set_input_tensor <doxid-classov_1_1_infer_request_1a5ddca7af7faffa2c90fd600a3f84aa6e>``` , ``:ref:`ov::InferRequest::get_output_tensor <doxid-classov_1_1_infer_request_1a350159a8d967022db46633eed50d073a>```
      - Common API to do inference: read and compile a model, create an infer request, configure input and output tensors
    * - Synchronous Infer
      - ``:ref:`ov::InferRequest::infer <doxid-classov_1_1_infer_request_1abcb7facc9f7c4b9226a1fd343e56958d>```
      - Do synchronous inference
    * - Model Operations
      - ``:ref:`ov::Model::inputs <doxid-classov_1_1_model_1a7121b50a2990b63eb6a73945f0cae089>``` , ``:ref:`ov::Model::outputs <doxid-classov_1_1_model_1a89c629856666f1064cf0418c432004f0>```
      - Get inputs and outputs of a model
    * - Tensor Operations
      - ``:ref:`ov::Tensor::get_shape <doxid-classov_1_1_tensor_1a706163e01fb555eb9ccdfb5204cf7834>```
      - Get a tensor shape
    * - Preprocessing
      - ``:ref:`ov::preprocess::InputTensorInfo::set_element_type <doxid-classov_1_1preprocess_1_1_input_tensor_info_1a320c54e50d794da07852ccecf9468e2a>``` , ``:ref:`ov::preprocess::InputTensorInfo::set_layout <doxid-classov_1_1preprocess_1_1_input_tensor_info_1af10932e00c45bb0ef09b2f856fab5268>``` , ``:ref:`ov::preprocess::InputTensorInfo::set_spatial_static_shape <doxid-classov_1_1preprocess_1_1_input_tensor_info_1a03db58db580f2974469a01da5b03f511>``` , ``:ref:`ov::preprocess::PreProcessSteps::resize <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a910dfdc8dc19b1890b2e8f111162a8d6>``` , ``:ref:`ov::preprocess::InputModelInfo::set_layout <doxid-classov_1_1preprocess_1_1_input_model_info_1aeac53aa90be5b8a6b86def31fab396b4>``` , ``:ref:`ov::preprocess::OutputTensorInfo::set_element_type <doxid-classov_1_1preprocess_1_1_output_tensor_info_1a9c2a13f397541993747a5bce4165d17e>``` , ``:ref:`ov::preprocess::PrePostProcessor::build <doxid-classov_1_1preprocess_1_1_pre_post_processor_1a62bde91535a3cd93cb2dcf5f416fe24a>```
      - Set image of the original size as input for a model with other input size. Resize and layout conversions are performed automatically by the corresponding plugin just before inference.

.. list-table::
    :header-rows: 1

    * - Options
      - Values
    * - Validated Models
      - alexnet, googlenet-v1
    * - Model Format
      - OpenVINO™ toolkit Intermediate Representation (\*.xml + \*.bin), ONNX (\*.onnx)
    * - Supported devices
      - :ref:`All <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`
    * - Other language realization
      - :ref:`C <doxid-openvino_inference_engine_ie_bridges_c_samples_hello_classification__r_e_a_d_m_e>` , :ref:`Python <doxid-openvino_inference_engine_ie_bridges_python_sample_hello_classification__r_e_a_d_m_e>`

How It Works
~~~~~~~~~~~~

At startup, the sample application reads command line parameters, prepares input data, loads a specified model and image to the OpenVINO™ Runtime plugin and performs synchronous inference. Then processes output data and write it to a standard output stream.

You can see the explicit description of each sample step at :ref:`Integration Steps <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>` section of "Integrate OpenVINO™ Runtime with Your Application" guide.

Building
~~~~~~~~

To build the sample, please use instructions available at :ref:`Build the Sample Applications <doxid-openvino_docs__o_v__u_g__samples__overview>` section in OpenVINO™ Toolkit Samples guide.

Running
~~~~~~~

.. ref-code-block:: cpp

	hello_classification <path_to_model> <path_to_image> <device_name>

To run the sample, you need specify a model and image:

* you can use public or Intel's pre-trained models from the Open Model Zoo. The models can be downloaded using the Model Downloader.

* you can use images from the media files collection available at `https://storage.openvinotoolkit.org/data/test_data <https://storage.openvinotoolkit.org/data/test_data>`__.

**NOTES** :

* By default, OpenVINO™ Toolkit Samples and Demos expect input with BGR channels order. If you trained your model to work with RGB order, you need to manually rearrange the default channels order in the sample or demo application or reconvert your model using the Model Optimizer tool with ``--reverse_input_channels`` argument specified. For more information about the argument, refer to **When to Reverse Input Channels** section of :ref:`Embedding Preprocessing Computation <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__converting__model>`.

* Before running the sample with a trained model, make sure the model is converted to the intermediate representation (IR) format (\*.xml + \*.bin) using the :ref:`Model Optimizer tool <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`.

* The sample accepts models in ONNX format (.onnx) that do not require preprocessing.

Example
-------

#. Install the ``openvino-dev`` Python package to use Open Model Zoo Tools:

.. ref-code-block:: cpp

	python -m pip install openvino-dev[caffe,onnx,tensorflow2,pytorch,mxnet]

#. Download a pre-trained model using:

.. ref-code-block:: cpp

	omz_downloader --name googlenet-v1

#. If a model is not in the IR or ONNX format, it must be converted. You can do this using the model converter:

.. ref-code-block:: cpp

	omz_converter --name googlenet-v1

#. Perform inference of ``car.bmp`` using the ``googlenet-v1`` model on a ``GPU``, for example:

.. ref-code-block:: cpp

	hello_classification googlenet-v1.xml car.bmp GPU

Sample Output
~~~~~~~~~~~~~

The application outputs top-10 inference results.

.. ref-code-block:: cpp

	[ INFO ] OpenVINO Runtime version ......... <version>
	[ INFO ] Build ........... <build>
	[ INFO ]
	[ INFO ] Loading model files: /models/googlenet-v1.xml
	[ INFO ] model name: GoogleNet
	[ INFO ]     inputs
	[ INFO ]         input name: data
	[ INFO ]         input type: f32
	[ INFO ]         input shape: {1, 3, 224, 224}
	[ INFO ]     outputs
	[ INFO ]         output name: prob
	[ INFO ]         output type: f32
	[ INFO ]         output shape: {1, 1000}
	
	Top 10 results:
	
	Image /images/car.bmp
	
	classid probability
	------- -----------
	656     0.8139648
	654     0.0550537
	468     0.0178375
	436     0.0165405
	705     0.0111694
	817     0.0105820
	581     0.0086823
	575     0.0077515
	734     0.0064468
	785     0.0043983

See Also
~~~~~~~~

* :ref:`Integrate the OpenVINO™ Runtime with Your Application <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>`

* :ref:`Using OpenVINO™ Toolkit Samples <doxid-openvino_docs__o_v__u_g__samples__overview>`

* Model Downloader

* :ref:`Model Optimizer <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`

