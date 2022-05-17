.. index:: pair: page; Image Classification Async Python\* Sample
.. _doxid-openvino_inference_engine_ie_bridges_python_sample_classification_sample_async__r_e_a_d_m_e:


Image Classification Async Python\* Sample
==========================================

:target:`doxid-openvino_inference_engine_ie_bridges_python_sample_classification_sample_async__r_e_a_d_m_e_1md_openvino_samples_python_classification_sample_async_readme` This sample demonstrates how to do inference of image classification models using Asynchronous Inference Request API.

Models with only 1 input and output are supported.

The following Python API is used in the application:

.. list-table::
    :header-rows: 1

    * - Feature
      - API
      - Description
    * - Asynchronous Infer
      - [openvino.runtime.AsyncInferQueue], `openvino.runtime.AsyncInferQueue.set_callback <[openvino.runtime.AsyncInferQueue.start_async]:>`__ , [openvino.runtime.AsyncInferQueue.start_async], [openvino.runtime.AsyncInferQueue.wait_all], [openvino.runtime.InferRequest.results]
      - Do asynchronous inference

Basic OpenVINO™ Runtime API is covered by :ref:`Hello Classification Python\* Sample <doxid-openvino_inference_engine_ie_bridges_python_sample_hello_classification__r_e_a_d_m_e>`.

.. list-table::
    :header-rows: 1

    * - Options
      - Values
    * - Validated Models
      - alexnet
    * - Model Format
      - OpenVINO™ toolkit Intermediate Representation (.xml + .bin), ONNX (.onnx)
    * - Supported devices
      - :ref:`All <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`
    * - Other language realization
      - :ref:`C++ <doxid-openvino_inference_engine_samples_classification_sample_async__r_e_a_d_m_e>`

How It Works
~~~~~~~~~~~~

At startup, the sample application reads command-line parameters, prepares input data, loads a specified model and image(s) to the OpenVINO™ Runtime plugin, performs synchronous inference, and processes output data, logging each step in a standard output stream.

You can see the explicit description of each sample step at :ref:`Integration Steps <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>` section of "Integrate OpenVINO™ Runtime with Your Application" guide.

Running
~~~~~~~

Run the application with the ``-h`` option to see the usage message:

.. ref-code-block:: cpp

	python classification_sample_async.py -h

Usage message:

.. ref-code-block:: cpp

	usage: classification_sample_async.py [-h] -m MODEL -i INPUT [INPUT ...]
	                                      [-d DEVICE]
	
	Options:
	  -h, --help            Show this help message and exit.
	  -m MODEL, --model MODEL
	                        Required. Path to an .xml or .onnx file with a trained
	                        model.
	  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
	                        Required. Path to an image file(s).
	  -d DEVICE, --device DEVICE
	                        Optional. Specify the target device to infer on; CPU,
	                        GPU, MYRIAD, HDDL or HETERO: is acceptable. The sample
	                        will look for a suitable plugin for device specified.
	                        Default value is CPU.

To run the sample, you need specify a model and image:

* you can use public or Intel's pre-trained models from the Open Model Zoo. The models can be downloaded using the Model Downloader.

* you can use images from the media files collection available at `https://storage.openvinotoolkit.org/data/test_data <https://storage.openvinotoolkit.org/data/test_data>`__.

**NOTES** :

* By default, OpenVINO™ Toolkit Samples and demos expect input with BGR channels order. If you trained your model to work with RGB order, you need to manually rearrange the default channels order in the sample or demo application or reconvert your model using the Model Optimizer tool with ``--reverse_input_channels`` argument specified. For more information about the argument, refer to **When to Reverse Input Channels** section of :ref:`Embedding Preprocessing Computation <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__converting__model>`.

* Before running the sample with a trained model, make sure the model is converted to the intermediate representation (IR) format (\*.xml + \*.bin) using the :ref:`Model Optimizer tool <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`.

* The sample accepts models in ONNX format (.onnx) that do not require preprocessing.

Example
-------

#. Install the ``openvino-dev`` Python package to use Open Model Zoo Tools:

.. ref-code-block:: cpp

	python -m pip install openvino-dev[caffe,onnx,tensorflow2,pytorch,mxnet]

#. Download a pre-trained model:
   
   .. ref-code-block:: cpp
   
   	omz_downloader --name alexnet

#. If a model is not in the IR or ONNX format, it must be converted. You can do this using the model converter:

.. ref-code-block:: cpp

	omz_converter --name alexnet

#. Perform inference of ``banana.jpg`` and ``car.bmp`` using the ``alexnet`` model on a ``GPU``, for example:

.. ref-code-block:: cpp

	python classification_sample_async.py -m alexnet.xml -i banana.jpg car.bmp -d GPU

Sample Output
~~~~~~~~~~~~~

The sample application logs each step in a standard output stream and outputs top-10 inference results.

.. ref-code-block:: cpp

	[ INFO ] Creating OpenVINO Runtime Core
	[ INFO ] Reading the model: C:/test_data/models/alexnet.xml
	[ INFO ] Loading the model to the plugin
	[ INFO ] Starting inference in asynchronous mode
	[ INFO ] Image path: /test_data/images/banana.jpg
	[ INFO ] Top 10 results:
	[ INFO ] class_id probability
	[ INFO ] --------------------
	[ INFO ] 954      0.9707602
	[ INFO ] 666      0.0216788
	[ INFO ] 659      0.0032558
	[ INFO ] 435      0.0008082
	[ INFO ] 809      0.0004359
	[ INFO ] 502      0.0003860
	[ INFO ] 618      0.0002867
	[ INFO ] 910      0.0002866
	[ INFO ] 951      0.0002410
	[ INFO ] 961      0.0002193
	[ INFO ]
	[ INFO ] Image path: /test_data/images/car.bmp
	[ INFO ] Top 10 results:
	[ INFO ] class_id probability
	[ INFO ] --------------------
	[ INFO ] 656      0.5120340
	[ INFO ] 874      0.1142275
	[ INFO ] 654      0.0697167
	[ INFO ] 436      0.0615163
	[ INFO ] 581      0.0552262
	[ INFO ] 705      0.0304179
	[ INFO ] 675      0.0151660
	[ INFO ] 734      0.0151582
	[ INFO ] 627      0.0148493
	[ INFO ] 757      0.0120964
	[ INFO ]
	[ INFO ] This sample is an API example, for any performance measurements please use the dedicated benchmark_app tool

See Also
~~~~~~~~

* :ref:`Integrate the OpenVINO™ Runtime with Your Application <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>`

* :ref:`Using OpenVINO™ Toolkit Samples <doxid-openvino_docs__o_v__u_g__samples__overview>`

* Model Downloader

* :ref:`Model Optimizer <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`

