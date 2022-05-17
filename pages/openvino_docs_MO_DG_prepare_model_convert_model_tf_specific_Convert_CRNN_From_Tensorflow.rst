.. index:: pair: page; Convert TensorFlow CRNN Model
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__c_r_n_n__from__tensorflow:


Convert TensorFlow CRNN Model
=============================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__c_r_n_n__from__tensorflow_1md_openvino_docs_mo_dg_prepare_model_convert_model_tf_specific_convert_crnn_from_tensorflow` This tutorial explains how to convert a CRNN model to Intermediate Representation (IR).

On GitHub\*, you can find several public versions of TensorFlow\* CRNN model implementation. This tutorial explains how to convert the model from the `https://github.com/MaybeShewill-CV/CRNN_Tensorflow <https://github.com/MaybeShewill-CV/CRNN_Tensorflow>`__ repository to IR. If you have another implementation of CRNN model, you can convert it to IR in similar way: you need to get inference graph and run the Model Optimizer on it.

**To convert this model to the IR:**

**Step 1.** Clone this GitHub repository and checkout the commit:

#. Clone repository:
   
   .. ref-code-block:: cpp
   
   	git clone https://github.com/MaybeShewill-CV/CRNN_Tensorflow.git
   
   
   
   .. code-block:: cpp
   
   	2. Checkout necessary commit:
   
   
   
   .. ref-code-block:: cpp
   
   	git checkout 64f1f1867bffaacfeacc7a80eebf5834a5726122

**Step 2.** Train the model using framework or use the pre-trained checkpoint provided in this repository.

**Step 3.** Create an inference graph:

#. Go to the ``CRNN_Tensorflow`` directory with the cloned repository:
   
   .. ref-code-block:: cpp
   
   	cd path/to/CRNN_Tensorflow
   
   
   
   .. code-block:: cpp
   
   	2. Add `CRNN_Tensorflow` folder to `PYTHONPATH`.
   	   \* For Linux\\* OS:
   
   
   
   .. ref-code-block:: cpp
   
   	export PYTHONPATH="${PYTHONPATH}:/path/to/CRNN_Tensorflow/"
   
   
   
   .. code-block:: cpp
   
   	   \* For  Windows\\* OS add `/path/to/CRNN_Tensorflow/` to the `PYTHONPATH` environment variable in settings.
   	3. Open the `tools/test_shadownet.py` script. After `saver.restore(sess=sess, save_path=weights_path)` line, add the following code:
   
   
   
   .. ref-code-block:: cpp
   
   	import tensorflow as tf
   	from tensorflow.python.framework import graph_io
   	frozen = tf.compat.v1.graph_util.convert_variables_to_constants(sess, sess.graph_def, ['shadow/LSTMLayers/transpose_time_major'])
   	graph_io.write_graph(frozen, '.', 'frozen_graph.pb', as_text=False)
   
   
   
   .. code-block:: cpp
   
   	4. Run the demo with the following command:
   
   
   
   .. ref-code-block:: cpp
   
   	python tools/test_shadownet.py --image_path data/test_images/test_01.jpg --weights_path model/shadownet/shadownet_2017-10-17-11-47-46.ckpt-199999

If you want to use your checkpoint, replace the path in the ``--weights_path`` parameter with a path to your checkpoint.

#. In the ``CRNN_Tensorflow`` directory, you will find the inference CRNN graph ``frozen_graph.pb``. You can use this graph with the OpenVINO toolkit to convert the model into IR and run inference.

**Step 4.** Convert the model into IR:

.. ref-code-block:: cpp

	mo --input_model path/to/your/CRNN_Tensorflow/frozen_graph.pb

