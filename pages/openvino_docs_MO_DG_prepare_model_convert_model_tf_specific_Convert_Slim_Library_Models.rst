.. index:: pair: page; Convert TensorFlow Slim Image Classification Model Library Models
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__slim__library__models:


Convert TensorFlow Slim Image Classification Model Library Models
=================================================================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__slim__library__models_1md_openvino_docs_mo_dg_prepare_model_convert_model_tf_specific_convert_slim_library_models` `TensorFlow\*-Slim Image Classification Model Library <https://github.com/tensorflow/models/tree/master/research/slim/README.md>`__ is a library to define, train and evaluate classification models in TensorFlow\*. The library contains Python scripts defining the classification topologies together with checkpoint files for several pre-trained classification topologies. To convert a TensorFlow\*-Slim library model, complete the following steps:

#. Download the TensorFlow\*-Slim models `git repository <https://github.com/tensorflow/models>`__.

#. Download the pre-trained model `checkpoint <https://github.com/tensorflow/models/tree/master/research/slim#pre-trained-models>`__.

#. Export the inference graph.

#. Convert the model using the Model Optimizer.

The `Example of an Inception V1 Model Conversion <#example_of_an_inception_v1_model_conversion>`__ section below illustrates the process of converting an Inception V1 Model.

.. _example_of_an_inception_v1_model_conversion:

Example of an Inception V1 Model Conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to convert the model on Linux\* OSes, but it could be easily adopted for the Windows\* OSes.

Step 1. Create a new directory to clone the TensorFlow\*-Slim git repository to:

.. ref-code-block:: cpp

	mkdir tf_models

.. ref-code-block:: cpp

	git clone https://github.com/tensorflow/models.git tf_models

Step 2. Download and unpack the `Inception V1 model checkpoint file <http://download.tensorflow.org/models/inception_v1_2016_08_28.tar.gz>`__ :

.. ref-code-block:: cpp

	wget http://download.tensorflow.org/models/inception_v1_2016_08_28.tar.gz

.. ref-code-block:: cpp

	tar xzvf inception_v1_2016_08_28.tar.gz

Step 3. Export the inference graph the protobuf file (``.pb``) containing the architecture of the topology. Note, this file *doesn't* contain the neural network weights and cannot be used for inference.

.. ref-code-block:: cpp

	python3 tf_models/research/slim/export_inference_graph.py \
	    --model_name inception_v1 \
	    --output_file inception_v1_inference_graph.pb

Model Optimizer comes with the summarize graph utility, which identifies graph input and output nodes. Run the utility to determine input/output nodes of the Inception V1 model:

.. ref-code-block:: cpp

	python3 <PYTHON_SITE_PACKAGES>/openvino/tools/mo/utils/summarize_graph.py --input_model ./inception_v1_inference_graph.pb

The output looks as follows:



.. ref-code-block:: cpp

	1 input(s) detected:
	Name: input, type: float32, shape: (-1,224,224,3)
	1 output(s) detected:
	InceptionV1/Logits/Predictions/Reshape_1

The tool finds one input node with name ``input``, type ``float32``, fixed image size ``(224,224,3)`` and undefined batch size ``-1``. The output node name is ``InceptionV1/Logits/Predictions/Reshape_1``.

Step 4. Convert the model with the Model Optimizer:

.. ref-code-block:: cpp

	mo --input_model ./inception_v1_inference_graph.pb --input_checkpoint ./inception_v1.ckpt -b 1 --mean_value [127.5,127.5,127.5] --scale 127.5

The ``-b`` command line parameter is required because the Model Optimizer cannot convert a model with undefined input size.

Refer to the `Mean and Scale Values for TensorFlow\*-Slim Models <#tf_slim_mean_scale_values>`__ for the information why ``--mean_values`` and ``--scale`` command line parameters are used.

.. _tf_slim_mean_scale_values:

Mean and Scale Values for TensorFlow\*-Slim Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The TensorFlow\*-Slim Models were trained with normalized input data. There are several different normalization algorithms used in the Slim library. OpenVINO classification sample does not perform image pre-processing except resizing to the input layer size. It is necessary to pass mean and scale values to the Model Optimizer so they are embedded into the generated IR in order to get correct classification results.

The file `preprocessing_factory.py <https://github.com/tensorflow/models/blob/master/research/slim/preprocessing/preprocessing_factory.py>`__ contains a dictionary variable ``preprocessing_fn_map`` defining mapping between the model type and pre-processing function to be used. The function code should be analyzed to figure out the mean/scale values.

The `inception_preprocessing.py <https://github.com/tensorflow/models/blob/master/research/slim/preprocessing/inception_preprocessing.py>`__ file defines the pre-processing function for the Inception models. The ``preprocess_for_eval`` function contains the following code:

.. ref-code-block:: cpp

	...
	import tensorflow as tf
	if image.dtype != tf.float32:
	  image = tf.image.convert_image_dtype(image, dtype=tf.float32)
	...
	image = tf.subtract(image, 0.5)
	image = tf.multiply(image, 2.0)
	return image

Firstly, the ``image`` is converted to data type ``tf.float32`` and the values in the tensor are scaled to the ``[0, 1]`` range using the `tf.image.convert_image_dtype <https://www.tensorflow.org/api_docs/python/tf/image/convert_image_dtype>`__ function. Then the ``0.5`` is subtracted from the image values and values multiplied by ``2.0``. The final image range of values is ``[-1, 1]``.

OpenVINO classification sample reads an input image as a three-dimensional array of integer values from the range ``[0, 255]``. In order to scale them to ``[-1, 1]`` range, the mean value ``127.5`` for each image channel should be specified as well as scale factor ``127.5``.

Similarly, the mean/scale values can be determined for other Slim models.

The exact mean/scale values are defined in the table with list of supported TensorFlow\*-Slim models at the :ref:`Converting a TensorFlow\* Model <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__tensor_flow>`.

