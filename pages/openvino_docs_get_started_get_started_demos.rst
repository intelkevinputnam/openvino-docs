.. index:: pair: page; Get Started with Sample and Demo Applications
.. _doxid-openvino_docs_get_started_get_started_demos:


Get Started with Sample and Demo Applications
=============================================

:target:`doxid-openvino_docs_get_started_get_started_demos_1md_openvino_docs_get_started_get_started_demos`

Introduction
~~~~~~~~~~~~

This section guides you through a simplified workflow for the Intel® Distribution of OpenVINO™ toolkit using code samples and demo applications. You will perform the following steps:

#. `Use the Model Downloader to download suitable models. <#download-models>`__

#. `Convert the models with the Model Optimizer. <#convert-models-to-intermediate-representation>`__

#. `Download media files to run inference on. <#download-media>`__

#. `Run inference on the sample and see the results: <#run-image-classification>`__
   
   * `Image Classification Code Sample <#run-image-classification>`__

This guide assumes you completed all installation and configuration steps. If you have not yet installed and configured the toolkit:

.. tab:: Linux

   See :doc:`Install Intel® Distribution of OpenVINO™ toolkit for Linux* <openvino_docs_install_guides_installing_openvino_linux>`

.. tab:: Windows

   See :doc:`Install Intel® Distribution of OpenVINO™ toolkit for Windows* <openvino_docs_install_guides_installing_openvino_windows>`

.. tab:: macOS

   See :doc:`Install Intel® Distribution of OpenVINO™ toolkit for macOS* <openvino_docs_install_guides_installing_openvino_macos>`

Install OpenVINO Development Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install OpenVINO Development Tools for working with Caffe\* models, use the following command:

.. ref-code-block:: cpp

	pip install openvino-dev[caffe]

Build Samples and Demos
~~~~~~~~~~~~~~~~~~~~~~~

If you have already built the demos and samples, you can skip this section. The build will take about 5-10 minutes, depending on your system.

To build OpenVINO samples:

.. tab:: Linux

   Go to the :doc:`OpenVINO Samples page <openvino_docs_OV_UG_Samples_Overview>` and see the "Build the Sample Applications on Linux*" section.

.. tab:: Windows

   Go to the :doc:`OpenVINO Samples page <openvino_docs_OV_UG_Samples_Overview>` and see the "Build the Sample Applications on Microsoft Windows* OS" section.

.. tab:: macOS

   Go to the :doc:`OpenVINO Samples page <openvino_docs_OV_UG_Samples_Overview>` and see the "Build the Sample Applications on macOS*" section.

To build OpenVINO demos:




.. tab:: Linux

   Go to the :doc:`Open Model Zoo Demos page <omz_demos>` and see the "Build the Demo Applications on Linux*" section.

.. tab:: Windows

   Go to the :doc:`Open Model Zoo Demos page <omz_demos>` and see the "Build the Demo Applications on Microsoft Windows* OS" section.

.. tab:: macOS

   Go to the :doc:`Open Model Zoo Demos page <omz_demos>` and see the "Build the Demo Applications on Linux*" section. You can use the requirements from "To build OpenVINO samples" above and adapt the Linux build steps for macOS*.

.. _download-models:

Step 1: Download the Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You must have a model that is specific for your inference task. Example model types are:

* Classification (AlexNet, GoogleNet, SqueezeNet, others): Detects one type of element in an image

* Object Detection (SSD, YOLO): Draws bounding boxes around multiple types of objects in an image

* Custom: Often based on SSD

Options to find a model suitable for the OpenVINO™ toolkit:

* Download public or Intel pre-trained models from the `Open Model Zoo <https://github.com/openvinotoolkit/open_model_zoo>`__ using the Model Downloader tool

* Download from GitHub\*, Caffe\* Zoo, TensorFlow\* Zoo, etc.

* Train your own model with machine learning tools

This guide uses the OpenVINO™ Model Downloader to get pre-trained models. You can use one of the following commands to find a model:

* List the models available in the downloader

.. ref-code-block:: cpp

	omz_info_dumper --print_all

* Use ``grep`` to list models that have a specific name pattern

.. ref-code-block:: cpp

	omz_info_dumper --print_all | grep <model_name>

* Use Model Downloader to download models.
  
  This guide uses ``<models_dir>`` and ``<models_name>`` as placeholders for the models directory and model name:

.. ref-code-block:: cpp

	omz_downloader --name <model_name> --output_dir <models_dir>

* Download the following models to run the Image Classification Sample:

.. list-table::
    :header-rows: 1

    * - Model Name
      - Code Sample or Demo App
    * - ``googlenet-v1``
      - Image Classification Sample

.. raw:: html

   <div class="collapsible-section" data-title="Click for an example of downloading the GoogleNet v1 Caffe* model">

To download the GoogleNet v1 Caffe\* model to the ``models`` folder:

.. tab:: Linux

   .. code-block:: sh

      omz_downloader --name googlenet-v1 --output_dir ~/models

.. tab:: Windows

   .. code-block:: bat

      omz_downloader --name googlenet-v1 --output_dir %USERPROFILE%\Documents\models

