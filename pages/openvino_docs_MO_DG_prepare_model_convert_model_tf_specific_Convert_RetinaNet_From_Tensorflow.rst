.. index:: pair: page; Converting TensorFlow RetinaNet Model
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__retina_net__from__tensorflow:


Converting TensorFlow RetinaNet Model
=====================================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_tf_specific__convert__retina_net__from__tensorflow_1md_openvino_docs_mo_dg_prepare_model_convert_model_tf_specific_convert_retinanet_from_tensorflow` This tutorial explains how to convert RetinaNet model to the Intermediate Representation (IR).

`Public RetinaNet model <https://github.com/fizyr/keras-retinanet>`__ does not contain pretrained TensorFlow\* weights. To convert this model to the TensorFlow\* format, you can use Reproduce Keras\* to TensorFlow\* Conversion tutorial.

After you convert the model to TensorFlow\* format, run the Model Optimizer command below:

.. ref-code-block:: cpp

	mo --input "input_1[1 1333 1333 3]" --input_model retinanet_resnet50_coco_best_v2.1.0.pb --data_type FP32 --transformations_config front/tf/retinanet.json

Where ``transformations_config`` command-line parameter specifies the configuration json file containing model conversion hints for the Model Optimizer. The json file contains some parameters that need to be changed if you train the model yourself. It also contains information on how to match endpoints to replace the subgraph nodes. After the model is converted to IR, the output nodes will be replaced with DetectionOutput layer.

