.. index:: pair: page; Plugin Testing
.. _doxid-openvino_docs_ie_plugin_dg_plugin_testing:


Plugin Testing
==============

:target:`doxid-openvino_docs_ie_plugin_dg_plugin_testing_1md_openvino_docs_ie_plugin_dg_plugintesting` Inference Engine (IE) tests infrastructure provides a predefined set of functional tests and utilities. They are used to verify a plugin using the Inference Engine public API. All the tests are written in the `Google Test C++ framework <https://github.com/google/googletest>`__.

Inference Engine Plugin tests are included in the ``IE::funcSharedTests`` CMake target which is built within the OpenVINO repository (see :ref:`Build Plugin Using CMake <doxid-openvino_docs_ie_plugin_dg_plugin_build>` guide). This library contains tests definitions (the tests bodies) which can be parametrized and instantiated in plugins depending on whether a plugin supports a particular feature, specific sets of parameters for test on supported operation set and so on.

Test definitions are split into tests class declaration (see ``inference_engine/tests/functional/plugin/shared/include``) and tests class implementation (see ``inference_engine/tests/functional/plugin/shared/src``) and include the following scopes of plugin conformance tests:

#. **Behavior tests** (``behavior`` sub-folder), which are a separate test group to check that a plugin satisfies basic Inference Engine concepts: plugin creation, multiple executable networks support, multiple synchronous and asynchronous inference requests support, and so on. See the next section with details how to instantiate the tests definition class with plugin-specific parameters.

#. **Single layer tests** (``single_layer_tests`` sub-folder). This groups of tests checks that a particular single layer can be inferenced on a device. An example of test instantiation based on test definition from ``IE::funcSharedTests`` library:
   
   * From the declaration of convolution test class we can see that it's a parametrized GoogleTest based class with the ``convLayerTestParamsSet`` tuple of parameters:
   
   .. ref-code-block:: cpp
   
   	typedef std::tuple<
   	        :ref:`InferenceEngine::SizeVector <doxid-namespace_inference_engine_1a9400de686d3d0f48c30cd73d40e48576>`,    // Kernel size
   	        :ref:`InferenceEngine::SizeVector <doxid-namespace_inference_engine_1a9400de686d3d0f48c30cd73d40e48576>`,    // Strides
   	        std::vector<ptrdiff_t>,         // Pad begin
   	        std::vector<ptrdiff_t>,         // Pad end
   	        :ref:`InferenceEngine::SizeVector <doxid-namespace_inference_engine_1a9400de686d3d0f48c30cd73d40e48576>`,    // Dilation
   	        size_t,                         // Num out channels
   	        :ref:`ngraph::op::PadType <doxid-namespaceov_1_1op_1a287af03f211ecac2b876d35a1130e50d>`             // Padding type
   	> convSpecificParams;
   	typedef std::tuple<
   	        convSpecificParams,
   	        :ref:`InferenceEngine::Precision <doxid-class_inference_engine_1_1_precision>`,     // Net precision
   	        :ref:`InferenceEngine::Precision <doxid-class_inference_engine_1_1_precision>`,     // Input precision
   	        :ref:`InferenceEngine::Precision <doxid-class_inference_engine_1_1_precision>`,     // Output precision
   	        :ref:`InferenceEngine::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`,        // Input layout
   	        :ref:`InferenceEngine::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`,        // Output layout
   	        :ref:`InferenceEngine::SizeVector <doxid-namespace_inference_engine_1a9400de686d3d0f48c30cd73d40e48576>`,    // Input shapes
   	        LayerTestsUtils::TargetDevice   // Device name
   	> convLayerTestParamsSet;
   	
   	class ConvolutionLayerTest : public testing::WithParamInterface<convLayerTestParamsSet>,
   	                             virtual public LayerTestsUtils::LayerTestsCommon {
   	public:
   	    static std::string getTestCaseName(const testing::TestParamInfo<convLayerTestParamsSet>& obj);
   	
   	protected:
   	    void SetUp() override;
   	};
   
   
   
   * Based on that, define a set of parameters for ``Template`` plugin functional test instantiation:
   
   .. ref-code-block:: cpp
   
   	const std::vector<InferenceEngine::Precision> netPrecisions = {
   	        :ref:`InferenceEngine::Precision::FP32 <doxid-class_inference_engine_1_1_precision_1ade75bd7073b4aa966c0dda4025bcd0f5a6b062312b968a46ae0baf14cc3665e1e>`,
   	        :ref:`InferenceEngine::Precision::FP16 <doxid-class_inference_engine_1_1_precision_1ade75bd7073b4aa966c0dda4025bcd0f5a084e737560206865337ee681e1ab3f5a>`,
   	};
   	
   	/\* ============= 2D Convolution ============= \*/
   	
   	const std::vector<std::vector<size_t >> kernels = {{3, 3},
   	                                                   {3, 5}};
   	const std::vector<std::vector<size_t >> :ref:`strides <doxid-core_2reference_2include_2ngraph_2runtime_2reference_2convolution_8hpp_1a971d047e7b3290908654e5b6a9c6794d>` = {{1, 1},
   	                                                   {1, 3}};
   	const std::vector<std::vector<ptrdiff_t>> padBegins = {{0, 0},
   	                                                       {0, 3}};
   	const std::vector<std::vector<ptrdiff_t>> padEnds = {{0, 0},
   	                                                     {0, 3}};
   	const std::vector<std::vector<size_t >> dilations = {{1, 1},
   	                                                     {3, 1}};
   	const std::vector<size_t> numOutChannels = {1, 5};
   	const std::vector<ngraph::op::PadType> padTypes = {
   	        ngraph::op::PadType::EXPLICIT,
   	        ngraph::op::PadType::VALID
   	};
   	
   	const auto conv2DParams_ExplicitPadding = ::testing::Combine(
   	        ::testing::ValuesIn(kernels),
   	        ::testing::ValuesIn(:ref:`strides <doxid-core_2reference_2include_2ngraph_2runtime_2reference_2convolution_8hpp_1a971d047e7b3290908654e5b6a9c6794d>`),
   	        ::testing::ValuesIn(padBegins),
   	        ::testing::ValuesIn(padEnds),
   	        ::testing::ValuesIn(dilations),
   	        ::testing::ValuesIn(numOutChannels),
   	        ::testing::Values(ngraph::op::PadType::EXPLICIT)
   	);
   
   
   
   * Instantiate the test itself using standard GoogleTest macro ``INSTANTIATE_TEST_SUITE_P`` :
   
   .. ref-code-block:: cpp
   
   	INSTANTIATE_TEST_SUITE_P(Convolution2D_ExplicitPadding, ConvolutionLayerTest,
   	                         ::testing::Combine(
   	                                 conv2DParams_ExplicitPadding,
   	                                 ::testing::ValuesIn(netPrecisions),
   	                                 ::testing::Values(:ref:`InferenceEngine::Precision::UNSPECIFIED <doxid-class_inference_engine_1_1_precision_1ade75bd7073b4aa966c0dda4025bcd0f5ae27ff65d395667d17067e83d932a2045>`),
   	                                 ::testing::Values(:ref:`InferenceEngine::Precision::UNSPECIFIED <doxid-class_inference_engine_1_1_precision_1ade75bd7073b4aa966c0dda4025bcd0f5ae27ff65d395667d17067e83d932a2045>`),
   	                                 ::testing::Values(:ref:`InferenceEngine::Layout::ANY <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8a890528943ea12cf9832d7f437ea149b5>`),
   	                                 ::testing::Values(:ref:`InferenceEngine::Layout::ANY <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8a890528943ea12cf9832d7f437ea149b5>`),
   	                                 ::testing::Values(std::vector<size_t >({1, 3, 30, 30})),
   	                                 ::testing::Values(CommonTestUtils::DEVICE_TEMPLATE)),
   	                         ConvolutionLayerTest::getTestCaseName);

