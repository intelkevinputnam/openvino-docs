.. index:: pair: page; Build Your Application with Deployment Package
.. _doxid-workbench_docs__workbench__d_g__deployment__package:


Build Your Application with Deployment Package
==============================================

:target:`doxid-workbench_docs__workbench__d_g__deployment__package_1md_openvino_workbench_docs_workbench_dg_deployment_package`





.. toctree::
   :maxdepth: 1
   :hidden:

   workbench_docs_Workbench_DG_Deploy_and_Integrate_Performance_Criteria_into_Application

When you find an optimal configuration for your model, the next step is to use this model with optimal parameters in your own application on a target device. OpenVINO™ toolkit includes all you need to run the application on the target. However, the target might have a limited drive space to store all OpenVINO™ components. OpenVINO™ :ref:`Deployment Manager <doxid-openvino_docs_install_guides_deployment_manager_tool>` available inside the DL Workbench extracts the minimum set of libraries required for a target device.

.. warning:: Deployment Manager available inside the DL Workbench provides libraries compatible with Ubuntu 18.04 and 20.04.

Refer to the section below to learn how to download a deployment package for your configuration. Once you download the package, see how to `create a binary with your application <#sample>`__ on your developer machine and `deploy it on a target device <#deploy>`__.

.. note:: *Developer machine* is the machine where you use the DL Workbench to download the package and where you prepare your own application. *Target machine* is the machine where you deploy the application.

Download Deployment Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: Perform these steps on your developer machine.

Go to the **Perform** tab on the **Projects** page and open the **Create Deployment Package** subtab.

.. image:: export_package.png

In this tab, select all the targets you want to apply your model to. You can also opt whether to include the model, Python API, and installation scripts. Python API enables the OpenVINO™ Runtime to work in Python scripts. You can then import the Python API into your own scripts and use IE via it. Installation scripts install OpenVINO™ dependencies and drivers for selected targets, if needed.

The package size displayed at the bottom of the form changes depending on your selection. If you do not include the model in the package, the archive contains only libraries for selected plugins.

Once you click **Pack**, the packaging process starts on the server followed by an automatic archive download:

.. image:: package_status.png

Now you have an archive that contains the required libraries and your model.

.. warning:: * The archive does not contain your application, and copying the archive to the target device does not mean deployment.

* The archive contains C++\* libraries, so your application can be written in C++ only. A Python\* application cannot use these libraries directly and Python bindings are not included in the deployment package. This document does not contain instructions on how to prepare a Python application for deployment.

Your application should be compiled into a binary file. If you do not have an application, see `Create Binary Sample <#sample>`__. The next step is `moving a binary to the target device and deploying it there <#deploy>`__.

.. _sample:

Create Binary Sample
~~~~~~~~~~~~~~~~~~~~

You can learn how to use batches and streams in your application with DL Workbench :ref:`C++ Sample Application <doxid-workbench_docs__workbench__d_g__deploy_and__integrate__performance__criteria_into__application>`.

.. note:: Perform these steps on your developer machine.

Prerequisite
------------

:ref:`Install the Intel® Distribution of OpenVINO™ toolkit for Linux\* <doxid-openvino_docs_install_guides_installing_openvino_linux>` on your developer machine. OpenVINO™ toolkit and DL Workbench should be of the same release version.

Step 1. Create main.cpp
-----------------------

Create a file named ``main.cpp`` with the source code of your application:

.. raw:: html

    <div class="collapsible-section">

.. ref-code-block:: cpp

	#include <inference_engine.hpp>
	#include <vector>
	
	using namespace :ref:`InferenceEngine <doxid-namespace_inference_engine>`;
	
	int main(int argc, char \*argv[]) {
	    if (argc < 3) {
	        std::cerr << "Usage: " << argv[0] << " PATH_TO_MODEL_XML DEVICE" << std::endl;
	        return 1;
	    }
	
	    int batchSize = 1;
	
	    int numInferReq = 1;
	
	    if (argc == 5) {
	
	        batchSize = std::stoi(argv[3]);
	
	        numInferReq = std::stoi(argv[4]);
	    }
	
	    const std::string modelXml = argv[1];
	
	    std::string device = argv[2];
	
	    std::transform(device.begin(), device.end(), device.begin(), ::toupper);
	
	    :ref:`Core <doxid-class_inference_engine_1_1_core>` :ref:`ie <doxid-namespace_inference_engine>`;
	
	    // Start setting number of streams
	    int numStreams = numInferReq;
	
	    if (device == "CPU") {
	        :ref:`ie <doxid-namespace_inference_engine>`.SetConfig({{:ref:`CONFIG_KEY <doxid-ie__plugin__config_8hpp_1aad09cfba062e8ec9fb7ab9383f656ec7>`(CPU_THROUGHPUT_STREAMS), std::to_string(numStreams)}}, device);
	    }
	
	    if (device == "GPU") {
	        numStreams = numInferReq / 2;
	        if (numStreams % 2) {
	            numStreams++;
	        }
	        :ref:`ie <doxid-namespace_inference_engine>`.SetConfig({{:ref:`CONFIG_KEY <doxid-ie__plugin__config_8hpp_1aad09cfba062e8ec9fb7ab9383f656ec7>`(GPU_THROUGHPUT_STREAMS), std::to_string(numStreams)}}, device);
	    }
	    // Finish setting number of streams
	
	    :ref:`CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` network = :ref:`ie <doxid-namespace_inference_engine>`.ReadNetwork(modelXml);
	
	    // Set batch
	    network.:ref:`setBatchSize <doxid-class_inference_engine_1_1_c_n_n_network_1a8e9d19270a48aab50cb5b1c43eecb8e9>`(batchSize);
	
	    :ref:`ExecutableNetwork <doxid-class_inference_engine_1_1_executable_network>` executableNetwork = :ref:`ie <doxid-namespace_inference_engine>`.LoadNetwork(network, device);
	
	    std::vector<InferRequest> requests(numInferReq);
	
	    for (std::size_t i = 0; i < numInferReq; i++) {
	        // Create an InferRequest
	        requests[i] = executableNetwork.CreateInferRequest();
	        // run the InferRequest
	        requests[i].StartAsync();
	    }
	
	    for (std::size_t i = 0; i < numInferReq; i++){
	        :ref:`StatusCode <doxid-namespace_inference_engine_1a2ce897aa6a353c071958fe379f5d6421>` status = requests[i].Wait(IInferRequest::WaitMode::RESULT_READY);
	        if (status != :ref:`StatusCode::OK <doxid-namespace_inference_engine_1a2ce897aa6a353c071958fe379f5d6421a084fcaf510851d3281e7bd45db802c6a>`){
	            std::cout<< "inferRequest " << i << "failed" << std::endl;
	        }
	    }
	    std::cout << "Inference completed successfully"<<std::endl;
	    return 0;
	}

