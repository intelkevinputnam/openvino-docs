.. index:: pair: page; Hello Classification Python\* Sample
.. _doxid-openvino_inference_engine_ie_bridges_python_sample_hello_classification__r_e_a_d_m_e:


Hello Classification Python\* Sample
====================================

:target:`doxid-openvino_inference_engine_ie_bridges_python_sample_hello_classification__r_e_a_d_m_e_1md_openvino_samples_python_hello_classification_readme` This sample demonstrates how to do inference of image classification models using Synchronous Inference Request API.

Models with only 1 input and output are supported.

The following Python API is used in the application:

.. list-table::
    :header-rows: 1

    * - Feature
      - API
      - Description
    * - Basic Infer Flow
      - [openvino.runtime.Core], `openvino.runtime.Core.read_model <[openvino.runtime.Core.compile_model]:>`__ , [openvino.runtime.Core.compile_model]
      - Common API to do inference
    * - Synchronous Infer
      - `openvino.runtime.CompiledModel.infer_new_request <[openvino.runtime.Model.inputs]:>`__
      - Do synchronous inference
    * - Model Operations
      - [openvino.runtime.Model.inputs], `openvino.runtime.Model.outputs <[openvino.preprocess.PrePostProcessor]:>`__
      - Managing of model
    * - Preprocessing
      - [openvino.preprocess.PrePostProcessor], `openvino.preprocess.InputTensorInfo.set_element_type <[openvino.preprocess.InputTensorInfo.set_layout]:>`__ ,[openvino.preprocess.InputTensorInfo.set_layout], `openvino.preprocess.InputTensorInfo.set_spatial_static_shape <[openvino.preprocess.PreProcessSteps.resize]:>`__ ,[openvino.preprocess.PreProcessSteps.resize], `openvino.preprocess.InputModelInfo.set_layout <[openvino.preprocess.OutputTensorInfo.set_element_type]:>`__ ,[openvino.preprocess.OutputTensorInfo.set_element_type],[openvino.preprocess.PrePostProcessor.build]
      - Set image of the original size as input for a model with other input size. Resize and layout conversions will be performed automatically by the corresponding plugin just before inference

.. list-table::
    :header-rows: 1

    * - Options
      - Values
    * - Validated Models
      - alexnet, googlenet-v1
    * - Model Format
      - OpenVINO™ toolkit Intermediate Representation (.xml + .bin), ONNX (.onnx)
    * - Supported devices
      - :ref:`All <doxid-openvino_docs__o_v__u_g_supported_plugins__supported__devices>`
    * - Other language realization
      - :ref:`C++ <doxid-openvino_inference_engine_samples_hello_classification__r_e_a_d_m_e>` , :ref:`C <doxid-openvino_inference_engine_ie_bridges_c_samples_hello_classification__r_e_a_d_m_e>`

How It Works
~~~~~~~~~~~~

At startup, the sample application reads command-line parameters, prepares input data, loads a specified model and image to the OpenVINO™ Runtime plugin, performs synchronous inference, and processes output data, logging each step in a standard output stream.

You can see the explicit description of each sample step at :ref:`Integration Steps <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>` section of "Integrate OpenVINO™ Runtime with Your Application" guide.

Running
~~~~~~~

.. ref-code-block:: cpp

	python hello_classification.py <path_to_model> <path_to_image> <device_name>

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

#. Perform inference of ``banana.jpg`` using the ``alexnet`` model on a ``GPU``, for example:

.. ref-code-block:: cpp

	python hello_classification.py alexnet.xml banana.jpg GPU

Sample Output
~~~~~~~~~~~~~

The sample application logs each step in a standard output stream and outputs top-10 inference results.

.. ref-code-block:: cpp

	[ INFO ] Creating OpenVINO Runtime Core
	[ INFO ] Reading the model: /models/alexnet/alexnet.xml
	[ INFO ] Loading the model to the plugin
	[ INFO ] Starting inference in synchronous mode
	[ INFO ] Image path: /images/banana.jpg
	[ INFO ] Top 10 results:     
	[ INFO ] class_id probability
	[ INFO ] --------------------
	[ INFO ] 954      0.9703885
	[ INFO ] 666      0.0219518
	[ INFO ] 659      0.0033120
	[ INFO ] 435      0.0008246
	[ INFO ] 809      0.0004433
	[ INFO ] 502      0.0003852
	[ INFO ] 618      0.0002906
	[ INFO ] 910      0.0002848
	[ INFO ] 951      0.0002427
	[ INFO ] 961      0.0002213
	[ INFO ]
	[ INFO ] This sample is an API example, for any performance measurements please use the dedicated benchmark_app tool

See Also
~~~~~~~~

* :ref:`Integrate the OpenVINO™ Runtime with Your Application <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>`

* :ref:`Using OpenVINO™ Toolkit Samples <doxid-openvino_docs__o_v__u_g__samples__overview>`

* Model Downloader

* :ref:`Model Optimizer <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>`

