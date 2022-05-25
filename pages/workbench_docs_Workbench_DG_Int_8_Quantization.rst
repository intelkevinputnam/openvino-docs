.. index:: pair: page; INT8 Calibration
.. _doxid-workbench_docs__workbench__d_g__int_8__quantization:


INT8 Calibration
================

:target:`doxid-workbench_docs__workbench__d_g__int_8__quantization_1md_openvino_workbench_docs_workbench_dg_int-8_quantization` DL Workbench can lower the precision of a model from FP32 to INT8 with a process called calibration. Calibration accelerates the performance of certain models on hardware that supports INT8. A model in INT8 precision takes up less memory and has higher throughput capacity. Often this performance boost is achieved at the cost of a small accuracy reduction. With the DL Workbench, you can calibrate your model locally, on a `remote target <#remote-calibration>`__, or in the `Intel® DevCloud for the Edge <#devcloud-calibration>`__.

To read more about INT8 inference, see :ref:`Using Low-Precision INT8 Integer Inference <doxid-openvino_docs_model_optimization_guide>` and :ref:`Post-Training Optimization Toolkit <doxid-pot_introduction>`.

.. note:: INT8 calibration is **not** available in the following cases:

#. The model belongs to Natural Language Processing domain.

#. You run the configuration on an Intel® Movidius™ Neural Compute Stick 2, or Intel® Vision Accelerator Design with Intel® Movidius™ VPUs plugin.

#. AccuracyAware method is disabled if your configuration uses a not annotated dataset.

INT8 Calibration Methods
~~~~~~~~~~~~~~~~~~~~~~~~

DL Workbench supports two calibration methods: `Default method <#default>`__ and `AccuracyAware <#accuracyaware>`__. Each method is further configured with a calibration scheme configuration: the `performance-oriented preset <#performance-preset>`__, which is the default scheme, or the `mixed preset <#mixed-preset>`__. Calibration schemes do not depend on a selected calibration method.

.. tip:: As a rule, the smaller the calibration subset, the less time the algorithms take. It is recommended to use at least a 3-5% subset of the validation dataset (300-1000 images).

.. note:: A model optimized by the Default method translates all layers that support INT8 execution into INT8 precision, while the AccuracyAware method translates only those layers that both can be executed in INT8 precision and almost do not increase accuracy drop.

.. _default:

Default Method
--------------

Default method optimizes your model to achieve best performance. The algorithm usually produces the fastest model and usually but not always results in accuracy drop within 1%. Also, this algorithm takes less time than the AccuracyAware optimization method.

.. note:: This method supports both annotated and not annotated datasets. See :ref:`Dataset Types <doxid-workbench_docs__workbench__d_g__dataset__types>` for details.

.. _accuracyaware:

AccuracyAware method
--------------------

AccuracyAware calibration optimizes your model to achieve best performance possible with the specified maximum acceptable accuracy drop. The AccuracyAware method might result in lower performance compared to the Default method, while the accuracy drop is predictable. Accuracy drop is the difference between the parent model accuracy and the optimized model accuracy. Accuracy of the optimized model is guaranteed to be not smaller than the difference between the parent model accuracy and the accuracy drop.

.. note:: This method supports only annotated datasets. See :ref:`Dataset Types <doxid-workbench_docs__workbench__d_g__dataset__types>` for details.

.. _performance-preset:

Performance Preset
------------------

Performance preset guarantees uncompromising performance of a selected calibration method, as with this preset both weights and activations are calibrated in a symmetric mode. Performance preset is a default option because it provides maximum performance speedup and is independent from a target platform.

.. _mixed-preset:

Mixed Preset
------------

Mixed preset is a tradeoff between accuracy and performance, and with this preset weights and activations are calibrated in symmetric and asymmetric modes correspondingly. Compared to the performance preset, the mixed preset may result in a more accurate model at the cost of performance drop. Depending on a target platform and a model, performance drop usually varies from 5 to 15%. For example, use this preset if a model has convolutional or fully-connected layers with both negative and positive activations, like a model with non-ReLU activations.

Workflow
~~~~~~~~

.. raw:: html

   <iframe  allowfullscreen mozallowfullscreen msallowfullscreen oallowfullscreen webkitallowfullscreen  width="560" height="315" src="https://www.youtube.com/embed/7XQAZBdA_wo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Overall flow for converting a model from FP32 to INT8:

#. :ref:`Select an FP32 model <doxid-workbench_docs__workbench__d_g__select__models>`

#. :ref:`Select an appropriate dataset <doxid-workbench_docs__workbench__d_g__generate__datasets>`

#. :ref:`Run a baseline inference <doxid-workbench_docs__workbench__d_g__work_with__models_and__sample__datasets>`

#. `Configure INT8 calibration settings and select a calibration dataset <#8-bit-config>`__

#. :ref:`Configure inference settings for a calibrated model <doxid-workbench_docs__workbench__d_g__run__single__inference>`

#. `View INT8 calibration <#review-calibration-progress>`__

