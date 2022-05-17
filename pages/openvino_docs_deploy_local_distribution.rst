.. index:: pair: page; Local distribution
.. _doxid-openvino_docs_deploy_local_distribution:


Local distribution
==================

:target:`doxid-openvino_docs_deploy_local_distribution_1md_openvino_docs_ov_runtime_ug_deployment_local-distribution` The local distribution implies that each C or C++ application / installer will have its own copies of OpenVINO Runtime binaries. However, OpenVINO has a scalable plugin-based architecture which implies that some components can be loaded in runtime only if they are really needed. So, it is important to understand which minimal set of libraries is really needed to deploy the application and this guide helps to achieve this goal.

.. note:: The steps below are operation system independent and refer to a library file name without any prefixes (like ``lib`` on Unix systems) or suffixes (like ``.dll`` on Windows OS). Do not put ``.lib`` files on Windows OS to the distribution, because such files are needed only on a linker stage.

Local dsitribution is also appropriate for OpenVINO binaries built from sources using `Build instructions <https://github.com/openvinotoolkit/openvino/wiki#how-to-build>`__, but the guide below supposes OpenVINO Runtime is built dynamically. For case of `Static OpenVINO Runtime <https://github.com/openvinotoolkit/openvino/wiki/StaticLibraries>`__ select the required OpenVINO capabilities on CMake configuration stage using `CMake Options for Custom Compilation <https://github.com/openvinotoolkit/openvino/wiki/CMakeOptionsForCustomCompilation>`__, the build and link the OpenVINO components into the final application.

C++ or C language
-----------------

Independently on language used to write the application, ``openvino`` must always be put to the final distribution since is a core library which orshectrates with all the inference and frontend plugins. If your application is written with C language, then you need to put ``openvino_c`` additionally.

The ``plugins.xml`` file with information about inference devices must also be taken as support file for ``openvino``.

.. note:: in Intel Distribution of OpenVINO, ``openvino`` depends on TBB libraries which are used by OpenVINO Runtime to optimally saturate the devices with computations, so it must be put to the distribution package

Pluggable components
--------------------

The picture below demonstrates dependnecies between the OpenVINO Runtime core and pluggable libraries:

.. image:: deployment_full.png

Compute devices
+++++++++++++++

For each inference device, OpenVINO Runtime has its own plugin library:

* ``openvino_intel_cpu_plugin`` for :ref:`Intel CPU devices <doxid-openvino_docs__o_v__u_g_supported_plugins__c_p_u>`

* ``openvino_intel_gpu_plugin`` for :ref:`Intel GPU devices <doxid-openvino_docs__o_v__u_g_supported_plugins__g_p_u>`

* ``openvino_intel_gna_plugin`` for :ref:`Intel GNA devices <doxid-openvino_docs__o_v__u_g_supported_plugins__g_n_a>`

* ``openvino_intel_myriad_plugin`` for :ref:`Intel MYRIAD devices <doxid-openvino_docs__o_v__u_g_supported_plugins__m_y_r_i_a_d>`

* ``openvino_intel_hddl_plugin`` for :ref:`Intel HDDL device <doxid-openvino_docs__o_v__u_g_supported_plugins__h_d_d_l>`

* ``openvino_arm_cpu_plugin`` for :ref:`ARM CPU devices <doxid-openvino_docs__o_v__u_g_supported_plugins__a_r_m__c_p_u>`

Depending on what devices is used in the app, put the appropriate libraries to the distribution package.

As it is shown on the picture above, some plugin libraries may have OS-specific dependencies which are either backend libraries or additional supports files with firmware, etc. Refer to the table below for details:

.. raw:: html

    <div class="collapsible-section" data-title="Windows OS: Click to expand/collapse">

.. list-table::
    :header-rows: 1

    * - Device
      - Dependency
    * - CPU
      - ``-``
    * - GPU
      - ``OpenCL.dll`` , ``cache.json``
    * - MYRIAD
      - ``usb.dll`` , ``usb-ma2x8x.mvcmd`` , ``pcie-ma2x8x.elf``
    * - HDDL
      - ``bsl.dll`` , ``hddlapi.dll`` , ``json-c.dll`` , ``libcrypto-1_1-x64.dll`` , ``libssl-1_1-x64.dll`` , ``mvnc-hddl.dll``
    * - GNA
      - ``gna.dll``
    * - Arm® CPU
      - ``-``

.. raw:: html

    </div>









.. raw:: html

    <div class="collapsible-section" data-title="Linux OS: Click to expand/collapse">

.. list-table::
    :header-rows: 1

    * - Device
      - Dependency
    * - CPU
      - ``-``
    * - GPU
      - ``libOpenCL.so`` , ``cache.json``
    * - MYRIAD
      - ``libusb.so`` , ``usb-ma2x8x.mvcmd`` , ``pcie-ma2x8x.mvcmd``
    * - HDDL
      - ``libbsl.so`` , ``libhddlapi.so`` , ``libmvnc-hddl.so``
    * - GNA
      - ``gna.dll``
    * - Arm® CPU
      - ``-``

.. raw:: html

    </div>









.. raw:: html

    <div class="collapsible-section" data-title="MacOS: Click to expand/collapse">

.. list-table::
    :header-rows: 1

    * - Device
      - Dependency
    * - CPU
      - ``-``
    * - MYRIAD
      - ``libusb.dylib`` , ``usb-ma2x8x.mvcmd`` , ``pcie-ma2x8x.mvcmd``
    * - Arm® CPU
      - ``-``

.. raw:: html

    </div>

Execution capabilities
++++++++++++++++++++++

