.. index:: pair: page; Convert TensorFlow BERT Model
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__b_e_r_t__from__tensorflow:


Convert TensorFlow BERT Model
=============================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__b_e_r_t__from__tensorflow_1md_openvino_docs_mo_dg_prepare_model_convert_model_tf_specific_convert_bert_from_tensorflow` Pre-trained models for BERT (Bidirectional Encoder Representations from Transformers) are `publicly available <https://github.com/google-research/bert>`__.

.. _supported_models:

Supported Models
~~~~~~~~~~~~~~~~

Currently, the following models from the `pre-trained BERT model list <https://github.com/google-research/bert#pre-trained-models>`__ are supported:

* ``BERT-Base, Cased``

* ``BERT-Base, Uncased``

* ``BERT-Base, Multilingual Cased``

* ``BERT-Base, Multilingual Uncased``

* ``BERT-Base, Chinese``

* ``BERT-Large, Cased``

* ``BERT-Large, Uncased``

Download the Pre-Trained BERT Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download and unzip an archive with the `BERT-Base, Multilingual Uncased Model <https://storage.googleapis.com/bert_models/2018_11_03/multilingual_L-12_H-768_A-12.zip>`__.

After the archive is unzipped, the directory ``uncased_L-12_H-768_A-12`` is created and contains the following files:

* ``bert_config.json``

* ``bert_model.ckpt.data-00000-of-00001``

* ``bert_model.ckpt.index``

* ``bert_model.ckpt.meta``

* ``vocab.txt``

Pre-trained model meta-graph files are ``bert_model.ckpt.\*``.

Convert TensorFlow BERT Model to IR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To generate the BERT Intermediate Representation (IR) of the model, run the Model Optimizer with the following parameters:

.. ref-code-block:: cpp

	 mo \
	--input_meta_graph uncased_L-12_H-768_A-12/bert_model.ckpt.meta \
	--output bert/pooler/dense/Tanh                                 \
	--input Placeholder{i32},Placeholder_1{i32},Placeholder_2{i32}

Pre-trained models are not suitable for batch reshaping out-of-the-box because of multiple hardcoded shapes in the model.

Convert Reshape-able TensorFlow\* BERT Model to the Intermediate Representation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow these steps to make pre-trained TensorFlow BERT model reshape-able over batch dimension:

#. Download pre-trained BERT model you would like to use from the `Supported Models list <#supported_models>`__

#. Clone google-research/bert git repository:
   
   .. ref-code-block:: cpp
   
   	https://github.com/google-research/bert.git

#. Go to the root directory of the cloned repository:
   
   
   
   .. ref-code-block:: cpp
   
   	cd bert

#. (Optional) Checkout to the commit that the conversion was tested on:
   
   
   
   .. ref-code-block:: cpp
   
   	git checkout eedf5716c

#. Download script to load GLUE data:
   
   * For UNIX\*-like systems, run the following command:
     
     .. ref-code-block:: cpp
     
     	wget https://gist.githubusercontent.com/W4ngatang/60c2bdb54d156a41194446737ce03e2e/raw/17b8dd0d724281ed7c3b2aeeda662b92809aadd5/download_glue_data.py
     
     
     
     .. code-block:: cpp
     
     	\* For Windows\* systems:<br>
     	    Download the [Python script](https://gist.githubusercontent.com/W4ngatang/60c2bdb54d156a41194446737ce03e2e/raw/17b8dd0d724281ed7c3b2aeeda662b92809aadd5/download_glue_data.py) to the current working directory.

#. Download GLUE data by running:
   
   .. ref-code-block:: cpp
   
   	python3 download_glue_data.py --tasks MRPC

#. Open the file ``modeling.py`` in the text editor and delete lines 923-924. They should look like this:
   
   .. ref-code-block:: cpp
   
   	if not non_static_indexes:
   	    return shape

#. Open the file ``run_classifier.py`` and insert the following code after the line 645:
   
   .. ref-code-block:: cpp
   
   	import os, sys
   	import tensorflow as tf
   	from tensorflow.python.framework import graph_io
   	with tf.compat.v1.Session(graph=tf.compat.v1.get_default_graph()) as sess:
   	    (assignment_map, initialized_variable_names) = \
   	        modeling.get_assignment_map_from_checkpoint(tf.compat.v1.trainable_variables(), init_checkpoint)
   	    tf.compat.v1.train.init_from_checkpoint(init_checkpoint, assignment_map)
   	    sess.run(tf.compat.v1.global_variables_initializer())
   	    frozen = tf.compat.v1.graph_util.convert_variables_to_constants(sess, sess.graph_def, ["bert/pooler/dense/Tanh"])
   	    graph_io.write_graph(frozen, './', 'inference_graph.pb', as_text=False)
   	print('BERT frozen model path {}'.format(os.path.join(os.path.dirname(__file__), 'inference_graph.pb')))
   	sys.exit(0)

Lines before the inserted code should look like this:

.. ref-code-block:: cpp

	(total_loss, per_example_loss, logits, probabilities) = create_model(
	    bert_config, is_training, input_ids, input_mask, segment_ids, label_ids,
	    num_labels, use_one_hot_embeddings)

#. Set environment variables ``BERT_BASE_DIR``, ``BERT_REPO_DIR`` and run the script ``run_classifier.py`` to create ``inference_graph.pb`` file in the root of the cloned BERT repository.
   
   .. ref-code-block:: cpp
   
   	export BERT_BASE_DIR=/path/to/bert/uncased_L-12_H-768_A-12
   	export BERT_REPO_DIR=/current/working/directory
   	
   	python3 run_classifier.py \
   	    --task_name=MRPC \
   	    --do_eval=true \
   	    --data_dir=$BERT_REPO_DIR/glue_data/MRPC \
   	    --vocab_file=$BERT_BASE_DIR/vocab.txt \
   	    --bert_config_file=$BERT_BASE_DIR/bert_config.json \
   	    --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
   	    --output_dir=./

Run the Model Optimizer with the following command line parameters to generate reshape-able BERT Intermediate Representation (IR):

.. ref-code-block:: cpp

	 mo \
	--input_model inference_graph.pb \
	--input "IteratorGetNext:0{i32}[1 128],IteratorGetNext:1{i32}[1 128],IteratorGetNext:4{i32}[1 128]"

For other applicable parameters, refer to :ref:`Convert Model from TensorFlow <doxid-openvino_docs__m_o__d_g_prepare_model_convert_model__convert__model__from__tensor_flow>`.

For more information about reshape abilities, refer to :ref:`Using Shape Inference <doxid-openvino_docs__o_v__u_g__shape_inference>`.

