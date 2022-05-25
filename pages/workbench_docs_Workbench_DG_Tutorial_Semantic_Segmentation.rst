.. index:: pair: page; Optimize Semantic Segmentation Model
.. _doxid-workbench_docs__workbench__d_g__tutorial__semantic__segmentation:


Optimize Semantic Segmentation Model
====================================

:target:`doxid-workbench_docs__workbench__d_g__tutorial__semantic__segmentation_1md_openvino_workbench_docs_workbench_dg_tutorial_semantic_segmentation`

Summary
~~~~~~~

INT8 Calibration is a universal method for accelerating deep learning models. Calibration is a process of converting a Deep Learning model weights to a lower 8-bit precision such that it needs less computation.

In this tutorial, you will learn how to optimize your model using INT8 Calibration, examine how much quicker the model has become, and check the difference between original and optimized model accuracy.

.. list-table::
    :header-rows: 1

    * - Model
      - Task Type
      - Format
      - Source
      - Dataset
    * - `deeplabv3 <https://docs.openvinotoolkit.org/latest/omz_models_model_fast_neural_style_mosaic_onnx.html>`__
      - `Semantic Segmentation <https://paperswithcode.com/task/semantic-segmentation>`__
      - `TensorFlow\* <https://www.tensorflow.org/>`__
      - `Open Model Zoo <https://github.com/openvinotoolkit/open_model_zoo/tree/master/models/public/deeplabv3>`__
      - :ref:`Pascal Visual Object Classes (Pascal VOC) <doxid-workbench_docs__workbench__d_g__dataset__types>`

.. tip:: You can learn how to :ref:`import a model <doxid-workbench_docs__workbench__d_g__select__model>` and :ref:`a dataset <doxid-workbench_docs__workbench__create__project>` in the DL Workbench :ref:`Get Started Guide <doxid-workbench_docs__workbench__d_g__work_with__models_and__sample__datasets>`.

.. note:: For deeplabv3 model, it is highly recommended to use `Pascal VOC <https://docs.openvino.ai/latest/workbench_docs_Workbench_DG_Dataset_Types.html#pascal-visual-object-classes-pascal-voc>`__ dataset to get the accurate results.

Optimize Model Using INT8 Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To convert the model to INT8, go to **Perform** tab on the Project page and open **Optimize** subtab. Check **INT8** and click **Optimize**.

.. image:: optimize_face_detection.png

It takes you to the **Optimize INT8** page. Select the imported dataset and perform INT8 Calibration with Default optimization method and Performance Preset calibration scheme first as it provides maximum performance speedup.

.. image:: optimization_settings_segmentation.png

After optimization, you will be redirected to a new Project page for optimized ``deeplabv3`` model.

.. image:: optimized_semantic_segmentation.png

To ensure that the optimized model performance is sufficiently accelerated and its predictions can be trusted, evaluate the key characteristics: performance and accuracy.

Compare Optimized and Parent Model Performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go back to the model page and check the performance of the imported and optimized models. Compare the throughput numbers and click **Compare Projects** button to see more details. Learn more about projects comparison on the :ref:`Compare Performance <doxid-workbench_docs__workbench__d_g__compare__performance_between__two__versions_of__models>` page.

.. note:: Throughput is the number of images processed in a given amount of time. It is measured in frames per second (FPS). Higher throughput value means better performance.

.. image:: compare_semantic_segmentation.png

You can observe that ``deeplabv3`` model has become 2.6x times faster on CPU device after optimization.

Lowering the precision of the model using quantization leads to a loss in prediction capability. Therefore you need to assess the model prediction capability to ensure that the model has not lost a significant amount of accuracy.

Compare Parent and Optimized Model Predictions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create Accuracy Report
----------------------

Create an Accuracy Report that allows you to visualize and compare Optimized and Parent model predictions. Go to the **Perform** tab and select **Create Accuracy Report** :

.. image:: create_accuracy_report_semantic.png

Comparison of Optimized and Parent Model Predictions Report allows you to find out on which validation dataset images the predictions of the model have become different after optimization. Let's compare Optimized model predictions with Parent model predictions used as optimal references.

Interpret Report Results
------------------------

The Report has two display options: Basic and Advanced mode. Each line of the report table in basic mode contains an **Image Name** and **Optimized Model Average Result** for all objects in the image. Advanced mode shows **Class Predicted by Optimized Model**.

Basic mode:

.. image:: report_table_segmentation.png

Advanced mode:

.. image:: report_table_segmentation_advanced.png

**TIP:** To sort the numbers from lowest to highest, click on the parameter name in the table.

Click **Visualize** to see the prediction difference:

.. image:: semantic_segmentation_results.png

In our case, the optimized ``deeplabv3`` model recognized all object of class #6 - buses. You can see that the clustering parts for each object coincide in Optimized and Parent model predictions.

.. image:: semantic_segmentation_fail.png

In another example, clustering parts for each object in Optimized ``deeplabv3`` predictions are less accurate than the Parent model prediction.

Next Step
~~~~~~~~~

After evaluating the accuracy, you can decide whether the difference between imported and optimized models predictions is critical or not:

* If the tradeoff between accuracy and performance is too big, :ref:`import an annotated dataset <doxid-workbench_docs__workbench__d_g__generate__datasets>` and use `AccuracyAware optimization method <Int-8_Quantization.md#accuracyaware>`__, then repeat the steps from this tutorial.

* If the tradeoff is acceptable, :ref:`explore inference configurations <doxid-workbench_docs__workbench__d_g__deploy_and__integrate__performance__criteria_into__application>` to further enhance the performance. Then create a :ref:`deployment package <doxid-workbench_docs__workbench__d_g__deployment__package>` with your ready-to-deploy model.

*All images were taken from ImageNet, Pascal Visual Object Classes, and Common Objects in Context datasets for demonstration purposes only.*

See Also
~~~~~~~~

* :ref:`Create Accuracy Report <doxid-workbench_docs__workbench__d_g__measure__accuracy>`

* :ref:`Configure Accuracy Settings <doxid-workbench_docs__workbench__d_g__accuracy__configuration>`

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