.. tab:: macOS

   .. code-block:: sh

      omz_downloader --name googlenet-v1 --output_dir ~/models

Your screen looks similar to this after the download and shows the paths of downloaded files:

.. tab:: Linux

   .. code-block:: sh

      ###############|| Downloading models ||###############

      ========= Downloading /home/username/models/public/googlenet-v1/googlenet-v1.prototxt

      ========= Downloading /home/username/models/public/googlenet-v1/googlenet-v1.caffemodel
      ... 100%, 4834 KB, 3157 KB/s, 1 seconds passed

      ###############|| Post processing ||###############

      ========= Replacing text in /home/username/models/public/googlenet-v1/googlenet-v1.prototxt =========

.. tab:: Windows

   .. code-block:: bat

      ################|| Downloading models ||################

      ========== Downloading C:\Users\username\Documents\models\public\googlenet-v1\googlenet-v1.prototxt
      ... 100%, 9 KB, ? KB/s, 0 seconds passed

      ========== Downloading C:\Users\username\Documents\models\public\googlenet-v1\googlenet-v1.caffemodel
      ... 100%, 4834 KB, 571 KB/s, 8 seconds passed

      ################|| Post-processing ||################

      ========== Replacing text in C:\Users\username\Documents\models\public\googlenet-v1\googlenet-v1.prototxt

.. tab:: macOS

   .. code-block:: sh

      ###############|| Downloading models ||###############

      ========= Downloading /Users/username/models/public/googlenet-v1/googlenet-v1.prototxt
      ... 100%, 9 KB, 44058 KB/s, 0 seconds passed

      ========= Downloading /Users/username/models/public/googlenet-v1/googlenet-v1.caffemodel
      ... 100%, 4834 KB, 4877 KB/s, 0 seconds passed

      ###############|| Post processing ||###############

      ========= Replacing text in /Users/username/models/public/googlenet-v1/googlenet-v1.prototxt =========

.. raw:: html

   </div>

.. _convert-models-to-intermediate-representation:

Step 2: Convert the Model with Model Optimizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this step, your trained models are ready to run through the Model Optimizer to convert them to the IR (Intermediate Representation) format. For most model types, this is required before using the OpenVINO Runtime with the model.

Models in the IR format always include an ``.xml`` and ``.bin`` file and may also include other files such as ``.json`` or ``.mapping``. Make sure you have these files together in a single directory so the OpenVINO Runtime can find them.

REQUIRED: ``model_name.xml`` REQUIRED: ``model_name.bin`` OPTIONAL: ``model_name.json``, ``model_name.mapping``, etc.

This tutorial uses the public GoogleNet v1 Caffe\* model to run the Image Classification Sample. See the example in the Download Models section of this page to learn how to download this model.

The googlenet-v1 model is downloaded in the Caffe\* format. You must use the Model Optimizer to convert the model to IR.

Create an ``<ir_dir>`` directory to contain the model's Intermediate Representation (IR).

.. tab:: Linux

   .. code-block:: sh

      mkdir ~/ir

.. tab:: Windows

   .. code-block:: bat

      mkdir %USERPROFILE%\Documents\ir

.. tab:: macOS

   .. code-block:: sh

      mkdir ~/ir

The OpenVINO Runtime can infer models where floating-point weights are :ref:`compressed to FP16 <doxid-openvino_docs__m_o__d_g__f_p16__compression>`. To generate an IR with a specific precision, run the Model Optimizer with the appropriate ``--data_type`` option.

Generic Model Optimizer script:

.. ref-code-block:: cpp

	mo --input_model <model_dir>/<model_file> --data_type <model_precision> --output_dir <ir_dir>

IR files produced by the script are written to the <ir_dir> directory.

The command with most placeholders filled in and FP16 precision:

.. tab:: Linux

   .. code-block:: sh

      mo --input_model ~/models/public/googlenet-v1/googlenet-v1.caffemodel --data_type FP16 --output_dir ~/ir

.. tab:: Windows

   .. code-block:: bat

      mo --input_model %USERPROFILE%\Documents\models\public\googlenet-v1\googlenet-v1.caffemodel --data_type FP16 --output_dir %USERPROFILE%\Documents\ir

.. tab:: macOS

   .. code-block:: sh

      mo --input_model ~/models/public/googlenet-v1/googlenet-v1.caffemodel --data_type FP16 --output_dir ~/ir

.. _download-media:

Step 3: Download a Video or Still Photo as Media
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many sources are available from which you can download video media to use the code samples and demo applications. Possibilities include:

* `Pexels <https://pexels.com>`__

* `Google Images <https://images.google.com>`__

As an alternative, the Intel® Distribution of OpenVINO™ toolkit includes several sample images and videos that you can use for running code samples and demo applications:

* `Sample images and video <https://storage.openvinotoolkit.org/data/test_data/>`__

* `Sample videos <https://github.com/intel-iot-devkit/sample-videos>`__

.. _run-image-classification:

Step 4: Run Inference on the Sample
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the Image Classification Code Sample
----------------------------------------

To run the **Image Classification** code sample with an input image using the IR model:

