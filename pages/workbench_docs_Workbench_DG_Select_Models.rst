.. index:: pair: page; Obtain Models
.. _doxid-workbench_docs__workbench__d_g__select__models:


Obtain Models
=============

:target:`doxid-workbench_docs__workbench__d_g__select__models_1md_openvino_workbench_docs_workbench_dg_select_models`





.. toctree::
   :maxdepth: 1
   :hidden:

   workbench_docs_Workbench_DG_OMZ_Models
   workbench_docs_Workbench_DG_Original_Model_Import

In the DL Workbench, you can import original and the Open Model Zoo (OMZ) models. Click **Create Project** on the Start Page to import a model or select **Explore 100+ OMZ Models** to upload a model from Open Model Zoo.

.. panels::

    Import your original model to start experiments in the DL Workbench and maximize the performance. 

    +++

    .. link-button:: workbench_docs_Workbench_DG_Original_Model_Import
        :type: ref
        :text: Import original models
        :classes: btn-outline-primary btn-block stretched-link 

    ---

    Import models from OpenVINO Open Model Zoo (OMZ) in a quick intuitive way to get started with the pretrained high-quality models (100+).

    +++

    .. link-button:: workbench_docs_Workbench_DG_OMZ_Models
        :type: ref
        :text: Import OMZ models
        :classes: btn-outline-primary btn-block stretched-link

Once you have imported a model, you are redirected to the **Create Project** page, where you can select the imported model and proceed to :ref:`select a dataset <doxid-workbench_docs__workbench__d_g__generate__datasets>`.

You can find all imported models on the **Start Page** :

.. image:: start_page_models.png

Supported Frameworks
~~~~~~~~~~~~~~~~~~~~

DL Workbench supports the following frameworks whether uploaded from a local folder or imported from the Open Model Zoo.

.. list-table::
    :header-rows: 1

    * - Framework
      - Original Models
      - Open Model Zoo
    * - OpenVINO™
      - ✔
      - ✔
    * - TensorFlow\*
      - ✔
      - ✔
    * - MXNet\*
      - ✔
      - ✔
    * - ONNX\*
      - ✔
      - ✔
    * - Caffe\*
      - ✔
      - ✔
    * - PyTorch\*
      - 
      - ✔

See Also
~~~~~~~~

* :ref:`Open Model Zoo <doxid-model_zoo>`

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