#. **Sub-graph tests** (``subgraph_tests`` sub-folder). This group of tests is designed to tests small patterns or combination of layers. E.g. when a particular topology is being enabled in a plugin e.g. TF ResNet-50, there is no need to add the whole topology to test tests. In opposite way, a particular repetitive subgraph or pattern can be extracted from ``ResNet-50`` and added to the tests. The instantiation of the sub-graph tests is done in the same way as for single layer tests.	**Note**, such sub-graphs or patterns for sub-graph tests should be added to ``IE::ngraphFunctions`` library first (this library is a pre-defined set of small ``:ref:`ov::Model <doxid-classov_1_1_model>```) and re-used in sub-graph tests after.

#. **HETERO tests** (``subgraph_tests`` sub-folder) contains tests for ``HETERO`` scenario (manual or automatic affinities settings, tests for ``QueryNetwork``).

#. **Other tests**, which contain tests for other scenarios and has the following types of tests:
   
   * Tests for execution graph
   
   * Etc.

To use these tests for your own plugin development, link the ``IE::funcSharedTests`` library to your test binary and instantiate required test cases with desired parameters values.

.. note:: A plugin may contain its own tests for use cases that are specific to hardware or need to be extensively tested.

To build test binaries together with other build artifacts, use the ``make all`` command. For details, see :ref:`Build Plugin Using CMake\* <doxid-openvino_docs_ie_plugin_dg_plugin_build>`.

How to Extend Inference Engine Plugin Tests
-------------------------------------------

Inference Engine Plugin tests are open for contribution. Add common test case definitions applicable for all plugins to the ``IE::funcSharedTests`` target within the DLDT repository. Then, any other plugin supporting corresponding functionality can instantiate the new test.

All Inference Engine per-layer tests check test layers functionality. They are developed using :ref:`ov::Model <doxid-classov_1_1_model>`. as input graphs used by tests. In this case, to test a new layer with layer tests, extend the ``IE::ngraphFunctions`` library, which is also included in the Inference Engine Developer package, with a new model. including the corresponding operation.

.. note:: When implementing a new subgraph test, add new single-layer tests for each operation of the subgraph if such test does not exist.