#. :ref:`View inference results <doxid-workbench_docs__workbench__d_g__view__inference__results>`

#. :ref:`Compare the calibrated model with the original FP32 model <doxid-workbench_docs__workbench__d_g__compare__performance_between__two__versions_of__models>`

Use the links above to walk through the steps and workflow for creating a calibrated model. Topics specific *only* to the INT8 calibration process (steps 4-6) are described below.

.. _8-bit-config:

Configure INT8 Calibration Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once a model has been profiled by the DL Workbench, you can convert it from FP32 to to INT8. For non-FP32 models, the INT8 option is grayed out. Go to the **Perform** tab on the **Projects** page and open the **Optimize** subtab.

.. image:: optimize_options.png

**NOTE:** Using INT8 calibration, you can tune only an original (top-level) model.

Check **INT8** and click **Optimize**. It takes you to the **Optimize INT8** page where you need to:

#. `Select or import a calibration dataset <#dataset>`__.

#. Define the percentage of images to use.

#. `Select an optimization method <#method>`__.

#. Optionally, `select an optimization scheme <#preset>`__.

.. _dataset:

Select Calibration Dataset (Optional)
-------------------------------------

.. note:: During the calibration process, a model tends to overfit the dataset its being calibrated on. To avoid overfitting, use separate datasets for calibration and validation.

Select a dataset you want to calibrate the model on, or import a calibration dataset by clicking **Select** :

.. image:: calibration_dataset_01.png

The **Import Calibration Dataset** page appears. Select the file with a dataset, enter the dataset name, and click **Import** :

.. image:: calibration_dataset_02.png

You are directed back to the **Optimize INT8** page. Specify the percentage of images you will use during the calibration procedure in the **Subset Size** box. The default value is 100%.

.. image:: subset_size.png

.. _method:

Select Optimization Method
--------------------------

Select an optimization method: `Default Method <#default>`__ or `AccuracyAware Method <#accuracyaware>`__.

.. image:: calibration_options.png

For the AccuracyAware option, specify the **Maximum Accuracy Drop** to instruct the DL Workbench to only convert layers that do not exceed the maximum accuracy drop you can tolerate. If a layer is estimated to exceed this value, it is not calibrated and remains at the original precision.

.. note:: See :ref:`Configure Accuracy Settings <doxid-workbench_docs__workbench__d_g__accuracy__configuration>` for details.

.. image:: configure_calibration_01-b.png

.. _preset:

Select Calibration Scheme (Advanced)
------------------------------------

Calibration scheme is a collection of optimization algorithm parameters that improve a certain metric of an algorithm. See :ref:`optimization parameters <doxid-pot_compression_algorithms_quantization_default__r_e_a_d_m_e>` for details.

.. image:: calibration_scheme.png

.. _review-calibration-progress:

View INT8 Calibration
~~~~~~~~~~~~~~~~~~~~~

Click **Calibrate**, and a new project for your model appears. You can work with other projects while the calibration is performed.

.. image:: calibration_process.png

.. _review-calibration-progress:

View INT8 Calibration Results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optimized model project is available at the Model Page:

.. image:: optimized_model_project.png

Once the job is done, you can compare an optimized model with the original model. For more details, go to :ref:`Compare Performance between Two Versions of Models <doxid-workbench_docs__workbench__d_g__compare__performance_between__two__versions_of__models>`.

The value of the **outputPrecisions** parameter in the **Layer Name** table for layers of INT8 optimized models is U8 (INT8 unsigned integer value).

.. _remote-calibration:

Remote Calibration
~~~~~~~~~~~~~~~~~~

Remote calibration is available only for configurations that use remote machines. To calibrate on a remote machine, follow the same workflow as for local calibration. However, remote calibration usually takes some more time due to data exchange between a host machine and a remote machine. Once inference on the remote machine is complete, the DL Workbench sends the calibrated model to the host machine and saves it there.

When you calibrate on a remote system, the progress bar first shows the progress for asset preparation and upload, and then for calibration and inference:



.. image:: remote_calibration_02.png

.. _devcloud-calibration:

Calibration in the Intel® DevCloud for the Edge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To calibrate on a platform from the :ref:`Intel® DevCloud for the Edge <doxid-workbench_docs__workbench__d_g__start__d_l__workbench_in__dev_cloud>`, follow the same workflow as for local calibration. However, calibration in the DevCloud usually takes some more time due to data exchange between a host machine and a remote machine.

When you calibrate in the DevCloud, the progress bar first shows the progress for asset preparation and upload, and then for calibration and inference:



.. image:: remote_calibration_02.png

See Also
~~~~~~~~

* :ref:`Compare Performance between Two Versions of a Model <doxid-workbench_docs__workbench__d_g__compare__performance_between__two__versions_of__models>`

* :ref:`Optimization Guide <doxid-openvino_docs_optimization_guide_dldt_optimization_guide>`

* :ref:`Post-Training Optimization Tool <doxid-pot_introduction>`

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