#. Set up the OpenVINO environment variables:
   
   
   
   
   .. tab:: Linux
   
      .. code-block:: sh
   
         source  <INSTALL_DIR>/setupvars.sh
   
   .. tab:: Windows
   
      .. code-block:: bat
   
         <INSTALL_DIR>\setupvars.bat
   
   .. tab:: macOS
   
      .. code-block:: sh
   
         source <INSTALL_DIR>/setupvars.sh

#. Go to the code samples release directory created when you built the samples earlier:
   
   
   
   
   .. tab:: Linux
   
      .. code-block:: sh
   
         cd ~/inference_engine_cpp_samples_build/intel64/Release
   
   .. tab:: Windows
   
      .. code-block:: bat
   
         cd  %USERPROFILE%\Documents\Intel\OpenVINO\inference_engine_samples_build\intel64\Release
   
   .. tab:: macOS
   
      .. code-block:: sh
   
         cd ~/inference_engine_cpp_samples_build/intel64/Release

#. Run the code sample executable, specifying the input media file, the IR for your model, and a target device for performing inference:

.. tab:: Linux

   .. code-block:: sh

      classification_sample_async -i <path_to_media> -m <path_to_model> -d <target_device>

.. tab:: Windows

   .. code-block:: bat

      classification_sample_async.exe -i <path_to_media> -m <path_to_model> -d <target_device>

.. tab:: macOS

   .. code-block:: sh

      classification_sample_async -i <path_to_media> -m <path_to_model> -d <target_device>

.. raw:: html

   <div class="collapsible-section" data-title="Click for examples of running the Image Classification code sample on different devices">

The following commands run the Image Classification Code Sample using the `dog.bmp <https://storage.openvinotoolkit.org/data/test_data/images/224x224/dog.bmp>`__ file as an input image, the model in IR format from the ``ir`` directory, and on different hardware devices:

**CPU:**






.. tab:: Linux

   .. code-block:: sh

      ./classification_sample_async -i ~/Downloads/dog.bmp -m ~/ir/googlenet-v1.xml -d CPU

.. tab:: Windows

   .. code-block:: bat

      .\classification_sample_async.exe -i %USERPROFILE%\Downloads\dog.bmp -m %USERPROFILE%\Documents\ir\googlenet-v1.xml -d CPU

.. tab:: macOS

   .. code-block:: sh

      ./classification_sample_async -i ~/Downloads/dog.bmp -m ~/ir/googlenet-v1.xml -d CPU

**GPU:**

.. note:: Running inference on Intel® Processor Graphics (GPU) requires :ref:`additional hardware configuration steps <doxid-openvino_docs_install_guides_configurations_for_intel_gpu>`, as described earlier on this page. Running on GPU is not compatible with macOS\*.

.. tab:: Linux

   .. code-block:: sh

      ./classification_sample_async -i ~/Downloads/dog.bmp -m ~/ir/googlenet-v1.xml -d GPU

.. tab:: Windows

   .. code-block:: bat

      .\classification_sample_async.exe -i %USERPROFILE%\Downloads\dog.bmp -m %USERPROFILE%\Documents\ir\googlenet-v1.xml -d GPU

**MYRIAD:**

.. note:: Running inference on VPU devices (Intel® Movidius™ Neural Compute Stick or Intel® Neural Compute Stick 2) with the MYRIAD plugin requires :ref:`additional hardware configuration steps <doxid-openvino_docs_install_guides_configurations_for_ncs2>`, as described earlier on this page.

.. tab:: Linux

   .. code-block:: sh

      ./classification_sample_async -i ~/Downloads/dog.bmp -m ~/ir/googlenet-v1.xml -d MYRIAD

.. tab:: Windows

   .. code-block:: bat

      .\classification_sample_async.exe -i %USERPROFILE%\Downloads\dog.bmp -m %USERPROFILE%\Documents\ir\googlenet-v1.xml -d MYRIAD

.. tab:: macOS

   .. code-block:: sh

      ./classification_sample_async -i ~/Downloads/dog.bmp -m ~/ir/googlenet-v1.xml -d MYRIAD

When the sample application is complete, you see the label and confidence for the top 10 categories on the display. Below is a sample output with inference results on CPU:

.. code-block:: sh

   Top 10 results:

   Image dog.bmp

      classid probability label
      ------- ----------- -----
      156     0.6875963   Blenheim spaniel
      215     0.0868125   Brittany spaniel
      218     0.0784114   Welsh springer spaniel
      212     0.0597296   English setter
      217     0.0212105   English springer, English springer spaniel
      219     0.0194193   cocker spaniel, English cocker spaniel, cocker
      247     0.0086272   Saint Bernard, St Bernard
      157     0.0058511   papillon
      216     0.0057589   clumber, clumber spaniel
      154     0.0052615   Pekinese, Pekingese, Peke

.. raw:: html

   </div>

Other Demos/Samples
~~~~~~~~~~~~~~~~~~~

For more samples and demos, you can visit the samples and demos pages below. You can review samples and demos by complexity or by usage, run the relevant application, and adapt the code for your use.

:ref:`Samples <doxid-openvino_docs__o_v__u_g__samples__overview>`

Demos