``HETERO``, ``MULTI``, ``BATCH``, ``AUTO`` execution capabilities can also be used explicitly or implicitly by the application. Use the following recommendation scheme to decide whether to put the appropriate libraries to the distribution package:

* If :ref:`AUTO <doxid-openvino_docs__o_v__u_g_supported_plugins__a_u_t_o>` is used explicitly in the application or ``:ref:`ov::Core::compile_model <doxid-classov_1_1_core_1a46555f0803e8c29524626be08e7f5c5a>``` is used without specifying a device, put the ``openvino_auto_plugin`` to the distribution
  
  .. note:: Auto device selection relies on :ref:`inference device plugins <doxid-openvino_docs__o_v__u_g__working_with_devices>`, so if are not sure what inference devices are available on target machine, put all inference plugin libraries to the distribution. If the ``:ref:`ov::device::priorities <doxid-group__ov__runtime__cpp__prop__api_1gae88af90a18871677f39739cb0ef0101e>``` is used for ``AUTO`` to specify a limited device list, grab the corresponding device plugins only.

* If :ref:`MULTI <doxid-openvino_docs__o_v__u_g__running_on_multiple_devices>` is used explicitly, put the ``openvino_auto_plugin`` to the distribution

* If :ref:`HETERO <doxid-openvino_docs__o_v__u_g__hetero_execution>` is either used explicitly or ``:ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>``` is used with GPU, put the ``openvino_hetero_plugin`` to the distribution

* If :ref:`BATCH <doxid-openvino_docs__o_v__u_g__automatic__batching>` is either used explicitly or ``:ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>``` is used with GPU, put the ``openvino_batch_plugin`` to the distribution

Reading models
++++++++++++++

OpenVINO Runtime uses frontend libraries dynamically to read models in different formats:

* To read OpenVINO IR ``openvino_ir_frontend`` is used

* To read ONNX file format ``openvino_onnx_frontend`` is used

* To read Paddle file format ``openvino_paddle_frontend`` is used

Depending on what types of model file format are used in the application in ``:ref:`ov::Core::read_model <doxid-classov_1_1_core_1a3cca31e2bb5d569330daa8041e01f6f1>```, peek up the appropriate libraries.

.. note:: The recommended way to optimize the size of final distribution package is to :ref:`convert models using Model Optimizer <doxid-openvino_docs__m_o__d_g__deep__learning__model__optimizer__dev_guide>` to OpenVINO IR, in this case you don't have to keep ONNX, Paddle and other frontend libraries in the distribution package.

(Legacy) Preprocessing via G-API
++++++++++++++++++++++++++++++++

.. note:: :ref:`G-API <doxid-openvino_docs_gapi_gapi_intro>` preprocessing is a legacy functionality, use :ref:`preprocessing capabilities from OpenVINO 2.0 <doxid-openvino_docs__o_v__u_g__preprocessing__overview>` which do not require any additional libraries.

If the application uses ``:ref:`InferenceEngine::PreProcessInfo::setColorFormat <doxid-class_inference_engine_1_1_pre_process_info_1a3a10ba0d562a2268fe584d4d2db94cac>``` or ``:ref:`InferenceEngine::PreProcessInfo::setResizeAlgorithm <doxid-class_inference_engine_1_1_pre_process_info_1a0c083c43d01c53c327f09095e3e3f004>``` methods, OpenVINO Runtime dynamically loads ``openvino_gapi_preproc`` plugin to perform preprocessing via G-API.

Examples
--------

CPU + IR in C-written application
+++++++++++++++++++++++++++++++++

C-written application performs inference on CPU and reads models stored as OpenVINO IR:

* ``openvino_c`` library is a main dependency of the application. It links against this library

* ``openvino`` is used as a private dependency for ``openvino`` and also used in the deployment

* ``openvino_intel_cpu_plugin`` is used for inference

* ``openvino_ir_frontend`` is used to read source model

MULTI execution on GPU and MYRIAD in tput mode
++++++++++++++++++++++++++++++++++++++++++++++

C++ written application performs inference :ref:`simultaneously on GPU and MYRIAD devices <doxid-openvino_docs__o_v__u_g__running_on_multiple_devices>` with ``ov::hint::PerformanceMode::THROUGHPUT`` property, reads models stored in ONNX file format:

* ``openvino`` library is a main dependency of the application. It links against this library

* ``openvino_intel_gpu_plugin`` and ``openvino_intel_myriad_plugin`` are used for inference

* ``openvino_auto_plugin`` is used for ``MULTI`` multi-device execution

* ``openvino_auto_batch_plugin`` can be also put to the distribution to improve saturation of :ref:`Intel GPU <doxid-openvino_docs__o_v__u_g_supported_plugins__g_p_u>` device. If there is no such plugin, :ref:`Automatic batching <doxid-openvino_docs__o_v__u_g__automatic__batching>` is turned off.

* ``openvino_onnx_frontend`` is used to read source model

Auto device selection between HDDL and CPU
++++++++++++++++++++++++++++++++++++++++++

C++ written application performs inference with :ref:`automatic device selection <doxid-openvino_docs__o_v__u_g_supported_plugins__a_u_t_o>` with device list limited to HDDL and CPU, model is :ref:`created using C++ code <doxid-openvino_docs__o_v__u_g__model__representation>` :

* ``openvino`` library is a main dependency of the application. It links against this library

* ``openvino_auto_plugin`` is used to enable automatic device selection feature

* ``openvino_intel_hddl_plugin`` and ``openvino_intel_cpu_plugin`` are used for inference, ``AUTO`` selects between CPU and HDDL devices according to their physical existance on deployed machine.

* No frontend library is needed because ``:ref:`ov::Model <doxid-classov_1_1_model>``` is created in code.

