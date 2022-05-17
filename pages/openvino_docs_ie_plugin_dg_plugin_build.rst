.. index:: pair: page; Build Plugin Using CMake\*
.. _doxid-openvino_docs_ie_plugin_dg_plugin_build:


Build Plugin Using CMake\*
==========================

:target:`doxid-openvino_docs_ie_plugin_dg_plugin_build_1md_openvino_docs_ie_plugin_dg_building` Inference Engine build infrastructure provides the Inference Engine Developer Package for plugin development.

Inference Engine Developer Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To automatically generate the Inference Engine Developer Package, run the ``cmake`` tool during a DLDT build:

.. ref-code-block:: cpp

	$ mkdir dldt-release-build
	$ cd dldt-release-build
	$ cmake -DCMAKE_BUILD_TYPE=Release ../dldt

Once the commands above are executed, the Inference Engine Developer Package is generated in the ``dldt-release-build`` folder. It consists of several files:

* ``InferenceEngineDeveloperPackageConfig.cmake`` - the main CMake script which imports targets and provides compilation flags and CMake options.

* ``InferenceEngineDeveloperPackageConfig-version.cmake`` - a file with a package version.

* ``targets_developer.cmake`` - an automatically generated file which contains all targets exported from the OpenVINO build tree. This file is included by ``InferenceEngineDeveloperPackageConfig.cmake`` to import the following targets:
  
  * Libraries for plugin development:
    
    * ``IE::ngraph`` - shared nGraph library
    
    * ``IE::inference_engine`` - shared Inference Engine library
    
    * ``IE::inference_engine_transformations`` - shared library with Inference Engine ngraph-based Transformations
    
    * ``IE::openvino_gapi_preproc`` - shared library with Inference Engine preprocessing plugin
    
    * ``IE::inference_engine_plugin_api`` - interface library with Inference Engine Plugin API headers
    
    * ``IE::inference_engine_lp_transformations`` - shared library with low-precision transformations
    
    * ``IE::pugixml`` - static Pugixml library
    
    * ``IE::xbyak`` - interface library with Xbyak headers
    
    * ``IE::itt`` - static library with tools for performance measurement using Intel ITT
  
  * Libraries for tests development:
    
    * ``IE::gtest``, ``IE::gtest_main``, ``IE::gmock`` - Google Tests framework libraries
    
    * ``IE::commonTestUtils`` - static library with common tests utilities
    
    * ``IE::funcTestUtils`` - static library with functional tests utilities
    
    * ``IE::unitTestUtils`` - static library with unit tests utilities
    
    * ``IE::ngraphFunctions`` - static library with the set of ``:ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>``` builders
    
    * ``IE::funcSharedTests`` - static library with common functional tests

.. note:: it's enough just to run ``cmake --build . --target ie_dev_targets`` command to build only targets from the Inference Engine Developer package.

Build Plugin using Inference Engine Developer Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To build a plugin source tree using the Inference Engine Developer Package, run the commands below:

.. ref-code-block:: cpp

	$ mkdir template-plugin-release-build
	$ cd template-plugin-release-build
	$ cmake -DInferenceEngineDeveloperPackage_DIR=../dldt-release-build ../template-plugin

A common plugin consists of the following components:

#. Plugin code in the ``src`` folder

#. Code of tests in the ``tests`` folder

To build a plugin and its tests, run the following CMake scripts:

* Root ``CMakeLists.txt``, which finds the Inference Engine Developer Package using the ``find_package`` CMake command and adds the ``src`` and ``tests`` subdirectories with plugin sources and their tests respectively:

.. ref-code-block:: cpp

	cmake_minimum_required(VERSION 3.13)
	
	project(OpenVINOTemplatePlugin)
	
	set(TEMPLATE_PLUGIN_SOURCE_DIR ${OpenVINOTemplatePlugin_SOURCE_DIR})
	
	find_package(OpenVINODeveloperPackage REQUIRED)
	
	if(CMAKE_COMPILER_IS_GNUCXX)
	    ov_add_compiler_flags(-Wall)
	endif()
	
	add_subdirectory(src)
	
	if(ENABLE_TESTS)
	    include(CTest)
	    enable_testing()
	
	    if(ENABLE_FUNCTIONAL_TESTS)
	        add_subdirectory(tests/functional)
	    endif()
	endif()

.. note:: The default values of the ``ENABLE_TESTS``, ``ENABLE_FUNCTIONAL_TESTS`` options are shared via the Inference Engine Developer Package and they are the same as for the main DLDT build tree. You can override them during plugin build using the command below:





.. code-block:: cpp

	```bash
	$ cmake -DENABLE_FUNCTIONAL_TESTS=OFF -DInferenceEngineDeveloperPackage_DIR=../dldt-release-build ../template-plugin
	```

* ``src/CMakeLists.txt`` to build a plugin shared library from sources:

.. ref-code-block:: cpp

	set(TARGET_NAME "openvino_template_plugin")
	
	file(GLOB_RECURSE SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/\*.cpp)
	file(GLOB_RECURSE HEADERS ${CMAKE_CURRENT_SOURCE_DIR}/\*.hpp)
	
	if (NOT ENABLE_TEMPLATE_REGISTRATION)
	    # Skip install and registration of template component
	    set(skip_plugin SKIP_INSTALL SKIP_REGISTRATION)
	endif()
	
	# adds a shared library with plugin
	ov_add_plugin(NAME ${TARGET_NAME}
	              DEVICE_NAME "TEMPLATE"
	              SOURCES ${SOURCES} ${HEADERS}
	              ${skip_plugin}
	              VERSION_DEFINES_FOR template_plugin.cpp
	              ADD_CLANG_FORMAT)
	
	# Enable support of CC for the plugin
	ov_mark_target_as_cc(${TARGET_NAME})
	
	target_include_directories(${TARGET_NAME} PRIVATE
	    "${CMAKE_CURRENT_SOURCE_DIR}"
	    "${TEMPLATE_PLUGIN_SOURCE_DIR}/include")
	
	# link common Inference Engine libraries
	target_link_libraries(${TARGET_NAME} PRIVATE
	    interpreter_backend
	    openvino::ngraph_reference)
	
	set_target_properties(${TARGET_NAME} PROPERTIES INTERPROCEDURAL_OPTIMIZATION_RELEASE ${ENABLE_LTO})
	
	if (ENABLE_TEMPLATE_REGISTRATION)
	    # Update the plugins.xml file
	    ov_register_plugins(MAIN_TARGET ${TARGET_NAME})
	endif()



.. note:: ``IE::inference_engine`` target is imported from the Inference Engine Developer Package.

* ``tests/functional/CMakeLists.txt`` to build a set of functional plugin tests:

.. ref-code-block:: cpp

	set(TARGET_NAME ov_template_func_tests)
	
	ov_add_test_target(
	        NAME ${TARGET_NAME}
	        ROOT ${CMAKE_CURRENT_SOURCE_DIR}
	        DEPENDENCIES
	            openvino_template_plugin
	        LINK_LIBRARIES
	            openvino::funcSharedTests
	        INCLUDES
	            "${TEMPLATE_PLUGIN_SOURCE_DIR}/include"
	            "${CMAKE_CURRENT_SOURCE_DIR}/op_reference"
	        # ADD_CPPLINT
	        LABELS
	            TEMPLATE
	)
	
	if(ENABLE_HETERO)
	    add_dependencies(${TARGET_NAME} openvino_hetero_plugin)
	endif()
	
	find_package(OpenCV QUIET COMPONENTS core imgproc)
	
	if(OpenCV_FOUND)
	    message("-- Reference preprocessing: OpenCV tests are enabled")
	    target_compile_definitions(${TARGET_NAME} PRIVATE OPENCV_TEMPLATE_TESTS)
	    target_link_libraries(${TARGET_NAME} PRIVATE opencv_imgproc opencv_core)
	else()
	    message("-- Reference preprocessing: OpenCV tests are disabled")
	endif()



.. note:: The ``IE::funcSharedTests`` static library with common functional Inference Engine Plugin tests is imported via the Inference Engine Developer Package.

