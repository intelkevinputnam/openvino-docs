.. index:: pair: page; Import Model
.. _doxid-workbench_docs__workbench__d_g__select__model:


Import Model
============

:target:`doxid-workbench_docs__workbench__d_g__select__model_1md_openvino_workbench_docs_workbench_dg_select_model` This document describes the first part of :ref:`Get Started with DL Workbench <doxid-workbench_docs__workbench__d_g__work_with__models_and__sample__datasets>` workflow, following the model import steps from the Create Project video.

.. list-table::

   * - .. raw:: html

           <iframe  allowfullscreen mozallowfullscreen msallowfullscreen oallowfullscreen webkitallowfullscreen height="315" width="560"
           src="https://www.youtube.com/embed/gzUFYxomjn8">
           </iframe>
   * - **Get Started with the DL Workbench**. Duration: 8:27

To start working with DL Workbench, you need to obtain a model. A model is a neural network that has been trained over a set of data using a certain frameworks, such as TensorFlow, ONNX, Caffe, MXNet, and others.

.. image:: obtain_model.png

There are two ways to import a model in DL Workbench:

* Select a model from the Open Model Zoo. Open Model Zoo includes a set of high-quality pretrained Deep Learning `public <https://docs.openvinotoolkit.org/latest/omz_models_group_public.html>`__ and `Intel-trained <https://docs.openvinotoolkit.org/latest/omz_models_group_intel.html>`__ models for different use cases, such as classification, object detection, segmentation and many others.

* Import your :ref:`original model <doxid-workbench_docs__workbench__d_g__select__models>`. Upload the files and start the import if you have a model pretrained in one of the supported frameworks or you already have an Intermediate Representation(IR) model.

This document focuses on importing a model from the Open Model Zoo. If you want to learn about importing original model, see the :ref:`Obtain Models <doxid-workbench_docs__workbench__d_g__select__models>` page.

Download Model
~~~~~~~~~~~~~~

First, you need to select a model. Click **Explore 100+ OMZ Models** on the start page.

.. image:: start_page_crop.png

This guide uses ``ssd_mobilenet_v2_coco`` SSD `model <https://docs.openvinotoolkit.org/latest/omz_models_model_ssd_mobilenet_v2_coco.html>`__ for `object detection <https://machinelearningmastery.com/object-recognition-with-deep-learning/>`__ use case, pretrained with `TensorFlow\* <https://www.tensorflow.org/>`__ framework. Type the name in the search, select the model and click **Download and Import**. During this step, you can also inspect the model details.

.. image:: import_model_mobilenet.png

Convert Model
~~~~~~~~~~~~~

To work with DL Workbench, you need to obtain a model in the Intermediate Representation (IR) format. Specify the precision in which model weights should be stored to convert the selected TensorFlow model to IR. You can select either 32-bit (FP32) or 16-bit (FP16) floating-point values. In this tutorial we choose FP16, as it keeps good accuracy and provides smaller footprint. Select the precision and click **Convert**.

.. image:: convert_model_mobilenet.png

You will be redirected to the **Create Project** page, where you can check the import status.

.. image:: mobilenet_imported.png

You have completed the first part of :ref:`Get Started with DL Workbench <doxid-workbench_docs__workbench__d_g__work_with__models_and__sample__datasets>` guide. The next step is to :ref:`create a project <doxid-workbench_docs__workbench__create__project>`. Before creating a project, you can find out how your model works on test images.

Optional. Visualize Model
~~~~~~~~~~~~~~~~~~~~~~~~~

To check your model and explore its properties, click **Open** under the **Actions** column.

.. image:: actions.png

The **Model Page** will open. You can also access this page from the **Start Page** where all imported models are displayed:

.. image:: mobilenet_start_page.png

On this page you can see the list of available model projects, visualize the model structure and output, read information about theoretical analysis, conversion settings, and accuracy configurations.

.. image:: mobilenet_model_page.png

Drag and drop your image to evaluate the model performance:

.. image:: mobilenet_visualization.png

*All images were taken from Common Objects in Context datasets for demonstration purposes only.*

See Also
~~~~~~~~

* :ref:`Next Step: Create Project <doxid-workbench_docs__workbench__create__project>`

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

