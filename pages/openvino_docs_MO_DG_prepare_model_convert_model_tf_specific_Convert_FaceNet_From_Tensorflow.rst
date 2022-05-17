.. index:: pair: page; Convert TensorFlow FaceNet Models
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__face_net__from__tensorflow:


Convert TensorFlow FaceNet Models
=================================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__face_net__from__tensorflow_1md_openvino_docs_mo_dg_prepare_model_convert_model_tf_specific_convert_facenet_from_tensorflow` `Public pre-trained FaceNet models <https://github.com/davidsandberg/facenet#pre-trained-models>`__ contain both training and inference part of graph. Switch between this two states is manageable with placeholder value. Intermediate Representation (IR) models are intended for inference, which means that train part is redundant.

There are two inputs in this network: boolean ``phase_train`` which manages state of the graph (train/infer) and ``batch_size`` which is a part of batch joining pattern.

.. image:: FaceNet.png
	:alt: FaceNet model view

Convert TensorFlow FaceNet Model to IR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To generate FaceNet IR provide TensorFlow FaceNet model to Model Optimizer with parameters:

.. ref-code-block:: cpp

	 mo
	--input_model path_to_model/model_name.pb       \
	--freeze_placeholder_with_value "phase_train->False"

Batch joining pattern transforms to placeholder with model default shape if ``--input_shape`` or ``--batch`` / ``-b`` was not provided. Otherwise, placeholder shape has custom parameters.

* ``--freeze_placeholder_with_value "phase_train->False"`` to switch graph to inference mode

* ``--batch`` / ``-b`` is applicable to override original network batch

* ``--input_shape`` is applicable with or without ``--input``

* other options are applicable

