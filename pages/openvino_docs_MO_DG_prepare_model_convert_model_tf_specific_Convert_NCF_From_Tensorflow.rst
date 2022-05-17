.. index:: pair: page; Convert TensorFlow Neural Collaborative Filtering Model
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__n_c_f__from__tensorflow:


Convert TensorFlow Neural Collaborative Filtering Model
=======================================================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__n_c_f__from__tensorflow_1md_openvino_docs_mo_dg_prepare_model_convert_model_tf_specific_convert_ncf_from_tensorflow` This tutorial explains how to convert Neural Collaborative Filtering (NCF) model to Intermediate Representation (IR).

`Public TensorFlow NCF model <https://github.com/tensorflow/models/tree/master/official/recommendation>`__ does not contain pre-trained weights. To convert this model to the IR:

#. Use `the instructions <https://github.com/tensorflow/models/tree/master/official/recommendation#train-and-evaluate-model>`__ from this repository to train the model.

#. Freeze the inference graph you get on previous step in ``model_dir`` following the instructions from the Freezing Custom Models in Python\* section of :ref:`Converting a TensorFlow\* Model <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__tensor_flow>`. Run the following commands:
   
   .. ref-code-block:: cpp
   
   	import tensorflow as tf
   	from tensorflow.python.framework import graph_io
   	
   	sess = tf.compat.v1.Session()
   	saver = tf.compat.v1.train.import_meta_graph("/path/to/model/model.meta")
   	saver.restore(sess, tf.train.latest_checkpoint('/path/to/model/'))
   	
   	frozen = tf.compat.v1.graph_util.convert_variables_to_constants(sess, sess.graph_def, \
   	                                                      ["rating/BiasAdd"])
   	graph_io.write_graph(frozen, './', 'inference_graph.pb', as_text=False)

where ``rating/BiasAdd`` is an output node.

#. Convert the model to the IR.If you look at your frozen model, you can see that it has one input that is split into four ``ResourceGather`` layers. (Click image to zoom in.)

.. image:: NCF_start.png
	:alt: NCF model beginning

But as the Model Optimizer does not support such data feeding, you should skip it. Cut the edges incoming in ``ResourceGather`` s port 1:

.. ref-code-block:: cpp

	 mo --input_model inference_graph.pb                    \
	--input 1:embedding/embedding_lookup,1:embedding_1/embedding_lookup, \
	1:embedding_2/embedding_lookup,1:embedding_3/embedding_lookup        \
	--input_shape [256],[256],[256],[256]                                \
	--output_dir <OUTPUT_MODEL_DIR>

In the ``input_shape`` parameter, 256 specifies the ``batch_size`` for your model.

Alternatively, you can do steps 2 and 3 in one command line:

.. ref-code-block:: cpp

	 mo --input_meta_graph /path/to/model/model.meta        \
	--input 1:embedding/embedding_lookup,1:embedding_1/embedding_lookup, \
	1:embedding_2/embedding_lookup,1:embedding_3/embedding_lookup        \
	--input_shape [256],[256],[256],[256] --output rating/BiasAdd        \
	--output_dir <OUTPUT_MODEL_DIR>

