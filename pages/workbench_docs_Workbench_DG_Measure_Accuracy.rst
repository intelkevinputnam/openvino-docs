.. index:: pair: page; Create Accuracy Report
.. _doxid-workbench_docs__workbench__d_g__measure__accuracy:


Create Accuracy Report
======================

:target:`doxid-workbench_docs__workbench__d_g__measure__accuracy_1md_openvino_workbench_docs_workbench_dg_measure_accuracy`





.. toctree::
   :maxdepth: 1
   :hidden:

   workbench_docs_Workbench_DG_Accuracy_Configuration
   workbench_docs_Workbench_DG_Configure_Accuracy_Settings
   workbench_docs_Workbench_DG_Accuracy_Report_Results

.. note:: Accuracy Measurements are not available for Natural Language Processing models.

Once you select a model and a dataset and run a baseline inference, the **Projects** page appears. Go to the **Perform** tab and select **Create Accuracy Report** :

.. image:: create_report.png

Accuracy Report Types
~~~~~~~~~~~~~~~~~~~~~

In the DL Workbench, you can create the following reports:

* `Accuracy Evaluation on Validation Dataset <#dataset-annotations>`__

* `Comparison of Optimized and Parent Model Predictions <#model-predictions>`__

* `Calculation of Tensor Distance to Parent Model Output <#tensor-distance>`__

.. list-table::
    :header-rows: 1

    * - Requirement
      - Accuracy Evaluation on Validation Dataset
      - Comparison of Optimized and Parent Model Predictions
      - Calculation of Tensor Distance to Parent Model Output
    * - Model
      - Original or Optimized
      - Optimized
      - Optimized
    * - Dataset​
      - Annotated​
      - Annotated or Not Annotated
      - Annotated or Not Annotated
    * - Use Case​
      - Classification, Object-Detection, Instance-Segmentation, Semantic-Segmentation, Super-Resolution, Style-Transfer, Image-Inpainting
      - Classification, Object-Detection, Instance-Segmentation, Semantic-Segmentation
      - Classification, Object-Detection, Instance-Segmentation, Semantic-Segmentation, Super-Resolution, Style-Transfer, Image-Inpainting
    * - Accuracy Configuration​
      - Required
      - Not Required
      - Not Required

.. _dataset-annotations:

Accuracy Evaluation on Validation Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Accuracy Evaluation on Validation Dataset report provides information for evaluating model quality and allows you to compare the model output and validation dataset annotations. This type of report is explained in details in the :ref:`Object Detection <doxid-workbench_docs__workbench__d_g__measure__accuracy__object_detection>` and :ref:`Classification <doxid-workbench_docs__workbench__d_g__measure__accuracy__classification>` model tutorials.

.. _model-predictions:

Comparison of Optimized and Parent Model Predictions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get other types of Accuracy Report, you need to [optimize the model](Int-8_Quantization). Comparison of Optimized and Parent Model Predictions Report allows you to find out on which validation dataset images the predictions of the model became different after optimization. This type of report is explained in details in the :ref:`Optimize Object Detection <doxid-workbench_docs__workbench__d_g__tutorial__import__y_o_l_o>` model and :ref:`Optimize Classification <doxid-workbench_docs__workbench__d_g__tutorial__classification>` model tutorials.

.. _tensor-distance:

Calculation of Tensor Distance to Parent Model Output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tensor Distance Calculation Report allows to evaluate the mean squared error (MSE) between Optimized and Parent models output on tensor level for each image in the validation dataset. Mean Squared Error (MSE) is an average of the square of the difference between actual and estimated values. MSE evaluation enables you to identify significant differences between Parent and Optimized model predictions for a wider set of use cases besides classification and object detection. This type of report is explained in details in the :ref:`Optimize Style Transfer <doxid-workbench_docs__workbench__d_g__tutorial__style__transfer>` model tutorial.

See Also
~~~~~~~~

* :ref:`Object Detection model tutorial <doxid-workbench_docs__workbench__d_g__measure__accuracy__object_detection>`

* :ref:`Classification model tutorial <doxid-workbench_docs__workbench__d_g__measure__accuracy__classification>`

* :ref:`Optimize Object Detection model tutorial <doxid-workbench_docs__workbench__d_g__tutorial__import__y_o_l_o>`

* :ref:`Optimize Classification model tutorial <doxid-workbench_docs__workbench__d_g__tutorial__classification>`

* :ref:`Optimize Style Transfer model tutorial <doxid-workbench_docs__workbench__d_g__tutorial__style__transfer>`

* `Accuracy Checker <https://docs.openvinotoolkit.org/latest/omz_tools_accuracy_checker.html>`__

* :ref:`Configure Accuracy Settings <doxid-workbench_docs__workbench__d_g__accuracy__configuration>`

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