.. raw:: html

    </div>

Step 2. Create CMakeLists.txt
-----------------------------

In the same folder as ``main.cpp``, create a file named ``CMakeLists.txt`` with the following commands to compile ``main.cpp`` into an executable file:

.. raw:: html

    <div class="collapsible-section">

.. ref-code-block:: cpp

	cmake_minimum_required(VERSION 3.10)
	
	project(ie_sample)
	
	set(CMAKE_CXX_STANDARD 14)
	
	set(IE_SAMPLE_NAME ie_sample)
	
	find_package(InferenceEngine 2.1 REQUIRED)
	
	add_executable(${IE_SAMPLE_NAME} main.cpp ${IE_SAMPLE_SOURCES} ${IE_SAMPLES_HEADERS})
	
	target_link_libraries(${IE_SAMPLE_NAME} PUBLIC ${InferenceEngine_LIBRARIES})

.. raw:: html

    </div>

Step 3. Compile Application
---------------------------

Open a terminal in the directory with ``main.cpp`` and ``CMakeLists.txt``, and run the following commands to build the sample:



.. ref-code-block:: cpp

	source <INSTALL_OPENVINO_DIR>/setupvars.sh
	mkdir build
	cd build
	cmake ../
	make

.. note:: Replace ``<INSTALL_OPENVINO_DIR>`` with the directory where you installed the OpenVINO™ package. By default, the package is installed in ``/opt/intel/openvino`` or ``~/intel/openvino``.



Once the commands are executed, find the ``ie_sample`` binary in the ``build`` folder in the directory with the source files.

.. _deploy:

Deploy Your Application on Target Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Step 1.** Make sure you have the following components on your developer machine:

* Deployment package

* Model (if it is not included in the package)

* Binary file with your application, ``ie_sample``, for example

**Step 2.** Unarchive the deployment package. Place the binary and the model in the ``deployment_package`` folder as follows:

.. ref-code-block:: cpp

	|-- deployment_package
	    |-- bin
	    |-- deployment_tools
	    |-- install_dependencies
	    |-- model
	        |-- model.xml
	        |-- model.bin
	    |-- ie_sample

**Step 3.** Archive the ``deployment_package`` folder and copy it to the target machine.

.. note:: Perform the steps below on your target machine.

**Step 4.** Open a terminal in the ``deployment_package`` folder on the target machine.

**Step 5.** Optional: for inference on Intel® GPU, Intel® Movidius™ VPU, or Intel® Vision Accelerator Design with Intel® Movidius™ VPUs targets.

Install dependencies by running the ``install_openvino_dependencies.sh`` script:

.. ref-code-block:: cpp

	sudo -E ./install_dependencies/install_openvino_dependencies.sh

**Step 6.** Set up the environment variables by running ``setupvars.sh`` :

.. ref-code-block:: cpp

	source ./setupvars.sh

**Step 7.** Run your application:

.. ref-code-block:: cpp

	./ie_sample  <path>/<model>.xml CPU

**NOTES** :

* Replace ``<path>`` and ``<model>`` with the path to your model and its name.

* In the command above, the application is run on a CPU device. See the **Supported Inference Devices** section of :ref:`Install DL Workbench <doxid-workbench_docs__workbench__d_g__install>` for code names of other devices.

**Step 8.** If you run the application created in the `Create Binary Sample <#sample>`__, you get the following output:

.. ref-code-block:: cpp

	Inference completed successfully

See Also
~~~~~~~~

* :ref:`Deploy and Integrate Performance Criteria into Application <doxid-workbench_docs__workbench__d_g__deploy_and__integrate__performance__criteria_into__application>`

* :ref:`Deployment Manager Guide <doxid-openvino_docs_install_guides_deployment_manager_tool>`

* :ref:`Integrate the OpenVINO™ Runtime with Your Application <doxid-openvino_docs__o_v__u_g__integrate__o_v_with_your_application>`

* :ref:`Troubleshooting <doxid-workbench_docs__workbench__d_g__troubleshooting>`

