.. index:: pair: page; Image Classification Async C++ Sample
.. _doxid-openvino_inference_engine_samples_classification_sample_async__r_e_a_d_m_e:


Image Classification Async C++ Sample
=====================================

:target:`doxid-openvino_inference_engine_samples_classification_sample_async__r_e_a_d_m_e_1md_openvino_samples_cpp_classification_sample_async_readme` This sample demonstrates how to do inference of image classification models using Asynchronous Inference Request API.

Models with only one input and output are supported.

In addition to regular images, the sample also supports single-channel ``ubyte`` images as an input for LeNet model.

The following C++ API is used in the application:

.. list-table::
    :header-rows: 1

    * - Feature
      - API
      - Description
    * - Asynchronous Infer
      - ``:ref:`ov::InferRequest::start_async <doxid-classov_1_1_infer_request_1a5a05ae4352f804c865e11f5d68b983d5>``` , ``:ref:`ov::InferRequest::set_callback <doxid-classov_1_1_infer_request_1afba2a10162ab356728ec8901973e8f02>```
      - Do asynchronous inference with callback.
    * - Model Operations
      - ``ov::Output::get_shape`` , ``:ref:`ov::set_batch <doxid-namespaceov_1a3314e2ff91fcc9ffec05b1a77c37862b>```
      - Manage the model, operate with its batch size. Set batch size using input image count.
    * - Infer Request Operations
      - ``:ref:`ov::InferRequest::get_input_tensor <doxid-classov_1_1_infer_request_1a5f0bc1ab40de6a7a12136b4a4e6a8b54>```
      - Get an input tensor.
    * - Tensor Operations
      - ``:ref:`ov::shape_size <doxid-group__ov__model__cpp__api_1gafe8cdd6477ae9810c2bf368602d35883>``` , ``:ref:`ov::Tensor::data <doxid-classov_1_1_tensor_1ac1b8835f54d67d92969d7979e666e2a8>```
      - Get a tensor shape size and its data.

Basic OpenVINO™ Runtime API is covered by :ref:`Hello Classification C++ sample <doxid-openvino_inference_engine_samples_hello_classification__r_e_a_d_m_e>`.

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
      - :ref:`Python <doxid-openvino_inference_engine_ie_bridges_python_sample_classification_sample_async__r_e_a_d_m_e>`

How It Works
~~~~~~~~~~~~

At startup, the sample application reads command line parameters and loads the specified model and input images (or a folder with images) to the OpenVINO™ Runtime plugin. The batch size of the model is set according to the number of read images. The batch mode is an independent attribute on the asynchronous mode. Asynchronous mode works efficiently with any batch size.

Then, the sample creates an inference request object and assigns completion callback for it. In scope of the completion callback handling the inference request is executed again.

After that, the application starts inference for the first infer request and waits of 10th inference request execution being completed. The asynchronous mode might increase the throughput of the pictures.

When inference is done, the application outputs data to the standard output stream. You can place labels in .labels file near the model to get pretty output.

You can see the explicit description of each sample step at :ref:`Integration Steps <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>` section of "Integrate OpenVINO™ Runtime with Your Application" guide.

Building
~~~~~~~~

To build the sample, please use instructions available at :ref:`Build the Sample Applications <doxid-openvino_docs__o_v__u_g__samples__overview>` section in OpenVINO™ Toolkit Samples guide.

Running
~~~~~~~

Run the application with the ``-h`` option to see the usage instructions:

.. ref-code-block:: cpp

	classification_sample_async -h

Usage instructions:

.. ref-code-block:: cpp

	[ INFO ] OpenVINO Runtime version ......... <version>
	[ INFO ] Build ........... <build>
	
	classification_sample_async [OPTION]
	Options:
	
	    -h                      Print usage instructions.
	    -m "<path>"             Required. Path to an .xml file with a trained model.
	    -i "<path>"             Required. Path to a folder with images or path to image files: a .ubyte file for LeNet and a .bmp file for other models.
	    -d "<device>"           Optional. Specify the target device to infer on (the list of available devices is shown below). Default value is CPU. Use "-d HETERO:<comma_separated_devices_list>" format to specify the HETERO plugin. Sample will look for a suitable plugin for the device specified.
	
	Available target devices: <devices>

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

#. Perform inference of ``dog.bmp`` using ``googlenet-v1`` model on a ``GPU``, for example:

.. ref-code-block:: cpp

	classification_sample_async -m googlenet-v1.xml -i dog.bmp -d GPU

Sample Output
~~~~~~~~~~~~~

.. ref-code-block:: cpp

	[ INFO ] OpenVINO Runtime version ......... <version>
	[ INFO ] Build ........... <build>
	[ INFO ]
	[ INFO ] Parsing input parameters
	[ INFO ] Files were added: 1
	[ INFO ]     /images/dog.bmp
	[ INFO ] Loading model files:
	[ INFO ] /models/googlenet-v1.xml
	[ INFO ] model name: GoogleNet
	[ INFO ]     inputs
	[ INFO ]         input name: data
	[ INFO ]         input type: f32
	[ INFO ]         input shape: {1, 3, 224, 224}
	[ INFO ]     outputs
	[ INFO ]         output name: prob
	[ INFO ]         output type: f32
	[ INFO ]         output shape: {1, 1000}
	[ INFO ] Read input images
	[ INFO ] Set batch size 1
	[ INFO ] model name: GoogleNet
	[ INFO ]     inputs
	[ INFO ]         input name: data
	[ INFO ]         input type: u8
	[ INFO ]         input shape: {1, 224, 224, 3}
	[ INFO ]     outputs
	[ INFO ]         output name: prob
	[ INFO ]         output type: f32
	[ INFO ]         output shape: {1, 1000}
	[ INFO ] Loading model to the device GPU
	[ INFO ] Create infer request
	[ INFO ] Start inference (asynchronous executions)
	[ INFO ] Completed 1 async request execution
	[ INFO ] Completed 2 async request execution
	[ INFO ] Completed 3 async request execution
	[ INFO ] Completed 4 async request execution
	[ INFO ] Completed 5 async request execution
	[ INFO ] Completed 6 async request execution
	[ INFO ] Completed 7 async request execution
	[ INFO ] Completed 8 async request execution
	[ INFO ] Completed 9 async request execution
	[ INFO ] Completed 10 async request execution
	[ INFO ] Completed async requests execution
	
	Top 10 results:
	
	Image /images/dog.bmp
	
	classid probability
	------- -----------
	156     0.8935547
	218     0.0608215
	215     0.0217133
	219     0.0105667
	212     0.0018835
	217     0.0018730
	152     0.0018730
	157     0.0015745
	154     0.0012817
	220     0.0010099

See Also
~~~~~~~~

* :ref:`Integrate the OpenVINO™ Runtime with Your Application <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>`

* :ref:`Using OpenVINO™ Toolkit Samples <doxid-openvino_docs__o_v__u_g__samples__overview>`

* Model Downloader

* :ref:`Model Optimizer <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`

