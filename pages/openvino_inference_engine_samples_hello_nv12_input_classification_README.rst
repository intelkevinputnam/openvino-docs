.. index:: pair: page; Hello NV12 Input Classification C++ Sample
.. _doxid-openvino_inference_engine_samples_hello_nv12_input_classification__r_e_a_d_m_e:


Hello NV12 Input Classification C++ Sample
==========================================

:target:`doxid-openvino_inference_engine_samples_hello_nv12_input_classification__r_e_a_d_m_e_1md_openvino_samples_cpp_hello_nv12_input_classification_readme` This sample demonstrates how to execute an inference of image classification models with images in NV12 color format using Synchronous Inference Request API.

The following C++ API is used in the application:

.. list-table::
    :header-rows: 1

    * - Feature
      - API
      - Description
    * - Node Operations
      - ``ov::Output::get_any_name``
      - Get a layer name
    * - Infer Request Operations
      - ``:ref:`ov::InferRequest::set_tensor <doxid-classov_1_1_infer_request_1af54f126e7fb3b3a0343841dda8bcc368>``` , ``:ref:`ov::InferRequest::get_tensor <doxid-classov_1_1_infer_request_1a75b8da7c6b00686bede600dddceaffc4>```
      - Operate with tensors
    * - Preprocessing
      - ``:ref:`ov::preprocess::InputTensorInfo::set_color_format <doxid-classov_1_1preprocess_1_1_input_tensor_info_1a32df813b541b01ac7df6ae93d7f1f163>``` , ``:ref:`ov::preprocess::PreProcessSteps::convert_element_type <doxid-classov_1_1preprocess_1_1_pre_process_steps_1ab9e7979668e7403a72b07786f76ec0e0>``` , ``:ref:`ov::preprocess::PreProcessSteps::convert_color <doxid-classov_1_1preprocess_1_1_pre_process_steps_1a1cc7cc3fc7afb5992c1920c483ce3332>```
      - Change the color format of the input data

Basic OpenVINO™ Runtime API is covered by :ref:`Hello Classification C++ sample <doxid-openvino_inference_engine_samples_hello_classification__r_e_a_d_m_e>`.

.. list-table::
    :header-rows: 1

    * - Options
      - Values
    * - Validated Models
      - alexnet
    * - Model Format
      - OpenVINO™ toolkit Intermediate Representation (\*.xml + \*.bin), ONNX (\*.onnx)
    * - Validated images
      - An uncompressed image in the NV12 color format - \*.yuv
    * - Supported devices
      - :ref:`All <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`
    * - Other language realization
      - :ref:`C <doxid-openvino_inference_engine_ie_bridges_c_samples_hello_nv12_input_classification__r_e_a_d_m_e>`

How It Works
~~~~~~~~~~~~

At startup, the sample application reads command line parameters, loads the specified model and an image in the NV12 color format to an OpenVINO™ Runtime plugin. Then, the sample creates an synchronous inference request object. When inference is done, the application outputs data to the standard output stream. You can place labels in .labels file near the model to get pretty output.

You can see the explicit description of each sample step at :ref:`Integration Steps <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>` section of "Integrate OpenVINO™ Runtime with Your Application" guide.

Building
~~~~~~~~

To build the sample, please use instructions available at :ref:`Build the Sample Applications <doxid-openvino_docs__o_v__u_g__samples__overview>` section in OpenVINO™ Toolkit Samples guide.

Running
~~~~~~~

.. ref-code-block:: cpp

	hello_nv12_input_classification <path_to_model> <path_to_image> <image_size> <device_name>

To run the sample, you need specify a model and image:

* you can use public or Intel's pre-trained models from the Open Model Zoo. The models can be downloaded using the Model Downloader.

* you can use images from the media files collection available at `https://storage.openvinotoolkit.org/data/test_data <https://storage.openvinotoolkit.org/data/test_data>`__.

The sample accepts an uncompressed image in the NV12 color format. To run the sample, you need to convert your BGR/RGB image to NV12. To do this, you can use one of the widely available tools such as FFmpeg\* or GStreamer\*. The following command shows how to convert an ordinary image into an uncompressed NV12 image using FFmpeg:

.. ref-code-block:: cpp

	ffmpeg -i cat.jpg -pix_fmt nv12 car.yuv

**NOTES** :

* Because the sample reads raw image files, you should provide a correct image size along with the image path. The sample expects the logical size of the image, not the buffer size. For example, for 640x480 BGR/RGB image the corresponding NV12 logical image size is also 640x480, whereas the buffer size is 640x720.

* By default, this sample expects that model input has BGR channels order. If you trained your model to work with RGB order, you need to reconvert your model using the Model Optimizer tool with ``--reverse_input_channels`` argument specified. For more information about the argument, refer to **When to Reverse Input Channels** section of :ref:`Embedding Preprocessing Computation <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__converting__model>`.

* Before running the sample with a trained model, make sure the model is converted to the intermediate representation (IR) format (\*.xml + \*.bin) using the :ref:`Model Optimizer tool <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`.

* The sample accepts models in ONNX format (.onnx) that do not require preprocessing.

Example
-------

#. Install openvino-dev python package if you don't have it to use Open Model Zoo Tools:

.. ref-code-block:: cpp

	python -m pip install openvino-dev[caffe,onnx,tensorflow2,pytorch,mxnet]

#. Download a pre-trained model:
   
   .. ref-code-block:: cpp
   
   	omz_downloader --name alexnet

#. If a model is not in the IR or ONNX format, it must be converted. You can do this using the model converter:

.. ref-code-block:: cpp

	omz_converter --name alexnet

#. Perform inference of NV12 image using ``alexnet`` model on a ``CPU``, for example:

.. ref-code-block:: cpp

	hello_nv12_input_classification alexnet.xml car.yuv 300x300 CPU

Sample Output
~~~~~~~~~~~~~

The application outputs top-10 inference results.

.. ref-code-block:: cpp

	[ INFO ] OpenVINO Runtime version ......... <version>
	[ INFO ] Build ........... <build>
	[ INFO ]
	[ INFO ] Loading model files: \models\alexnet.xml
	[ INFO ] model name: AlexNet
	[ INFO ]     inputs
	[ INFO ]         input name: data
	[ INFO ]         input type: f32
	[ INFO ]         input shape: {1, 3, 227, 227}
	[ INFO ]     outputs
	[ INFO ]         output name: prob
	[ INFO ]         output type: f32
	[ INFO ]         output shape: {1, 1000}
	
	Top 10 results:
	
	Image \images\car.yuv
	
	classid probability
	------- -----------
	656     0.6668988
	654     0.1125269
	581     0.0679280
	874     0.0340229
	436     0.0257744
	817     0.0169367
	675     0.0110199
	511     0.0106134
	569     0.0083373
	717     0.0061734

See Also
~~~~~~~~

* :ref:`Integrate the OpenVINO™ Runtime with Your Application <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>`

* :ref:`Using OpenVINO™ Toolkit Samples <doxid-openvino_docs__o_v__u_g__samples__overview>`

* Model Downloader

* :ref:`Model Optimizer <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`

