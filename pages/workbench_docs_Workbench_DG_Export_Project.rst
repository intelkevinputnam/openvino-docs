.. index:: pair: page; Export Project
.. _doxid-workbench_docs__workbench__d_g__export__project:


Export Project
==============

:target:`doxid-workbench_docs__workbench__d_g__export__project_1md_openvino_workbench_docs_workbench_dg_export_project`

You can download an archive with artifacts of your project:

* Model

* Dataset

* Accuracy measurement configuration delivered as a valid configuration file for the `Accuracy Checker <https://docs.openvino.ai/latest/omz_tools_accuracy_checker.html>`__

* `Post-training Optimization Tool <https://docs.openvino.ai/latest/pot_README.html>`__ calibration configuration file

A downloaded archive also contains information on the project and best model performance.

The archive is organized as follows:

.. ref-code-block:: cpp

	|-- configs
	  |-- accuracy_config.yml
	  |-- calibration_config.json
	|-- dataset
	  |-- dataset.tar.gz
	|-- model 
	  |-- model.xml
	  |-- model.bin
	|-- description.txt

The example for the ``mobilenet-ssd`` model with a COCO dataset.

.. raw:: html

    <div class="collapsible-section">

.. ref-code-block:: cpp

	models:
	- name: mobilenet-ssd
	  launchers:
	  - framework: dlsdk
	    device: CPU
	    adapter:
	      type: ssd
	    batch: 1
	    model: /home/workbench/.workbench/models/3/16/mobilenet-ssd.xml
	    weights: /home/workbench/.workbench/models/3/16/mobilenet-ssd.bin
	  datasets:
	  - name: dataset
	    data_source: /home/workbench/.workbench/datasets/2
	    annotation_conversion:
	      annotation_file: /home/workbench/.workbench/datasets/2/instances_val2017_200pictures.json
	      converter: mscoco_detection
	      images_dir: /home/workbench/.workbench/datasets/2
	    subsample_size: 100%
	    preprocessing:
	    - type: resize
	      size: 300
	    postprocessing:
	    - type: resize_prediction_boxes
	    metrics:
	    - type: map
	      integral: 11point
	      ignore_difficult: true
	      presenter: print_vector

.. raw:: html

    </div>

The example is for the ``mobilenet-ssd`` model calibrated on a COCO dataset with Default method.

.. raw:: html

    <div class="collapsible-section">

.. ref-code-block:: cpp

	{
	   "model": {
	      "model_name": "mobilenet-ssd",
	      "model": "/home/workbench/.workbench/models/3/original/mobilenet-ssd.xml",
	      "weights": "/home/workbench/.workbench/models/3/original/mobilenet-ssd.bin"
	   },
	   "engine": {
	      "name": "mobilenet-ssd",
	      "launchers": [
	         {
	            "framework": "dlsdk",
	            "device": "CPU",
	            "adapter": {
	               "type": "ssd"
	            },
	            "batch": 1
	         }
	      ],
	      "datasets": [
	         {
	            "name": "dataset",
	            "data_source": "/home/workbench/.workbench/datasets/2",
	            "annotation_conversion": {
	               "annotation_file": "/home/workbench/.workbench/datasets/2/instances_val2017_200pictures.json",
	               "converter": "mscoco_detection",
	               "images_dir": "/home/workbench/.workbench/datasets/2"
	            },
	            "subsample_size": "100%",
	            "preprocessing": [
	               {
	                  "type": "resize",
	                  "size": 300
	               }
	            ],
	            "postprocessing": [
	               {
	                  "type": "resize_prediction_boxes"
	               }
	            ],
	            "metrics": [
	               {
	                  "type": "map",
	                  "integral": "11point",
	                  "ignore_difficult": true,
	                  "presenter": "print_vector"
	               }
	            ]
	         }
	      ]
	   },
	   "compression": {
	      "target_device": "CPU",
	      "algorithms": [
	         {
	            "name": "DefaultQuantization",
	            "params": {
	               "preset": "performance",
	               "stat_subset_size": 60
	            }
	         }
	      ]
	   }
	}

.. raw:: html

    </div>

The example of description.txt with information on the project, best model performance, corresponding performance reports, and the execution graph of the model on the device that you used in the project.

.. raw:: html

    <div class="collapsible-section">

.. ref-code-block:: cpp

	Model: mobilenet-ssd
	Dataset: coco200
	Device: CPU | Intel(R) Core(TM) i5-7300U CPU @ 2.60GHz
	Target: local | 127.0.0.1 | Local Workstation
	Optimized with :ref:`INT8 <doxid-namespace_inference_engine_1_1_metrics_1ad31c07cfba5d2d2859af67742ca5a89b>` Calibration: Yes
	Corresponding latency: <latency value>
	Best :ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>` FPS: <FPS value>
	Best :ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>` batch configuration: 1
	Best :ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>` stream configuration: 1
	DL Workbench version: 2022.1
	
	Accuracy Checker version: 0.8.6
	Post-training Optimization Tool version: 1.0

.. raw:: html

    </div>

If you submit a ticket about model support to the `OpenVINO™ team <https://github.com/openvinotoolkit/openvino/issues>`__, it is highly recommended to attach the model and its execution graph, which you can obtain on this tab.

To export a project, follow the steps below.

#. Go to the **Perform** tab on the **Projects** page. Open the **Export Project** subtab.

#. Check the items you want to include. You cannot export project-related information without including at least one element to the package.

#. Click Export. The exporting process starts on the server followed by an automatic archive download.

Below is an example of a project being ready for export. In this example, the model, accuracy configuration, and calibration configuration will be included in the export package, while the package will not contain the dataset.

.. image:: export_project.png

See Also
~~~~~~~~

* `OpenVINO™ team GitHub issues <https://github.com/openvinotoolkit/openvino/issues>`__

* `DL Workbench on Intel Community Forum <https://community.intel.com/t5/Intel-Distribution-of-OpenVINO/bd-p/distribution-openvino-toolkit>`__

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

